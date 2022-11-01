# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcheckin.proto\"\x99\x13\n\x0e\x43heckinRequest\x12\x0c\n\x04imei\x18\x01 \x01(\t\x12\x11\n\tandroidId\x18\x02 \x01(\x03\x12\x11\n\tgsfDigest\x18\x03 \x01(\t\x12(\n\x07\x63heckin\x18\x04 \x02(\x0b\x32\x17.CheckinRequest.Checkin\x12\x14\n\x0c\x64\x65siredBuild\x18\x05 \x01(\t\x12\x13\n\x0blanguageTag\x18\x06 \x01(\t\x12\x11\n\tloggingId\x18\x07 \x01(\x04\x12\x15\n\rmarketCheckin\x18\x08 \x01(\t\x12\x16\n\x0ewifiMacAddress\x18\t \x03(\t\x12\x0c\n\x04IMEI\x18\n \x01(\t\x12\x15\n\raccountCookie\x18\x0b \x03(\t\x12\x10\n\x08timeZone\x18\x0c \x01(\t\x12\x15\n\rsecurityToken\x18\r \x01(\x06\x12\x0f\n\x07version\x18\x0e \x01(\x05\x12\x0f\n\x07otaCert\x18\x0f \x03(\t\x12\x1c\n\x14hardwareSerialNumber\x18\x10 \x01(\t\x12\x19\n\x11phoneDeviceId_esn\x18\x11 \x01(\t\x12\x39\n\x13\x64\x65viceConfiguration\x18\x12 \x01(\x0b\x32\x1c.CheckinRequest.DeviceConfig\x12\x16\n\x0emacAddressType\x18\x13 \x03(\t\x12\x10\n\x08\x66ragment\x18\x14 \x02(\x05\x12\x10\n\x08userName\x18\x15 \x01(\t\x12\x18\n\x10userSerialNumber\x18\x16 \x01(\x05\x12 \n\x18\x64roidguardResultsRequest\x18\x18 \x01(\t\x12\x1d\n\x15\x64\x65viceDataVersionInfo\x18\x19 \x01(\t\x1a\xcc\n\n\x07\x43heckin\x12,\n\x05\x62uild\x18\x01 \x02(\x0b\x32\x1d.CheckinRequest.Checkin.Build\x12\x15\n\rlastCheckinMs\x18\x02 \x01(\x03\x12,\n\x05\x65vent\x18\x03 \x03(\x0b\x32\x1d.CheckinRequest.Checkin.Event\x12/\n\x04stat\x18\x04 \x03(\x0b\x32!.CheckinRequest.Checkin.Statistic\x12\x16\n\x0erequestedGroup\x18\x05 \x03(\t\x12\x16\n\x0emobileOperator\x18\x06 \x01(\t\x12\x13\n\x0bsimOperator\x18\x07 \x01(\t\x12\x15\n\ractiveNetwork\x18\x08 \x01(\t\x12\x12\n\nuserNumber\x18\t \x01(\x05\x12\x36\n\ndeviceType\x18\x0e \x01(\x0e\x32\".CheckinRequest.Checkin.DeviceType\x12<\n\rmobileNetwork\x18\x10 \x01(\x0b\x32%.CheckinRequest.Checkin.MobileNetwork\x12\x14\n\x0cvoiceCapable\x18\x12 \x01(\x08\x12\x17\n\x0f\x64\x61taNetworkType\x18\x13 \x01(\t\x1a\xb3\x03\n\x05\x42uild\x12\x18\n\x10\x62uildFingerprint\x18\x01 \x01(\t\x12\x10\n\x08hardware\x18\x02 \x01(\t\x12\r\n\x05\x62rand\x18\x03 \x01(\t\x12\x14\n\x0cradioVersion\x18\x04 \x01(\t\x12\x12\n\nbootloader\x18\x05 \x01(\t\x12\x10\n\x08\x63lientId\x18\x06 \x01(\t\x12\x0c\n\x04time\x18\x07 \x01(\x03\x12!\n\x19googlePlayServicesVersion\x18\x08 \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\t \x01(\t\x12\x12\n\nsdkVersion\x18\n \x01(\x05\x12\r\n\x05model\x18\x0b \x01(\t\x12\x14\n\x0cmanufacturer\x18\x0c \x01(\t\x12\x0f\n\x07product\x18\r \x01(\t\x12\x14\n\x0cotaInstalled\x18\x0e \x01(\x08\x12\x46\n\x0f\x63ontentProvider\x18\x0f \x03(\x0b\x32-.CheckinRequest.Checkin.Build.ContentProvider\x12\x1a\n\x12securityPatchLevel\x18\x13 \x01(\t\x1a.\n\x0f\x43ontentProvider\x12\x0f\n\x07unknown\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x1a\x33\n\x05\x45vent\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0e\n\x06timeMs\x18\x03 \x01(\x03\x1a\x34\n\tStatistic\x12\x0b\n\x03tag\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0b\n\x03sum\x18\x03 \x01(\x02\x1a\x80\x02\n\rMobileNetwork\x12\x13\n\x0bsimOperator\x18\x01 \x01(\t\x12\x17\n\x0fsimOperatorName\x18\x02 \x01(\t\x12\x0f\n\x07roaming\x18\x03 \x01(\t\x12J\n\rdeviceFeature\x18\x04 \x03(\x0e\x32\x33.CheckinRequest.Checkin.MobileNetwork.DeviceFeature\x12\x0c\n\x04IMSI\x18\x06 \x01(\t\x12\x15\n\rgroupIdLevel1\x18\x07 \x01(\t\x12\x10\n\x08hashIMSI\x18\x08 \x01(\x0c\"-\n\rDeviceFeature\x12\t\n\x05VOICE\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x12\x07\n\x03SMS\x10\x02\"d\n\nDeviceType\x12\t\n\x05OTHER\x10\x01\x12\t\n\x05PHONE\x10\x02\x12\n\n\x06TABLET\x10\x03\x12\x06\n\x02TV\x10\x04\x12\t\n\x05GLASS\x10\x05\x12\x07\n\x03\x43\x41R\x10\x06\x12\x0c\n\x08WEARABLE\x10\x07\x12\n\n\x06THINGS\x10\t\x1a\xf1\x03\n\x0c\x44\x65viceConfig\x12\x13\n\x0btouchScreen\x18\x01 \x01(\x05\x12\x14\n\x0ckeyboardType\x18\x02 \x01(\x05\x12\x12\n\nnavigation\x18\x03 \x01(\x05\x12\x14\n\x0cscreenLayout\x18\x04 \x01(\x05\x12\x17\n\x0fhasHardKeyboard\x18\x05 \x01(\x08\x12\x1c\n\x14hasFiveWayNavigation\x18\x06 \x01(\x08\x12\x18\n\x10screenDensityDpi\x18\x07 \x01(\x05\x12\x13\n\x0bglEsVersion\x18\x08 \x01(\x05\x12\x15\n\rsharedLibrary\x18\t \x03(\t\x12\x18\n\x10\x61vailableFeature\x18\n \x03(\t\x12\x10\n\x08\x63puTypes\x18\x0b \x03(\t\x12\x19\n\x11screenWidthPixels\x18\x0c \x01(\x05\x12\x1a\n\x12screenHeightPixels\x18\r \x01(\x05\x12\x18\n\x10supportedLocales\x18\x0e \x03(\t\x12!\n\x19supportedOpenGLExtensions\x18\x0f \x03(\t\x12\x13\n\x0b\x64\x65viceClass\x18\x10 \x01(\x05\x12\x1c\n\x14maxApkDownloadSizeMb\x18\x11 \x01(\x05\x12\x1b\n\x13smallestScreenWidth\x18\x13 \x01(\x05\x12\x0e\n\x06memory\x18\x14 \x01(\x03\x12\x0f\n\x07numCPUs\x18\x15 \x01(\x05\"\x92\x04\n\x0f\x43heckinResponse\x12\x0f\n\x07statsOk\x18\x01 \x01(\x08\x12\'\n\x06intent\x18\x02 \x03(\x0b\x32\x17.CheckinResponse.Intent\x12\x0e\n\x06timeMs\x18\x03 \x01(\x03\x12\x0e\n\x06\x64igest\x18\x04 \x01(\t\x12\x32\n\x07setting\x18\x05 \x03(\x0b\x32!.CheckinResponse.GservicesSetting\x12\x10\n\x08marketOk\x18\x06 \x01(\x08\x12\x11\n\tandroidId\x18\x07 \x01(\x06\x12\x15\n\rsecurityToken\x18\x08 \x01(\x06\x12\x14\n\x0csettingsDiff\x18\t \x01(\x08\x12\x15\n\rdeleteSetting\x18\n \x03(\t\x12\x13\n\x0bversionInfo\x18\x0b \x01(\t\x12\x1d\n\x15\x64\x65viceDataVersionInfo\x18\x0c \x01(\t\x1a\xa2\x01\n\x06Intent\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taUri\x18\x02 \x01(\t\x12\x10\n\x08mimeType\x18\x03 \x01(\t\x12\x11\n\tjavaClass\x18\x04 \x01(\t\x12,\n\x05\x65xtra\x18\x05 \x03(\x0b\x32\x1d.CheckinResponse.Intent.Extra\x1a$\n\x05\x45xtra\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\r\n\x05value\x18\x07 \x01(\t\x1a/\n\x10GservicesSetting\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c')



