from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from reviews_pb2 import (
    ReviewObject,
    ListReviewsResponse
)
import reviews_pb2_grpc

class ReviewService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        return
    def AddReview(self, request, context):
        return
    def UpdateReview(self, request, context):
        return
    def DeleteReview(self, request, context):
        return
    def ListReviews(self, request, context):
        return


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    reviews_pb2_grpc.add_ReviewsServicer_to_server(
        ReviewService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()