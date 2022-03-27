### Generate protofus files

```bash
python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/adminOperations.proto
```