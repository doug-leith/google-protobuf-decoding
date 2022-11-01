# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/stats/connectivity/tethering.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGframeworks/proto_logging/stats/enums/stats/connectivity/tethering.proto\x12\x1a\x61ndroid.stats.connectivity*\xd0\x03\n\tErrorCode\x12\x0f\n\x0b\x45\x43_NO_ERROR\x10\x00\x12\x14\n\x10\x45\x43_UNKNOWN_IFACE\x10\x01\x12\x16\n\x12\x45\x43_SERVICE_UNAVAIL\x10\x02\x12\x12\n\x0e\x45\x43_UNSUPPORTED\x10\x03\x12\x14\n\x10\x45\x43_UNAVAIL_IFACE\x10\x04\x12\x15\n\x11\x45\x43_INTERNAL_ERROR\x10\x05\x12\x19\n\x15\x45\x43_TETHER_IFACE_ERROR\x10\x06\x12\x1b\n\x17\x45\x43_UNTETHER_IFACE_ERROR\x10\x07\x12\x1e\n\x1a\x45\x43_ENABLE_FORWARDING_ERROR\x10\x08\x12\x1f\n\x1b\x45\x43_DISABLE_FORWARDING_ERROR\x10\t\x12\x16\n\x12\x45\x43_IFACE_CFG_ERROR\x10\n\x12\x1a\n\x16\x45\x43_PROVISIONING_FAILED\x10\x0b\x12\x17\n\x13\x45\x43_DHCPSERVER_ERROR\x10\x0c\x12\x1a\n\x16\x45\x43_ENTITLEMENT_UNKNOWN\x10\r\x12%\n!EC_NO_CHANGE_TETHERING_PERMISSION\x10\x0e\x12%\n!EC_NO_ACCESS_TETHERING_PERMISSION\x10\x0f\x12\x13\n\x0f\x45\x43_UNKNOWN_TYPE\x10\x10*\xb9\x01\n\x0e\x44ownstreamType\x12\x12\n\x0e\x44S_UNSPECIFIED\x10\x00\x12\x15\n\x11\x44S_TETHERING_WIFI\x10\x01\x12\x14\n\x10\x44S_TETHERING_USB\x10\x02\x12\x1a\n\x16\x44S_TETHERING_BLUETOOTH\x10\x03\x12\x19\n\x15\x44S_TETHERING_WIFI_P2P\x10\x04\x12\x14\n\x10\x44S_TETHERING_NCM\x10\x05\x12\x19\n\x15\x44S_TETHERING_ETHERNET\x10\x06*\x8e\x02\n\x0cUpstreamType\x12\x0e\n\nUT_UNKNOWN\x10\x00\x12\x0f\n\x0bUT_CELLULAR\x10\x01\x12\x0b\n\x07UT_WIFI\x10\x02\x12\x10\n\x0cUT_BLUETOOTH\x10\x03\x12\x0f\n\x0bUT_ETHERNET\x10\x04\x12\x11\n\rUT_WIFI_AWARE\x10\x05\x12\r\n\tUT_LOWPAN\x10\x06\x12\x13\n\x0fUT_CELLULAR_VPN\x10\x07\x12\x0f\n\x0bUT_WIFI_VPN\x10\x08\x12\x14\n\x10UT_BLUETOOTH_VPN\x10\t\x12\x13\n\x0fUT_ETHERNET_VPN\x10\n\x12\x18\n\x14UT_WIFI_CELLULAR_VPN\x10\x0b\x12\x0b\n\x07UT_TEST\x10\x0c\x12\x13\n\x0fUT_DUN_CELLULAR\x10\r*P\n\x08UserType\x12\x10\n\x0cUSER_UNKNOWN\x10\x00\x12\x11\n\rUSER_SETTINGS\x10\x01\x12\x11\n\rUSER_SYSTEMUI\x10\x02\x12\x0c\n\x08USER_GMS\x10\x03\x42\x12\x42\x0eTetheringProtoP\x01')

_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
_DOWNSTREAMTYPE = DESCRIPTOR.enum_types_by_name['DownstreamType']
DownstreamType = enum_type_wrapper.EnumTypeWrapper(_DOWNSTREAMTYPE)
_UPSTREAMTYPE = DESCRIPTOR.enum_types_by_name['UpstreamType']
UpstreamType = enum_type_wrapper.EnumTypeWrapper(_UPSTREAMTYPE)
_USERTYPE = DESCRIPTOR.enum_types_by_name['UserType']
UserType = enum_type_wrapper.EnumTypeWrapper(_USERTYPE)
EC_NO_ERROR = 0
EC_UNKNOWN_IFACE = 1
EC_SERVICE_UNAVAIL = 2
EC_UNSUPPORTED = 3
EC_UNAVAIL_IFACE = 4
EC_INTERNAL_ERROR = 5
EC_TETHER_IFACE_ERROR = 6
EC_UNTETHER_IFACE_ERROR = 7
EC_ENABLE_FORWARDING_ERROR = 8
EC_DISABLE_FORWARDING_ERROR = 9
EC_IFACE_CFG_ERROR = 10
EC_PROVISIONING_FAILED = 11
EC_DHCPSERVER_ERROR = 12
EC_ENTITLEMENT_UNKNOWN = 13
EC_NO_CHANGE_TETHERING_PERMISSION = 14
EC_NO_ACCESS_TETHERING_PERMISSION = 15
EC_UNKNOWN_TYPE = 16
DS_UNSPECIFIED = 0
DS_TETHERING_WIFI = 1
DS_TETHERING_USB = 2
DS_TETHERING_BLUETOOTH = 3
DS_TETHERING_WIFI_P2P = 4
DS_TETHERING_NCM = 5
DS_TETHERING_ETHERNET = 6
UT_UNKNOWN = 0
UT_CELLULAR = 1
UT_WIFI = 2
UT_BLUETOOTH = 3
UT_ETHERNET = 4
UT_WIFI_AWARE = 5
UT_LOWPAN = 6
UT_CELLULAR_VPN = 7
UT_WIFI_VPN = 8
UT_BLUETOOTH_VPN = 9
UT_ETHERNET_VPN = 10
UT_WIFI_CELLULAR_VPN = 11
UT_TEST = 12
UT_DUN_CELLULAR = 13
USER_UNKNOWN = 0
USER_SETTINGS = 1
USER_SYSTEMUI = 2
USER_GMS = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\016TetheringProtoP\001'
  _ERRORCODE._serialized_start=104
  _ERRORCODE._serialized_end=568
  _DOWNSTREAMTYPE._serialized_start=571
  _DOWNSTREAMTYPE._serialized_end=756
  _UPSTREAMTYPE._serialized_start=759
  _UPSTREAMTYPE._serialized_end=1029
  _USERTYPE._serialized_start=1031
  _USERTYPE._serialized_end=1111
# @@protoc_insertion_point(module_scope)
