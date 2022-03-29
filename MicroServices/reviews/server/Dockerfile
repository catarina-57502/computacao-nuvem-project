# syntax=docker/dockerfile:1

FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY server/ /service/reviews-server/

WORKDIR /service/reviews-server
RUN pip install -r requirements.txt
RUN pip uninstall -y protobuf python3-protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/reviews.proto

EXPOSE 50055
ENTRYPOINT [ "python", "reviews-server.py" ]