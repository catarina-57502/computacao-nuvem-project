## app.py - Datasets files (csv) to MongoDB
## Version: 1.0
## Cloud Computing - 2022
## Group 7 

STEAM_REVIEWS = './csvFiles/steam_reviews_eng.csv'
STEAM_GAMES = './csvFiles/steam_games.csv'

CONNECTION_STRING = "mongodb://admin:admin@127.0.0.1:27017/admin"

def writeCSVtoDB(CSVFile,tableDB):

    import csv
    from csv import reader
    import pymongo

    #Allow big reviews inputs
    csv.field_size_limit(100000000)
    atributes = []

    print("Opening file:",CSVFile)
    try:
        file = open(CSVFile, 'r',encoding="utf8")
    except OSError:
        print ("Could not open/read file:", CSVFile)
        sys.exit()
    num = 1
    listDocs = []
    numberWriteToDB = 500000
    print("Writing to DB!")
    with file as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if num == 1:
                atributes = row
                num = num + 1
            else:
                n = 0
                doc = {}
                for value in row:
                    if(atributes[n] != ''):
                        doc[atributes[n]] = value
                    n = n + 1
                listDocs.append(doc)
                if num == numberWriteToDB:
                    print("Added: ",num)
                    tableDB.insert_many(listDocs)
                    listDocs = []
                    numberWriteToDB = numberWriteToDB + 500000
                num = num + 1
        tableDB.insert_many(listDocs)
        listDocs = []
    file.close()
    print("DONE", CSVFile)
def get_database():
    from pymongo import MongoClient
    import pymongo

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    print("DataBase Created")
    return client['steam']

def get_databaseUsers():
    from pymongo import MongoClient
    import pymongo

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    print("DataBase Created")
    return client['users']

def get_table(db,table):
    print("Table:",table,"created!")
    return db[table]

if __name__ == "__main__":
    def writeUser(dbUsers):
        library = [
            "6240977ffee051363df02ff9",
            "6240977ffee051363df03003",
        ]
        wishlist = [
            "6240977ffee051363df0300c",
        ]
        myquery = { "userid": "00000000000000000",
                "nickname": "userTest",
                "email": "teste@teste.com",
                "password": "qwerty",
                "type": "user",
                "library": library,
                "wishlist": wishlist
                }
        dbUsers.insert_one(myquery)
    
if __name__ == "__main__":    

    print("WELCOME")
    db = get_database()
    dbReviews = get_table(db,'Reviews')
    dbGames = get_table(db,'Games')
    dbUsers = get_table(get_databaseUsers(),'users')
    # Reviews and games
    #writeCSVtoDB(STEAM_REVIEWS,dbReviews)
    #writeCSVtoDB(STEAM_GAMES,dbGames)
    # User default
    writeUser(dbUsers)
