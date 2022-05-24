import os
import datetime

from flask import Flask, json, request, g
import grpc

from google.protobuf.json_format import MessageToJson, ParseDict

from searches_pb2 import *
from searches_pb2_grpc import SearchesStub

from logging_pb2 import (
    Log,
    Empty
)
from logging_pb2_grpc import LoggingStub

api = Flask(__name__)


searches_channel = grpc.insecure_channel(os.environ['searchesserver_KEY'])
searches_client = SearchesStub(searches_channel)

logging_channel = grpc.insecure_channel(os.environ['logging-server-s_KEY'])
logging_client = LoggingStub(logging_channel)

def DocToGame(game):
    g.req = request
    return  {
        "url" : game.url,
        "types" : game.types,
        "name" : game.name,
        "desc_snippet" : game.desc_snippet,
        "recent_reviews" : game.recent_reviews,
        "all_reviews" : game.all_reviews,
        "release_date" : game.release_date,
        "developer" : game.developer,
        "publisher" : game.publisher,
        "popular_tags" : game.popular_tags,
        "game_details" : game.game_details,
        "languages" : game.languages,
        "achievements" : game.achievements,
        "genre" : game.genre,
        "game_description" : game.game_description,
        "mature_content" : game.mature_content,
        "minimum_requirements" : game.minimum_requirements,
        "recommended_requirements" : game.recommended_requirements,
        "original_price" : game.original_price,
        "discount_price" : game.discount_price,
        "_id" : game._id
    }

def DocToReview(review):
    g.req = request
    return  {
        "review_id" : review.review_id,
        "app_id" : review.app_id,
        "app_name" : review.app_name,
        "language" : review.language,
        "review" : review.review,
        "timestamp_created" : review.timestamp_created,
        "timestamp_updated" : review.timestamp_updated,
        "recommended" : review.recommended,
        "votes_helpful" : review.votes_helpful,
        "votes_funny" : review.votes_funny,
        "weighted_vote_score" : review.weighted_vote_score,
        "comment_count" : review.comment_count,
        "steam_purchase" : review.steam_purchase,
        "received_for_free" : review.received_for_free,
        "written_during_early_access" : review.written_during_early_access,
        "author_steamid" : review.author_steamid,
        "author_num_games_owned" : review.author_num_games_owned,
        "author_num_reviews" : review.author_num_reviews,
        "author_playtime_forever" : review.author_playtime_forever,
        "author_playtime_last_two_weeks" : review.author_playtime_last_two_weeks,
        "author_playtime_at_review" : review.author_playtime_at_review,
        "author_last_played" : review.author_last_played,
    }

@api.route('/healthz', methods=['GET'])
def healthz():
    g.req = request
    return json.dumps("Ok")

@api.route('/searches/games', methods=['GET'])
def searchGames():

    searchGames_request = SearchGamesRequest(
        types = request.args.get('types'),
        name = request.args.get('name'),
        release_date = request.args.get('release_date'),
        developer = request.args.get('developer'),
        publisher = request.args.get('publisher'),
        popular_tags = request.args.get('popular_tags'),
        languages = request.args.get('languages'),
        genre = request.args.get('genre'),
        original_price = request.args.get('original_price')
    )
    searchGames_response = searches_client.SearchGames(
        searchGames_request
    )
    map = {}
    i = 0
    for doc in searchGames_response.games:
        map[str(i)] = DocToGame(searchGames_response.games[str(i)])
        i+=1
    g.req = request
    return json.dumps(map)

@api.route('/searches/game', methods=['GET'])
def getGame():
    id = request.args.get('id')
    searchGame_request = SearchGameRequest(
        id = id
    )
    searchGame_response = searches_client.SearchGameById(
        searchGame_request
    )
    g.req = request
    return MessageToJson(searchGame_response)

@api.route('/searches/reviews', methods=['GET'])
def searchReviews():

    app_name = request.args.get('app_name')
    timestamp_created = request.args.get('timestamp_created')
    recommended = request.args.get('recommended')
    votes_helpful = request.args.get('votes_helpful')
    votes_funny = request.args.get('votes_funny')
    comment_count = request.args.get('comment_count')

    searchReviews_request = SearchReviewsRequest(
        app_name = app_name,
        timestamp_created = timestamp_created,
        recommended = recommended,
        votes_helpful = votes_helpful,
        votes_funny = votes_funny,
        comment_count = comment_count
    )
    searchReviews_response = searches_client.SearchReviews(
        searchReviews_request
    )

    map = {}
    i = 0
    for doc in searchReviews_response.reviews:
        map[str(i)] = DocToReview(searchReviews_response.reviews[str(i)])
        i+=1
    g.req = request
    return json.dumps(map)

@api.route('/searches/review', methods=['GET'])
def getReview():
    id = request.args.get('id')
    searchReview_request = SearchReviewRequest(
        id = id
    )

    searchReview_response = searches_client.SearchReviewById(
        searchReview_request
    )
    g.req = request
    return MessageToJson(searchReview_response)

@api.after_request
def searches_ar(response):
    req = g.get("req")
    log = ParseDict({
        "operation": str(req.method),
        "endpoint": req.full_path,
        "status": response.status,
        "service": "Searches",
        "remote_addr": str(req.remote_addr),
        "user": "default",
        "host": req.host,
        "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }, Log())
    logging_client.StoreLog(log)
    return response
