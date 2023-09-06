#servidor de ejemplo para testear GRPS

import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')
sys.path.append(r'C:\Users\camil\Documents\GitHub\tpSD1\grpc-server\proto')
sys.path.append(r'C:\Users\camil\Documents\GitHub\tpSD1\grpc-server\DAO')

import logging 
import grpc

from concurrent import futures


from proto import usuario_pb2 as usuario_pb2
from proto import usuario_pb2_grpc as usuario_pb2_grpc
from proto import receta_pb2 as receta_pb2
from proto import receta_pb2_grpc as receta_pb2_grpc
from DAO.RecetaDAO import *

#### Aca te entra los request de RECETAS
class RecetaServicer(receta_pb2_grpc.servicioRecetaServicer):
    def traerRecetasPor(self, request, context):
        lstRecetas = []
        rdao = RecetaDAO()
        if(request.creador != ""):
            print("xcreador")
            lstRecetas = rdao.traerRecetasxCreador(request.creador)
        elif(request.categoria != ""):
            print("xcategoria")
            lstRecetas = rdao.traerRecetasxCategoria(request.categoria)
        else:
            print("xtiempo")
            lstRecetas = rdao.traerRecetasxTiempo(request.tpMin, request.tpMax)

        listaRecetas = []
        for r in lstRecetas:
            receta1 = receta_pb2.receta(
                titulo = str(r['titulo']),
                foto = str(r['foto1']),
                tpMin = str(r['tiempoEnMinutos']),
                tpMax = "",
                idReceta = str(r['idReceta'])
            )
            listaRecetas.append(receta1) 
        print("Enviando recetas al cliente")
        respuesta = receta_pb2.traerRecetasPorResponse(recetas=listaRecetas)
        return respuesta



#### Aca te entra los request de Usuario
class UsuarioServicer(usuario_pb2_grpc.servicioUsuarioServicer):
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
    print("arrancando el server")
    iniciar_servidor()