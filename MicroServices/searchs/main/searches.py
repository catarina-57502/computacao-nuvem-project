from concurrent import futures
import random

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

def get_table(db,table):
    return db[table]

client = MongoClient('172.23.0.9', 27017 ,username='admin', password='admin' )
db = client['steam']
gamesDB = get_table(db,"Games")

#genreDB = gamesDB.find("genre")

class SearchesService(searches_pb2_grpc.SearchesServicer):
    def SearchGames(self, request, context):
        findGame = request
        findGameList = []
        myQuery = {"popular_tags": findGame.popular_tags}
        popular_tagsDB = gamesDB.find(myQuery)

        for findGame in gamesDB:
            if findGame == gamesDB:
                findGameList.append(findGame)
                return findGameList

        for findGame in popular_tagsDB:
            if findGame == popular_tagsDB:
                findGameList.append(findGame)
                return findGameList

        for findGame in genreDB:
            if findGame == genreDB:
                findGameList.append(findGame)
                return findGameList




