### Generate protofus files

```bash
python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/adminOperations.proto
```

### Create Containers

```bash
docker build . -f main/Dockerfile -t adminoperations
docker build . -f server/Dockerfile -t serveradminoperations
```

### Run Containers

```bash
docker run -p 127.0.0.1:50052:50052 --network test --name adminoperations adminoperations
docker run -p 127.0.0.1:5000:5000 --network test -e ADMINOPERATIONS_HOST=adminoperations serveradminoperations
```

### Important Notes (delete)
Dont forget to create a network  
```bash
docker network create test
```
For the DB container to communicate with the other containers you need to check the ip of the mongodb container:  
```bash
docker exec -it mongodb /bin/bash
hostname -i
```
You should use that IP to create the db connections  