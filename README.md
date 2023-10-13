# Instalar

```bash
pip install mysql-connector-python grpcio-tools
```

# Correr server python

```bash
pip install mysql-connector-python grpcio-tools
```

# Iniciar base de datos

Copiar el contenido del archivo `grpc-server/ModeloWB/modeloDatosBDRecetas.sql`

```bash
mysql -u root -p
```

Introducir tu contraseña de root
Pegar contenido del archivo `grpc-server/ModeloWB/modeloDatosBDRecetas.sql`

### Puertos

Front: 3000
Backend node: 3000
Backend python (GRPC): 50051
Broker kafka: 9092
Zookeeper: 2181
