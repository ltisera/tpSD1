#servidor de ejemplo para testear GRPS

import os, sys

from time import sleep  
from json import dumps  
from kafka import KafkaProducer  
from kafka import KafkaConsumer

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(CURRENT_DIR + '\\proto')
sys.path.append(CURRENT_DIR + '\\DAO')

import logging 
import grpc
import mysql.connector
import json
from mysql.connector import Error
from concurrent import futures


from proto import usuario_pb2 as usuario_pb2
from proto import usuario_pb2_grpc as usuario_pb2_grpc
from proto import receta_pb2 as receta_pb2
from proto import receta_pb2_grpc as receta_pb2_grpc
from proto import comentarios_pb2 as comentarios_pb2
from proto import comentarios_pb2_grpc as comentarios_pb2_grpc


from DAO.RecetaDAO import RecetaDAO
from DAO.UsuarioDAO import UsuarioDAO
from DAO.ComentarioDAO import ComentarioDAO
from DAO.CONFIGS.variablesGlobales import *

from objetos.Receta import *
from objetos.Usuario import *
from objetos.Comentario import *

### Productor kafka popularidadReceta
def popularidadReceta(idReceta, signo):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  
    mkafka = {
        "idReceta": idReceta, 
        "popularidad" : signo
    }
    #signo + para agregar 1 o - para restar 1
    print("este es el json") 
    print(mkafka)
    producer.send(topic = TOPIC_RECIPE_POPULARIDAD, value=json.dumps(mkafka).encode("utf-8"))
    producer.close()

### Productor kafka popularidadUsuario
def popularidadUsuario(usuario, signo):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  
    mkafka = {
        "usuario": usuario, 
        "popularidad" : signo
    }
    #signo + para agregar 1 o - para restar 1
    print("este es el json") 
    print(mkafka)
    producer.send(topic = TOPIC_USUARIO_POPULARIDAD, value=json.dumps(mkafka).encode("utf-8"))
    producer.close()

class ComentarioServicer(comentarios_pb2_grpc.servicioComentariosServicer):
    
    def crearComentario(self,request,context):
        admincomentario = ComentarioDAO()
        comentario = Comentario()
        comentario.idReceta = request.idReceta
        comentario.idUsuario = request.idUsuario
        comentario.comentario = request.comentario
        #admincomentario.agregarComentario(comentario)
        #Ya nno persistimos el comentario
        respuesta = comentarios_pb2.comentarioStatus(estado=1)
        return respuesta
    
    
    def eliminarComentario(self,request,context):
        admincomentario = ComentarioDAO()
        print(request.idComentario)
        admincomentario.eliminarComentario(request.idComentario)
        respuesta = comentarios_pb2.comentarioStatus(estado=1)
        return respuesta

    def obtenerComentarios(self,request,context):
        responseListaComentarios=[]
        listaComentarios=[]
        listaComentarios=ComentarioDAO().traerComentarios(request.idReceta)
        for com in listaComentarios:
            comentario=comentarios_pb2.comentario(
                idComentario = com["idComentario"],
                idReceta = com["idReceta"],
                idUsuario = com["idUsuario"],
                comentario = com["comentario"],
            )
            responseListaComentarios.append(comentario)
        respuesta = comentarios_pb2.traerComentariosResponse(comentarios=responseListaComentarios)
        return respuesta


