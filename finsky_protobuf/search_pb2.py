# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import document_v2_pb2 as document__v2__pb2
import doc_list_pb2 as doc__list__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csearch.proto\x12\x06Search\x1a\x11\x64ocument_v2.proto\x1a\x0e\x64oc_list.proto\"g\n\rRelatedSearch\x12\x11\n\tsearchUrl\x18\x01 \x01(\t\x12\x0e\n\x06header\x18\x02 \x01(\t\x12\x11\n\tbackendId\x18\x03 \x01(\x05\x12\x0f\n\x07\x64ocType\x18\x04 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\x08\"\x90\x02\n\x0eSearchResponse\x12\x15\n\roriginalQuery\x18\x01 \x01(\t\x12\x16\n\x0esuggestedQuery\x18\x02 \x01(\t\x12\x16\n\x0e\x61ggregateQuery\x18\x03 \x01(\x08\x12\x1f\n\x06\x62ucket\x18\x04 \x03(\x0b\x32\x0f.DocList.Bucket\x12\x1e\n\x03\x64oc\x18\x05 \x03(\x0b\x32\x11.DocumentV2.DocV2\x12,\n\rrelatedSearch\x18\x06 \x03(\x0b\x32\x15.Search.RelatedSearch\x12\x18\n\x10serverLogsCookie\x18\x07 \x01(\x0c\x12\x18\n\x10\x66ullPageReplaced\x18\x08 \x01(\x08\x12\x14\n\x0c\x63ontainsSnow\x18\t \x01(\x08\x42*\n com.google.android.finsky.protosB\x06Search')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\006Search'
  _globals['_RELATEDSEARCH']._serialized_start=59
  _globals['_RELATEDSEARCH']._serialized_end=162
  _globals['_SEARCHRESPONSE']._serialized_start=165
  _globals['_SEARCHRESPONSE']._serialized_end=437
# @@protoc_insertion_point(module_scope)
