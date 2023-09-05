-desde python consola

pip install grpcio-tools

-y para compilar, te paras donde esta el archivo proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mi_archivo.proto

esto me genero 2 archivos py que voya ver como se usan

## Solucion de errores

Si ves este error al levantar el server python grpc

```bash
❯ python serverTST.py
Traceback (most recent call last):
  File "/home/julian/dev/tpSD1/grpc-server/serverTST.py", line 13, in <module>
    from proto import usuario_pb2_grpc as usuario_pb2_grpc
  File "/home/julian/dev/tpSD1/grpc-server/proto/usuario_pb2_grpc.py", line 5, in <module>
    import usuario_pb2 as usuario__pb2
ModuleNotFoundError: No module named 'usuario_pb2'
```

Solucion: https://stackoverflow.com/a/72372318

```bash
export PYTHONPATH=${PYTHONPATH}:/path/to/project/root/src/grpc/generated
```

## TODO

- Alta de usuarios
- Login
- Lista de receta
- Crear receta
- Mostrar receta

- Filtros de receta
  - Nombre
  - Tiempo
  - Categoria
  - Creador
