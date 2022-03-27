import os

from flask import Flask, json, request
import grpc

from wishlist_pb2 import *
from wishlist_pb2_grpc import WishlistStub

api = Flask(__name__)

wishlist_host = os.getenv("WISHLIST_HOST", "localhost")

wishlist_channel = grpc.insecure_channel(
    f"{wishlist_host}:50056"
)

wishlist_client = WishlistStub(wishlist_channel)


@api.route('/addGame', methods=['POST'])
def addGame():
    data = json.loads(request.data)
    addGameLib_request = Game(
        url=data['url'],
        types=data['types'],
        name=data['name'],
        desc_snippet=data['desc_snippet'],
        recent_reviews=data['recent_reviews'],
        all_reviews=data['all_reviews'],
        release_date=data['release_date'],
        developer=data['developer'],
        publisher=data['publisher'],
        popular_tags=data['popular_tags'],
        game_details=data['game_details'],
        languages=data['languages'],
        achievements=data['achievements'],
        genre=data['genre'],
        game_description=data['game_description'],
        mature_content=data['mature_content'],
        minimum_requirements=data['minimum_requirements'],
        recommended_requirements=data['recommended_requirements'],
        original_price=data['original_price'],
        discount_price=data['discount_price']
    )
    addGameWish_response = wishlist_client.AddGame(
        addGameWish_request
    )
    return json.dumps(addGameWish_response.message)


@api.route('/delGame', methods=['DELETE'])
def deleteGame():
    url = request.args.get('url')
    deleteGameWish_request = DeleteGameWishRequest(
        url=url,
    )
    deleteGame_response = wishlist_client.DeleteGame(
        deleteGameWish_request
    )
    return json.dumps(deleteGameWish_response.message)

@api.route('/getGames', methods=['GET'])
def listGames():

    listGamesWish_request = ListGamesWishRequest(
        page=1, max_results=3
    )
    listGamesWish_response = wishlist_client.ListGames(
        listGamesWish_request
    )
    return json.dumps(listGamesWish_response.games)

