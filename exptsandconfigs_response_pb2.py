# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: exptsandconfigs_response.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'exptsandconfigs_response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65xptsandconfigs_response.proto\x1a\x19google/protobuf/any.proto\"\x9c\n\n\x12HeterodyneResponse\x12>\n\x10heterodyneConfig\x18\x01 \x03(\x0b\x32$.HeterodyneResponse.HeterodyneConfig\x12\x10\n\x08\x62ytesTag\x18\x02 \x01(\x0c\x12\x1b\n\x13pseudonymousIdToken\x18\x03 \x01(\t\x12\x17\n\x0fservertimestamp\x18\x04 \x01(\x03\x1a\xfd\x08\n\x10HeterodyneConfig\x12K\n\x0epackageDetails\x18\x01 \x01(\x0b\x32\x33.HeterodyneResponse.HeterodyneConfig.PackageDetails\x12[\n\x16tagOrFlagListProtoList\x18\x02 \x03(\x0b\x32;.HeterodyneResponse.HeterodyneConfig.TagOrFlagListProtoList\x12-\n\x0f\x65xperimentToken\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x13\n\x0bserverToken\x18\x04 \x01(\t\x12\x37\n\x04\x63\x66kn\x18\x06 \x03(\x0b\x32).HeterodyneResponse.HeterodyneConfig.Cfkn\x1a\x1f\n\x0e\x41uthTokenIndex\x12\r\n\x05index\x18\x01 \x01(\x05\x1a\x97\x01\n\x0ePackageDetails\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12K\n\x0e\x61uthTokenIndex\x18\x03 \x01(\x0b\x32\x33.HeterodyneResponse.HeterodyneConfig.AuthTokenIndex\x12\x12\n\nbaselineCl\x18\x04 \x01(\x03\x1a,\n\x03Tag\x12\x13\n\x0bpartitionId\x18\x01 \x01(\x05\x12\x10\n\x08\x62ytesTag\x18\x02 \x01(\x0c\x1a\xcb\x01\n\x04\x46lag\x12\x10\n\x08\x66lagName\x18\x01 \x01(\t\x12\x0e\n\x06intVal\x18\x02 \x01(\x05\x12\x0f\n\x07\x62oolVal\x18\x03 \x01(\x08\x12\x10\n\x08\x66loatVal\x18\x04 \x01(\x02\x12\x11\n\tstringVal\x18\x05 \x01(\t\x12\x12\n\nvalueIsSet\x18\x07 \x01(\x08\x12\x10\n\x08\x66lagType\x18\x08 \x01(\x05\x12\x45\n\tvalueType\x18\t \x01(\x0e\x32\x32.HeterodyneResponse.HeterodyneConfig.FlagValueType\x1a\x8d\x01\n\x16TagOrFlagListProtoList\x12:\n\x08tagProto\x18\x01 \x01(\x0b\x32(.HeterodyneResponse.HeterodyneConfig.Tag\x12\x37\n\x04\x66lag\x18\x02 \x03(\x0b\x32).HeterodyneResponse.HeterodyneConfig.Flag\x1a\x8c\x01\n\x04\x43\x66kn\x12K\n\x0epackageDetails\x18\x01 \x01(\x0b\x32\x33.HeterodyneResponse.HeterodyneConfig.PackageDetails\x12#\n\x05token\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x12\n\nprovenance\x18\x03 \x01(\x05\"l\n\rFlagValueType\x12\x0f\n\x0bUNKNOWN_VAL\x10\x00\x12\x0f\n\x0bINTEGER_VAL\x10\x01\x12\x0c\n\x08\x42OOL_VAL\x10\x02\x12\r\n\tFLOAT_VAL\x10\x03\x12\x0e\n\nSTRING_VAL\x10\x04\x12\x0c\n\x08\x42LOB_VAL\x10\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exptsandconfigs_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HETERODYNERESPONSE']._serialized_start=62
  _globals['_HETERODYNERESPONSE']._serialized_end=1370
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG']._serialized_start=221
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG']._serialized_end=1370
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_AUTHTOKENINDEX']._serialized_start=536
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_AUTHTOKENINDEX']._serialized_end=567
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_PACKAGEDETAILS']._serialized_start=570
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_PACKAGEDETAILS']._serialized_end=721
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_TAG']._serialized_start=723
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_TAG']._serialized_end=767
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_FLAG']._serialized_start=770
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_FLAG']._serialized_end=973
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_TAGORFLAGLISTPROTOLIST']._serialized_start=976
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_TAGORFLAGLISTPROTOLIST']._serialized_end=1117
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_CFKN']._serialized_start=1120
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_CFKN']._serialized_end=1260
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_FLAGVALUETYPE']._serialized_start=1262
  _globals['_HETERODYNERESPONSE_HETERODYNECONFIG_FLAGVALUETYPE']._serialized_end=1370
# @@protoc_insertion_point(module_scope)
