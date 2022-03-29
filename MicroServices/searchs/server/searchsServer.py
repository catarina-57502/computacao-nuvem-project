import os

from flask import Flask, json, request
import grpc

from adminOperations_pb2 import GameObject
from adminOperations_pb2_grpc import AdminOperationsStub

api = Flask(__name__)


adminoperations_host = os.getenv("ADMINOPERATIONS_HOST", "localhost")

adminoperations_channel = grpc.insecure_channel(
    f"{adminoperations_host}:50069"
)

searches_client = AdminOperationsStub(adminoperations_channel)


@api.route('/searchGames', methods=['GET'])
def searchGames():
    data = json.loads(request.data)
    searchGames_request = ListSearchGamesRequest(
        types = data['types'],
        name = data['name'],
        release_date = data['release_date'],
        developer = data['developer'],
        publisher = data['publisher'],
        popular_tags = data['popular_tags'],
        languages = data['languages'],
        genre = data['genre'],
        original_price = data['original_price'],
        discount_price = data['discount_price']
    )
    searchGames_response = searchs_client.SearchGames(
        searchGames_request
    )

    return json.dumps(searchGames_response.gameIds)

@api.route('/getGame', methods=['GET'])
def getGame():
    id = request.args.get('id')
    getGame_request = GetGameRequest(
        id = id
    )

    getGame_response = searchs_client.SearchGameById(
        GetGameRequest
    )
    return json.dumps(getGame_response.gameId)

@api.route('/searchReviews', methods=['GET'])
def searchReviews():
    data = json.loads(request.data)
    searchReviews_request = SearchReviewsRequest(
        id = data['id'],
        app_name = data['app_name'],
        language = data['language'],
        timestamp_created = data['timestamp_created'],
        timestamp_updated = data['timestamp_updated'],
        votes_helpful = data['votes_helpful'],
        votes_funny = data['votes_funny'],
        weighted_vote_score = data['weighted_vote_score'],
        comment_count = data['comment_count'],
        author_steamid = data['author_steamid']
    )
    searchReviews_response = searchs_client.SearchReviews(
        searchReviews_request
    )


    return json.dumps(searchReviews_response.id)

@api.route('/getReviews', methods=['GET'])
def getReviews():
    id = request.args.get('id')
    getGameReview_request = GetGameReviewRequest(
        id = id
    )

    getGameReview_response = searchs_client.SearchsReviewById(
        getGameReview_request
    )
    return json.dumps(getGameReview_response.reviewId)