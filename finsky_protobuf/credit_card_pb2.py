# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: credit_card.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import image_with_caption_outer_class_pb2 as image__with__caption__outer__class__pb2
import legal_message_set_outer_class_pb2 as legal__message__set__outer__class__pb2
import address_form_outer_class_pb2 as address__form__outer__class__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63redit_card.proto\x12\nCreditCard\x1a$image_with_caption_outer_class.proto\x1a#legal_message_set_outer_class.proto\x1a\x1e\x61\x64\x64ress_form_outer_class.proto\"\xd7\x02\n\x1c\x43reditCardExpirationDateForm\x12\x11\n\tcardLabel\x18\x02 \x01(\t\x12\x11\n\tcvcLength\x18\x03 \x01(\x05\x12\x10\n\x08minMonth\x18\x04 \x01(\x05\x12\x0f\n\x07minYear\x18\x05 \x01(\x05\x12\x10\n\x08maxMonth\x18\x06 \x01(\x05\x12\x0f\n\x07maxYear\x18\x07 \x01(\x05\x12\n\n\x02id\x18\x08 \x01(\t\x12:\n\x04icon\x18\t \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x13\n\x0bhiddenField\x18\n \x03(\x05\x12\x42\n\x0c\x63vcHintImage\x18\x0b \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x13\n\x0b\x63vcHintText\x18\x0c \x01(\t\x12\x15\n\rcvcHintHeader\x18\r \x01(\t\"\xe1\x03\n\x0e\x43reditCardForm\x12:\n\x0e\x62illingAddress\x18\x02 \x01(\x0b\x32\".AddressFormOuterClass.AddressForm\x12\x35\n\x0cinitialValue\x18\x03 \x01(\x0b\x32\x1f.CreditCard.CreditCardFormValue\x12\x41\n\rlegalMessages\x18\x04 \x01(\x0b\x32*.LegalMessageSetOuterClass.LegalMessageSet\x12\n\n\x02id\x18\x05 \x01(\t\x12-\n\x0f\x61llowedCardType\x18\x06 \x03(\x0b\x32\x14.CreditCard.CardType\x12(\n\ninvalidBin\x18\x07 \x03(\x0b\x32\x14.CreditCard.BinRange\x12\x1a\n\x12minExpirationMonth\x18\x08 \x01(\x05\x12\x19\n\x11minExpirationYear\x18\t \x01(\x05\x12\x1a\n\x12maxExpirationMonth\x18\n \x01(\x05\x12\x19\n\x11maxExpirationYear\x18\x0b \x01(\x05\x12\x18\n\x10\x61llowCameraInput\x18\x0c \x01(\x08\x12\r\n\x05title\x18\r \x01(\t\x12\x1d\n\x15\x63\x61meraInputPreference\x18\x0f \x01(\x05\"\x8d\x02\n\x13\x43reditCardFormValue\x12\x12\n\ncardNumber\x18\x01 \x01(\t\x12\x0b\n\x03\x63vc\x18\x02 \x01(\t\x12\x17\n\x0f\x65xpirationMonth\x18\x03 \x01(\x05\x12\x16\n\x0e\x65xpirationYear\x18\x04 \x01(\x05\x12\x16\n\x0elastFourDigits\x18\x06 \x01(\t\x12\x16\n\x0e\x63\x61rdholderName\x18\t \x01(\t\x12?\n\x0e\x62illingAddress\x18\n \x01(\x0b\x32\'.AddressFormOuterClass.AddressFormValue\x12\x11\n\ttypeToken\x18\x0b \x01(\x0c\x12\x14\n\x0clegalDocData\x18\x0c \x01(\t\x12\n\n\x02id\x18\r \x01(\t\"\x84\x02\n\x08\x43\x61rdType\x12&\n\x08\x62inRange\x18\x01 \x03(\x0b\x32\x14.CreditCard.BinRange\x12\x11\n\tcvcLength\x18\x03 \x01(\x05\x12\x11\n\ttypeToken\x18\x04 \x01(\x0c\x12\x13\n\x0b\x63vcHintText\x18\x07 \x01(\t\x12\x15\n\rcvcHintHeader\x18\x08 \x01(\t\x12:\n\x04icon\x18\t \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x42\n\x0c\x63vcHintImage\x18\x0b \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\"m\n\x08\x42inRange\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x18\n\x10\x63\x61rdNumberLength\x18\x03 \x01(\x05\x12\x15\n\rdigitGrouping\x18\x04 \x03(\x05\x12\x14\n\x0c\x65rrorMessage\x18\x05 \x01(\t\"S\n!CreditCardExpirationDateFormValue\x12\x10\n\x08newMonth\x18\x01 \x01(\x05\x12\x0f\n\x07newYear\x18\x02 \x01(\x05\x12\x0b\n\x03\x63vc\x18\x03 \x01(\tBd\nVcom.google.commerce.payments.orchestration.proto.ui.common.components.instrument.typesB\nCreditCard')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'credit_card_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\nVcom.google.commerce.payments.orchestration.proto.ui.common.components.instrument.typesB\nCreditCard'
  _globals['_CREDITCARDEXPIRATIONDATEFORM']._serialized_start=141
  _globals['_CREDITCARDEXPIRATIONDATEFORM']._serialized_end=484
  _globals['_CREDITCARDFORM']._serialized_start=487
  _globals['_CREDITCARDFORM']._serialized_end=968
  _globals['_CREDITCARDFORMVALUE']._serialized_start=971
  _globals['_CREDITCARDFORMVALUE']._serialized_end=1240
  _globals['_CARDTYPE']._serialized_start=1243
  _globals['_CARDTYPE']._serialized_end=1503
  _globals['_BINRANGE']._serialized_start=1505
  _globals['_BINRANGE']._serialized_end=1614
  _globals['_CREDITCARDEXPIRATIONDATEFORMVALUE']._serialized_start=1616
  _globals['_CREDITCARDEXPIRATIONDATEFORMVALUE']._serialized_end=1699
# @@protoc_insertion_point(module_scope)
