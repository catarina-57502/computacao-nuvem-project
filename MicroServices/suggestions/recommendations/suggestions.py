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
CONNECTION_STRING = "mongodb://admin:admin@localhost:27017/admin"
myClient = MongoClient(CONNECTION_STRING)
myDB = myClient["steam"]
myGames = myDB["Games"]
myReviews = myDB["Reviews"]

class RecommendationService(suggestions_pb2_grpc.RecommendationsServicer):
    def GetGames(self, request, context):
        myQuery = { "$or":[{"release_date": "May 12, 2016"}, {"developer": "id Software"},
                           {"popular_tags": "FPS,Gore,Action,Demons,Shooter,First-Person,Great Soundtrack,Multiplayer,Singleplayer,Fast-Paced,Sci-fi,Horror,Classic,Atmospheric,Difficult,Blood,Remake,Zombies,Co-op,Memes"},
                           {"genre": "Action"}, {"original_price": "$19.99"}]}
        mydoc = myGames.find(myQuery)
        for x in mydoc:
            games.append(x)
        games_to_suggest = random.sample(games,10)
        return GameResponse(recommendations=games_to_suggest)
    def GetReviews(self, request, context):
        myQuery = { "$or":[{"app_name": "The Witcher 3: Wild Hunt"}, {"timestamp_updated": "1611379970"}
            ,{"recommended": "true"}, {"author_playtime_at_review": "5524"}]}

        mydoc = myReviews.find(myQuery).limit(100)
        for x in mydoc:
            reviews.append(x)
        reviews_to_suggest = random.sample(reviews,10)
        return ReviewResponse(recommendations=reviews_to_suggest)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    suggestions_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()