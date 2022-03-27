import pymongo
from pymongo import MongoClient


def get_table(db,table):
    return db[table]

client = MongoClient('localhost', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

docUser = usersDB.find({"email": "martimmourao@gmail.com"} )
for doc in docUser:
    print(doc["userid"])