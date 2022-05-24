import os
import datetime

from flask import Flask, json, request, g
import grpc

from google.protobuf.json_format import ParseDict

from adminOperations_pb2 import *
from adminOperations_pb2_grpc import AdminOperationsStub

api = Flask(__name__)

ca_cert = 'keys/caAdminOperations.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

adminoperations_channel = grpc.secure_channel("adminoperationsserver:50051",credentials)

adminoperations_client = AdminOperationsStub(adminoperations_channel)

ca_cert = 'keys/caLogging.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

logging_channel = grpc.secure_channel(os.environ['logging-server-s_KEY'],credentials)
logging_client = LoggingStub(logging_channel)


@api.route('/healthz', methods=['GET'])
def healthz():
    g.req = request
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
    g.req = request    
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
    g.req = request
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
    g.req = request
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
    g.req = request
    return json.dumps(deleteUser_response.message)


@api.after_request
def adminoperations_ar(response):
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