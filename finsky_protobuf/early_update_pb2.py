# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: early_update.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import device_configuration_proto_pb2 as device__configuration__proto__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65\x61rly_update.proto\x12\x0b\x45\x61rlyUpdate\x1a device_configuration_proto.proto\x1a\x0c\x63ommon.proto\"P\n\x13\x45\x61rlyUpdateResponse\x12\x39\n\x11\x65\x61rlyDocumentInfo\x18\x01 \x03(\x0b\x32\x1e.EarlyUpdate.EarlyDocumentInfo\"e\n\x12\x45\x61rlyUpdateRequest\x12O\n\x13\x64\x65viceConfiguration\x18\x01 \x01(\x0b\x32\x32.DeviceConfigurationProto.DeviceConfigurationProto\"{\n\x11\x45\x61rlyDocumentInfo\x12\x1c\n\x05\x64ocid\x18\x01 \x01(\x0b\x32\r.Common.Docid\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bversionCode\x18\x03 \x01(\x05\x12\x12\n\nbackground\x18\x04 \x01(\x08\x12\x10\n\x08\x63ritical\x18\x05 \x01(\x08\x42/\n com.google.android.finsky.protosB\x0b\x45\x61rlyUpdate')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'early_update_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\013EarlyUpdate'
  _globals['_EARLYUPDATERESPONSE']._serialized_start=83
  _globals['_EARLYUPDATERESPONSE']._serialized_end=163
  _globals['_EARLYUPDATEREQUEST']._serialized_start=165
  _globals['_EARLYUPDATEREQUEST']._serialized_end=266
  _globals['_EARLYDOCUMENTINFO']._serialized_start=268
  _globals['_EARLYDOCUMENTINFO']._serialized_end=391
# @@protoc_insertion_point(module_scope)
