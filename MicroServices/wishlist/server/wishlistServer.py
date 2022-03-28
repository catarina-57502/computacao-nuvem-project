import os

from flask import Flask, json, request
import grpc

from wishlist_pb2 import *
from wishlist_pb2_grpc import WishlistStub

api = Flask(__name__)

wishlist_host = os.getenv("WISHLIST_HOST", "localhost")

wishlist_channel = grpc.insecure_channel(
    f"{wishlist_host}:50058"
)

wishlist_client = WishlistStub(wishlist_channel)


@api.route('/addGame_wish', methods=['POST'])
def addGame():

    data = json.loads(request.data)
    addGameWish_request = AddGameWishRequest(
        id=data['id'],
        userid=data['userid'],
    )
    addGameWish_response = wishlist_client.AddGame(
        addGameWish_request
    )
    return json.dumps(addGameWish_response.message)


@api.route('/delGame_wish', methods=['DELETE'])
def deleteGame():

    data = json.loads(request.data)
    deleteGameWish_request = DeleteGameWishRequest(
        id=data['id'],
        userid=data['userid'],
    )
    deleteGameWish_response = wishlist_client.DeleteGame(
        deleteGameWish_request
    )
    return json.dumps(deleteGameWish_response.message)

@api.route('/getGame_wish', methods=['GET'])
def listGames():

    userid = request.args.get('userid')
    listGamesWish_request = ListGamesWishRequest(
        userid=userid
    )
    listGamesWish_response = wishlist_client.ListGames(
        listGamesWish_request
    )

    return json.dumps(listGamesWish_response.gameids)