_CHECKINREQUEST = DESCRIPTOR.message_types_by_name['CheckinRequest']
_CHECKINREQUEST_CHECKIN = _CHECKINREQUEST.nested_types_by_name['Checkin']
_CHECKINREQUEST_CHECKIN_BUILD = _CHECKINREQUEST_CHECKIN.nested_types_by_name['Build']
_CHECKINREQUEST_CHECKIN_BUILD_CONTENTPROVIDER = _CHECKINREQUEST_CHECKIN_BUILD.nested_types_by_name['ContentProvider']
_CHECKINREQUEST_CHECKIN_EVENT = _CHECKINREQUEST_CHECKIN.nested_types_by_name['Event']
_CHECKINREQUEST_CHECKIN_STATISTIC = _CHECKINREQUEST_CHECKIN.nested_types_by_name['Statistic']
_CHECKINREQUEST_CHECKIN_MOBILENETWORK = _CHECKINREQUEST_CHECKIN.nested_types_by_name['MobileNetwork']
_CHECKINREQUEST_DEVICECONFIG = _CHECKINREQUEST.nested_types_by_name['DeviceConfig']
_CHECKINRESPONSE = DESCRIPTOR.message_types_by_name['CheckinResponse']
_CHECKINRESPONSE_INTENT = _CHECKINRESPONSE.nested_types_by_name['Intent']
_CHECKINRESPONSE_INTENT_EXTRA = _CHECKINRESPONSE_INTENT.nested_types_by_name['Extra']
_CHECKINRESPONSE_GSERVICESSETTING = _CHECKINRESPONSE.nested_types_by_name['GservicesSetting']
_CHECKINREQUEST_CHECKIN_MOBILENETWORK_DEVICEFEATURE = _CHECKINREQUEST_CHECKIN_MOBILENETWORK.enum_types_by_name['DeviceFeature']
_CHECKINREQUEST_CHECKIN_DEVICETYPE = _CHECKINREQUEST_CHECKIN.enum_types_by_name['DeviceType']
CheckinRequest = _reflection.GeneratedProtocolMessageType('CheckinRequest', (_message.Message,), {

  'Checkin' : _reflection.GeneratedProtocolMessageType('Checkin', (_message.Message,), {

    'Build' : _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {

      'ContentProvider' : _reflection.GeneratedProtocolMessageType('ContentProvider', (_message.Message,), {
        'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN_BUILD_CONTENTPROVIDER,
        '__module__' : 'checkin_pb2'
        # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin.Build.ContentProvider)
        })
      ,
      'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN_BUILD,
      '__module__' : 'checkin_pb2'
      # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin.Build)
      })
    ,

    'Event' : _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
      'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN_EVENT,
      '__module__' : 'checkin_pb2'
      # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin.Event)
      })
    ,

    'Statistic' : _reflection.GeneratedProtocolMessageType('Statistic', (_message.Message,), {
      'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN_STATISTIC,
      '__module__' : 'checkin_pb2'
      # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin.Statistic)
      })
    ,

    'MobileNetwork' : _reflection.GeneratedProtocolMessageType('MobileNetwork', (_message.Message,), {
      'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN_MOBILENETWORK,
      '__module__' : 'checkin_pb2'
      # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin.MobileNetwork)
      })
    ,
    'DESCRIPTOR' : _CHECKINREQUEST_CHECKIN,
    '__module__' : 'checkin_pb2'
    # @@protoc_insertion_point(class_scope:CheckinRequest.Checkin)
    })
  ,

  'DeviceConfig' : _reflection.GeneratedProtocolMessageType('DeviceConfig', (_message.Message,), {
    'DESCRIPTOR' : _CHECKINREQUEST_DEVICECONFIG,
    '__module__' : 'checkin_pb2'
    # @@protoc_insertion_point(class_scope:CheckinRequest.DeviceConfig)
    })
  ,
  'DESCRIPTOR' : _CHECKINREQUEST,
  '__module__' : 'checkin_pb2'
  # @@protoc_insertion_point(class_scope:CheckinRequest)
  })
