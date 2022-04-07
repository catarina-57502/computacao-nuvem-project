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
    info = jwt.decode(token, key_secret, algorithms=["HS256"])
    email = info["email"]
    userid = info["userID"]
    type = info["type"]
    return email

class UserManagementService(userManagement_pb2_grpc.UserManagementServicer):
    def AddUser(self, request, context):
        library = []
        wishlist = []
        myquery = { "userid": uuid.uuid4().hex,
                    "nickname": request.nickname,
                    "email": request.email,
                    "password": request.password,
                    "type": request.type,
                    "library": library,
                    "wishlist": wishlist
                    }
        myqueryemail = { "email": request.email}
        if usersDB.count_documents(myqueryemail) == 0 :
            usersDB.insert_one(myquery)
            return DefaultResponse(code=200,message="User Added")
        else:
            return DefaultResponse(code=409,message="Error - User already exists")

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
    def LoginUser(self, request, context):
        password = request.password
        email = request.email
        docUser = usersDB.find({"email": email} )
        for doc in docUser:
            if(password == doc["password"]):
                #Password Correct
                encoded_jwt = jwt.encode({
                    "userID": doc["userid"],
                    "type": doc["type"],
                    "email": doc["email"],
                },
                key_secret,
                algorithm="HS256")
                return LoginResponse(token=encoded_jwt)
            else:
                return LoginResponse(token="Error")
        return LoginResponse(token="Error")

    def Logout(self, request, context):
        email = request.email
        message = "User ", email, "logout..."
        return DefaultResponse(message=message)

    def GetInfoFromToken(self, request, context):
        token = request.token
        info = jwt.decode(token, key_secret, algorithms=["HS256"])
        email = info["email"]
        userid = info["userID"]
        type = info["type"]
        return TokenResponse(userID=userid,type = type,email = email)

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

