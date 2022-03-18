# Instructions

### 0. CSV files 

Unzip the file Arquivo.zip!

### 1. Docker
Get mongoDB Container:

```bash
docker --version
docker pull mongo
docker run --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin mongo
```

### 2. Connect to DB
You can use "MongoDB Compass" - Compass is an interactive tool for querying, optimizing, and analyzing your MongoDB data.

```bash
mongodb://admin:admin@localhost:27017/admin
```

### 3. Requirements to run the python script
```bash
pip install python-csv
pip install pymongo
```

### 4. Run the python script
```bash
python3 app.py
```

### Notes
- The script takes 5 minutes to write all data... :/
- You only need to run the script once if you dont delete the container. Just Stop the container!

DB should have:  
Games: 40.833  
Reviews: 9.635.437   