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

# Demo
## Entrega uno
### Login
![localhost_3000_login_](https://github.com/ltisera/tpSD1/assets/70329467/4f3ba121-2b1e-4a10-af97-7ccd3bb5a3e4)
### Registro
![localhost_3000_register_](https://github.com/ltisera/tpSD1/assets/70329467/3ddf80fb-e7ae-4013-b3b6-8c00c9d67379)
### Pagina de inicio
![localhost_3000_](https://github.com/ltisera/tpSD1/assets/70329467/0f0e406d-cc8b-418a-9984-c5686d4354d2)
### Búsqueda de receta
![localhost_3000__title=fri author= category= min-temp= max-temp=](https://github.com/ltisera/tpSD1/assets/70329467/7c1e93b8-f3dc-4808-b097-f6576c683d24)
### Marcar recetas como favoritas
![localhost_3000__title=fri author= category= min-temp= max-temp= (1)](https://github.com/ltisera/tpSD1/assets/70329467/780762a4-5cf6-40cd-96e8-16a710a7cdfd)
### Backoffice de recetas
![localhost_3000_backoffice_ (2)](https://github.com/ltisera/tpSD1/assets/70329467/7abd82d3-b432-4517-8d8b-d5485aa17c6d)
### Modal de creacion
![image](https://github.com/ltisera/tpSD1/assets/70329467/365c5226-b7b2-4912-8761-ea382d2daf22)
### Modal de edicion
![image](https://github.com/ltisera/tpSD1/assets/70329467/7f434bbb-ced0-4576-a499-9d4b5bd559ad)
### Eliminar recetas
![image](https://github.com/ltisera/tpSD1/assets/70329467/70ef91f7-b168-4cff-9009-8845d1d1ee8d)
### Panel de seguidores
![localhost_3000_followers_ (1)](https://github.com/ltisera/tpSD1/assets/70329467/63173bc1-09b7-4741-9eb6-21d15b4cb36b)
### Perfil de los usuarios
![localhost_3000_profile__author=roberto](https://github.com/ltisera/tpSD1/assets/70329467/0500810f-44d0-41d5-abbc-831a48d5a149)
### Detalle de las recetas
![localhost_3000_recipe__id=2](https://github.com/ltisera/tpSD1/assets/70329467/b6235e7c-035f-483d-8bf3-a2b782ddc4a0)

## Entrega dos
Las siguientes pruebas son hechas en dos navegadores diferentes con usuarios diferentes.
### Evento: publicar receta
[Screencast from 23-10-23 16:51:24.webm](https://github.com/ltisera/tpSD1/assets/70329467/8e9a6b1e-1311-4a12-9064-97daf1403575)
### Evento: popularidad de los seguidores
[Screencast from 23-10-23 16:56:04.webm](https://github.com/ltisera/tpSD1/assets/70329467/3492451f-74d4-4980-959c-ad1fa1220a4e)
### Comentarios en las recetas
[Screencast from 23-10-23 16:59:01.webm](https://github.com/ltisera/tpSD1/assets/70329467/5f3ef997-272d-4268-9370-4951026345eb)




# Puertos

Front: 3000

Websocket: 4004

Backend node: 3000

Backend python (GRPC): 50051

SQL: 3306

Broker kafka: 9092

Zookeeper: 2181
