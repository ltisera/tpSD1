cd grpc-server/proto
export PYTHONPATH=${PYTHONPATH}:~/dev/tpSD1/grpc-server/DAO
export PYTHONPATH=${PYTHONPATH}:~/dev/tpSD1/grpc-server/proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. receta.proto usuario.proto

cd ..
python server.py