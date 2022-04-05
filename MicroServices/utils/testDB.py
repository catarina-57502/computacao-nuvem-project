import pymongo
from pymongo import MongoClient


def get_table(db,table):
    return db[table]

client = MongoClient('localhost', 27017 ,username='admin', password='admin' )
db = client['users']
usersDB = get_table(db,"users")

docUser = usersDB.find({"userid": request.userid} )
for doc in docUser:
    library = doc["library"]
    wishlist = doc["wishlist"]
    wishlist.append(request.gameid)
    doc["wishlist"] = wishlist
    usersDB.delete_one({"userid": userid})
    usersDB.insert_one(doc)

dict = {}
i = 0
for game in games:
    str = "" + i
    dict[str] = game