# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resolve_link.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12resolve_link.proto\x12\x0bResolveLink\x1a\x0c\x63ommon.proto\"\xc6\x02\n\x0cResolvedLink\x12\x12\n\ndetailsUrl\x18\x01 \x01(\t\x12\x11\n\tbrowseUrl\x18\x02 \x01(\t\x12\x11\n\tsearchUrl\x18\x03 \x01(\t\x12\x33\n\x0e\x64irectPurchase\x18\x04 \x01(\x0b\x32\x1b.ResolveLink.DirectPurchase\x12\x0f\n\x07homeUrl\x18\x05 \x01(\t\x12\x33\n\x0eredeemGiftCard\x18\x06 \x01(\x0b\x32\x1b.ResolveLink.RedeemGiftCard\x12\x18\n\x10serverLogsCookie\x18\x07 \x01(\x0c\x12\x1c\n\x05\x64ocid\x18\x08 \x01(\x0b\x32\r.Common.Docid\x12\x13\n\x0bwishlistUrl\x18\t \x01(\t\x12\x0f\n\x07\x62\x61\x63kend\x18\n \x01(\x05\x12\r\n\x05query\x18\x0b \x01(\t\x12\x14\n\x0cmyAccountUrl\x18\x0c \x01(\t\"c\n\x0e\x44irectPurchase\x12\x12\n\ndetailsUrl\x18\x01 \x01(\t\x12\x15\n\rpurchaseDocid\x18\x02 \x01(\t\x12\x13\n\x0bparentDocid\x18\x03 \x01(\t\x12\x11\n\tofferType\x18\x04 \x01(\x05\"=\n\x0eRedeemGiftCard\x12\x13\n\x0bprefillCode\x18\x01 \x01(\t\x12\x16\n\x0epartnerPayload\x18\x02 \x01(\tB/\n com.google.android.finsky.protosB\x0bResolveLink')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resolve_link_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\013ResolveLink'
  _globals['_RESOLVEDLINK']._serialized_start=50
  _globals['_RESOLVEDLINK']._serialized_end=376
  _globals['_DIRECTPURCHASE']._serialized_start=378
  _globals['_DIRECTPURCHASE']._serialized_end=477
  _globals['_REDEEMGIFTCARD']._serialized_start=479
  _globals['_REDEEMGIFTCARD']._serialized_end=540
# @@protoc_insertion_point(module_scope)
