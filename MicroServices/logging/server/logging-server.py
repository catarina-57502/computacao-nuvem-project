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

client = MongoClient('mongo', 27017 ,username='admin', password='admin')
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

    keyfile = 'keys/serverLogging-key.pem'
    certfile = 'keys/serverLogging.pem'

    with open(keyfile,'rb') as f:
        private_key = f.read()

    with open(certfile,'rb') as f:
        certificate_chain = f.read()

    credentials = grpc.ssl_server_credentials([(private_key, certificate_chain)])
    server.add_secure_port("[::]:50160",credentials)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
