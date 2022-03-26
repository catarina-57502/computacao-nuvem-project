from concurrent import futures
import os

import grpc
from library_pb2 import *
from library_pb2_grpc import LibraryStub
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

class LibraryService(library_pb2_grpc.LibraryServicer):

    def AddGameLib(self, request, context):


    def ListGamesLib(self, request, context):


    def RemoveGameLib(self, request, context):


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryService(), server
    )
    """
    with open("server.key", "rb") as fp:
        server_key = fp.read()
    with open("server.pem", "rb") as fp:
        server_cert = fp.read()
    with open("ca.pem", "rb") as fp:
        ca_cert = fp.read()

    creds = grpc.ssl_server_credentials(
        [(server_key, server_cert)],
        root_certificates=ca_cert,
        require_client_auth=True,
    )
    """
    server.add_insecure_port("[::]:27018")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
