# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: toc.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttoc.proto\x12\x03Toc\"\x81\x01\n\x0e\x43orpusMetadata\x12\x0f\n\x07\x62\x61\x63kend\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nlandingUrl\x18\x03 \x01(\t\x12\x13\n\x0blibraryName\x18\x04 \x01(\t\x12\x15\n\rrecsWidgetUrl\x18\x06 \x01(\t\x12\x10\n\x08shopName\x18\x07 \x01(\t\"b\n\rBillingConfig\x12\x37\n\x14\x63\x61rrierBillingConfig\x18\x01 \x01(\x0b\x32\x19.Toc.CarrierBillingConfig\x12\x18\n\x10maxIabApiVersion\x18\x02 \x01(\x05\"#\n\x0b\x45xperiments\x12\x14\n\x0c\x65xperimentId\x18\x01 \x03(\t\"\xbc\x04\n\x0bTocResponse\x12#\n\x06\x63orpus\x18\x01 \x03(\x0b\x32\x13.Toc.CorpusMetadata\x12\x1c\n\x14tosVersionDeprecated\x18\x02 \x01(\x05\x12\x12\n\ntosContent\x18\x03 \x01(\t\x12\x0f\n\x07homeUrl\x18\x04 \x01(\t\x12%\n\x0b\x65xperiments\x18\x05 \x01(\x0b\x32\x10.Toc.Experiments\x12&\n\x1etosCheckboxTextMarketingEmails\x18\x06 \x01(\t\x12\x10\n\x08tosToken\x18\x07 \x01(\t\x12\'\n\x0cuserSettings\x18\x08 \x01(\x0b\x32\x11.Toc.UserSettings\x12\x17\n\x0ficonOverrideUrl\x18\t \x01(\t\x12/\n\x10selfUpdateConfig\x18\n \x01(\x0b\x32\x15.Toc.SelfUpdateConfig\x12\"\n\x1arequiresUploadDeviceConfig\x18\x0b \x01(\x08\x12)\n\rbillingConfig\x18\x0c \x01(\x0b\x32\x12.Toc.BillingConfig\x12\x15\n\rrecsWidgetUrl\x18\r \x01(\t\x12\x15\n\rsocialHomeUrl\x18\x0f \x01(\t\x12\x1f\n\x17\x61geVerificationRequired\x18\x10 \x01(\x08\x12\x1a\n\x12gplusSignupEnabled\x18\x11 \x01(\x08\x12\x15\n\rredeemEnabled\x18\x12 \x01(\x08\x12\x0f\n\x07helpUrl\x18\x13 \x01(\t\x12\x0f\n\x07themeId\x18\x14 \x01(\x05\"\xe9\x01\n\x14\x43\x61rrierBillingConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\napiVersion\x18\x03 \x01(\x05\x12\x17\n\x0fprovisioningUrl\x18\x04 \x01(\t\x12\x16\n\x0e\x63redentialsUrl\x18\x05 \x01(\t\x12\x13\n\x0btosRequired\x18\x06 \x01(\x08\x12)\n!perTransactionCredentialsRequired\x18\x07 \x01(\x08\x12\x32\n*sendSubscriberIdWithCarrierBillingRequests\x18\x08 \x01(\x08\"9\n\x0cUserSettings\x12)\n!tosCheckboxMarketingEmailsOptedIn\x18\x01 \x01(\x08\"3\n\x10SelfUpdateConfig\x12\x1f\n\x17latestClientVersionCode\x18\x01 \x01(\x05\x42\'\n com.google.android.finsky.protosB\x03Toc')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'toc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\003Toc'
  _globals['_CORPUSMETADATA']._serialized_start=19
  _globals['_CORPUSMETADATA']._serialized_end=148
  _globals['_BILLINGCONFIG']._serialized_start=150
  _globals['_BILLINGCONFIG']._serialized_end=248
  _globals['_EXPERIMENTS']._serialized_start=250
  _globals['_EXPERIMENTS']._serialized_end=285
  _globals['_TOCRESPONSE']._serialized_start=288
  _globals['_TOCRESPONSE']._serialized_end=860
  _globals['_CARRIERBILLINGCONFIG']._serialized_start=863
  _globals['_CARRIERBILLINGCONFIG']._serialized_end=1096
  _globals['_USERSETTINGS']._serialized_start=1098
  _globals['_USERSETTINGS']._serialized_end=1155
  _globals['_SELFUPDATECONFIG']._serialized_start=1157
  _globals['_SELFUPDATECONFIG']._serialized_end=1208
# @@protoc_insertion_point(module_scope)
