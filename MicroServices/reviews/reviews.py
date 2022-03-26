from concurrent import futures
import re

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient
import bson
import os

from reviews_pb2 import (
    ReviewObject,
    ListReviewsResponse
)
import reviews_pb2_grpc

connString = os.environ['MONGODB_CONNSTRING']
connection = MongoClient(connString)
db = connection['reviews']

class ReviewService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        review = db.find({"review_id": request.review_id})
        if review is None:
            raise NotFound("Review not found")
        return ReviewObject (
            review_id =
            app_id = 
            app_name = 
            language = 
            review = 
            timestamp_created = 
            timestamp_updated = 
            recommended = 
            votes_helpful = 
            votes_funny = 
            weighted_vote_score = 
            comment_count = 
            steam_purchase = 
            received_for_free = 
            written_during_early_access = 
            author_steamid = 
            author_num_games_owned = 
            author_num_reviews = 
            author_playtime_forever = 
            author_playtime_last_two_weeks =
            author_playtime_at_review = 
            author_last_played = 
        )

    def AddReview(self, request, context):
        return
    def UpdateReview(self, request, context):
        return
    def DeleteReview(self, request, context):
        return
    def ListReviews(self, request, context):
        return


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    reviews_pb2_grpc.add_ReviewsServicer_to_server(
        ReviewService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()