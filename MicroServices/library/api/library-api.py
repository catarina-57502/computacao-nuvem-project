import os
import datetime

from flask import Flask, json, request, g
import grpc
from google.protobuf.json_format import MessageToJson, ParseDict

from library_pb2 import *
from library_pb2_grpc import LibraryStub

from logging_pb2 import (
    Log,
    Empty
)
from logging_pb2_grpc import LoggingStub

api = Flask(__name__)

library_channel = grpc.insecure_channel(os.environ['libraryserver_KEY'])
library_client = LibraryStub(library_channel)

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
        "_id" : "NA"
    }

@api.route('/healthz', methods=['GET'])
def healthz():
    g.req = request
    return json.dumps("Ok")

@api.route('/library', methods=['POST'])
def addGame():
    addGameLib_request = AddGameLibRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    addGameLib_response = library_client.AddGame(
        addGameLib_request
    )
    g.req = request
    return json.dumps(addGameLib_response.message)


@api.route('/library', methods=['DELETE'])
def deleteGame():

    deleteGameLib_request = DeleteGameLibRequest(
        id = request.args.get('id'),
        token = request.headers.get('token')
    )
    deleteGameLib_response = library_client.DeleteGame(
        deleteGameLib_request
    )
    g.req = request
    return json.dumps(deleteGameLib_response.message)

@api.route('/library', methods=['GET'])
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
    g.req = request
    return json.dumps(map)

@api.after_request
def library_ar(response):
    req = g.get("req")
    log = ParseDict({
        "operation": str(req.method),
        "endpoint": req.full_path,
        "status": response.status,
        "service": "Library",
        "remote_addr": str(req.remote_addr),
        "user": "default",
        "host": req.host,
        "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }, Log())
    logging_client.StoreLog(log)
    return response
