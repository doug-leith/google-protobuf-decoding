# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_analytics.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63lient_analytics.proto\x12\x0f\x43lientAnalytics\"\x8d\x01\n\x11\x44\x65sktopClientInfo\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x11\n\tloggingId\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x16\n\x0eosMajorVersion\x18\x04 \x01(\t\x12\x15\n\rosFullVersion\x18\x05 \x01(\t\x12\x18\n\x10\x61pplicationBuild\x18\x06 \x01(\t\"\xbb\x02\n\nClientInfo\x12\x12\n\nclientType\x18\x01 \x01(\x05\x12=\n\x11\x61ndroidClientInfo\x18\x02 \x01(\x0b\x32\".ClientAnalytics.AndroidClientInfo\x12=\n\x11\x64\x65sktopClientInfo\x18\x03 \x01(\x0b\x32\".ClientAnalytics.DesktopClientInfo\x12\x35\n\riosClientInfo\x18\x04 \x01(\x0b\x32\x1e.ClientAnalytics.IosClientInfo\x12;\n\x10playCeClientInfo\x18\x05 \x01(\x0b\x32!.ClientAnalytics.PlayCeClientInfo\x12\x12\n\nremoteHost\x18\x06 \x01(\t\x12\x13\n\x0bremoteHost6\x18\x07 \x01(\t\"\x1e\n\x10\x45xperimentIdList\x12\n\n\x02id\x18\x01 \x03(\t\"}\n\x11\x41\x63tiveExperiments\x12 \n\x18\x63lientAlteringExperiment\x18\x01 \x03(\t\x12\x17\n\x0fotherExperiment\x18\x02 \x03(\t\x12\x15\n\rgwsExperiment\x18\x03 \x03(\x05\x12\x16\n\x0eplayExperiment\x18\x04 \x03(\x05\"/\n\x11LogEventKeyValues\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xea\x03\n\x08LogEvent\x12\x13\n\x0b\x65ventTimeMs\x18\x01 \x01(\x03\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x31\n\x05value\x18\x03 \x03(\x0b\x32\".ClientAnalytics.LogEventKeyValues\x12\x17\n\x0fsourceExtension\x18\x06 \x01(\x0c\x12/\n\x03\x65xp\x18\x07 \x01(\x0b\x32\".ClientAnalytics.ActiveExperiments\x12\x19\n\x11sourceExtensionJs\x18\x08 \x01(\x0c\x12\x37\n\nappUsage1P\x18\t \x01(\x0b\x32#.ClientAnalytics.AppUsage1pLogEvent\x12\x17\n\x0fisUserInitiated\x18\n \x01(\x08\x12\x11\n\teventCode\x18\x0b \x01(\x05\x12\x13\n\x0b\x65ventFlowId\x18\x0c \x01(\x05\x12\x1b\n\x13sourceExtensionJson\x18\r \x01(\x0c\x12\x0e\n\x06testId\x18\x0e \x01(\t\x12\x1d\n\x15timezoneOffsetSeconds\x18\x0f \x01(\x03\x12\x35\n\rexperimentIds\x18\x10 \x01(\x0b\x32\x1e.ClientAnalytics.ExperimentIds\x12\x15\n\reventUptimeMs\x18\x11 \x01(\x03\x12\x10\n\x08\x63lientVe\x18\x12 \x01(\x0c\"\x87\x01\n\x10PlayCeClientInfo\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x0c\n\x04make\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x18\n\x10\x61pplicationBuild\x18\x05 \x01(\t\x12\x17\n\x0fplatformVersion\x18\x06 \x01(\t\x12\x11\n\tloggingId\x18\x07 \x01(\t\"M\n\rExperimentIds\x12\x11\n\tclearBlob\x18\x01 \x01(\x0c\x12\x15\n\rencryptedBlob\x18\x02 \x03(\x0c\x12\x12\n\nusersMatch\x18\x03 \x01(\x08\"R\n\x12\x41ppUsage1pLogEvent\x12\x0f\n\x07\x61ppType\x18\x01 \x01(\x05\x12\x1a\n\x12\x61ndroidPackageName\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"}\n\rIosClientInfo\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x11\n\tloggingId\x18\x02 \x01(\t\x12\x16\n\x0eosMajorVersion\x18\x03 \x01(\t\x12\x15\n\rosFullVersion\x18\x04 \x01(\t\x12\x18\n\x10\x61pplicationBuild\x18\x05 \x01(\t\"d\n\x0bLogResponse\x12\x1d\n\x15nextRequestWaitMillis\x18\x01 \x01(\x03\x12\x36\n\x0b\x65xperiments\x18\x02 \x01(\x0b\x32!.ClientAnalytics.ExperimentIdList\"\xf8\x02\n\x11\x41ndroidClientInfo\x12\x11\n\tandroidId\x18\x01 \x01(\x03\x12\x11\n\tloggingId\x18\x02 \x01(\t\x12\x12\n\nsdkVersion\x18\x03 \x01(\x05\x12\r\n\x05model\x18\x04 \x01(\t\x12\x0f\n\x07product\x18\x05 \x01(\t\x12\x0f\n\x07osBuild\x18\x06 \x01(\t\x12\x18\n\x10\x61pplicationBuild\x18\x07 \x01(\t\x12\x10\n\x08hardware\x18\x08 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\t \x01(\t\x12\x0e\n\x06mccMnc\x18\n \x01(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x0f\n\x07\x63ountry\x18\x0c \x01(\t\x12\x14\n\x0cmanufacturer\x18\r \x01(\t\x12\r\n\x05\x62rand\x18\x0e \x01(\t\x12\r\n\x05\x62oard\x18\x0f \x01(\t\x12\x14\n\x0cradioVersion\x18\x10 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x11 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x12 \x01(\x03\x12\x1a\n\x12gmsCoreVersionCode\x18\x13 \x01(\x05\"\xf9\x01\n\nLogRequest\x12/\n\nclientInfo\x18\x01 \x01(\x0b\x32\x1b.ClientAnalytics.ClientInfo\x12\x11\n\tlogSource\x18\x02 \x01(\x05\x12+\n\x08logEvent\x18\x03 \x03(\x0b\x32\x19.ClientAnalytics.LogEvent\x12\x15\n\rrequestTimeMs\x18\x04 \x01(\x03\x12\x1b\n\x13serializedLogEvents\x18\x05 \x03(\x0c\x12\x15\n\rlogSourceName\x18\x06 \x01(\t\x12\x16\n\x0ezwiebackCookie\x18\x07 \x01(\t\x12\x17\n\x0frequestUptimeMs\x18\x08 \x01(\x03\x42\x34\n!com.google.android.play.analyticsB\x0f\x43lientAnalytics')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_analytics_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.android.play.analyticsB\017ClientAnalytics'
  _globals['_DESKTOPCLIENTINFO']._serialized_start=44
  _globals['_DESKTOPCLIENTINFO']._serialized_end=185
  _globals['_CLIENTINFO']._serialized_start=188
  _globals['_CLIENTINFO']._serialized_end=503
  _globals['_EXPERIMENTIDLIST']._serialized_start=505
  _globals['_EXPERIMENTIDLIST']._serialized_end=535
  _globals['_ACTIVEEXPERIMENTS']._serialized_start=537
  _globals['_ACTIVEEXPERIMENTS']._serialized_end=662
  _globals['_LOGEVENTKEYVALUES']._serialized_start=664
  _globals['_LOGEVENTKEYVALUES']._serialized_end=711
  _globals['_LOGEVENT']._serialized_start=714
  _globals['_LOGEVENT']._serialized_end=1204
  _globals['_PLAYCECLIENTINFO']._serialized_start=1207
  _globals['_PLAYCECLIENTINFO']._serialized_end=1342
  _globals['_EXPERIMENTIDS']._serialized_start=1344
  _globals['_EXPERIMENTIDS']._serialized_end=1421
  _globals['_APPUSAGE1PLOGEVENT']._serialized_start=1423
  _globals['_APPUSAGE1PLOGEVENT']._serialized_end=1505
  _globals['_IOSCLIENTINFO']._serialized_start=1507
  _globals['_IOSCLIENTINFO']._serialized_end=1632
  _globals['_LOGRESPONSE']._serialized_start=1634
  _globals['_LOGRESPONSE']._serialized_end=1734
  _globals['_ANDROIDCLIENTINFO']._serialized_start=1737
  _globals['_ANDROIDCLIENTINFO']._serialized_end=2113
  _globals['_LOGREQUEST']._serialized_start=2116
  _globals['_LOGREQUEST']._serialized_end=2365
# @@protoc_insertion_point(module_scope)
