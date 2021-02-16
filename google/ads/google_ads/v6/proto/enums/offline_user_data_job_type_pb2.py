# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/offline_user_data_job_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/offline_user_data_job_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\033OfflineUserDataJobTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads/v6/enums/offline_user_data_job_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xdf\x01\n\x1aOfflineUserDataJobTypeEnum\"\xc0\x01\n\x16OfflineUserDataJobType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\"\n\x1eSTORE_SALES_UPLOAD_FIRST_PARTY\x10\x02\x12\"\n\x1eSTORE_SALES_UPLOAD_THIRD_PARTY\x10\x03\x12\x1c\n\x18\x43USTOMER_MATCH_USER_LIST\x10\x04\x12\"\n\x1e\x43USTOMER_MATCH_WITH_ATTRIBUTES\x10\x05\x42\xf0\x01\n!com.google.ads.googleads.v6.enumsB\x1bOfflineUserDataJobTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_OFFLINEUSERDATAJOBTYPEENUM_OFFLINEUSERDATAJOBTYPE = _descriptor.EnumDescriptor(
  name='OfflineUserDataJobType',
  full_name='google.ads.googleads.v6.enums.OfflineUserDataJobTypeEnum.OfflineUserDataJobType',
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
      name='STORE_SALES_UPLOAD_FIRST_PARTY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STORE_SALES_UPLOAD_THIRD_PARTY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_MATCH_USER_LIST', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_MATCH_WITH_ATTRIBUTES', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=159,
  serialized_end=351,
)
_sym_db.RegisterEnumDescriptor(_OFFLINEUSERDATAJOBTYPEENUM_OFFLINEUSERDATAJOBTYPE)


_OFFLINEUSERDATAJOBTYPEENUM = _descriptor.Descriptor(
  name='OfflineUserDataJobTypeEnum',
  full_name='google.ads.googleads.v6.enums.OfflineUserDataJobTypeEnum',
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
    _OFFLINEUSERDATAJOBTYPEENUM_OFFLINEUSERDATAJOBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=351,
)

_OFFLINEUSERDATAJOBTYPEENUM_OFFLINEUSERDATAJOBTYPE.containing_type = _OFFLINEUSERDATAJOBTYPEENUM
DESCRIPTOR.message_types_by_name['OfflineUserDataJobTypeEnum'] = _OFFLINEUSERDATAJOBTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OfflineUserDataJobTypeEnum = _reflection.GeneratedProtocolMessageType('OfflineUserDataJobTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINEUSERDATAJOBTYPEENUM,
  '__module__' : 'google.ads.googleads.v6.enums.offline_user_data_job_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.OfflineUserDataJobTypeEnum)
  })
_sym_db.RegisterMessage(OfflineUserDataJobTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
