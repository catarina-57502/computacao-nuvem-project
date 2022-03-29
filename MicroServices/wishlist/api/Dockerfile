FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY api/ /service/wishlist-api/

WORKDIR /service/wishlist-api
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/wishlist.proto

EXPOSE 5002
ENV FLASK_APP=wishlist-api.py
ENV FLASK_RUN_PORT=5002
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]