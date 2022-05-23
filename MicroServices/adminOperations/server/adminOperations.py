from concurrent import futures
import random
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound


from adminOperations_pb2 import (
    GameObject,
    AddGameResponse,
    UpdateGameResponse,DeleteUserResponse,DeleteGameResponse
)
import adminOperations_pb2_grpc
import pymongo
from pymongo import MongoClient

from userManagement_pb2 import *
from userManagement_pb2_grpc import UserManagementStub

from prometheus_client import start_http_server, Summary

# Track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

def get_table(db,table):
    return db[table]

client = MongoClient('mongo', 27017 ,username='admin', password='admin')
db = client['steam']
gamesDB = get_table(db,"Games")
reviewsDB = get_table(db,"Reviews")
dbUsers = client['users']
userDB = get_table(dbUsers,"users")

def connectToClient():
    userManagement_channel = grpc.insecure_channel(os.environ['usermanagementserversvc_KEY'])
    userManagement_client = UserManagementStub(userManagement_channel)
    return userManagement_client

def createdoc(request):
    return {
        "url":request.url,
        "types":request.types,
        "name":request.name,
        "desc_snippet":request.desc_snippet,
        "recent_reviews":request.recent_reviews,
        "all_reviews":request.all_reviews,
        "release_date":request.release_date,
        "developer":request.developer,
        "publisher":request.publisher,
        "popular_tags":request.popular_tags,
        "game_details":request.game_details,
        "languages":request.languages,
        "achievements":request.achievements,
        "genre":request.genre,
        "game_description":request.game_description,
        "mature_content":request.mature_content,
        "minimum_requirements":request.minimum_requirements,
        "recommended_requirements":request.recommended_requirements,
        "original_price":request.original_price,
        "discount_price":request.discount_price
    }

class AdminOperationService(adminOperations_pb2_grpc.AdminOperationsServicer):

    @REQUEST_TIME.time()
    def AddGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        if getToken_response.type != "admin":
            return AddGameResponse(message="Not Admin :(")
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) == 0:
            gamesDB.insert_one(createdoc(request))
            return AddGameResponse(message="Game Added")
        else:
            return AddGameResponse(message="Error - Game URL already exists")

    @REQUEST_TIME.time()
    def UpdateGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        if getToken_response.type != "admin":
            return UpdateGameResponse(message="Not Admin :(")
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) >= 1:
            gamesDB.delete_one(myquery);
            gamesDB.insert_one(createdoc(request))
            return UpdateGameResponse(message="Game updated")
        else:
            return UpdateGameResponse(message="Error - Game not found")

    @REQUEST_TIME.time()
    def DeleteGame(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        if getToken_response.type != "admin":
            return DeleteGameResponse(message="Not Admin :(")
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) >= 1:
            gamesDB.delete_one(myquery);
            return DeleteGameResponse(message="Game deleted")
        else:
            return DeleteGameResponse(message="Error - Game not found")

    @REQUEST_TIME.time()
    def DeleteUser(self, request, context):
        getToken_request = TokenRequest(
            token = request.token
        )
        getToken_response = connectToClient().GetInfoFromToken(
            getToken_request
        )
        if getToken_response.type != "admin":
            return DeleteUserResponse(message="Not Admin :(")
        myquery = { "userid": request.id }
        userDB.delete_one(myquery)
        return DeleteUserResponse(message="User deleted")


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    adminOperations_pb2_grpc.add_AdminOperationsServicer_to_server(AdminOperationService(), server)


    caCRT = 'ca.crt'
    serverCRT = 'server.crt'
    serverKey = 'server.key'

    with open(caCRT, 'rb') as f:
        credsCA = f.read()
    with open(serverCRT, 'rb') as f:
        credsSCRT = f.read()
    with open(serverKey, 'rb') as f:
        credsSK = f.read()


    channel_creds = grpc.ssl_server_credentials( credsCA )

    server.add_secure_port("[::]:50051",channel_creds)
    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    start_http_server(51051)
    serve()

