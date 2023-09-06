#servidor de ejemplo para testear GRPS

import os, sys

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


from DAO.RecetaDAO import RecetaDAO
from DAO.UsuarioDAO import UsuarioDAO

from Receta import *

#### Aca te entra los request de RECETAS
class RecetaServicer(receta_pb2_grpc.servicioRecetaServicer):
    def traerRecetasPor(self, request, context):
        print(request.creador)
        print(request.categoria)
        responseListaRecetas=[]
    
            
        listaRecetas=[]

        if(request.creador == "" and request.categoria == ""):
            listaRecetas=RecetaDAO().traerRecetas()
        elif(request.categoria != ""):
            listaRecetas=RecetaDAO().traerRecetasxCategoria(request.categoria)
        else:
            listaRecetas=RecetaDAO().traerRecetasxCreador(request.creador)


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
            )
            responseListaRecetas.append(re)
        print(responseListaRecetas)
        respuesta = receta_pb2.traerRecetasPorResponse(recetas=responseListaRecetas)
        return respuesta
    def crearReceta(self, request, context):
        print(request)
        print(context)
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
        adminreceta.agregarReceta(receta)
   
        print(receta_pb2)
        respuesta = receta_pb2.status(status=1)
        return respuesta



#### Aca te entra los request de Usuario
class UsuarioServicer(usuario_pb2_grpc.servicioUsuarioServicer):
    def seguirUsuario(self, request, context):
        respuesta = usuario_pb2.solicitudDeSeguidorResponse(mensaje="Usuario SEGUIDO")
        return respuesta
    def loguearUsuario(self, request, context):
        
        udao = UsuarioDAO()
        ustmp = udao.traerUsuarioSIMPLE(request.username);
        
        if(ustmp == None):
            respuesta = usuario_pb2.loguearUsuarioResponse(username=request.username, estado="No existe el usuario")
        else:
            if(ustmp["password"] == request.password):
                respuesta = usuario_pb2.loguearUsuarioResponse(username=request.username, estado="VALIDO")
            else:
                respuesta = usuario_pb2.loguearUsuarioResponse(username=request.username, estado="Contra MAlaa")

        return respuesta
    
    def crearUsuario(self, request, context):
        
        print("LLEGO ALGO EHHHH")
        print("username:" + request.username)
        print("email:" + request.email)
        print("password: " + request.password)
        print("tipo: " + request.tipo)

        #Logica de crear usuario conexion a la bd y eso
        respuesta = usuario_pb2.crearUsuarioResponse(
            username=request.username,
            mensaje="alta exitosa"
        )
        return respuesta

def iniciar_servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    receta_pb2_grpc.add_servicioRecetaServicer_to_server(RecetaServicer(), server)
    usuario_pb2_grpc.add_servicioUsuarioServicer_to_server(UsuarioServicer(), server)
    server.add_insecure_port('[::]:50051')  # Escucha en el puerto 50051 sin cifrado
    server.start()
    logging.basicConfig(level=logging.DEBUG) 
    logging.info("Servidor gRPC iniciado en el puerto 50051")
    
    server.wait_for_termination()
    

if __name__ == '__main__':
    print("current dir: " + CURRENT_DIR)
    iniciar_servidor()
    