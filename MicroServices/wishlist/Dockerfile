FROM python

RUN mkdir /service
COPY ./  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 27019
ENTRYPOINT [ "python", "wishlist.py" ]