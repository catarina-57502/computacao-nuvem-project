from concurrent import futures
import grpc

from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    caCRT = 'ca.crt'
    serverCRT = 'server.crt'
    serverKey = 'server.key'

    with open(caCRT, 'rb') as f:
        credsCA = f.read()
    with open(serverCRT, 'rb') as f:
        credsSCRT = f.read()
    with open(serverKey, 'rb') as f:
        credsSK = f.read()


    channel_creds = grpc.ssl_server_credentials([(credsSK, credsSCRT)], credsCA, False)

    server.add_secure_port("[::]:5051",channel_creds)
    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    serve()

