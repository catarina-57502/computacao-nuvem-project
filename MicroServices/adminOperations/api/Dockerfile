FROM python

RUN mkdir /service
COPY /protobufs/ /service/protobufs/
COPY api/ /service/adminOperationAPI/


WORKDIR /service/adminOperationAPI
RUN pip install markupsafe==2.0.1
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/adminOperations.proto

EXPOSE 5003
ENV FLASK_APP=adminOperation-api.py
ENV FLASK_RUN_PORT=5003
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]