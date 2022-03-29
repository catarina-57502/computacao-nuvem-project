from concurrent import futures
import random
import pymongo
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from suggestions_pb2 import (
    Game,
    Review,
    GameResponse,
    ReviewResponse
)

import suggestions_pb2_grpc
games = []
reviews = []
dict_game = {}
myClient = MongoClient('172.18.0.2', 27017 ,username='admin', password='admin' )
myDB = myClient["steam"]
myGames = myDB["Games"]
myReviews = myDB["Reviews"]

class SuggestionsService(suggestions_pb2_grpc.SuggestionsServicer):
    def GetGames(self, request, context):
        myQuery = { "$or":[{"release_date": "May 12, 2016"}, {"developer": "id Software"},
                           {"popular_tags": "FPS,Gore,Action,Demons,Shooter,First-Person,Great Soundtrack,Multiplayer,Singleplayer,Fast-Paced,Sci-fi,Horror,Classic,Atmospheric,Difficult,Blood,Remake,Zombies,Co-op,Memes"},
                           {"genre": "Action"}, {"original_price": "$19.99"}]}
        mydoc = myGames.find(myQuery)
        for x in mydoc:
            x["_id"] = ""
            games.append(x)

        games_to_suggest = random.sample(games,10)
        i = 0
        for game in games_to_suggest:
            str1 = "" + str(i)
            dict_game[str1] = game
            i+=1
        return GameResponse(games=dict_game)
    def GetReviews(self, request, context):
        myQuery = { "$or":[{"app_name": "The Witcher 3: Wild Hunt"}, {"timestamp_updated": "1611379970"}
            ,{"recommended": "true"}, {"author_playtime_at_review": "5524"}]}

        mydoc = myReviews.find(myQuery).limit(100)
        for x in mydoc:
            x["_id"] = ""
            reviews.append(x)
        reviews_to_suggest = random.sample(reviews,10)
        return ReviewResponse(reviews=reviews_to_suggest)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    suggestions_pb2_grpc.add_SuggestionsServicer_to_server(
        SuggestionsService(), server
    )

    server.add_insecure_port("[::]:50059")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()