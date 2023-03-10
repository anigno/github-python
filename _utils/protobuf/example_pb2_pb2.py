# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example_pb2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example_pb2.proto',
  package='messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x11\x65xample_pb2.proto\x12\x08messages\"^\n\nprMessageA\x12\x1e\n\nuint_value\x18\x01 \x01(\r:\n4294967295\x12\x1b\n\x0cstring_value\x18\x02 \x01(\t:\x05\x45MPTY\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x02\"\x87\x02\n\nprMessageB\x12-\n\x0fmessage_a_value\x18\x01 \x01(\x0b\x32\x14.messages.prMessageA\x12\x1b\n\x13required_bool_value\x18\t \x02(\x08\x12\x13\n\x0blist_string\x18\x02 \x03(\t\x12W\n\x1b\x64ictionary_string_int_value\x18\x14 \x03(\x0b\x32\x32.messages.prMessageB.DictionaryStringIntValueEntry\x1a?\n\x1d\x44ictionaryStringIntValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01'
)




_PRMESSAGEA = _descriptor.Descriptor(
  name='prMessageA',
  full_name='messages.prMessageA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uint_value', full_name='messages.prMessageA.uint_value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967295,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='messages.prMessageA.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"EMPTY".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='messages.prMessageA.float_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=125,
)


_PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY = _descriptor.Descriptor(
  name='DictionaryStringIntValueEntry',
  full_name='messages.prMessageB.DictionaryStringIntValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='messages.prMessageB.DictionaryStringIntValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='messages.prMessageB.DictionaryStringIntValueEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=391,
)

_PRMESSAGEB = _descriptor.Descriptor(
  name='prMessageB',
  full_name='messages.prMessageB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_a_value', full_name='messages.prMessageB.message_a_value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_bool_value', full_name='messages.prMessageB.required_bool_value', index=1,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_string', full_name='messages.prMessageB.list_string', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dictionary_string_int_value', full_name='messages.prMessageB.dictionary_string_int_value', index=3,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=391,
)

_PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY.containing_type = _PRMESSAGEB
_PRMESSAGEB.fields_by_name['message_a_value'].message_type = _PRMESSAGEA
_PRMESSAGEB.fields_by_name['dictionary_string_int_value'].message_type = _PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY
DESCRIPTOR.message_types_by_name['prMessageA'] = _PRMESSAGEA
DESCRIPTOR.message_types_by_name['prMessageB'] = _PRMESSAGEB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

prMessageA = _reflection.GeneratedProtocolMessageType('prMessageA', (_message.Message,), {
  'DESCRIPTOR' : _PRMESSAGEA,
  '__module__' : 'example_pb2_pb2'
  # @@protoc_insertion_point(class_scope:messages.prMessageA)
  })
_sym_db.RegisterMessage(prMessageA)

prMessageB = _reflection.GeneratedProtocolMessageType('prMessageB', (_message.Message,), {

  'DictionaryStringIntValueEntry' : _reflection.GeneratedProtocolMessageType('DictionaryStringIntValueEntry', (_message.Message,), {
    'DESCRIPTOR' : _PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY,
    '__module__' : 'example_pb2_pb2'
    # @@protoc_insertion_point(class_scope:messages.prMessageB.DictionaryStringIntValueEntry)
    })
  ,
  'DESCRIPTOR' : _PRMESSAGEB,
  '__module__' : 'example_pb2_pb2'
  # @@protoc_insertion_point(class_scope:messages.prMessageB)
  })
_sym_db.RegisterMessage(prMessageB)
_sym_db.RegisterMessage(prMessageB.DictionaryStringIntValueEntry)


_PRMESSAGEB_DICTIONARYSTRINGINTVALUEENTRY._options = None
# @@protoc_insertion_point(module_scope)
