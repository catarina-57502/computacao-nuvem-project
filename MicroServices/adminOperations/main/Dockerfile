FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY main/ /service/adminOperations/

WORKDIR /service/adminOperations
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/adminOperations.proto

EXPOSE 50051
ENTRYPOINT [ "python", "adminOperations.py" ]
