# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x0cgrpc_example\"\x1b\n\x0bTextMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1f\n\x0fResponseMessage\x12\x0c\n\x04text\x18\x01 \x01(\t2_\n\x12TextMessageService\x12I\n\x11\x43lientSendMessage\x12\x19.grpc_example.TextMessage\x1a\x19.grpc_example.TextMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEXTMESSAGE']._serialized_start=32
  _globals['_TEXTMESSAGE']._serialized_end=59
  _globals['_RESPONSEMESSAGE']._serialized_start=61
  _globals['_RESPONSEMESSAGE']._serialized_end=92
  _globals['_TEXTMESSAGESERVICE']._serialized_start=94
  _globals['_TEXTMESSAGESERVICE']._serialized_end=189
# @@protoc_insertion_point(module_scope)