# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notifications.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import library_update_proto_pb2 as library__update__proto__pb2
import android_app_delivery_pb2 as android__app__delivery__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13notifications.proto\x12\rNotifications\x1a\x1alibrary_update_proto.proto\x1a\x1a\x61ndroid_app_delivery.proto\x1a\x0c\x63ommon.proto\"B\n\x1a\x41ndroidAppNotificationData\x12\x13\n\x0bversionCode\x18\x01 \x01(\x05\x12\x0f\n\x07\x61ssetId\x18\x02 \x01(\t\"6\n\x10LibraryDirtyData\x12\x0f\n\x07\x62\x61\x63kend\x18\x01 \x01(\x05\x12\x11\n\tlibraryId\x18\x02 \x01(\t\"M\n\x15InAppNotificationData\x12\x17\n\x0f\x63heckoutOrderId\x18\x01 \x01(\t\x12\x1b\n\x13inAppNotificationId\x18\x02 \x01(\t\"\x98\x05\n\x0cNotification\x12\x18\n\x10notificationType\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x1c\n\x05\x64ocid\x18\x04 \x01(\x0b\x32\r.Common.Docid\x12\x10\n\x08\x64ocTitle\x18\x05 \x01(\t\x12\x11\n\tuserEmail\x18\x06 \x01(\t\x12:\n\x07\x61ppData\x18\x07 \x01(\x0b\x32).Notifications.AndroidAppNotificationData\x12\x43\n\x0f\x61ppDeliveryData\x18\x08 \x01(\x0b\x32*.AndroidAppDelivery.AndroidAppDeliveryData\x12?\n\x13purchaseRemovalData\x18\t \x01(\x0b\x32\".Notifications.PurchaseRemovalData\x12\x41\n\x14userNotificationData\x18\n \x01(\x0b\x32#.Notifications.UserNotificationData\x12\x43\n\x15inAppNotificationData\x18\x0b \x01(\x0b\x32$.Notifications.InAppNotificationData\x12\x41\n\x14purchaseDeclinedData\x18\x0c \x01(\x0b\x32#.Notifications.PurchaseDeclinedData\x12\x16\n\x0enotificationId\x18\r \x01(\t\x12\x38\n\rlibraryUpdate\x18\x0e \x01(\x0b\x32!.LibraryUpdateProto.LibraryUpdate\x12\x39\n\x10libraryDirtyData\x18\x0f \x01(\x0b\x32\x1f.Notifications.LibraryDirtyData\"@\n\x14PurchaseDeclinedData\x12\x0e\n\x06reason\x18\x01 \x01(\x05\x12\x18\n\x10showNotification\x18\x02 \x01(\x08\"(\n\x13PurchaseRemovalData\x12\x11\n\tmalicious\x18\x01 \x01(\x08\"\x88\x01\n\x14UserNotificationData\x12\x19\n\x11notificationTitle\x18\x01 \x01(\t\x12\x18\n\x10notificationText\x18\x02 \x01(\t\x12\x12\n\ntickerText\x18\x03 \x01(\t\x12\x13\n\x0b\x64ialogTitle\x18\x04 \x01(\t\x12\x12\n\ndialogText\x18\x05 \x01(\tB1\n com.google.android.finsky.protosB\rNotifications')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\rNotifications'
  _globals['_ANDROIDAPPNOTIFICATIONDATA']._serialized_start=108
  _globals['_ANDROIDAPPNOTIFICATIONDATA']._serialized_end=174
  _globals['_LIBRARYDIRTYDATA']._serialized_start=176
  _globals['_LIBRARYDIRTYDATA']._serialized_end=230
  _globals['_INAPPNOTIFICATIONDATA']._serialized_start=232
  _globals['_INAPPNOTIFICATIONDATA']._serialized_end=309
  _globals['_NOTIFICATION']._serialized_start=312
  _globals['_NOTIFICATION']._serialized_end=976
  _globals['_PURCHASEDECLINEDDATA']._serialized_start=978
  _globals['_PURCHASEDECLINEDDATA']._serialized_end=1042
  _globals['_PURCHASEREMOVALDATA']._serialized_start=1044
  _globals['_PURCHASEREMOVALDATA']._serialized_end=1084
  _globals['_USERNOTIFICATIONDATA']._serialized_start=1087
  _globals['_USERNOTIFICATIONDATA']._serialized_end=1223
# @@protoc_insertion_point(module_scope)