#### Aca te entra los request de RECETAS
class RecetaServicer(receta_pb2_grpc.servicioRecetaServicer):
    def traerRecetasPor(self, request, context):
        responseListaRecetas=[]
        print("MIRA")
        if((request.tiempoEnMinutosMIN == "") 
            & (request.tiempoEnMinutosMIN == "")
            & (request.tiempoEnMinutosMIN == "")
            & (request.tiempoEnMinutosMAX == "")
            & (request.categoria == "")
            & (request.creador == "")
            & (request.titulo == "")
            & (request.idReceta == "")
            & (request.ingredientes == "")):
        
            # Configura las opciones del consumidor
            consumer = KafkaConsumer(
                'novedades',
                bootstrap_servers='localhost:9092',  # Reemplaza con la dirección de tu servidor Kafka
                group_id="un grupo",  # Puedes usar cualquier grupo de consumidores
                auto_offset_reset='latest',  # Lee desde la posición más reciente
                enable_auto_commit=False  # Desactiva el auto commit
            )




            # Obtiene la cantidad total de mensajes en el tema
            consumer.poll()
            consumer.seek_to_end()
            assignment = list(consumer.assignment())
            # Verificar si hay particiones antes de continuar
            if assignment:
                # Obtener la cantidad total de mensajes en la primera partición
                total_messages = consumer.position(assignment[0])
                # Lleva un registro de cuántos mensajes has consumido
                num_messages_to_read = 5
                messages_read = 0

                # Resto del código para leer los últimos mensajes
                # Lee los últimos 5 mensajes en orden inverso
                for _ in range(num_messages_to_read):
                    position = total_messages - messages_read - 1
                    if(position < 0):
                        break
                    consumer.seek(assignment[0], position)
                    message = next(consumer)
                    print('Mensaje leído: {}'.format(message.value.decode('utf-8')))
                    messages_read += 1


            # Cierra el consumidor al final
            consumer.close()
            respuesta=receta_pb2.receta(
                titulo = "titulo",
                descripcion = "descripcion",
                pasos = "pasos",
                tiempoEnMinutos = 2,
                categoria = "categoria",
                creador = "creador",
                foto1 = "foto1",
                foto2 = "foto2",
                foto3 = "foto3",
                foto4 = "foto4",
                foto5 = "foto5",
                idReceta = 33,
                ingredientes = "ingredientes",
            )
            print("Trqanqui que no cuelgo")
            return respuesta
            

        else:
            listaRecetas=RecetaDAO().traerRecetasXFiltro(
                tiempoEnMinutosMIN=request.tiempoEnMinutosMIN,
                tiempoEnMinutosMAX=request.tiempoEnMinutosMAX,
                categoria=request.categoria,
                creador=request.creador,
                titulo=request.titulo,
                idReceta=request.idReceta,
                ingredientes = request.ingredientes,
            )
            
            for rec in listaRecetas:
                re=receta_pb2.receta(
                    titulo = rec["titulo"],
                    descripcion = rec["descripcion"],
                    pasos = rec["pasos"],
                    tiempoEnMinutos = rec["tiempoEnMinutos"],
                    categoria = rec["categoria"],
                    creador = rec["creador"],
                    foto1 = rec["foto1"],
                    foto2 = rec["foto2"],
                    foto3 = rec["foto3"],
                    foto4 = rec["foto4"],
                    foto5 = rec["foto5"],
                    idReceta = rec["idReceta"],
                    ingredientes = rec["ingredientes"],
                )
                responseListaRecetas.append(re)
            respuesta = receta_pb2.traerRecetasPorResponse(recetas=responseListaRecetas)
            return respuesta

    def traerReceta(self, request, context):
        rec=RecetaDAO().traerReceta(request.idReceta)
        respuesta=receta_pb2.receta(
            titulo = rec["titulo"],
            descripcion = rec["descripcion"],
            pasos = rec["pasos"],
            tiempoEnMinutos = rec["tiempoEnMinutos"],
            categoria = rec["categoria"],
            creador = rec["creador"],
            foto1 = rec["foto1"],
            foto2 = rec["foto2"],
            foto3 = rec["foto3"],
            foto4 = rec["foto4"],
            foto5 = rec["foto5"],
            idReceta = rec["idReceta"],
            ingredientes = rec["ingredientes"],
        )
        return respuesta

    def agregarIngredienteAReceta(self, request, context):
        rDAO = RecetaDAO()
        res = rDAO.agregarIngredienteAReceta(request.idReceta, request.ingrediente, request.cantidad, request.tipoDeMedida)
        respuesta = receta_pb2.agregarIngredienteARecetaResponse(mensaje=res)
        return respuesta

    def traerIngredientesDeReceta(self, request, context):
        responseListaIngredientes=[]
        listaIngredientes=[]
        listaIngredientes=RecetaDAO().traerIngredientesDeReceta(request.idReceta)

        for ing in listaIngredientes:
            ingrediente=receta_pb2.ingredienteDeReceta(
                nombre = ing["ingrediente"],
                cantidad = ing["cantidad"],
                tipoDeMedida = ing["tipoDeMedida"],
            )
            responseListaIngredientes.append(ingrediente)
        respuesta = receta_pb2.listaIngredientesPorResponse(ingredientes=responseListaIngredientes)
        return respuesta

    def crearReceta(self, request, context):
        print("QUE RECIBNO DE ESTE MUCHACHO")
        print(request)
        print("Esto recibi")
        adminreceta = RecetaDAO()
        receta = Receta()
        receta.titulo = request.titulo
        receta.descripcion = request.descripcion
        receta.foto1 = request.foto1
        receta.foto2 = request.foto2
        receta.foto3 = request.foto3
        receta.foto4 = request.foto4
        receta.foto5 = request.foto5
        receta.pasos = request.pasos
        receta.tiempoEnMinutos = request.tiempoEnMinutos
        receta.categoria = request.categoria
        receta.creador = request.creador
        receta.ingredientes= request.ingredientes
        idUltimaReceta = adminreceta.agregarReceta(receta)
        ### Productor kafka
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        mkafka = {
            "idReceta": idUltimaReceta, 
            "tituloReceta" : receta.titulo,
            "urlFoto": receta.foto1,
            "usuario" : receta.creador
        }
        print("este es el json") 
        print(mkafka)
        producer.send(topic = TOPIC_NOVEDADES, value=json.dumps(mkafka).encode("utf-8"))
        producer.close()
        respuesta = receta_pb2.status(status=1)
        return respuesta
    
    def editarReceta(self, request, context):
        adminreceta = RecetaDAO()
        receta = Receta()
        receta.titulo = request.titulo
        receta.descripcion = request.descripcion
        receta.foto1 = request.foto1
        receta.foto2 = request.foto2
        receta.foto3 = request.foto3
        receta.foto4 = request.foto4
        receta.foto5 = request.foto5
        receta.pasos = request.pasos
        receta.tiempoEnMinutos = request.tiempoEnMinutos
        receta.categoria = request.categoria
        receta.creador = request.creador
        receta.ingredientes= request.ingredientes
        receta.idReceta = request.idReceta
        adminreceta.modificarReceta(receta)
        
        respuesta = receta_pb2.status(status=1)
        return respuesta
    
    def eliminarReceta(self, request,context):
        adminreceta = RecetaDAO()
        print(request)
        adminreceta.eliminarReceta(idReceta=request.idReceta)
        
        respuesta = receta_pb2.status(status=1)
        return respuesta
    
    def agregarRecetaAFavoritos(self, request, context):
        rdao = RecetaDAO()
        res = rdao.agregarFavorito(request.usuario, request.idReceta)
        popularidadReceta(request.idReceta, "+")
        return res
    def eliminarRecetaDeFavoritos(self, request, context):
        rdao = RecetaDAO()
        print(request)
        res = rdao.eliminarFavorito(request.usuario, request.idReceta)
        popularidadReceta(request.idReceta, "-")
        return res

    def traerRecetasFavoritas(self, request, context):
        responseListaRecetas=[]            
        listaRecetas = RecetaDAO().traerRecetasFavoritas(request.usuario)
        for rec in listaRecetas:
            re=receta_pb2.receta(
                titulo = rec["titulo"],
                tiempoEnMinutos = rec["tiempoEnMinutos"],
                creador = rec["creador"],
                foto1 = rec["foto1"],
                idReceta = rec["idReceta"],
            )
            responseListaRecetas.append(re)
        respuesta = receta_pb2.traerRecetasPorResponse(recetas=responseListaRecetas)
        return respuesta