_sym_db.RegisterMessage(CheckinRequest)
_sym_db.RegisterMessage(CheckinRequest.Checkin)
_sym_db.RegisterMessage(CheckinRequest.Checkin.Build)
_sym_db.RegisterMessage(CheckinRequest.Checkin.Build.ContentProvider)
_sym_db.RegisterMessage(CheckinRequest.Checkin.Event)
_sym_db.RegisterMessage(CheckinRequest.Checkin.Statistic)
_sym_db.RegisterMessage(CheckinRequest.Checkin.MobileNetwork)
_sym_db.RegisterMessage(CheckinRequest.DeviceConfig)

CheckinResponse = _reflection.GeneratedProtocolMessageType('CheckinResponse', (_message.Message,), {

  'Intent' : _reflection.GeneratedProtocolMessageType('Intent', (_message.Message,), {

    'Extra' : _reflection.GeneratedProtocolMessageType('Extra', (_message.Message,), {
      'DESCRIPTOR' : _CHECKINRESPONSE_INTENT_EXTRA,
      '__module__' : 'checkin_pb2'
      # @@protoc_insertion_point(class_scope:CheckinResponse.Intent.Extra)
      })
    ,
    'DESCRIPTOR' : _CHECKINRESPONSE_INTENT,
    '__module__' : 'checkin_pb2'
    # @@protoc_insertion_point(class_scope:CheckinResponse.Intent)
    })
  ,

  'GservicesSetting' : _reflection.GeneratedProtocolMessageType('GservicesSetting', (_message.Message,), {
    'DESCRIPTOR' : _CHECKINRESPONSE_GSERVICESSETTING,
    '__module__' : 'checkin_pb2'
    # @@protoc_insertion_point(class_scope:CheckinResponse.GservicesSetting)
    })
  ,
  'DESCRIPTOR' : _CHECKINRESPONSE,
  '__module__' : 'checkin_pb2'
  # @@protoc_insertion_point(class_scope:CheckinResponse)
  })
