# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: music_doc_details.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import doc_annotations_pb2 as doc__annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17music_doc_details.proto\x12\x0fMusicDocDetails\x1a\x15\x64oc_annotations.proto\"b\n\x13\x41rtistExternalLinks\x12\x12\n\nwebsiteUrl\x18\x01 \x03(\t\x12\x1c\n\x14googlePlusProfileUrl\x18\x02 \x01(\t\x12\x19\n\x11youtubeChannelUrl\x18\x03 \x01(\t\"\x83\x01\n\x0c\x41lbumDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1d.MusicDocDetails.MusicDetails\x12\x35\n\rdisplayArtist\x18\x03 \x01(\x0b\x32\x1e.MusicDocDetails.ArtistDetails\"\xe4\x01\n\x0bSongDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1d.MusicDocDetails.MusicDetails\x12\x11\n\talbumName\x18\x03 \x01(\t\x12\x13\n\x0btrackNumber\x18\x04 \x01(\x05\x12\x12\n\npreviewUrl\x18\x05 \x01(\t\x12\x35\n\rdisplayArtist\x18\x06 \x01(\x0b\x32\x1e.MusicDocDetails.ArtistDetails\x12$\n\x05\x62\x61\x64ge\x18\x07 \x01(\x0b\x32\x15.DocAnnotations.Badge\"n\n\rArtistDetails\x12\x12\n\ndetailsUrl\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\rexternalLinks\x18\x03 \x01(\x0b\x32$.MusicDocDetails.ArtistExternalLinks\"\xcb\x01\n\x0cMusicDetails\x12\x11\n\tcensoring\x18\x01 \x01(\x05\x12\x13\n\x0b\x64urationSec\x18\x02 \x01(\x05\x12\x1b\n\x13originalReleaseDate\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12.\n\x06\x61rtist\x18\x05 \x03(\x0b\x32\x1e.MusicDocDetails.ArtistDetails\x12\r\n\x05genre\x18\x06 \x03(\t\x12\x13\n\x0breleaseDate\x18\x07 \x01(\t\x12\x13\n\x0breleaseType\x18\x08 \x03(\x05\x42\x33\n com.google.android.finsky.protosB\x0fMusicDocDetails')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'music_doc_details_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.android.finsky.protosB\017MusicDocDetails'
  _globals['_ARTISTEXTERNALLINKS']._serialized_start=67
  _globals['_ARTISTEXTERNALLINKS']._serialized_end=165
  _globals['_ALBUMDETAILS']._serialized_start=168
  _globals['_ALBUMDETAILS']._serialized_end=299
  _globals['_SONGDETAILS']._serialized_start=302
  _globals['_SONGDETAILS']._serialized_end=530
  _globals['_ARTISTDETAILS']._serialized_start=532
  _globals['_ARTISTDETAILS']._serialized_end=642
  _globals['_MUSICDETAILS']._serialized_start=645
  _globals['_MUSICDETAILS']._serialized_end=848
# @@protoc_insertion_point(module_scope)
