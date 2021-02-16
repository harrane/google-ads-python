# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/change_client_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/change_client_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\025ChangeClientTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v6/enums/change_client_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xed\x02\n\x14\x43hangeClientTypeEnum\"\xd4\x02\n\x10\x43hangeClientType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x19\n\x15GOOGLE_ADS_WEB_CLIENT\x10\x02\x12\x1d\n\x19GOOGLE_ADS_AUTOMATED_RULE\x10\x03\x12\x16\n\x12GOOGLE_ADS_SCRIPTS\x10\x04\x12\x1a\n\x16GOOGLE_ADS_BULK_UPLOAD\x10\x05\x12\x12\n\x0eGOOGLE_ADS_API\x10\x06\x12\x15\n\x11GOOGLE_ADS_EDITOR\x10\x07\x12\x19\n\x15GOOGLE_ADS_MOBILE_APP\x10\x08\x12\x1e\n\x1aGOOGLE_ADS_RECOMMENDATIONS\x10\t\x12\x17\n\x13SEARCH_ADS_360_SYNC\x10\n\x12\x17\n\x13SEARCH_ADS_360_POST\x10\x0b\x12\x11\n\rINTERNAL_TOOL\x10\x0c\x12\t\n\x05OTHER\x10\rB\xea\x01\n!com.google.ads.googleads.v6.enumsB\x15\x43hangeClientTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CHANGECLIENTTYPEENUM_CHANGECLIENTTYPE = _descriptor.EnumDescriptor(
  name='ChangeClientType',
  full_name='google.ads.googleads.v6.enums.ChangeClientTypeEnum.ChangeClientType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_WEB_CLIENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_AUTOMATED_RULE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_SCRIPTS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_BULK_UPLOAD', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_API', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_EDITOR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_MOBILE_APP', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS_RECOMMENDATIONS', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_ADS_360_SYNC', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_ADS_360_POST', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TOOL', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=145,
  serialized_end=485,
)
_sym_db.RegisterEnumDescriptor(_CHANGECLIENTTYPEENUM_CHANGECLIENTTYPE)


_CHANGECLIENTTYPEENUM = _descriptor.Descriptor(
  name='ChangeClientTypeEnum',
  full_name='google.ads.googleads.v6.enums.ChangeClientTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANGECLIENTTYPEENUM_CHANGECLIENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=485,
)

_CHANGECLIENTTYPEENUM_CHANGECLIENTTYPE.containing_type = _CHANGECLIENTTYPEENUM
DESCRIPTOR.message_types_by_name['ChangeClientTypeEnum'] = _CHANGECLIENTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeClientTypeEnum = _reflection.GeneratedProtocolMessageType('ChangeClientTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _CHANGECLIENTTYPEENUM,
  '__module__' : 'google.ads.googleads.v6.enums.change_client_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.ChangeClientTypeEnum)
  })
_sym_db.RegisterMessage(ChangeClientTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
