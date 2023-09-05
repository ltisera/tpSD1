#servidor de ejemplo para testear GRPS

import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')

import grpc

from concurrent import futures


import usuario_pb2
import usuario_pb2_grpc

class UsuarioServicer(usuario_pb2_grpc.servicioUsuarioServicer):
    def crearUsuario(self, request, context):
        
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
    server.wait_for_termination()

if __name__ == '__main__':
    print("arrancando el server")
    iniciar_servidor()