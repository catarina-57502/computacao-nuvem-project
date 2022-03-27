FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/libraryServer/


WORKDIR /service/libraryServer
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/library.proto

EXPOSE 5000
ENV FLASK_APP=libraryServer.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]