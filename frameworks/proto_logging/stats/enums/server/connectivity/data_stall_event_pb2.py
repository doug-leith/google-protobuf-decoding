# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/server/connectivity/data_stall_event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOframeworks/proto_logging/stats/enums/server/connectivity/data_stall_event.proto\x12\x1f\x63om.android.server.connectivity\"\xa5\x01\n\x0c\x43\x65llularData\x12<\n\x08rat_type\x18\x01 \x01(\x0e\x32*.com.android.server.connectivity.RadioTech\x12\x12\n\nis_roaming\x18\x02 \x01(\x08\x12\x16\n\x0enetwork_mccmnc\x18\x03 \x01(\t\x12\x12\n\nsim_mccmnc\x18\x04 \x01(\t\x12\x17\n\x0fsignal_strength\x18\x05 \x01(\x05\"_\n\x08WifiData\x12\x17\n\x0fsignal_strength\x18\x01 \x01(\x05\x12:\n\twifi_band\x18\x02 \x01(\x0e\x32\'.com.android.server.connectivity.ApBand\"5\n\x08\x44nsEvent\x12\x17\n\x0f\x64ns_return_code\x18\x01 \x03(\x05\x12\x10\n\x08\x64ns_time\x18\x02 \x03(\x03*K\n\x0bProbeResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\n\n\x06PORTAL\x10\x03\x12\x0b\n\x07PARTIAL\x10\x04*S\n\x06\x41pBand\x12\x13\n\x0f\x41P_BAND_UNKNOWN\x10\x00\x12\x10\n\x0c\x41P_BAND_2GHZ\x10\x01\x12\x10\n\x0c\x41P_BAND_5GHZ\x10\x02\x12\x10\n\x0c\x41P_BAND_6GHZ\x10\x03*\xd5\x04\n\tRadioTech\x12\x1c\n\x18RADIO_TECHNOLOGY_UNKNOWN\x10\x00\x12\x19\n\x15RADIO_TECHNOLOGY_GPRS\x10\x01\x12\x19\n\x15RADIO_TECHNOLOGY_EDGE\x10\x02\x12\x19\n\x15RADIO_TECHNOLOGY_UMTS\x10\x03\x12\x1a\n\x16RADIO_TECHNOLOGY_IS95A\x10\x04\x12\x1a\n\x16RADIO_TECHNOLOGY_IS95B\x10\x05\x12\x1a\n\x16RADIO_TECHNOLOGY_1XRTT\x10\x06\x12\x1b\n\x17RADIO_TECHNOLOGY_EVDO_0\x10\x07\x12\x1b\n\x17RADIO_TECHNOLOGY_EVDO_A\x10\x08\x12\x1a\n\x16RADIO_TECHNOLOGY_HSDPA\x10\t\x12\x1a\n\x16RADIO_TECHNOLOGY_HSUPA\x10\n\x12\x19\n\x15RADIO_TECHNOLOGY_HSPA\x10\x0b\x12\x1b\n\x17RADIO_TECHNOLOGY_EVDO_B\x10\x0c\x12\x18\n\x14RADIO_TECHNOLOGY_LTE\x10\r\x12\x1a\n\x16RADIO_TECHNOLOGY_EHRPD\x10\x0e\x12\x1a\n\x16RADIO_TECHNOLOGY_HSPAP\x10\x0f\x12\x18\n\x14RADIO_TECHNOLOGY_GSM\x10\x10\x12\x1d\n\x19RADIO_TECHNOLOGY_TD_SCDMA\x10\x11\x12\x1a\n\x16RADIO_TECHNOLOGY_IWLAN\x10\x12\x12\x1b\n\x17RADIO_TECHNOLOGY_LTE_CA\x10\x13\x12\x17\n\x13RADIO_TECHNOLOGY_NR\x10\x14\x42\x17\x42\x13\x44\x61taStallEventProtoP\x01')

