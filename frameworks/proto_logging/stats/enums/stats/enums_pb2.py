# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/stats/enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6frameworks/proto_logging/stats/enums/stats/enums.proto\x12\randroid.stats*\xf9\x01\n\tEventType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x37\n3CONTENT_SUGGESTIONS_CLASSIFY_CONTENT_CALL_SUCCEEDED\x10\x01\x12\x34\n0CONTENT_SUGGESTIONS_CLASSIFY_CONTENT_CALL_FAILED\x10\x02\x12\x36\n2CONTENT_SUGGESTIONS_SUGGEST_CONTENT_CALL_SUCCEEDED\x10\x03\x12\x33\n/CONTENT_SUGGESTIONS_SUGGEST_CONTENT_CALL_FAILED\x10\x04\x42\x0c\x42\nStatsEnums')

_EVENTTYPE = DESCRIPTOR.enum_types_by_name['EventType']
EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
TYPE_UNKNOWN = 0
CONTENT_SUGGESTIONS_CLASSIFY_CONTENT_CALL_SUCCEEDED = 1
CONTENT_SUGGESTIONS_CLASSIFY_CONTENT_CALL_FAILED = 2
CONTENT_SUGGESTIONS_SUGGEST_CONTENT_CALL_SUCCEEDED = 3
CONTENT_SUGGESTIONS_SUGGEST_CONTENT_CALL_FAILED = 4


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\nStatsEnums'
  _EVENTTYPE._serialized_start=74
  _EVENTTYPE._serialized_end=323
# @@protoc_insertion_point(module_scope)
