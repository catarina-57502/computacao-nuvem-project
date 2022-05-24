FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY api/ /service/userManagementAPI/


WORKDIR /service/userManagementAPI
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN pip uninstall -y protobuf python3-protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/logging.proto
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/userManagement.proto

EXPOSE 5004
ENV FLASK_APP=userManagement-api.py
ENV FLASK_RUN_PORT=5004
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
