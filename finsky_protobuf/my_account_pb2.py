# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_account.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import doc_annotations_pb2 as doc__annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10my_account.proto\x12\tMyAccount\x1a\x15\x64oc_annotations.proto\"\x95\x01\n\x11MyAccountResponse\x12@\n\x17purchaseHistoryMetadata\x18\x01 \x01(\x0b\x32\x1f.DocAnnotations.SectionMetadata\x12>\n\x15subscriptionsMetadata\x18\x02 \x01(\x0b\x32\x1f.DocAnnotations.SectionMetadataB-\n com.google.android.finsky.protosB\tMyAccount')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_account_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\tMyAccount'
  _globals['_MYACCOUNTRESPONSE']._serialized_start=55
  _globals['_MYACCOUNTRESPONSE']._serialized_end=204
# @@protoc_insertion_point(module_scope)
