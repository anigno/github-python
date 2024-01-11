# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communication_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63ommunication_service.proto\x12\x15\x63ommunication_service\":\n\x0bpLocation3d\x12\r\n\x05x_lon\x18\n \x01(\x01\x12\r\n\x05y_lat\x18\x14 \x01(\x01\x12\r\n\x05h_asl\x18\x1e \x01(\x01\"2\n\x0cpDirection3d\x12\x0f\n\x07\x61zimuth\x18\n \x01(\x01\x12\x11\n\televation\x18\x14 \x01(\x01\"3\n\x0fpCapabilityData\x12\x12\n\ndescriptor\x18\n \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x14 \x01(\x0c\"\xa6\x02\n\npUavStatus\x12\x34\n\x08location\x18\n \x01(\x0b\x32\".communication_service.pLocation3d\x12\x36\n\tdirection\x18\x14 \x01(\x0b\x32#.communication_service.pDirection3d\x12\x10\n\x08velocity\x18\x1e \x01(\x01\x12\x1d\n\x15remaining_flight_time\x18( \x01(\r\x12\x38\n\x0c\x66light_state\x18\x32 \x01(\x0e\x32\".communication_service.FlightState\x12?\n\x0f\x63\x61pability_data\x18< \x03(\x0b\x32&.communication_service.pCapabilityData\"\x8e\x01\n\x11pFlyToDestination\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x12\n\nmission_id\x18\n \x01(\r\x12\x1b\n\x13is_destination_home\x18\x14 \x01(\x08\x12\x34\n\x08location\x18\x1e \x01(\x0b\x32\".communication_service.pLocation3d\"r\n\rpStatusUpdate\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x16\n\x0euav_descriptor\x18\n \x01(\t\x12\x35\n\nuav_status\x18\x14 \x01(\x0b\x32!.communication_service.pUavStatus\"$\n\tpResponse\x12\x17\n\x0fresponse_string\x18\n \x01(\t*T\n\x0b\x46lightState\x12\x07\n\x03OFF\x10\x00\x12\x08\n\x04IDLE\x10\n\x12\x12\n\x0eTO_DESTINATION\x10\x14\x12\x0b\n\x07TO_HOME\x10\x1e\x12\x11\n\rHOLD_POSITION\x10(2\xdc\x01\n\x14\x43ommunicationService\x12]\n\x13StatusUpdateRequest\x12$.communication_service.pStatusUpdate\x1a .communication_service.pResponse\x12\x65\n\x17\x46lyToDestinationRequest\x12(.communication_service.pFlyToDestination\x1a .communication_service.pResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'communication_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FLIGHTSTATE']._serialized_start=815
  _globals['_FLIGHTSTATE']._serialized_end=899
  _globals['_PLOCATION3D']._serialized_start=54
  _globals['_PLOCATION3D']._serialized_end=112
  _globals['_PDIRECTION3D']._serialized_start=114
  _globals['_PDIRECTION3D']._serialized_end=164
  _globals['_PCAPABILITYDATA']._serialized_start=166
  _globals['_PCAPABILITYDATA']._serialized_end=217
  _globals['_PUAVSTATUS']._serialized_start=220
  _globals['_PUAVSTATUS']._serialized_end=514
  _globals['_PFLYTODESTINATION']._serialized_start=517
  _globals['_PFLYTODESTINATION']._serialized_end=659
  _globals['_PSTATUSUPDATE']._serialized_start=661
  _globals['_PSTATUSUPDATE']._serialized_end=775
  _globals['_PRESPONSE']._serialized_start=777
  _globals['_PRESPONSE']._serialized_end=813
  _globals['_COMMUNICATIONSERVICE']._serialized_start=902
  _globals['_COMMUNICATIONSERVICE']._serialized_end=1122
# @@protoc_insertion_point(module_scope)
