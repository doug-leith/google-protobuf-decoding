# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/service/enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8frameworks/proto_logging/stats/enums/service/enums.proto\x12\x0f\x61ndroid.service*\x97\x01\n\x0fUsbEndPointType\x12\"\n\x1eUSB_ENDPOINT_TYPE_XFER_CONTROL\x10\x00\x12\x1f\n\x1bUSB_ENDPOINT_TYPE_XFER_ISOC\x10\x01\x12\x1f\n\x1bUSB_ENDPOINT_TYPE_XFER_BULK\x10\x02\x12\x1e\n\x1aUSB_ENDPOINT_TYPE_XFER_INT\x10\x03*J\n\x14UsbEndPointDirection\x12\x18\n\x14USB_ENDPOINT_DIR_OUT\x10\x00\x12\x18\n\x13USB_ENDPOINT_DIR_IN\x10\x80\x01*\xd8\x01\n\x17UsbConnectionRecordMode\x12&\n\"USB_CONNECTION_RECORD_MODE_CONNECT\x10\x00\x12/\n+USB_CONNECTION_RECORD_MODE_CONNECT_BADPARSE\x10\x01\x12\x30\n,USB_CONNECTION_RECORD_MODE_CONNECT_BADDEVICE\x10\x02\x12\x32\n%USB_CONNECTION_RECORD_MODE_DISCONNECT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xc8\x01\n\x19\x43ontaminantPresenceStatus\x12\x1e\n\x1a\x43ONTAMINANT_STATUS_UNKNOWN\x10\x00\x12$\n CONTAMINANT_STATUS_NOT_SUPPORTED\x10\x01\x12\x1f\n\x1b\x43ONTAMINANT_STATUS_DISABLED\x10\x02\x12#\n\x1f\x43ONTAMINANT_STATUS_NOT_DETECTED\x10\x03\x12\x1f\n\x1b\x43ONTAMINANT_STATUS_DETECTED\x10\x04\x42\x15\x42\x11ServiceProtoEnumsP\x01')

_USBENDPOINTTYPE = DESCRIPTOR.enum_types_by_name['UsbEndPointType']
UsbEndPointType = enum_type_wrapper.EnumTypeWrapper(_USBENDPOINTTYPE)
_USBENDPOINTDIRECTION = DESCRIPTOR.enum_types_by_name['UsbEndPointDirection']
UsbEndPointDirection = enum_type_wrapper.EnumTypeWrapper(_USBENDPOINTDIRECTION)
_USBCONNECTIONRECORDMODE = DESCRIPTOR.enum_types_by_name['UsbConnectionRecordMode']
UsbConnectionRecordMode = enum_type_wrapper.EnumTypeWrapper(_USBCONNECTIONRECORDMODE)
_CONTAMINANTPRESENCESTATUS = DESCRIPTOR.enum_types_by_name['ContaminantPresenceStatus']
ContaminantPresenceStatus = enum_type_wrapper.EnumTypeWrapper(_CONTAMINANTPRESENCESTATUS)
USB_ENDPOINT_TYPE_XFER_CONTROL = 0
USB_ENDPOINT_TYPE_XFER_ISOC = 1
USB_ENDPOINT_TYPE_XFER_BULK = 2
USB_ENDPOINT_TYPE_XFER_INT = 3
USB_ENDPOINT_DIR_OUT = 0
USB_ENDPOINT_DIR_IN = 128
USB_CONNECTION_RECORD_MODE_CONNECT = 0
USB_CONNECTION_RECORD_MODE_CONNECT_BADPARSE = 1
USB_CONNECTION_RECORD_MODE_CONNECT_BADDEVICE = 2
USB_CONNECTION_RECORD_MODE_DISCONNECT = -1
CONTAMINANT_STATUS_UNKNOWN = 0
CONTAMINANT_STATUS_NOT_SUPPORTED = 1
CONTAMINANT_STATUS_DISABLED = 2
CONTAMINANT_STATUS_NOT_DETECTED = 3
CONTAMINANT_STATUS_DETECTED = 4


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\021ServiceProtoEnumsP\001'
  _USBENDPOINTTYPE._serialized_start=78
  _USBENDPOINTTYPE._serialized_end=229
  _USBENDPOINTDIRECTION._serialized_start=231
  _USBENDPOINTDIRECTION._serialized_end=305
  _USBCONNECTIONRECORDMODE._serialized_start=308
  _USBCONNECTIONRECORDMODE._serialized_end=524
  _CONTAMINANTPRESENCESTATUS._serialized_start=527
  _CONTAMINANTPRESENCESTATUS._serialized_end=727
# @@protoc_insertion_point(module_scope)
