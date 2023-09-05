#servidor de ejemplo para testear GRPS

import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')

import logging 
import grpc

from concurrent import futures


from proto import receta_pb2 as receta_pb2
from proto import receta_pb2_grpc as receta_pb2_grpc

class RecetaServicer(receta_pb2_grpc.servicioRecetaServicer):
    def traerRecetasPor(self, request, context):
        print("A ve")
        print(request.creador)
        print("A11111")
        
        receta1 = receta_pb2.receta(
            
            titulo ="tomates con cherry",
            foto = "agregar foto",
            tpMin = "3",
            tpMax = "10"
        )

        receta2 = receta_pb2.receta(
            titulo = "Palta con Pan",
            foto = "no tenemos",
            tpMin = "3",
            tpMax = "10"
        )

        listaRecetas = [receta1, receta2]
        print("Enviando recetas al cliente")
        respuesta = receta_pb2.traerRecetasPorResponse(recetas=listaRecetas)
        return respuesta

def iniciar_servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    receta_pb2_grpc.add_servicioRecetaServicer_to_server(RecetaServicer(), server)
    server.add_insecure_port('[::]:50051')  # Escucha en el puerto 50051 sin cifrado
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    
    print("arrancando el server")
    iniciar_servidor()