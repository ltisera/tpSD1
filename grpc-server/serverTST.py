#servidor de ejemplo para testear GRPS

import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')

import logging 
import grpc

from concurrent import futures


from proto import usuario_pb2 as usuario_pb2
from proto import usuario_pb2_grpc as usuario_pb2_grpc

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
    usuario_pb2_grpc.add_servicioUsuarioServicer_to_server(UsuarioServicer(), server)
    server.add_insecure_port('[::]:50051')  # Escucha en el puerto 50051 sin cifrado
    server.start()
    logging.basicConfig(level=logging.DEBUG) 
    logging.info("Servidor gRPC iniciado en el puerto 50051")
    
    server.wait_for_termination()
    

if __name__ == '__main__':
    print("arrancando el server")
    iniciar_servidor()