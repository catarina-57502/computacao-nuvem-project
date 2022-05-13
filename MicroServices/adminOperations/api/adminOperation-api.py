import os

from flask import Flask, json, request
import grpc

from adminOperations_pb2 import *
from adminOperations_pb2_grpc import AdminOperationsStub


api = Flask(__name__)

print(os.environ['usermanagementserversvc_KEY'])

adminoperations_channel = grpc.insecure_channel("usermanagement:1220")
adminoperations_client = AdminOperationsStub(adminoperations_channel)

@api.route('/healthz', methods=['GET'])
def healthz():
    return json.dumps("Ok")

@api.route('/admin/games', methods=['POST'])
def addGame():
    data = json.loads(request.data)
    addGame_request = GameObject(
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
        discount_price=data['discount_price'],
        token = request.headers.get('token')
    )
    addGame_response = adminoperations_client.AddGame(
        addGame_request
    )
    return json.dumps(addGame_response.message)

@api.route('/admin/games', methods=['PUT'])
def updateGame():
    data = json.loads(request.data)
    updateGame_request = GameObject(
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
        discount_price=data['discount_price'],
        token = request.headers.get('token')
    )
    updateGame_response = adminoperations_client.UpdateGame(
        updateGame_request
    )
    return json.dumps(updateGame_response.message)

@api.route('/admin/games', methods=['DELETE'])
def deleteGame():
    url = request.args.get('url')
    deleteGame_request = DeleteGameRequest(
        url=url,
        token = request.headers.get('token')
    )
    deleteGame_response = adminoperations_client.DeleteGame(
        deleteGame_request
    )
    return json.dumps(deleteGame_response.message)

@api.route('/admin/users', methods=['DELETE'])
def deleteUser():
    id = request.args.get('id')
    deleteUser_request = DeleteUserRequest(
        id=id,
        token = request.headers.get('token')
    )
    deleteUser_response = adminoperations_client.DeleteUser(
        deleteUser_request
    )
    return json.dumps(deleteUser_response.message)

