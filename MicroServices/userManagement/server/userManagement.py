from concurrent import futures
import random

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from userManagement_pb2 import *
import userManagement_pb2_grpc


import pymongo
from pymongo import MongoClient

import uuid
import jwt
import requests
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import exceptions
from firebase_admin import auth

cred = credentials.Certificate('./authInfo.json')
default_app = firebase_admin.initialize_app(cred)


def get_table(db,table):
    return db[table]

#client = MongoClient('microservices_mongoDB_1', 27017 ,username='admin', password='admin' )
#db = client['users']
#usersDB = get_table(db,"users")

key_secret = ""
with open("./keys/keyToken.txt", "r") as text_file:
    key_secret = text_file.read()
text_file.close()

def loginCheckGetEmail (token):
    WEB_API_KEY = 'AIzaSyAI2IzUwQ0-Cnu66Vn_EXnYrCN31oD-my8'
    #Confirm Token signature
    payload = json.dumps({"token": token})
    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken"
    r1 = requests.post(rest_api_url, params={"key": WEB_API_KEY},data=payload)
    if "error" in r1.json():
        raise NotFound("Error Login")

    #If token ok get email
    info = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
    email = info["uid"]
    return email

class UserManagementService(userManagement_pb2_grpc.UserManagementServicer):

    #TODO not adding to local db, only cloud provider
    def AddUser(self, request, context):
        library = []
        wishlist = []
        #myquery = { "userid": uuid.uuid4().hex,
        #            "nickname": request.nickname,
        #            "email": request.email,
        #            "password": request.password,
        #            "type": request.type,
        #            "library": library,
        #            "wishlist": wishlist
        #            }
       #myqueryemail = { "email": request.email}

        auth.create_user(
            email=request.email,
            password=request.password,
            display_name=request.nickname)
        return DefaultResponse(code=200,message="User Added")

        #TODO add to bd!
        if usersDB.count_documents(myqueryemail) == 0 :
            usersDB.insert_one(myquery)
            return DefaultResponse(code=200,message="User Added")
        else:
            return DefaultResponse(code=409,message="Error - User already exists")

    #TODO edit cloud info is missing
    def EditUser(self, request, context):
        # New Info
        new_password = request.new_password
        new_email = request.new_email
        nickname = request.nickname
        type = request.type
        token = request.token
        # Get User Info
        email = loginCheckGetEmail(token)
        # Update User
        docUser = usersDB.find({"email": email} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            usersDB.delete_one({"email": email})
            if(new_password != ""):
                password = new_password
            else:
                password = doc["password"]
            if(nickname == ""):
                nickname = doc["nickname"]
            if(new_email != ""):
                email = new_email
            else:
                email = doc["email"]
            if (type != doc["type"] and type != ""):
                type = type
            else:
                type = doc["type"]
            id = doc["userid"]
            userUpdatedDoc = {
                "userid": id,
                "nickname": nickname,
                "email": email,
                "password": password,
                "type": type,
                "library": library,
                "wishlist": wishlist
            }
            usersDB.insert_one(userUpdatedDoc)
            return DefaultResponse(code=200,message="User Updated")
        return DefaultResponse(code=400,message="Not found - User")

    #TODO get type from db
    def LoginUser(self, request, context):
        password = request.password
        email = request.email
        WEB_API_KEY = 'AIzaSyAI2IzUwQ0-Cnu66Vn_EXnYrCN31oD-my8'
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        #check login
        payload = json.dumps({"email":request.email, "password":request.password})
        r = requests.post(rest_api_url, params={"key": WEB_API_KEY},data=payload)
        if "error" in r.json():
            return LoginResponse(token="Error - Login")

        # ask auth to create JWT
        email = request.email
        additional_claims = {'type': 'user'}
        custom_token = auth.create_custom_token(email, additional_claims)

        #Pyhton...
        token = custom_token.decode('UTF-8')
        return LoginResponse(token=token)

    #TODO not logout!!!!!! just test - (maybe delete uid...)
    def Logout(self, request, context):
        WEB_API_KEY = 'AIzaSyAI2IzUwQ0-Cnu66Vn_EXnYrCN31oD-my8'
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        #check login
        payload = json.dumps({"email":request.email, "password":request.password})
        r = requests.post(rest_api_url, params={"key": WEB_API_KEY},data=payload)
        if "error" in r.json():
            raise NotFound("Error Login")


        # ask auth to create JWT
        email = request.email
        #TODO get type from db
        additional_claims = {
            'type': 'user'
        }
        custom_token = auth.create_custom_token(email, additional_claims)

        #Pyhton...
        token = custom_token.decode('UTF-8')

        #Confirm Token signature
        payload = json.dumps({"token": token})
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken"
        r1 = requests.post(rest_api_url, params={"key": WEB_API_KEY},data=payload)
        if "error" in r1.json():
            raise NotFound("Error Login")

        #if ok token get email
        info = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
        email = info["uid"]
        return DefaultResponse(message=email)

    #TODO test claims option with other microservices
    def GetInfoFromToken(self, request, context):
        token = request.token
        WEB_API_KEY = 'AIzaSyAI2IzUwQ0-Cnu66Vn_EXnYrCN31oD-my8'
        #Confirm Token signature
        payload = json.dumps({"token": token})
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken"
        r1 = requests.post(rest_api_url, params={"key": WEB_API_KEY},data=payload)
        if "error" in r1.json():
            raise NotFound("Error Login")

        #If token ok get email
        info = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
        email = info["uid"]
        #TODO needs test
        type = info["claims"]["type"]
        return TokenResponse(userID=0,type = type,email = email)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    userManagement_pb2_grpc.add_UserManagementServicer_to_server(
        UserManagementService(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

