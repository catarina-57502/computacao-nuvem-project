from concurrent import futures
import random
import os

import grpc
import grpc_interceptor
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from wishlist_pb2 import *
import wishlist_pb2_grpc

from userManagement_pb2 import *
from userManagement_pb2_grpc import UserManagementStub

from searches_pb2 import *
from searches_pb2_grpc import SearchesStub

from prometheus_client import start_http_server, Summary
# Track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

import pymongo
from pymongo import MongoClient

def get_table(db,table):
    return db[table]

client = MongoClient('mongo', 27017 ,username='admin', password='admin')
db = client['users']
usersDB = get_table(db,"users")

def connectToClient():
    ca_cert = 'caUserManagement.pem'
    with open(ca_cert,'rb') as f:
        root_certs = f.read()


    credentials = grpc.ssl_channel_credentials(root_certs)
    userManagement_channel = grpc.secure_channel(os.environ['usermanagementserversvc_KEY'],credentials)
    userManagement_client = UserManagementStub(userManagement_channel)
    return userManagement_client


class WishlistService(wishlist_pb2_grpc.WishlistServicer):

    @REQUEST_TIME.time()
    def AddGame(self, request, context):

        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"email": getToken_response.email} )

        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.append(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"email": getToken_response.email})
            usersDB.insert_one(doc)
        return AddGameWishResponse(message="Game added in wishlist")

    @REQUEST_TIME.time()
    def DeleteGame(self, request, context):

        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"email": getToken_response.email} )

        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.remove(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"email": getToken_response.email})
            usersDB.insert_one(doc)
        return DeleteGameWishResponse(message="Game deleted from wishlist")

    @REQUEST_TIME.time()
    def ListGames(self, request, context):
        str = ""
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"email": getToken_response.email})
        for doc in docUser:
            library = doc["wishlist"]
        ca_cert = 'caSearches.pem'
        with open(ca_cert,'rb') as f:
            root_certs = f.read()


        credentials = grpc.ssl_channel_credentials(root_certs)
        searches_channel = grpc.secure_channel(os.environ['searchesserver_KEY'],credentials)
        searches_client = SearchesStub(searches_channel)

        gamesInfo = []
        for id in library:
            searchGame_request = SearchGameRequest(
                id = id
            )
            searchGame_response = searches_client.SearchGameById(
                searchGame_request
            )
            libraryGame = GameLibrary(
                url = searchGame_response.game.url,
                types = searchGame_response.game.types,
                name = searchGame_response.game.name,
                desc_snippet = searchGame_response.game.desc_snippet,
                recent_reviews = searchGame_response.game.recent_reviews,
                all_reviews = searchGame_response.game.all_reviews,
                release_date = searchGame_response.game.release_date,
                developer = searchGame_response.game.developer,
                publisher = searchGame_response.game.publisher,
                popular_tags = searchGame_response.game.popular_tags,
                game_details = searchGame_response.game.game_details,
                languages = searchGame_response.game.languages,
                achievements = searchGame_response.game.achievements,
                genre = searchGame_response.game.genre,
                game_description = searchGame_response.game.game_description,
                mature_content = searchGame_response.game.mature_content,
                minimum_requirements = searchGame_response.game.minimum_requirements,
                recommended_requirements = searchGame_response.game.recommended_requirements,
                original_price = searchGame_response.game.original_price,
                discount_price = searchGame_response.game.discount_price,
                _id = searchGame_response.game._id
            )
            gamesInfo.append(libraryGame)
        return ListGamesWishResponse(games=gamesInfo)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    wishlist_pb2_grpc.add_WishlistServicer_to_server(
        WishlistService(), server
    )
    keyfile = 'serverWishlist-key.pem'
    certfile = 'serverWishlist.pem'

    with open(keyfile,'rb') as f:
        private_key = f.read()

    with open(certfile,'rb') as f:
        certificate_chain = f.read()

    credentials = grpc.ssl_server_credentials([(private_key, certificate_chain)])
    server.add_secure_port("[::]:50058",credentials)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    start_http_server(51058)
    serve()