import os

from flask import Flask, json, request
import grpc
from google.protobuf.json_format import MessageToJson

from library_pb2 import *
from library_pb2_grpc import LibraryStub

api = Flask(__name__)

library_host = os.getenv("LIBRARY_HOST", "localhost")

library_channel = grpc.insecure_channel(
    f"{library_host}:50055"
)

library_client = LibraryStub(library_channel)


@api.route('/addGame', methods=['POST'])
def addGame():

    data = json.loads(request.data)
    addGameLib_request = AddGameLibRequest(
        id=data['id'],
        userid=data['userid'],
    )
    addGameLib_response = library_client.AddGame(
        addGameLib_request
    )
    return json.dumps(addGameLib_response.message)


@api.route('/delGame', methods=['DELETE'])
def deleteGame():

    data = json.loads(request.data)
    deleteGameLib_request = DeleteGameLibRequest(
        id=data['id'],
        userid=data['userid'],
    )
    deleteGameLib_response = library_client.DeleteGame(
        deleteGameLib_request
    )
    return json.dumps(deleteGameLib_response.message)

@api.route('/getGames', methods=['GET'])
def listGames():

    userid = request.args.get('userid')
    listGamesLib_request = ListGamesLibRequest(
        userid=userid
    )
    listGamesLib_response = library_client.ListGames(
        listGamesLib_request
    )

    return json.dumps(listGamesLib_response.gameids)

