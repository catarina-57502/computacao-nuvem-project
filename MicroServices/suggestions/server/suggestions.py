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

myClient = MongoClient('microservices-mongoDB-1', 27017 ,username='admin', password='admin' )
myDB = myClient["steam"]
myGames = myDB["Games"]
myReviews = myDB["Reviews"]

def DocToGame(doc):
    return Game(
    url = doc["url"],
     types = doc["types"],
     name = doc["name"],
     desc_snippet = doc["desc_snippet"],
     recent_reviews = doc["recent_reviews"],
     all_reviews = doc["all_reviews"],
     release_date = doc["release_date"],
     developer = doc["developer"],
     publisher = doc["publisher"],
     popular_tags = doc["popular_tags"],
     game_details = doc["game_details"],
     languages = doc["languages"],
     achievements = doc["achievements"],
     genre = doc["genre"],
     game_description = doc["game_description"],
     mature_content = doc["mature_content"],
     minimum_requirements = doc["minimum_requirements"],
     recommended_requirements = doc["recommended_requirements"],
     original_price = doc["original_price"],
     discount_price = doc["discount_price"],
     _id =doc["_id"]
    )

def DocToReview(doc):
    return Review(
    review_id = doc["review_id"],
     app_id = doc["app_id"],
     app_name = doc["app_name"],
     language = doc["language"],
     review = doc["review"],
     timestamp_created = doc["timestamp_created"],
     timestamp_updated = doc["timestamp_updated"],
     recommended = doc["recommended"],
     votes_helpful = doc["votes_helpful"],
     votes_funny = doc["votes_funny"],
     weighted_vote_score = doc["weighted_vote_score"],
     comment_count = doc["comment_count"],
     steam_purchase = doc["steam_purchase"],
     received_for_free = doc["received_for_free"],
     written_during_early_access = doc["written_during_early_access"],
     author_steamid = doc["author_steamid"],
     author_num_games_owned = doc["author_num_games_owned"],
     author_num_reviews = doc["author_num_reviews"],
     author_playtime_forever = doc["author_playtime_forever"],
     author_playtime_last_two_weeks = doc["author_playtime_last_two_weeks"],
     author_playtime_at_review = doc["author_playtime_at_review"],
     author_last_played = doc["author_last_played"],
     _id = doc["_id"]
    )


class SuggestionsService(suggestions_pb2_grpc.SuggestionsServicer):
    def GetGames(self, request, context):
        games = []
        reviews = []
        dict_game = {}
        if(request.release_date == ""):
            request.release_date = "NULL"
        if(request.developer == ""):
            request.developer = "NULL"
        if(request.popular_tags == ""):
            request.popular_tags = "NULL"
        if(request.genre == ""):
            request.genre = "NULL"
        if(request.original_price == ""):
            request.original_price = "NULL"
        myQuery = { "$or":
                        [{"release_date": request.release_date},
                           {"developer": request.developer},
                           {"popular_tags": request.popular_tags},
                           {"genre": request.genre},
                           {"original_price": request.original_price}]
                    }
        mydoc = myGames.find(myQuery).limit(50)
        if(myGames.count_documents(myQuery) < 1):
            return GameResponse(games=dict_game)
        for x in mydoc:
            x["_id"] = ""
            games.append(x)

        games_to_suggest = random.sample(games,10)
        i = 0
        dict_game= {}
        for game in games_to_suggest:
            str1 = "" + str(i)
            dict_game[str1] = DocToGame(game)
            i+=1
        return GameResponse(games=dict_game)
    def GetReviews(self, request, context):
        games = []
        reviews = []
        dict_review = {}
        myQuery = {"app_name": request.app_name}
        mydoc = myReviews.find(myQuery).limit(int(request.maxResults))
        for x in mydoc:
            x["_id"] = ""
            reviews.append(x)
        if(len(reviews) == 0):
            return ReviewResponse(games=dict_review)
        reviews_to_suggest = random.sample(reviews,int(request.maxResults))
        i = 0
        dict_review= {}
        for review in reviews_to_suggest:
            str1 = "" + str(i)
            dict_review[str1] = DocToReview(review)
            i+=1
        return ReviewResponse(games=dict_review)


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