FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY server/ /service/wishlistServer/


WORKDIR /service/wishlistServer
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/wishlist.proto

EXPOSE 5000
ENV FLASK_APP=wishlistServer.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]