_PROBERESULT = DESCRIPTOR.enum_types_by_name['ProbeResult']
ProbeResult = enum_type_wrapper.EnumTypeWrapper(_PROBERESULT)
_APBAND = DESCRIPTOR.enum_types_by_name['ApBand']
ApBand = enum_type_wrapper.EnumTypeWrapper(_APBAND)
_RADIOTECH = DESCRIPTOR.enum_types_by_name['RadioTech']
RadioTech = enum_type_wrapper.EnumTypeWrapper(_RADIOTECH)
UNKNOWN = 0
VALID = 1
INVALID = 2
PORTAL = 3
PARTIAL = 4
AP_BAND_UNKNOWN = 0
AP_BAND_2GHZ = 1
AP_BAND_5GHZ = 2
AP_BAND_6GHZ = 3
RADIO_TECHNOLOGY_UNKNOWN = 0
RADIO_TECHNOLOGY_GPRS = 1
RADIO_TECHNOLOGY_EDGE = 2
RADIO_TECHNOLOGY_UMTS = 3
RADIO_TECHNOLOGY_IS95A = 4
RADIO_TECHNOLOGY_IS95B = 5
RADIO_TECHNOLOGY_1XRTT = 6
RADIO_TECHNOLOGY_EVDO_0 = 7
RADIO_TECHNOLOGY_EVDO_A = 8
RADIO_TECHNOLOGY_HSDPA = 9
RADIO_TECHNOLOGY_HSUPA = 10
RADIO_TECHNOLOGY_HSPA = 11
RADIO_TECHNOLOGY_EVDO_B = 12
RADIO_TECHNOLOGY_LTE = 13
RADIO_TECHNOLOGY_EHRPD = 14
RADIO_TECHNOLOGY_HSPAP = 15
RADIO_TECHNOLOGY_GSM = 16
RADIO_TECHNOLOGY_TD_SCDMA = 17
RADIO_TECHNOLOGY_IWLAN = 18
RADIO_TECHNOLOGY_LTE_CA = 19
RADIO_TECHNOLOGY_NR = 20


_CELLULARDATA = DESCRIPTOR.message_types_by_name['CellularData']
_WIFIDATA = DESCRIPTOR.message_types_by_name['WifiData']
_DNSEVENT = DESCRIPTOR.message_types_by_name['DnsEvent']
CellularData = _reflection.GeneratedProtocolMessageType('CellularData', (_message.Message,), {
  'DESCRIPTOR' : _CELLULARDATA,
  '__module__' : 'frameworks.proto_logging.stats.enums.server.connectivity.data_stall_event_pb2'
  # @@protoc_insertion_point(class_scope:com.android.server.connectivity.CellularData)
  })
_sym_db.RegisterMessage(CellularData)

WifiData = _reflection.GeneratedProtocolMessageType('WifiData', (_message.Message,), {
  'DESCRIPTOR' : _WIFIDATA,
  '__module__' : 'frameworks.proto_logging.stats.enums.server.connectivity.data_stall_event_pb2'
  # @@protoc_insertion_point(class_scope:com.android.server.connectivity.WifiData)
  })
_sym_db.RegisterMessage(WifiData)

DnsEvent = _reflection.GeneratedProtocolMessageType('DnsEvent', (_message.Message,), {
  'DESCRIPTOR' : _DNSEVENT,
  '__module__' : 'frameworks.proto_logging.stats.enums.server.connectivity.data_stall_event_pb2'
  # @@protoc_insertion_point(class_scope:com.android.server.connectivity.DnsEvent)
  })
_sym_db.RegisterMessage(DnsEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\023DataStallEventProtoP\001'
  _PROBERESULT._serialized_start=436
  _PROBERESULT._serialized_end=511
  _APBAND._serialized_start=513
  _APBAND._serialized_end=596
  _RADIOTECH._serialized_start=599
  _RADIOTECH._serialized_end=1196
  _CELLULARDATA._serialized_start=117
  _CELLULARDATA._serialized_end=282
  _WIFIDATA._serialized_start=284
  _WIFIDATA._serialized_end=379
  _DNSEVENT._serialized_start=381
  _DNSEVENT._serialized_end=434
# @@protoc_insertion_point(module_scope)
