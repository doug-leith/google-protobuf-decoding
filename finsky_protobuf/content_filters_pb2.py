# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content_filters.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ontent_filters.proto\x12\x0e\x43ontentFilters\x1a\x0c\x63ommon.proto\"\xb6\x01\n\x1d\x43ontentFilterSettingsResponse\x12\x30\n\x0b\x66ilterRange\x18\x01 \x03(\x0b\x32\x1b.ContentFilters.FilterRange\x12\x14\n\x0ctutorialText\x18\x02 \x01(\t\x12(\n\x11tutorialImageFife\x18\x03 \x01(\x0b\x32\r.Common.Image\x12\x11\n\tinfoTitle\x18\x04 \x01(\t\x12\x10\n\x08infoText\x18\x05 \x01(\t\"\xcf\x02\n\x0b\x46ilterRange\x12\x14\n\x0c\x64ocumentType\x18\x01 \x03(\x05\x12\x13\n\x0b\x61uthorityId\x18\x02 \x01(\x05\x12\x32\n\x0c\x66ilterChoice\x18\x03 \x03(\x0b\x32\x1c.ContentFilters.FilterChoice\x12\r\n\x05label\x18\x04 \x01(\t\x12\x1f\n\x08iconFife\x18\x05 \x01(\x0b\x32\r.Common.Image\x12\x1c\n\x14selectionDialogLabel\x18\x06 \x01(\t\x12\x1f\n\x17\x63onfirmationDialogTitle\x18\x07 \x01(\t\x12!\n\x19\x63onfirmationDialogContent\x18\x08 \x01(\t\x12\x1f\n\x17representChoiceAsToggle\x18\t \x01(\x08\x12\x16\n\x0e\x61ppPackageName\x18\n \x01(\t\x12\x16\n\x0eminVersionCode\x18\x0b \x01(\x05\"\x8e\x01\n\x0c\x46ilterChoice\x12\r\n\x05level\x18\x01 \x01(\x05\x12 \n\timageFife\x18\x02 \x01(\x0b\x32\r.Common.Image\x12\r\n\x05label\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x66\x65HeaderValue\x18\x04 \x01(\t\x12\x10\n\x08selected\x18\x05 \x01(\x08\x12\x14\n\x0clabelSummary\x18\x06 \x01(\tB2\n com.google.android.finsky.protosB\x0e\x43ontentFilters')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'content_filters_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\016ContentFilters'
  _globals['_CONTENTFILTERSETTINGSRESPONSE']._serialized_start=56
  _globals['_CONTENTFILTERSETTINGSRESPONSE']._serialized_end=238
  _globals['_FILTERRANGE']._serialized_start=241
  _globals['_FILTERRANGE']._serialized_end=576
  _globals['_FILTERCHOICE']._serialized_start=579
  _globals['_FILTERCHOICE']._serialized_end=721
# @@protoc_insertion_point(module_scope)
