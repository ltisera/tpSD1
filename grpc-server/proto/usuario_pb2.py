# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usuario.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rusuario.proto\"V\n\x13\x63rearUsuarioRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0c\n\x04tipo\x18\x04 \x01(\t\"9\n\x14\x63rearUsuarioResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07mensaje\x18\x02 \x01(\t\";\n\x15loguearUsuarioRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\":\n\x16loguearUsuarioResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06\x65stado\x18\x02 \x01(\t\"M\n\x1asolicitudDeSeguidorRequest\x12\x17\n\x0fusuarioQueSigue\x18\x01 \x01(\t\x12\x16\n\x0eusuarioSeguido\x18\x02 \x01(\t\".\n\x1bsolicitudDeSeguidorResponse\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\"C\n\x1e\x61gregarRecetaAFavoritosRequest\x12\x0f\n\x07usuario\x18\x01 \x01(\t\x12\x10\n\x08idReceta\x18\x02 \x01(\t\"2\n\x1f\x61gregarRecetaAFavoritosResponse\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\".\n\x1btraerUsuariosQueSigoRequest\x12\x0f\n\x07usuario\x18\x01 \x01(\t\"0\n\x1ctraerUsuariosQueSigoResponse\x12\x10\n\x08usuarios\x18\x01 \x03(\t2\x8c\x03\n\x0fservicioUsuario\x12;\n\x0c\x63rearUsuario\x12\x14.crearUsuarioRequest\x1a\x15.crearUsuarioResponse\x12=\n\x0eloguearUsuario\x12\x14.crearUsuarioRequest\x1a\x15.crearUsuarioResponse\x12J\n\rseguirUsuario\x12\x1b.solicitudDeSeguidorRequest\x1a\x1c.solicitudDeSeguidorResponse\x12\\\n\x17\x61gregarRecetaAFavoritos\x12\x1f.agregarRecetaAFavoritosRequest\x1a .agregarRecetaAFavoritosResponse\x12S\n\x14traerUsuariosQueSigo\x12\x1c.traerUsuariosQueSigoRequest\x1a\x1d.traerUsuariosQueSigoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'usuario_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CREARUSUARIOREQUEST']._serialized_start=17
  _globals['_CREARUSUARIOREQUEST']._serialized_end=103
  _globals['_CREARUSUARIORESPONSE']._serialized_start=105
  _globals['_CREARUSUARIORESPONSE']._serialized_end=162
  _globals['_LOGUEARUSUARIOREQUEST']._serialized_start=164
  _globals['_LOGUEARUSUARIOREQUEST']._serialized_end=223
  _globals['_LOGUEARUSUARIORESPONSE']._serialized_start=225
  _globals['_LOGUEARUSUARIORESPONSE']._serialized_end=283
  _globals['_SOLICITUDDESEGUIDORREQUEST']._serialized_start=285
  _globals['_SOLICITUDDESEGUIDORREQUEST']._serialized_end=362
  _globals['_SOLICITUDDESEGUIDORRESPONSE']._serialized_start=364
  _globals['_SOLICITUDDESEGUIDORRESPONSE']._serialized_end=410
  _globals['_AGREGARRECETAAFAVORITOSREQUEST']._serialized_start=412
  _globals['_AGREGARRECETAAFAVORITOSREQUEST']._serialized_end=479
  _globals['_AGREGARRECETAAFAVORITOSRESPONSE']._serialized_start=481
  _globals['_AGREGARRECETAAFAVORITOSRESPONSE']._serialized_end=531
  _globals['_TRAERUSUARIOSQUESIGOREQUEST']._serialized_start=533
  _globals['_TRAERUSUARIOSQUESIGOREQUEST']._serialized_end=579
  _globals['_TRAERUSUARIOSQUESIGORESPONSE']._serialized_start=581
  _globals['_TRAERUSUARIOSQUESIGORESPONSE']._serialized_end=629
  _globals['_SERVICIOUSUARIO']._serialized_start=632
  _globals['_SERVICIOUSUARIO']._serialized_end=1028
# @@protoc_insertion_point(module_scope)
