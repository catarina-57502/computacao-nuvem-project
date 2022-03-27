import os

from flask import Flask, json, request
import grpc

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
    addGameLib_response = library_client.AddGame(
        addGameLib_request
    )
    return json.dumps(addGameLib_response.message)


@api.route('/delGame', methods=['DELETE'])
def deleteGame():
    url = request.args.get('url')
    deleteGameLib_request = DeleteGameLibRequest(
        url=url,
    )
    deleteGame_response = library_client.DeleteGame(
        deleteGameLib_request
    )
    return json.dumps(deleteGameLib_response.message)

@api.route('/getGames', methods=['GET'])
def listGames():

    listGamesLib_request = ListGamesLibRequest(
        page=1, max_results=3
    )
    listGamesLib_response = library_client.ListGames(
        listGamesLib_request
    )
    return json.dumps(listGamesLib_response.games)

