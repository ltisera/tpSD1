cd grpc-server/proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. receta.proto

cd ..
python server.py