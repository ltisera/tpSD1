import sys
sys.path.append('C:\\Users\\LucsPC\\Downloads\\distribuidos\\Entrega\\tpBDR\\tpSD1\\grpc-server\\proto')

import grpc
from proto import usuario_pb2 as usuario_pb2
from proto import usuario_pb2_grpc as usuario_pb2_grpc

def crearUsuario(cliente):
    sol = usuario_pb2.crearUsuarioRequest(
        username = "pepe",
        email = "notiene@gmail.com",
        password = "asd",
        tipo = "usuario"
    )
    respuesta = cliente.crearUsuario(sol)
    print("Mensaje del server", respuesta.mensaje)



def main():
    canal = grpc.insecure_channel('localhost:50051')
    cliente = usuario_pb2_grpc.servicioUsuarioStub(canal)
    crearUsuario(cliente)

if __name__ == '__main__':
    main()