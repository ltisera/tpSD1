-desde python consola

pip install grpcio-tools

-y para compilar, te paras donde esta el archivo proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mi_archivo.proto

esto me genero 2 archivos py que voya ver como se usan