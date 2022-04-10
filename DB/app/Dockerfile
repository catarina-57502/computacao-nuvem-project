FROM python

RUN mkdir /service
COPY app/ /service/writedb/

WORKDIR /service/writedb
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]