FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/suggestions/

WORKDIR /service/suggestions
RUN pip install -r requirements.txt
RUN pip uninstall -y protobuf python3-protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \--grpc_python_out=. ../protobufs/suggestions.proto

EXPOSE 50059
EXPOSE 51059
ENTRYPOINT [ "python", "suggestions.py" ]
