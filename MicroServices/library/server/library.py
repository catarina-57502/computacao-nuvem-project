from concurrent import futures
import random

import grpc
import grpc_interceptor
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from library_pb2 import *
import library_pb2_grpc
import pymongo
from pymongo import MongoClient

from searches_pb2 import *
from searches_pb2_grpc import SearchesStub

from userManagement_pb2 import *
from userManagement_pb2_grpc import UserManagementStub

def get_table(db,table):
    return db[table]

client = MongoClient('mongo', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

def connectToClient():
    userManagement_channel = grpc.insecure_channel("usermanagementserver:50052")
    userManagement_client = UserManagementStub(userManagement_channel)
    return userManagement_client

class LibraryService(library_pb2_grpc.LibraryServicer):
    def AddGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"email": getToken_response.email} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.append(request.id)
            doc["library"] = library
            usersDB.delete_one({"email": getToken_response.email})
            usersDB.insert_one(doc)
        return AddGameLibResponse(message="Game added in library")

    def DeleteGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"email": getToken_response.email} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.remove(request.id)
            doc["library"] = library
            usersDB.delete_one({"email": getToken_response.email})
            usersDB.insert_one(doc)
        return DeleteGameLibResponse(message="Game deleted from library")

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
            library = doc["library"]


        searches_channel = grpc.insecure_channel("searchesserver:50079")
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
        return ListGamesLibResponse(games=gamesInfo)



def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryService(), server
    )
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()