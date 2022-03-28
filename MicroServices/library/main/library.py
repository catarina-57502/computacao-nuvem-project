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

def get_table(db,table):
    return db[table]

client = MongoClient('172.23.0.9', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

class LibraryService(library_pb2_grpc.LibraryServicer):
    def AddGame(self, request, context):
        docUser = usersDB.find({"userid": request.userid} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.append(request.id)
            doc["library"] = library
            usersDB.delete_one({"userid": request.userid})
            usersDB.insert_one(doc)
        return AddGameLibResponse(message="Game added in library")

    def DeleteGame(self, request, context):
        docUser = usersDB.find({"userid": request.userid} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            library.remove(request.id)
            doc["library"] = library
            usersDB.delete_one({"userid": request.userid})
            usersDB.insert_one(doc)
        return DeleteGameLibResponse(message="Game deleted from library")

    def ListGames(self, request, context):
        str = ""
        docUser = usersDB.find({"userid": request.userid} )
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