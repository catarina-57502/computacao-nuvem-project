from concurrent import futures
import random

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from adminOperations_pb2 import (
    Game,
    AddGameResponse,
    UpdateGameResponse,DeleteUserResponse,DeleteGameResponse
)
import adminOperations_pb2_grpc
import pymongo
from pymongo import MongoClient

def get_table(db,table):
    return db[table]

client = MongoClient('172.21.0.5', 27017 ,username='admin', password='admin' )
db = client['steam']
gamesDB = get_table(db,"Games")
reviewsDB = get_table(db,"Reviews")

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
    def AddGame(self, request, context):
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) == 0:
            gamesDB.insert_one(createdoc(request))
            return AddGameResponse(message="Game Added")
        else:
            return AddGameResponse(message="Error - Game URL already exists")

    def UpdateGame(self, request, context):
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) >= 1:
            gamesDB.delete_one(myquery);
            gamesDB.insert_one(createdoc(request))
            return UpdateGameResponse(message="Game updated")
        else:
            return UpdateGameResponse(message="Error - Game not found")

    def DeleteGame(self, request, context):
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) >= 1:
            gamesDB.delete_one(myquery);
            return DeleteGameResponse(message="Game deleted")
        else:
            return DeleteGameResponse(message="Error - Game not found")

    def DeleteUser(self, request, context):
        myquery = { "_id": request.id }
        if 0 >= 1:
            # Delete user
            return DeleteUserResponse(message="User deleted")
        else:
            return DeleteUserResponse(message="Error - User not found")



def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    adminOperations_pb2_grpc.add_AdminOperationsServicer_to_server(
        AdminOperationService(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

