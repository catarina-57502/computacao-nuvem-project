import os
import datetime

from flask import Flask, json, request, jsonify, g
import grpc

from wishlist_pb2 import *
from wishlist_pb2_grpc import WishlistStub
from google.protobuf.json_format import MessageToJson, ParseDict

from logging_pb2 import (
    Log,
    Empty
)
from logging_pb2_grpc import LoggingStub

api = Flask(__name__)

ca_cert = 'caWishlist.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

wishlist_channel = grpc.secure_channel(os.environ['wishlistserver_KEY'],credentials)

wishlist_client = WishlistStub(wishlist_channel)

ca_cert = 'caLogging.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

logging_channel = grpc.secure_channel(os.environ['logging-server-s_KEY'],credentials)
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
        "_id" : "NA"
    }

@api.route('/healthz', methods=['GET'])
def healthz():
    g.req = request
    return json.dumps("Ok")

@api.route('/wishes', methods=['POST'])
def addGame():
    addGameWish_request = AddGameWishRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    addGameWish_response = wishlist_client.AddGame(
        addGameWish_request
    )
    g.req = request
    return json.dumps(addGameWish_response.message)


@api.route('/wishes', methods=['DELETE'])
def deleteGame():

    deleteGameWish_request = DeleteGameWishRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    deleteGameWish_response = wishlist_client.DeleteGame(
        deleteGameWish_request
    )
    g.req = request
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
    g.req = request
    return json.dumps(map)

@api.after_request
def wishlist_ar(response):
    req = g.get("req")
    log = ParseDict({
        "operation": str(req.method),
        "endpoint": req.full_path,
        "status": response.status,
        "service": "Wishlist",
        "remote_addr": str(req.remote_addr),
        "user": "default",
        "host": req.host,
        "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }, Log())
    logging_client.StoreLog(log)
    return response