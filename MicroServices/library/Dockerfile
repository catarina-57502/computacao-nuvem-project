# syntax = docker/dockerfile:1.0-experimental
# DOCKER_BUILDKIT=1 docker build . -f marketplace/Dockerfile -t marketplace --secret id=ca.key,src=ca.key

FROM python

RUN mkdir /service
COPY ../protobufs/ /service/protobufs/
COPY library/ /service/library/

WORKDIR /service/library
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/library.proto
#RUN openssl req -nodes -newkey rsa:4096 -subj /CN=library \
             #   -keyout client.key -out client.csr
#RUN --mount=type=secret,id=ca.key \
 #   openssl x509 -req -in client.csr -CA ca.pem -CAkey /run/secrets/ca.key \
   #              -set_serial 1 -out client.pem

EXPOSE 5000
ENV FLASK_APP=library.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]