from concurrent import futures
import random

import grpc
import grpc_interceptor
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from wishlist_pb2 import *
import wishlist_pb2_grpc

from userManagement_pb2 import *
from userManagement_pb2_grpc import UserManagementStub


import pymongo
from pymongo import MongoClient

def get_table(db,table):
    return db[table]

client = MongoClient('microservices_mongoDB_1', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

def connectToClient():
    userManagement_channel = grpc.insecure_channel("userManagement:50054")
    userManagement_client = UserManagementStub(userManagement_channel)
    return userManagement_client


class WishlistService(wishlist_pb2_grpc.WishlistServicer):
    def AddGame(self, request, context):

        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"userid": getToken_response.userID} )

        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.append(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"userid": getToken_response.userID})
            usersDB.insert_one(doc)
        return AddGameWishResponse(message="Game added in wishlist")

    def DeleteGame(self, request, context):

        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"userid": getToken_response.userID} )

        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.remove(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"userid": getToken_response.userID})
            usersDB.insert_one(doc)
        return DeleteGameWishResponse(message="Game deleted from wishlist")

    def ListGames(self, request, context):
        str = ""
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"userid": getToken_response.userID} )

        #TODO
        wishlist = {"111":"111","222":"333","3333":"4444"}

        return ListGamesWishResponse(MyMap=(wishlist))


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    wishlist_pb2_grpc.add_WishlistServicer_to_server(
        WishlistService(), server
    )
    server.add_insecure_port("[::]:50058")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()