import os

from flask import Flask, json, request
import grpc

from userManagement_pb2 import User,LoginRequest,LogoutRequest,AddUserRequest,EditUserRequest
from userManagement_pb2_grpc import UserManagementStub

api = Flask(__name__)


userManagement_channel = grpc.insecure_channel("usermanagementserver:50052")
usermanagement_client = UserManagementStub(userManagement_channel)


@api.route('/addUser', methods=['POST'])
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
    return json.dumps(addUser_response.message)

@api.route('/editUser', methods=['PUT'])
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
    return json.dumps(updateUser_response.message)

@api.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    login_request = LoginRequest(
        email=data['email'],
        password=data['password']
    )
    login_response = usermanagement_client.LoginUser(
        login_request
    )
    return json.dumps(login_response.token)

@api.route('/logout', methods=['GET'])
def logout():
    data = json.loads(request.data)
    logout_request = LogoutRequest(
        email=data['email'],
        password=data['password'],
    )
    logout_response = usermanagement_client.Logout(
        logout_request
    )
    return json.dumps(logout_response.message)