#### Aca te entra los request de Usuario
class UsuarioServicer(usuario_pb2_grpc.servicioUsuarioServicer):
    
    def seguirUsuario(self, request, context):
        udao = UsuarioDAO()
        print(request.usuarioQueSigue, request.usuarioSeguido)
        res = udao.seguirUsuario(request.usuarioQueSigue, request.usuarioSeguido)
        respuesta = usuario_pb2.solicitudDeSeguidorResponse(mensaje=res)
        popularidadUsuario(request.usuarioSeguido, "+")
        return respuesta
    
    def dejarDeSeguirUsuario(self, request, context):
        udao = UsuarioDAO()
        print(request.usuarioQueSigue, request.usuarioSeguido)
        res = udao.dejarDeSeguirUsuario(request.usuarioQueSigue, request.usuarioSeguido)
        respuesta = usuario_pb2.solicitudDeSeguidorResponse(mensaje=res)
        popularidadUsuario(request.usuarioSeguido, "-")
        return respuesta

    def traerUsuariosQueMeSiguen(self, request, context):
        responseListaUsuarios=[] 
        listaUsuario=[]
        udao = UsuarioDAO()
        listaUsuario = udao.traerUsuariosQueMeSiguen(request.usuario)
        for us in listaUsuario:
            responseListaUsuarios.append(us["Usuario_Seguidor"])
        respuesta = usuario_pb2.traerUsuariosQueSigoResponse(usuarios=responseListaUsuarios)
        return respuesta

    def traerUsuariosQueSigo(self, request, context):
        responseListaUsuarios=[] 
        listaUsuario=[]
        udao = UsuarioDAO()
        listaUsuario = udao.traerUsuariosQueSigo(request.usuario)
        for us in listaUsuario:
            responseListaUsuarios.append(us["Usuario_Seguido"])
        respuesta = usuario_pb2.traerUsuariosQueSigoResponse(usuarios=responseListaUsuarios)
        return respuesta

    def loguearUsuario(self, request, context):
        udao = UsuarioDAO()
        ustmp = udao.traerUsuarioSIMPLE(request.email);

        if(ustmp == None):
            respuesta = usuario_pb2.loguearUsuarioResponse(username=ustmp["usuario"], estado="NO_EXISTE_EL_USUARIO")
        else:
            if(ustmp["password"] == request.password):
                print("Te pasamos")
                print(ustmp["usuario"])
                print("Esto")
                respuesta = usuario_pb2.loguearUsuarioResponse(username=ustmp["usuario"], estado="VALIDO")
            else:
                respuesta = usuario_pb2.loguearUsuarioResponse(username=ustmp["usuario"], estado="INVALIDO")
        return respuesta
    
    def crearUsuario(self, request, context):
        udao = UsuarioDAO()
        ustmp = udao.traerUsuarioSIMPLE(request.username);
        msj = ""
        if (ustmp == None):
            us = Usuario()
            us.idUsuario = request.username
            us.email = request.email
            us.password = request.password
            us.tipo = request.tipo
            msj = udao.agregarUsuario(us)
        else:
            msj = "YA_EXISTE_EL_USUARIO"

        respuesta = usuario_pb2.crearUsuarioResponse(
            username = request.username,
            mensaje = msj,
        )
        return respuesta

def iniciar_servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    receta_pb2_grpc.add_servicioRecetaServicer_to_server(RecetaServicer(), server)
    usuario_pb2_grpc.add_servicioUsuarioServicer_to_server(UsuarioServicer(), server)
    comentarios_pb2_grpc.add_servicioComentariosServicer_to_server(ComentarioServicer(), server)
    server.add_insecure_port('[::]:50051')  # Escucha en el puerto 50051 sin cifrado
    server.start()
    logging.basicConfig(level=logging.ERROR) 
    logging.info("Servidor gRPC iniciado en el puerto 50051")
    
    server.wait_for_termination()
    

if __name__ == '__main__':


    #producer = KafkaProducer(bootstrap_servers='localhost:9092')  # Cambia esto a la dirección de tu servidor Kafka
    # Enviar un mensaje al tema 'mi-topic'
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO A')
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO B')
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO C')
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO D')
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO E')
    #producer.send('mi-topic', key=b'clave', value=b'CAMBIO F')

    # Cerrar el productor después de enviar el mensaje
    #producer.close()
    
    print("current dir: " + CURRENT_DIR)
    iniciar_servidor()
    