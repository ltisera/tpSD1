import os
from grpc_tools import protoc

#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mi_archivo.proto
def compilaProto(protoDir):
    print("Eliminando compilaciones anteriores")
    for archivo in os.listdir(protoDir):
        if archivo.endswith("_pb2.py") or archivo.endswith("pb2_grpc.py"):
            archivoyPath = os.path.join(protoDir, archivo)
            os.remove(archivoyPath)
    print("Compilando las nuevas")
    protoc.main(
    (
        "",
        f"--proto_path=.",
        f"--python_out=.",
        f"--grpc_python_out=.",
        "usuario.proto",
        "receta.proto",
    )
)

if __name__ == "__main__":
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    protoDir = CURRENT_DIR

    compilaProto(protoDir)
    print("COMPILADO")