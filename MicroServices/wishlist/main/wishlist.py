from concurrent import futures
import random

import grpc
import grpc_interceptor
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from wishlist_pb2 import *
import wishlist_pb2_grpc
import pymongo
from pymongo import MongoClient

def get_table(db,table):
    return db[table]

client = MongoClient('172.23.0.9', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

class WishlistService(wishlist_pb2_grpc.WishlistServicer):
    def AddGame(self, request, context):
        docUser = usersDB.find({"userid": request.userid} )
        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.append(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"userid": request.userid})
            usersDB.insert_one(doc)
        return AddGameWishResponse(message="Game added in wishlist")

    def DeleteGame(self, request, context):
        docUser = usersDB.find({"userid": request.userid} )
        for doc in docUser:
            wishlist = doc["wishlist"]
            wishlist.remove(request.id)
            doc["wishlist"] = wishlist
            usersDB.delete_one({"userid": request.userid})
            usersDB.insert_one(doc)
        return DeleteGameWishResponse(message="Game deleted from wishlist")

    def ListGames(self, request, context):
        str = ""
        docUser = usersDB.find({"userid": request.userid} )
        for doc in docUser:
            wishlist = doc["wishlist"]
        for game in wishlist:
            str += game+"\n"
        return ListGamesWishResponse(gameids=str)


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