# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_outer_class.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import device_fingerprinting_pb2 as device__fingerprinting__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ontext_outer_class.proto\x12\x11\x43ontextOuterClass\x1a\x1b\x64\x65vice_fingerprinting.proto\"\x98\x03\n\x13NativeClientContext\x12\x10\n\x08imsiHash\x18\x01 \x01(\t\x12\x0e\n\x06mccMnc\x18\x02 \x01(\t\x12\x11\n\tosVersion\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12\x15\n\rscreenWidthPx\x18\x05 \x01(\x05\x12\x16\n\x0escreenHeightPx\x18\x06 \x01(\x05\x12\x12\n\nscreenXDpi\x18\x07 \x01(\x02\x12\x12\n\nscreenYDpi\x18\x08 \x01(\x02\x12\x13\n\x0bpackageName\x18\t \x01(\t\x12\x1a\n\x12packageVersionCode\x18\n \x01(\t\x12\x1a\n\x12packageVersionName\x18\x0b \x01(\t\x12\x43\n\x08riskData\x18\x0c \x01(\x0b\x32\x31.DeviceFingerprinting.DeviceFingerprinting.Parsed\x12\x1d\n\x15integratorPackageName\x18\r \x01(\t\x12\x16\n\x0emarketClientId\x18\x0e \x01(\t\x12\x1c\n\x14\x61ndroidClientSubtype\x18\x0f \x01(\x05\x42L\n7com.google.commerce.payments.orchestration.proto.commonB\x11\x43ontextOuterClass')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'context_outer_class_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n7com.google.commerce.payments.orchestration.proto.commonB\021ContextOuterClass'
  _globals['_NATIVECLIENTCONTEXT']._serialized_start=78
  _globals['_NATIVECLIENTCONTEXT']._serialized_end=486
# @@protoc_insertion_point(module_scope)
