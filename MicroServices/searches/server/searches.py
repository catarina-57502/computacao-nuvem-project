from concurrent import futures
import random

import grpc
import grpc_interceptor
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from bson import ObjectId
from searches_pb2 import *
import searches_pb2_grpc
import pymongo
from pymongo import MongoClient

from prometheus_client import start_http_server, Summary

# Track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

def get_table(db,table):
    return db[table]

myClient = MongoClient('mongo', 27017 ,username='admin', password='admin' )
myDB = myClient["steam"]
myGames = myDB["Games"]
myReviews = myDB["Reviews"]

def DocToGame(doc):
    return Game(
        _id = str(doc["_id"]),
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
        discount_price = doc["discount_price"]
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
        author_last_played = doc["author_last_played"]
    )

class SearchesService(searches_pb2_grpc.SearchesServicer):

    @REQUEST_TIME.time()
    def SearchGames(self, request, context):
        games = []
        dict_game = {}

        if(request.name == ""):
            request.name = "NULL"
        if(request.types == ""):
            request.types = "NULL"
        if(request.release_date == ""):
            request.release_date = "NULL"
        if(request.developer == ""):
            request.developer = "NULL"
        if(request.publisher == ""):
            request.publisher = "NULL"
        if(request.popular_tags == ""):
            request.popular_tags = "NULL"
        if(request.languages == ""):
            request.languages = "NULL"
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

        docGame = myGames.find(myQuery).limit(50)

        if(myGames.count_documents(myQuery) < 1):
            return SearchGamesResponse(games=dict_game)

        for x in docGame:
            games.append(x)

        dict_game = {}
        i = 0
        for game in games:
            str1 = "" + str(i)
            dict_game[str1] = DocToGame(game)
            i+=1

        return SearchGamesResponse(games=dict_game)

    @REQUEST_TIME.time()
    def SearchGameById(self, request, context):
        docGame = myGames.find_one({"_id": ObjectId(request.id)})
        return SearchGameResponse(game=DocToGame(docGame))

    @REQUEST_TIME.time()
    def SearchReviews(self, request, context):
        if(request.app_name == ""):
            request.app_name = "NULL"
        if(request.timestamp_created == ""):
            request.timestamp_created = "NULL"
        if(request.recommended == ""):
            request.recommended = "NULL"
        if(request.votes_helpful == ""):
            request.votes_helpful = "NULL"
        if(request.votes_funny == ""):
            request.votes_funny = "NULL"
        if(request.comment_count == ""):
            request.comment_count = "NULL"


        myQuery = { "$or":
                        [{"app_name": request.app_name},
                         {"recommended": request.recommended},
                         {"votes_helpful": request.votes_helpful},
                         {"votes_funny": request.votes_funny},
                         {"comment_count": request.comment_count}]
                    }

        docReview = myReviews.find(myQuery).limit(5)

        reviews = []
        dict_review = {}

        for x in docReview:
            reviews.append(x)

        i = 0
        for review in reviews:
            str1 = "" + str(i)
            dict_review[str1] = DocToReview(review)
            i+=1

        return SearchReviewsResponse(reviews=dict_review)

    @REQUEST_TIME.time()
    def SearchReviewById(self, request, context):

        docReview = myReviews.find_one({"review_id": request.id})

        return SearchReviewResponse(review=DocToReview(docReview))

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    searches_pb2_grpc.add_SearchesServicer_to_server(
        SearchesService(), server
    )
    server.add_insecure_port("[::]:50079")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    start_http_server(51079)
    serve()