# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frameworks/proto_logging/stats/enums/bluetooth/smp/enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>frameworks/proto_logging/stats/enums/bluetooth/smp/enums.proto\x12\x15\x61ndroid.bluetooth.smp*\x8e\x03\n\x0b\x43ommandEnum\x12\x0f\n\x0b\x43MD_UNKNOWN\x10\x00\x12\x17\n\x13\x43MD_PAIRING_REQUEST\x10\x01\x12\x18\n\x14\x43MD_PAIRING_RESPONSE\x10\x02\x12\x17\n\x13\x43MD_PAIRING_CONFIRM\x10\x03\x12\x16\n\x12\x43MD_PAIRING_RANDOM\x10\x04\x12\x16\n\x12\x43MD_PAIRING_FAILED\x10\x05\x12\x18\n\x14\x43MD_ENCRYPTION_INFON\x10\x06\x12\x1d\n\x19\x43MD_MASTER_IDENTIFICATION\x10\x07\x12\x15\n\x11\x43MD_IDENTITY_INFO\x10\x08\x12\x1a\n\x16\x43MD_IDENTITY_ADDR_INFO\x10\t\x12\x14\n\x10\x43MD_SIGNING_INFO\x10\n\x12\x18\n\x14\x43MD_SECURITY_REQUEST\x10\x0b\x12\x1a\n\x16\x43MD_PAIRING_PUBLIC_KEY\x10\x0c\x12\x1b\n\x17\x43MD_PAIRING_DHKEY_CHECK\x10\r\x12\x1d\n\x19\x43MD_PAIRING_KEYPRESS_INFO\x10\x0e*\xe9\x04\n\x15PairingFailReasonEnum\x12 \n\x1cPAIRING_FAIL_REASON_RESERVED\x10\x00\x12%\n!PAIRING_FAIL_REASON_PASSKEY_ENTRY\x10\x01\x12\x1b\n\x17PAIRING_FAIL_REASON_OOB\x10\x02\x12 \n\x1cPAIRING_FAIL_REASON_AUTH_REQ\x10\x03\x12%\n!PAIRING_FAIL_REASON_CONFIRM_VALUE\x10\x04\x12(\n$PAIRING_FAIL_REASON_PAIR_NOT_SUPPORT\x10\x05\x12$\n PAIRING_FAIL_REASON_ENC_KEY_SIZE\x10\x06\x12#\n\x1fPAIRING_FAIL_REASON_INVALID_CMD\x10\x07\x12#\n\x1fPAIRING_FAIL_REASON_UNSPECIFIED\x10\x08\x12)\n%PAIRING_FAIL_REASON_REPEATED_ATTEMPTS\x10\t\x12*\n&PAIRING_FAIL_REASON_INVALID_PARAMETERS\x10\n\x12!\n\x1dPAIRING_FAIL_REASON_DHKEY_CHK\x10\x0b\x12*\n&PAIRING_FAIL_REASON_NUMERIC_COMPARISON\x10\x0c\x12\x30\n,PAIRING_FAIL_REASON_CLASSIC_PAIRING_IN_PROGR\x10\r\x12/\n+PAIRING_FAIL_REASON_XTRANS_DERIVE_NOT_ALLOW\x10\x0e\x42\x1a\x42\x16\x42luetoothSmpProtoEnumsP\x01')

_COMMANDENUM = DESCRIPTOR.enum_types_by_name['CommandEnum']
CommandEnum = enum_type_wrapper.EnumTypeWrapper(_COMMANDENUM)
_PAIRINGFAILREASONENUM = DESCRIPTOR.enum_types_by_name['PairingFailReasonEnum']
PairingFailReasonEnum = enum_type_wrapper.EnumTypeWrapper(_PAIRINGFAILREASONENUM)
CMD_UNKNOWN = 0
CMD_PAIRING_REQUEST = 1
CMD_PAIRING_RESPONSE = 2
CMD_PAIRING_CONFIRM = 3
CMD_PAIRING_RANDOM = 4
CMD_PAIRING_FAILED = 5
CMD_ENCRYPTION_INFON = 6
CMD_MASTER_IDENTIFICATION = 7
CMD_IDENTITY_INFO = 8
CMD_IDENTITY_ADDR_INFO = 9
CMD_SIGNING_INFO = 10
CMD_SECURITY_REQUEST = 11
CMD_PAIRING_PUBLIC_KEY = 12
CMD_PAIRING_DHKEY_CHECK = 13
CMD_PAIRING_KEYPRESS_INFO = 14
PAIRING_FAIL_REASON_RESERVED = 0
PAIRING_FAIL_REASON_PASSKEY_ENTRY = 1
PAIRING_FAIL_REASON_OOB = 2
PAIRING_FAIL_REASON_AUTH_REQ = 3
PAIRING_FAIL_REASON_CONFIRM_VALUE = 4
PAIRING_FAIL_REASON_PAIR_NOT_SUPPORT = 5
PAIRING_FAIL_REASON_ENC_KEY_SIZE = 6
PAIRING_FAIL_REASON_INVALID_CMD = 7
PAIRING_FAIL_REASON_UNSPECIFIED = 8
PAIRING_FAIL_REASON_REPEATED_ATTEMPTS = 9
PAIRING_FAIL_REASON_INVALID_PARAMETERS = 10
PAIRING_FAIL_REASON_DHKEY_CHK = 11
PAIRING_FAIL_REASON_NUMERIC_COMPARISON = 12
PAIRING_FAIL_REASON_CLASSIC_PAIRING_IN_PROGR = 13
PAIRING_FAIL_REASON_XTRANS_DERIVE_NOT_ALLOW = 14


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\026BluetoothSmpProtoEnumsP\001'
  _COMMANDENUM._serialized_start=90
  _COMMANDENUM._serialized_end=488
  _PAIRINGFAILREASONENUM._serialized_start=491
  _PAIRINGFAILREASONENUM._serialized_end=1108
# @@protoc_insertion_point(module_scope)
