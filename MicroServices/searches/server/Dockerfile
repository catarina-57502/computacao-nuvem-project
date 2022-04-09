FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/searches/

WORKDIR /service/searches
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN pip3 install pymongo
RUN pip install grpc-interceptor
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/searches.proto

EXPOSE 50079
ENTRYPOINT [ "python", "searches.py" ]
