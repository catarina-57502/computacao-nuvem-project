# syntax=docker/dockerfile:1

FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY api/ /service/reviews-api/

WORKDIR /service/reviews-api
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN pip uninstall -y protobuf python3-protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/reviews.proto

EXPOSE 5012
ENV FLASK_APP=reviews-api.py
ENV FLASK_RUN_PORT=5012
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]