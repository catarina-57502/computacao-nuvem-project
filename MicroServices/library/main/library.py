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

client = MongoClient('172.20.0.2', 27017 ,username='admin', password='admin' )
db = client['steam']
gamesDB = get_table(db,"Games")

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

class LibraryService(library_pb2_grpc.LibraryServicer):
    def AddGame(self, request, context):
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) == 0:
            gamesDB.insert_one(createdoc(request))
            return AddGameLibResponse(message="Game Added")
        else:
            return AddGameLibResponse(message="Error - Game URL already exists")

    def DeleteGame(self, request, context):
        myquery = { "url": request.url }
        if gamesDB.count_documents(myquery) >= 1:
            gamesDB.delete_one(myquery);
            return DeleteGame(message="Game deleted")
        else:
            return DeleteGame(message="Error - Game not found")

    def ListGames(self, request, context):
        page = request.page
        max_results = request.max_result

        listGamesLib_request = ListGamesLibRequest(page=page, max_results=n)
        g = client.ListGames(listGamesLib_request).games

        return ListGamesLibResponse(games=g)


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