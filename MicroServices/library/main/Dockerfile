FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY main/ /service/library/


WORKDIR /service/library
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN pip3 install pymongo
RUN pip install grpc-interceptor
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/library.proto

EXPOSE 50053
ENTRYPOINT [ "python", "library.py" ]