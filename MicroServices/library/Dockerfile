FROM python

RUN mkdir /service
COPY ./  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 27018
ENTRYPOINT [ "python", "library.py" ]