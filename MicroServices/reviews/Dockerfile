# syntax=docker/dockerfile:1

FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY reviews/ /service/reviews/

WORKDIR /service/reviews
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/reviews.proto

EXPOSE 50051
ENTRYPOINT [ "python", "reviews.py" ]