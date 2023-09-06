import os
from grpc_tools import protoc

#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mi_archivo.proto
def compilaProto(protoDir):
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