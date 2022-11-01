# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/system/security/keystore2/enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJframeworks/proto_logging/stats/enums/system/security/keystore2/enums.proto\x12!android.system.security.keystore2*\xb3\x01\n\x11SecurityLevelEnum\x12\x1e\n\x1aSECURITY_LEVEL_UNSPECIFIED\x10\x00\x12\x1b\n\x17SECURITY_LEVEL_SOFTWARE\x10\x01\x12&\n\"SECURITY_LEVEL_TRUSTED_ENVIRONMENT\x10\x02\x12\x1c\n\x18SECURITY_LEVEL_STRONGBOX\x10\x03\x12\x1b\n\x17SECURITY_LEVEL_KEYSTORE\x10\x04*[\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x07\n\x03RSA\x10\x01\x12\x06\n\x02\x45\x43\x10\x03\x12\x07\n\x03\x41\x45S\x10 \x12\x0e\n\nTRIPLE_DES\x10!\x12\t\n\x04HMAC\x10\x80\x01')

_SECURITYLEVELENUM = DESCRIPTOR.enum_types_by_name['SecurityLevelEnum']
SecurityLevelEnum = enum_type_wrapper.EnumTypeWrapper(_SECURITYLEVELENUM)
_ALGORITHM = DESCRIPTOR.enum_types_by_name['Algorithm']
Algorithm = enum_type_wrapper.EnumTypeWrapper(_ALGORITHM)
SECURITY_LEVEL_UNSPECIFIED = 0
SECURITY_LEVEL_SOFTWARE = 1
SECURITY_LEVEL_TRUSTED_ENVIRONMENT = 2
SECURITY_LEVEL_STRONGBOX = 3
SECURITY_LEVEL_KEYSTORE = 4
ALGORITHM_UNSPECIFIED = 0
RSA = 1
EC = 3
AES = 32
TRIPLE_DES = 33
HMAC = 128


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SECURITYLEVELENUM._serialized_start=114
  _SECURITYLEVELENUM._serialized_end=293
  _ALGORITHM._serialized_start=295
  _ALGORITHM._serialized_end=386
# @@protoc_insertion_point(module_scope)
