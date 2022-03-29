from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from pymongo import MongoClient
import os

from reviews_pb2 import (
    ReviewObject,
    ListReviewsResponse,
    SimpleResponse
)
import reviews_pb2_grpc

#connString = os.environ["MONGODB_CONNSTRING"]
connection = MongoClient('reviews-db', 27017, username='admin', password='admin')
revs = connection["reviews"]
db = revs["data"]

class ReviewService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        doc = db.find_one({"review_id": request.review_id})
        if doc is None:
            return ReviewObject (
                review_id = "",
                app_id = "",
                app_name = "",
                language = "",
                review = "",
                timestamp_created = "",
                timestamp_updated = "",
                recommended = "",
                votes_helpful = "",
                votes_funny = "",
                weighted_vote_score = "",
                comment_count = "",
                steam_purchase = "",
                received_for_free = "",
                written_during_early_access = "",
                author_steamid = "",
                author_num_games_owned = "",
                author_num_reviews = "",
                author_playtime_forever = "",
                author_playtime_last_two_weeks = "",
                author_playtime_at_review = "",
                author_last_played = ""
            )
        return ReviewObject (
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

    def AddReview(self, request, context):
        doc = db.find_one({"review_id": request.review_id})
        if doc is None:
            db.insert_one({
                "review_id": request.review_id,
                "app_id": request.app_id,
                "app_name": request.app_name,
                "language": request.language,
                "review": request.review,
                "timestamp_created": request.timestamp_created,
                "timestamp_updated": request.timestamp_updated,
                "recommended": request.recommended,
                "votes_helpful": request.votes_helpful,
                "votes_funny": request.votes_funny,
                "weighted_vote_score": request.weighted_vote_score,
                "comment_count": request.comment_count,
                "steam_purchase": request.steam_purchase,
                "received_for_free": request.received_for_free,
                "written_during_early_access": request.written_during_early_access,
                "author_steamid": request.author_steamid,
                "author_num_games_owned": request.author_num_games_owned,
                "author_num_reviews": request.author_num_reviews,
                "author_playtime_forever": request.author_playtime_forever,
                "author_playtime_last_two_weeks": request.author_playtime_last_two_weeks,
                "author_playtime_at_review": request.author_playtime_at_review,
                "author_last_played": request.author_last_played
            })
            return SimpleResponse(code="200", description="Review added")
        return SimpleResponse(code="400", description="Review already exists")

    def UpdateReview(self, request, context):
        doc = db.find_one({"review_id": request.review_id})
        if doc is None:
            return SimpleResponse(code="404", description="Review not found")
        db.replace_one({"review_id": request.review_id},
        {
            "review_id": request.review_id,
            "app_id": request.app_id,
            "app_name": request.app_name,
            "language": request.language,
            "review": request.review,
            "timestamp_created": request.timestamp_created,
            "timestamp_updated": request.timestamp_updated,
            "recommended": request.recommended,
            "votes_helpful": request.votes_helpful,
            "votes_funny": request.votes_funny,
            "weighted_vote_score": request.weighted_vote_score,
            "comment_count": request.comment_count,
            "steam_purchase": request.steam_purchase,
            "received_for_free": request.received_for_free,
            "written_during_early_access": request.written_during_early_access,
            "author_steamid": request.author_steamid,
            "author_num_games_owned": request.author_num_games_owned,
            "author_num_reviews": request.author_num_reviews,
            "author_playtime_forever": request.author_playtime_forever,
            "author_playtime_last_two_weeks": request.author_playtime_last_two_weeks,
            "author_playtime_at_review": request.author_playtime_at_review,
            "author_last_played": request.author_last_played
        })
        return SimpleResponse(code="200", description="Review updated")

    def DeleteReview(self, request, context):
        doc = db.find_one({"review_id": request.review_id})
        if doc is None:
            return SimpleResponse(code="404", description="Review not found")
        db.delete_one(doc)
        return SimpleResponse(code="204", description="Review deleted")

    def ListReviews(self, request, context):
        docs = db.aggregate([{"$sample": {"size": int(request.max_results)}},{"$project": {"_id": 0}}]);
        if docs is None:
            return ListReviewsResponse(reviews="")
        return ListReviewsResponse(reviews=docs)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    reviews_pb2_grpc.add_ReviewsServicer_to_server(
        ReviewService(), server
    )

    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
