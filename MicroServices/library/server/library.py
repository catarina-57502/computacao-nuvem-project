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

from userManagement_pb2 import *
from userManagement_pb2_grpc import UserManagementStub

def get_table(db,table):
    return db[table]

client = MongoClient('microservices_mongoDB_1', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

def connectToClient():
    userManagement_channel = grpc.insecure_channel("userManagement:50054")
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
        docUser = usersDB.find({"userid": getToken_response.userID} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.append(request.id)
            doc["library"] = library
            usersDB.delete_one({"userid": getToken_response.userID})
            usersDB.insert_one(doc)
        return AddGameLibResponse(message="Game added in library")

    def DeleteGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        docUser = usersDB.find({"userid": getToken_response.userID} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.remove(request.id)
            doc["library"] = library
            usersDB.delete_one({"userid": getToken_response.userID})
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
        docUser = usersDB.find({"userid": getToken_response.userID} )
        for doc in docUser:
            library = doc["library"]
        for game in library:
            str += game+"\n"
        return ListGamesLibResponse(gameids=str)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryService(), server
    )
    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()