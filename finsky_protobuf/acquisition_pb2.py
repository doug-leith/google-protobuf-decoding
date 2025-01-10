# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acquisition.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import doc_annotations_pb2 as doc__annotations__pb2
import document_v2_pb2 as document__v2__pb2
import library_update_proto_pb2 as library__update__proto__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61\x63quisition.proto\x12\x0b\x41\x63quisition\x1a\x15\x64oc_annotations.proto\x1a\x11\x64ocument_v2.proto\x1a\x1alibrary_update_proto.proto\x1a\x0c\x63ommon.proto\"\xfb\x01\n\x0bSuccessInfo\x12\x13\n\x0bmessageHtml\x18\x01 \x01(\t\x12\x13\n\x0b\x62uttonLabel\x18\x02 \x01(\t\x12\x39\n\x11postSuccessAction\x18\x03 \x01(\x0b\x32\x1e.Acquisition.PostSuccessAction\x12\x38\n\rlibraryUpdate\x18\x04 \x01(\x0b\x32!.LibraryUpdateProto.LibraryUpdate\x12\r\n\x05title\x18\x05 \x01(\t\x12\x17\n\x0ftitleBylineHtml\x18\x06 \x01(\t\x12%\n\x0ethumbnailImage\x18\x07 \x01(\x0b\x32\r.Common.Image\"/\n\rOpenDocAction\x12\x1e\n\x03\x64oc\x18\x01 \x01(\x0b\x32\x11.DocumentV2.DocV2\"\x9a\x02\n\x11PostSuccessAction\x12+\n\x07openDoc\x18\x01 \x01(\x0b\x32\x1a.Acquisition.OpenDocAction\x12-\n\x08openHome\x18\x02 \x01(\x0b\x32\x1b.Acquisition.OpenHomeAction\x12\x31\n\ninstallApp\x18\x03 \x01(\x0b\x32\x1d.Acquisition.InstallAppAction\x12\x35\n\x0cpurchaseFlow\x18\x04 \x01(\x0b\x32\x1f.Acquisition.PurchaseFlowAction\x12?\n\ropenContainer\x18\x05 \x01(\x0b\x32(.Acquisition.OpenContainerDocumentAction\"W\n\x12PurchaseFlowAction\x12&\n\x0bpurchaseDoc\x18\x01 \x01(\x0b\x32\x11.DocumentV2.DocV2\x12\x19\n\x11purchaseOfferType\x18\x02 \x01(\x05\"A\n\x1bOpenContainerDocumentAction\x12\"\n\x04link\x18\x01 \x01(\x0b\x32\x14.DocAnnotations.Link\"2\n\x10InstallAppAction\x12\x1e\n\x03\x64oc\x18\x01 \x01(\x0b\x32\x11.DocumentV2.DocV2\"\x10\n\x0eOpenHomeActionB/\n com.google.android.finsky.protosB\x0b\x41\x63quisition')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'acquisition_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\013Acquisition'
  _globals['_SUCCESSINFO']._serialized_start=119
  _globals['_SUCCESSINFO']._serialized_end=370
  _globals['_OPENDOCACTION']._serialized_start=372
  _globals['_OPENDOCACTION']._serialized_end=419
  _globals['_POSTSUCCESSACTION']._serialized_start=422
  _globals['_POSTSUCCESSACTION']._serialized_end=704
  _globals['_PURCHASEFLOWACTION']._serialized_start=706
  _globals['_PURCHASEFLOWACTION']._serialized_end=793
  _globals['_OPENCONTAINERDOCUMENTACTION']._serialized_start=795
  _globals['_OPENCONTAINERDOCUMENTACTION']._serialized_end=860
  _globals['_INSTALLAPPACTION']._serialized_start=862
  _globals['_INSTALLAPPACTION']._serialized_end=912
  _globals['_OPENHOMEACTION']._serialized_start=914
  _globals['_OPENHOMEACTION']._serialized_end=930
# @@protoc_insertion_point(module_scope)
