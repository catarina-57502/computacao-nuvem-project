FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/userManagementServer/


WORKDIR /service/userManagementServer
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/userManagement.proto

EXPOSE 5004
ENV FLASK_APP=userManagementServer.py
ENV FLASK_RUN_PORT=5004
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
