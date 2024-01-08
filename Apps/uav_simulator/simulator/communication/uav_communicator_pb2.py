# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uav_communicator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16uav_communicator.proto\x12\x0fUavCommunicator\"9\n\nLocation3d\x12\r\n\x05x_lon\x18\n \x01(\x01\x12\r\n\x05y_lat\x18\x14 \x01(\x01\x12\r\n\x05h_asl\x18\x1e \x01(\x01\"1\n\x0b\x44irection3d\x12\x0f\n\x07\x61zimuth\x18\n \x01(\x01\x12\x11\n\televation\x18\x14 \x01(\x01\"\xd0\x01\n\tUavStatus\x12-\n\x08location\x18\n \x01(\x0b\x32\x1b.UavCommunicator.Location3d\x12/\n\tdirection\x18\x14 \x01(\x0b\x32\x1c.UavCommunicator.Direction3d\x12\x10\n\x08velocity\x18\x1e \x01(\x01\x12\x1d\n\x15remaining_flight_time\x18( \x01(\r\x12\x32\n\x0c\x66light_state\x18\x32 \x01(\x0e\x32\x1c.UavCommunicator.FlightState\"\x86\x01\n\x10\x46lyToDestination\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x12\n\nmission_id\x18\n \x01(\r\x12\x1b\n\x13is_destination_home\x18\x14 \x01(\x08\x12-\n\x08location\x18\x1e \x01(\x0b\x32\x1b.UavCommunicator.Location3d\"j\n\x0cStatusUpdate\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x16\n\x0euav_descriptor\x18\n \x01(\t\x12.\n\nuav_status\x18\x14 \x01(\x0b\x32\x1a.UavCommunicator.UavStatus\"#\n\x08response\x12\x17\n\x0fresponse_string\x18\n \x01(\t*T\n\x0b\x46lightState\x12\x07\n\x03OFF\x10\x00\x12\x08\n\x04IDLE\x10\n\x12\x12\n\x0eTO_DESTINATION\x10\x14\x12\x0b\n\x07TO_HOME\x10\x1e\x12\x11\n\rHOLD_POSITION\x10(2\xba\x01\n\x14\x43ommunicationService\x12L\n\x10SendStatusUpdate\x12\x1d.UavCommunicator.StatusUpdate\x1a\x19.UavCommunicator.response\x12T\n\x14SendFlyToDestination\x12!.UavCommunicator.FlyToDestination\x1a\x19.UavCommunicator.responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uav_communicator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FLIGHTSTATE']._serialized_start=646
  _globals['_FLIGHTSTATE']._serialized_end=730
  _globals['_LOCATION3D']._serialized_start=43
  _globals['_LOCATION3D']._serialized_end=100
  _globals['_DIRECTION3D']._serialized_start=102
  _globals['_DIRECTION3D']._serialized_end=151
  _globals['_UAVSTATUS']._serialized_start=154
  _globals['_UAVSTATUS']._serialized_end=362
  _globals['_FLYTODESTINATION']._serialized_start=365
  _globals['_FLYTODESTINATION']._serialized_end=499
  _globals['_STATUSUPDATE']._serialized_start=501
  _globals['_STATUSUPDATE']._serialized_end=607
  _globals['_RESPONSE']._serialized_start=609
  _globals['_RESPONSE']._serialized_end=644
  _globals['_COMMUNICATIONSERVICE']._serialized_start=733
  _globals['_COMMUNICATIONSERVICE']._serialized_end=919
# @@protoc_insertion_point(module_scope)