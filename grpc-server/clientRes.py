import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')

import grpc
from proto import receta_pb2 as receta_pb2
from proto import receta_pb2_grpc as receta_pb2_grpc


def traerRecetaPor(cliente):
#    sol = usuario_pb2.crearUsuarioRequest(
#        username = "pepe",
#        email = "notiene@gmail.com",
#        password = "asd",
#        tipo = "usuario"
#    )

    sol = receta_pb2.traerRecetasPorRequest(
        tiempoEnMinutos = "20",
        categoria = "Desayuno",
        creador = "MATHOV"
    )

    respuesta = cliente.traerRecetasPor(sol)
    print("Mensaje del server", respuesta)



def main():
    canal = grpc.insecure_channel('localhost:50051')
    cliente = receta_pb2_grpc.servicioRecetaStub(canal)
    traerRecetaPor(cliente)

if __name__ == '__main__':
    main()

