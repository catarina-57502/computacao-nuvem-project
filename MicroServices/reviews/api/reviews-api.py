import os
import grpc
from google.protobuf.json_format import MessageToJson, ParseDict

from reviews_pb2 import (
    ReviewObject,
    ListReviewsRequest,
    GetReviewRequest
)
from reviews_pb2_grpc import ReviewsStub

from flask import Flask, json, request

api = Flask(__name__)

reviews_channel = grpc.insecure_channel("reviews-server:50060")
reviews_client = ReviewsStub(reviews_channel)

@api.route('/reviews', methods=['GET'])
def list_reviews():
    max_results = request.args.get('max_results')
    req = ListReviewsRequest (
        max_results = max_results
    )
    res = reviews_client.ListReviews(req)     
    return MessageToJson(res)

@api.route('/reviews', methods=['POST'])
def add_review():
    req = ParseDict(request.json, ReviewObject())
    # data = json.loads(request.data)
    # req = ReviewObject (
    #     review_id = data["review_id"],
    #     app_id = data["app_id"],
    #     app_name = data["app_name"],
    #     language = data["language"],
    #     review = data["review"],
    #     timestamp_created = data["timestamp_created"],
    #     timestamp_updated = data["timestamp_updated"],
    #     recommended = data["recommended"],
    #     votes_helpful = data["votes_helpful"],
    #     votes_funny = data["votes_funny"],
    #     weighted_vote_score = data["weighted_vote_score"],
    #     comment_count = data["comment_count"],
    #     steam_purchase = data["steam_purchase"],
    #     received_for_free = data["received_for_free"],
    #     written_during_early_access = data["written_during_early_access"],
    #     author_steamid = data["author_steamid"],
    #     author_num_games_owned = data["author_num_games_owned"],
    #     author_num_reviews = data["author_num_reviews"],
    #     author_playtime_forever = data["author_playtime_forever"],
    #     author_playtime_last_two_weeks = data["author_playtime_last_two_weeks"],
    #     author_playtime_at_review = data["author_playtime_at_review"],
    #     author_last_played = data["author_last_played"]        
    # )
    res = reviews_client.AddReview(req)
    # return json.dumps({
    #     "code": res.code,
    #     "description": res.description})
    return MessageToJson(res)

@api.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    req = GetReviewRequest (
        review_id=review_id,
    )
    res = reviews_client.GetReview(req)
    if res.review_id == "":
        return json.dumps({
            "code": "404", 
            "description": "Review not found"})
    return MessageToJson(res)

    # return json.dumps({
    #     "review_id": res.review_id,
    #     "app_id": res.app_id,
    #     "app_name": res.app_name,
    #     "language": res.language,
    #     "review": res.review,
    #     "timestamp_created": res.timestamp_created,
    #     "timestamp_updated": res.timestamp_updated,
    #     "recommended": res.recommended,
    #     "votes_helpful": res.votes_helpful,
    #     "votes_funny": res.votes_funny,
    #     "weighted_vote_score": res.weighted_vote_score,
    #     "comment_count": res.comment_count,
    #     "steam_purchase": res.steam_purchase,
    #     "received_for_free": res.received_for_free,
    #     "written_during_early_access": res.written_during_early_access,
    #     "author_steamid": res.author_steamid,
    #     "author_num_games_owned": res.author_num_games_owned,
    #     "author_num_reviews": res.author_num_reviews,
    #     "author_playtime_forever": res.author_playtime_forever,
    #     "author_playtime_last_two_weeks": res.author_playtime_last_two_weeks,
    #     "author_playtime_at_review": res.author_playtime_at_review,
    #     "author_last_played": res.author_last_played
    # })

@api.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    req = ParseDict(request.json, ReviewObject())
    # data = json.loads(request.data)
    # req = ReviewObject (
    #     review_id = data["review_id"],
    #     app_id = data["app_id"],
    #     app_name = data["app_name"],
    #     language = data["language"],
    #     review = data["review"],
    #     timestamp_created = data["timestamp_created"],
    #     timestamp_updated = data["timestamp_updated"],
    #     recommended = data["recommended"],
    #     votes_helpful = data["votes_helpful"],
    #     votes_funny = data["votes_funny"],
    #     weighted_vote_score = data["weighted_vote_score"],
    #     comment_count = data["comment_count"],
    #     steam_purchase = data["steam_purchase"],
    #     received_for_free = data["received_for_free"],
    #     written_during_early_access = data["written_during_early_access"],
    #     author_steamid = data["author_steamid"],
    #     author_num_games_owned = data["author_num_games_owned"],
    #     author_num_reviews = data["author_num_reviews"],
    #     author_playtime_forever = data["author_playtime_forever"],
    #     author_playtime_last_two_weeks = data["author_playtime_last_two_weeks"],
    #     author_playtime_at_review = data["author_playtime_at_review"],
    #     author_last_played = data["author_last_played"]        
    # )
    res = reviews_client.UpdateReview(req)
    # return json.dumps({
    #     "code": res.code,
    #     "description": res.description})
    return MessageToJson(res)

@api.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    req = GetReviewRequest (
        review_id=review_id,
    )
    res = reviews_client.DeleteReview(req)
    # return json.dumps({
    #     "code": res.code,
    #     "description": res.description})
    return MessageToJson(res)
