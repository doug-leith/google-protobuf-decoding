# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preloads.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epreloads.proto\x12\x08Preloads\x1a\x0c\x63ommon.proto\"\xa6\x01\n\x07Preload\x12\x1c\n\x05\x64ocid\x18\x01 \x01(\x0b\x32\r.Common.Docid\x12\x13\n\x0bversionCode\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x1b\n\x04icon\x18\x04 \x01(\x0b\x32\r.Common.Image\x12\x15\n\rdeliveryToken\x18\x05 \x01(\t\x12\x17\n\x0finstallLocation\x18\x06 \x01(\x05\x12\x0c\n\x04size\x18\x07 \x01(\x03\"c\n\x10PreloadsResponse\x12(\n\rconfigPreload\x18\x01 \x01(\x0b\x32\x11.Preloads.Preload\x12%\n\nappPreload\x18\x02 \x03(\x0b\x32\x11.Preloads.PreloadB,\n com.google.android.finsky.protosB\x08Preloads')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'preloads_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\010Preloads'
  _globals['_PRELOAD']._serialized_start=43
  _globals['_PRELOAD']._serialized_end=209
  _globals['_PRELOADSRESPONSE']._serialized_start=211
  _globals['_PRELOADSRESPONSE']._serialized_end=310
# @@protoc_insertion_point(module_scope)
