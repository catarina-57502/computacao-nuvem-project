from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from pymongo import MongoClient
from datetime import datetime

from logging_pb2 import (
    Log,
    Empty
)
import logging_pb2_grpc

client = MongoClient('mongo', 27017 ,username='YWRtaW4=', password='YWRtaW4=')
logs = client["steam"]
db = logs["logs"]
db_healthz = logs["healthz"]

class LoggingService(logging_pb2_grpc.LoggingServicer):
    def StoreLog(self, request, context):
        if(request.endpoint == "/healthz?"):
            db_healthz.insert_one({
                "operation": request.operation,
                "endpoint": request.endpoint,
                "status": request.status,
                "service": request.service,
                "remote_addr": request.remote_addr,
                "user": request.user,
                "host": request.host,
                "date": request.date
            })
        else:
            db.insert_one({
                "operation": request.operation,
                "endpoint": request.endpoint,
                "status": request.status,
                "service": request.service,
                "remote_addr": request.remote_addr,
                "user": request.user,
                "host": request.host,
                "date": request.date
            })            
        return Empty()

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    logging_pb2_grpc.add_LoggingServicer_to_server(
        LoggingService(), server
    )

    server.add_insecure_port("[::]:50160")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
