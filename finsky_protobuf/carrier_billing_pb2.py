# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carrier_billing.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import billing_address_pb2 as billing__address__pb2
import common_device_pb2 as common__device__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63\x61rrier_billing.proto\x12\x0e\x43\x61rrierBilling\x1a\x15\x62illing_address.proto\x1a\x13\x63ommon_device.proto\"0\n\x1bInitiateAssociationResponse\x12\x11\n\tuserToken\x18\x01 \x01(\t\"\xa7\x01\n\x19VerifyAssociationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0e\x62illingAddress\x18\x02 \x01(\x0b\x32\x17.BillingAddress.Address\x12,\n\ncarrierTos\x18\x03 \x01(\x0b\x32\x18.CommonDevice.CarrierTos\x12\x1b\n\x13\x63\x61rrierErrorMessage\x18\x04 \x01(\tB2\n com.google.android.finsky.protosB\x0e\x43\x61rrierBilling')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'carrier_billing_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\016CarrierBilling'
  _globals['_INITIATEASSOCIATIONRESPONSE']._serialized_start=85
  _globals['_INITIATEASSOCIATIONRESPONSE']._serialized_end=133
  _globals['_VERIFYASSOCIATIONRESPONSE']._serialized_start=136
  _globals['_VERIFYASSOCIATIONRESPONSE']._serialized_end=303
# @@protoc_insertion_point(module_scope)
