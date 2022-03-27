from concurrent import futures
import os

import grpc
from wishlist_pb2 import *
from wishlist_pb2_grpc import WishlistStub
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

class WishlistService(wishlist_pb2_grpc.WishlistServicer):

    def AddGameWish(self, request, context):


    def ListGamesWish(self, request, context):


    def RemoveGameWish(self, request, context):


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    wishlist_pb2_grpc.add_WishlistServicer_to_server(
        WishlistService(), server
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
    server.add_insecure_port("[::]:27019")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
