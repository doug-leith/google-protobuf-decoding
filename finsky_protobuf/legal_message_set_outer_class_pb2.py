# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: legal_message_set_outer_class.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import legal_message_outer_class_pb2 as legal__message__outer__class__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#legal_message_set_outer_class.proto\x12\x19LegalMessageSetOuterClass\x1a\x1flegal_message_outer_class.proto\"_\n\x15LegalMessageByCountry\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x35\n\x07message\x18\x02 \x01(\x0b\x32$.LegalMessageOuterClass.LegalMessage\"\x9b\x01\n\x0fLegalMessageSet\x12<\n\x0e\x64\x65\x66\x61ultMessage\x18\x01 \x01(\x0b\x32$.LegalMessageOuterClass.LegalMessage\x12J\n\x10messageByCountry\x18\x02 \x03(\x0b\x32\x30.LegalMessageSetOuterClass.LegalMessageByCountryBh\nKcom.google.commerce.payments.orchestration.proto.ui.common.components.legalB\x19LegalMessageSetOuterClass')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'legal_message_set_outer_class_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\nKcom.google.commerce.payments.orchestration.proto.ui.common.components.legalB\031LegalMessageSetOuterClass'
  _globals['_LEGALMESSAGEBYCOUNTRY']._serialized_start=99
  _globals['_LEGALMESSAGEBYCOUNTRY']._serialized_end=194
  _globals['_LEGALMESSAGESET']._serialized_start=197
  _globals['_LEGALMESSAGESET']._serialized_end=352
# @@protoc_insertion_point(module_scope)
