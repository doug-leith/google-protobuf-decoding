# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_activity.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import document_v2_pb2 as document__v2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13user_activity.proto\x12\x0cUserActivity\x1a\x11\x64ocument_v2.proto\"\xa2\x01\n\x1cUserActivitySettingsResponse\x12&\n\x0b\x63urrentUser\x18\x01 \x01(\x0b\x32\x11.DocumentV2.DocV2\x12\x15\n\rsettingsTitle\x18\x02 \x01(\t\x12\x1b\n\x13settingsDescription\x18\x03 \x01(\t\x12\x17\n\x0fsettingsTosHtml\x18\x04 \x01(\t\x12\r\n\x05optIn\x18\x05 \x01(\x08\"\x1c\n\x1aRecordUserActivityResponseB0\n com.google.android.finsky.protosB\x0cUserActivity')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_activity_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\014UserActivity'
  _globals['_USERACTIVITYSETTINGSRESPONSE']._serialized_start=57
  _globals['_USERACTIVITYSETTINGSRESPONSE']._serialized_end=219
  _globals['_RECORDUSERACTIVITYRESPONSE']._serialized_start=221
  _globals['_RECORDUSERACTIVITYRESPONSE']._serialized_end=249
# @@protoc_insertion_point(module_scope)
