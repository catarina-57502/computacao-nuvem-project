FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/searchesServer/


WORKDIR /service/searchesServer
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/searches.proto

EXPOSE 5010
ENV FLASK_APP=searchesServer.py
ENV FLASK_RUN_PORT=5010
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]