FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/adminOperations/

WORKDIR /service/adminOperations
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/adminOperations.proto
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/userManagement.proto

EXPOSE 50052
ENTRYPOINT [ "python", "adminOperations.py" ]