_sym_db.RegisterMessage(CheckinResponse)
_sym_db.RegisterMessage(CheckinResponse.Intent)
_sym_db.RegisterMessage(CheckinResponse.Intent.Extra)
_sym_db.RegisterMessage(CheckinResponse.GservicesSetting)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKINREQUEST._serialized_start=18
  _CHECKINREQUEST._serialized_end=2475
  _CHECKINREQUEST_CHECKIN._serialized_start=619
  _CHECKINREQUEST_CHECKIN._serialized_end=1975
  _CHECKINREQUEST_CHECKIN_BUILD._serialized_start=1072
  _CHECKINREQUEST_CHECKIN_BUILD._serialized_end=1507
  _CHECKINREQUEST_CHECKIN_BUILD_CONTENTPROVIDER._serialized_start=1461
  _CHECKINREQUEST_CHECKIN_BUILD_CONTENTPROVIDER._serialized_end=1507
  _CHECKINREQUEST_CHECKIN_EVENT._serialized_start=1509
  _CHECKINREQUEST_CHECKIN_EVENT._serialized_end=1560
  _CHECKINREQUEST_CHECKIN_STATISTIC._serialized_start=1562
  _CHECKINREQUEST_CHECKIN_STATISTIC._serialized_end=1614
  _CHECKINREQUEST_CHECKIN_MOBILENETWORK._serialized_start=1617
  _CHECKINREQUEST_CHECKIN_MOBILENETWORK._serialized_end=1873
  _CHECKINREQUEST_CHECKIN_MOBILENETWORK_DEVICEFEATURE._serialized_start=1828
  _CHECKINREQUEST_CHECKIN_MOBILENETWORK_DEVICEFEATURE._serialized_end=1873
  _CHECKINREQUEST_CHECKIN_DEVICETYPE._serialized_start=1875
  _CHECKINREQUEST_CHECKIN_DEVICETYPE._serialized_end=1975
  _CHECKINREQUEST_DEVICECONFIG._serialized_start=1978
  _CHECKINREQUEST_DEVICECONFIG._serialized_end=2475
  _CHECKINRESPONSE._serialized_start=2478
  _CHECKINRESPONSE._serialized_end=3008
  _CHECKINRESPONSE_INTENT._serialized_start=2797
  _CHECKINRESPONSE_INTENT._serialized_end=2959
  _CHECKINRESPONSE_INTENT_EXTRA._serialized_start=2923
  _CHECKINRESPONSE_INTENT_EXTRA._serialized_end=2959
  _CHECKINRESPONSE_GSERVICESSETTING._serialized_start=2961
  _CHECKINRESPONSE_GSERVICESSETTING._serialized_end=3008
# @@protoc_insertion_point(module_scope)
