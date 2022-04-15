import os

from flask import Flask, json, request,jsonify
import grpc

from wishlist_pb2 import *
from wishlist_pb2_grpc import WishlistStub
from google.protobuf.json_format import MessageToJson

api = Flask(__name__)



wishlist_channel = grpc.insecure_channel("wishlistserver:50058")

wishlist_client = WishlistStub(wishlist_channel)

def DocToGame(game):
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
        "_id" : "NA"
    }

@api.route('/wishes', methods=['POST'])
def addGame():
    data = json.loads(request.data)
    addGameWish_request = AddGameWishRequest(
        id=data['id'],
        token = request.headers.get('token')
    )
    addGameWish_response = wishlist_client.AddGame(
        addGameWish_request
    )
    return json.dumps(addGameWish_response.message)


@api.route('/wishes', methods=['DELETE'])
def deleteGame():

    data = json.loads(request.data)
    deleteGameWish_request = DeleteGameWishRequest(
        id=data['id'],
        token = request.headers.get('token')
    )
    deleteGameWish_response = wishlist_client.DeleteGame(
        deleteGameWish_request
    )
    return json.dumps(deleteGameWish_response.message)

@api.route('/wishes', methods=['GET'])
def listGames():
    listGamesWish_request = ListGamesWishRequest(
        token = request.headers.get('token')
    )
    listGamesWish_response = wishlist_client.ListGames(
        listGamesWish_request
    )
    map = {}
    i = 0
    for doc in listGamesWish_response.games:
        map[str(i)] = DocToGame(doc)
        i+=1

    return json.dumps(map)
