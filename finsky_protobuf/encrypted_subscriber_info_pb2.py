# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encrypted_subscriber_info.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65ncrypted_subscriber_info.proto\x12\x17\x45ncryptedSubscriberInfo\"\x99\x01\n\x17\x45ncryptedSubscriberInfo\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x14\n\x0c\x65ncryptedKey\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\x12\x12\n\ninitVector\x18\x04 \x01(\t\x12\x18\n\x10googleKeyVersion\x18\x05 \x01(\x05\x12\x19\n\x11\x63\x61rrierKeyVersion\x18\x06 \x01(\x05\x42=\n com.google.android.finsky.protosB\x17\x45ncryptedSubscriberInfoP\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'encrypted_subscriber_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\027EncryptedSubscriberInfoP\001'
  _globals['_ENCRYPTEDSUBSCRIBERINFO']._serialized_start=61
  _globals['_ENCRYPTEDSUBSCRIBERINFO']._serialized_end=214
# @@protoc_insertion_point(module_scope)
