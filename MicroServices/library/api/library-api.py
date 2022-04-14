import os

from flask import Flask, json, request
import grpc
from google.protobuf.json_format import MessageToJson

from library_pb2 import *
from library_pb2_grpc import LibraryStub

api = Flask(__name__)

library_channel = grpc.insecure_channel("libraryserver:50053")
library_client = LibraryStub(library_channel)

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



@api.route('/addGame', methods=['POST'])
def addGame():

    data = json.loads(request.data)
    addGameLib_request = AddGameLibRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    addGameLib_response = library_client.AddGame(
        addGameLib_request
    )
    return json.dumps(addGameLib_response.message)


@api.route('/delGame', methods=['DELETE'])
def deleteGame():

    data = json.loads(request.data)
    deleteGameLib_request = DeleteGameLibRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    deleteGameLib_response = library_client.DeleteGame(
        deleteGameLib_request
    )
    return json.dumps(deleteGameLib_response.message)

@api.route('/getGames', methods=['GET'])
def listGames():
    listGamesLib_request = ListGamesLibRequest(
        token = request.headers.get('token')
    )
    listGamesLib_response = library_client.ListGames(
        listGamesLib_request
    )

    map = {}
    i = 0
    for doc in listGamesLib_response.games:
        map[str(i)] = DocToGame(doc)
        i+=1

    return json.dumps(map)

