from concurrent import futures
import random

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from userManagement_pb2 import (
    User,DefaultResponse
)
import userManagement_pb2_grpc
import pymongo
from pymongo import MongoClient

import uuid

def get_table(db,table):
    return db[table]

client = MongoClient('172.23.0.9', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")


def createdoc(request):
    return {
        "userid":request.url,
        "nickname":request.types,
        "password":request.name,
        "email":request.desc_snippet,
        "library":request.recent_reviews,
        "wishlist":request.all_reviews
    }

class UserManagementService(userManagement_pb2_grpc.UserManagementServicer):
    def AddUser(self, request, context):
        library = [
             "6240977ffee051363df02ff9",
            "6240977ffee051363df03003",
        ]
        wishlist = [
            "6240977ffee051363df0300c",
        ]
        myquery = { "userid": uuid.uuid4().hex,
                    "nickname": request.nickname,
                    "email": request.email,
                    "password": request.password,
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
        password = request.password
        new_password = request.new_password
        email = request.email
        new_email = request.new_email
        nickname = request.nickname
        id = 0
        docUser = usersDB.find({"email": email} )
        for doc in docUser:
            library = doc["library"]
            wishlist = doc["wishlist"]
            if(password == doc["password"]):
                usersDB.delete_one({"email": email})
                if(new_password != ""):
                   password = new_password
                if(email != ""):
                    email = email
                if(nickname != ""):
                    nickname = nickname
                if(email != ""):
                    email = new_email
                id = doc["userid"]
            else:
                return DefaultResponse(code=400,message="Password incorrect")
            userUpdatedDoc = {
                "userid": id,
                "nickname": nickname,
                "email": email,
                "password": password,
                "library": library,
                "wishlist": wishlist
            }
            usersDB.insert_one(userUpdatedDoc)
            return DefaultResponse(code=200,message="User Updated")
        return DefaultResponse(code=400,message="Not found - User")
    def LoginUser(self, request, context):
        email = request.email
        password = request.password
        message = "User ", email, "login"
        return DefaultResponse(message=message)

    def Logout(self, request, context):
        email = request.email
        password = request.password
        message = "User ", email, "logout..."
        return DefaultResponse(message=message)



def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    userManagement_pb2_grpc.add_UserManagementServicer_to_server(
        UserManagementService(), server
    )
    server.add_insecure_port("[::]:50054")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

