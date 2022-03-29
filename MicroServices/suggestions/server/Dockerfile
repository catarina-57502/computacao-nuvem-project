FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/suggestionsServer/


WORKDIR /service/suggestionsServer
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN pip uninstall -y protobuf python3-protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/suggestions.proto

EXPOSE 5008
ENV FLASK_APP=suggestionsServer.py
ENV FLASK_RUN_PORT=5008
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
