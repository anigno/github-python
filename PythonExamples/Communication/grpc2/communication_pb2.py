# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ommunication.proto\x12\rcommunication\"1\n\x07Mission\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\t\x12\x14\n\x0cmission_data\x18\x02 \x01(\t\"8\n\x0cStatusUpdate\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\t\x12\x16\n\x0estatus_message\x18\x02 \x01(\t2\xa8\x01\n\x14\x43ommunicationService\x12\x42\n\x0bSendMission\x12\x16.communication.Mission\x1a\x1b.communication.StatusUpdate\x12L\n\x10SendStatusUpdate\x12\x1b.communication.StatusUpdate\x1a\x1b.communication.StatusUpdateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'communication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MISSION']._serialized_start=38
  _globals['_MISSION']._serialized_end=87
  _globals['_STATUSUPDATE']._serialized_start=89
  _globals['_STATUSUPDATE']._serialized_end=145
  _globals['_COMMUNICATIONSERVICE']._serialized_start=148
  _globals['_COMMUNICATIONSERVICE']._serialized_end=316
# @@protoc_insertion_point(module_scope)