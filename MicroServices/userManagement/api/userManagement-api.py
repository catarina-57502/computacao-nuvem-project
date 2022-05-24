import os
from google.protobuf.json_format import MessageToJson, ParseDict
import datetime

from flask import Flask, json, request, g
import grpc

from userManagement_pb2 import User,LoginRequest,LogoutRequest,AddUserRequest,EditUserRequest
from userManagement_pb2_grpc import UserManagementStub

from logging_pb2 import (
    Log,
    Empty
)
from logging_pb2_grpc import LoggingStub

api = Flask(__name__)

ca_cert = 'caUserManagement.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

userManagement_channel = grpc.secure_channel(os.environ['usermanagementserversvc_KEY'],credentials)
usermanagement_client = UserManagementStub(userManagement_channel)

ca_cert = 'caLogging.pem'
with open(ca_cert,'rb') as f:
    root_certs = f.read()


credentials = grpc.ssl_channel_credentials(root_certs)

logging_channel = grpc.secure_channel(os.environ['logging-server-s_KEY'],credentials)
logging_client = LoggingStub(logging_channel)

@api.route('/user', methods=['POST'])
def addUser():
    data = json.loads(request.data)
    addUser_request = AddUserRequest(
        id=data['id'],
        nickname=data['nickname'],
        email=data['email'],
        password=data['password'],
        type=data["type"]
    )
    addUser_response = usermanagement_client.AddUser(
        addUser_request
    )
    g.req = request
    return json.dumps(addUser_response.message)

@api.route('/healthz', methods=['GET'])
def healthz():
    g.req = request
    return json.dumps("Ok")

@api.route('/user', methods=['PUT'])
def editUser():
    data = json.loads(request.data)
    updateUser_request = EditUserRequest(
        new_password=data['new_password'],
        nickname=data['nickname'],
        new_email=data['new_email'],
        type = data["type"],
        token = request.headers.get('token')
    )
    updateUser_response = usermanagement_client.EditUser(
        updateUser_request
    )
    g.req = request
    return json.dumps(updateUser_response.message)

@api.route('/user/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    login_request = LoginRequest(
        email=data['email'],
        password=data['password']
    )
    login_response = usermanagement_client.LoginUser(
        login_request
    )
    g.req = request
    return json.dumps(login_response.token)

@api.route('/user/logout', methods=['GET'])
def logout():
    data = json.loads(request.data)
    logout_request = LogoutRequest(
        email=data['email'],
        password=data['password'],
    )
    logout_response = usermanagement_client.Logout(
        logout_request
    )
    g.req = request
    return json.dumps(logout_response.message)

@api.after_request
def user_ar(response):
    req = g.get("req")
    log = ParseDict({
        "operation": str(req.method),
        "endpoint": req.full_path,
        "status": response.status,
        "service": "User Management",
        "remote_addr": str(req.remote_addr),
        "user": "default",
        "host": req.host,
        "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }, Log())
    logging_client.StoreLog(log)
    return response