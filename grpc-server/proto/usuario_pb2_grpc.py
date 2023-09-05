# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import usuario_pb2 as usuario__pb2


class servicioUsuarioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.crearUsuario = channel.unary_unary(
                '/servicioUsuario/crearUsuario',
                request_serializer=usuario__pb2.crearUsuarioRequest.SerializeToString,
                response_deserializer=usuario__pb2.crearUsuarioResponse.FromString,
                )
        self.seguirUsuario = channel.unary_unary(
                '/servicioUsuario/seguirUsuario',
                request_serializer=usuario__pb2.solicitudDeSeguidorRequest.SerializeToString,
                response_deserializer=usuario__pb2.solicitudDeSeguidorResponse.FromString,
                )


class servicioUsuarioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def crearUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def seguirUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_servicioUsuarioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'crearUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.crearUsuario,
                    request_deserializer=usuario__pb2.crearUsuarioRequest.FromString,
                    response_serializer=usuario__pb2.crearUsuarioResponse.SerializeToString,
            ),
            'seguirUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.seguirUsuario,
                    request_deserializer=usuario__pb2.solicitudDeSeguidorRequest.FromString,
                    response_serializer=usuario__pb2.solicitudDeSeguidorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'servicioUsuario', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class servicioUsuario(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def crearUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/servicioUsuario/crearUsuario',
            usuario__pb2.crearUsuarioRequest.SerializeToString,
            usuario__pb2.crearUsuarioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def seguirUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/servicioUsuario/seguirUsuario',
            usuario__pb2.solicitudDeSeguidorRequest.SerializeToString,
            usuario__pb2.solicitudDeSeguidorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)