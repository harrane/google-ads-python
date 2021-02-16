# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/errors/keyword_plan_idea_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/errors/keyword_plan_idea_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\031KeywordPlanIdeaErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads/v6/errors/keyword_plan_idea_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"x\n\x18KeywordPlanIdeaErrorEnum\"\\\n\x14KeywordPlanIdeaError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fURL_CRAWL_ERROR\x10\x02\x12\x11\n\rINVALID_VALUE\x10\x03\x42\xf4\x01\n\"com.google.ads.googleads.v6.errorsB\x19KeywordPlanIdeaErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_KEYWORDPLANIDEAERRORENUM_KEYWORDPLANIDEAERROR = _descriptor.EnumDescriptor(
  name='KeywordPlanIdeaError',
  full_name='google.ads.googleads.v6.errors.KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError',
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
      name='URL_CRAWL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_VALUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=246,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANIDEAERRORENUM_KEYWORDPLANIDEAERROR)


_KEYWORDPLANIDEAERRORENUM = _descriptor.Descriptor(
  name='KeywordPlanIdeaErrorEnum',
  full_name='google.ads.googleads.v6.errors.KeywordPlanIdeaErrorEnum',
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
    _KEYWORDPLANIDEAERRORENUM_KEYWORDPLANIDEAERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=246,
)

_KEYWORDPLANIDEAERRORENUM_KEYWORDPLANIDEAERROR.containing_type = _KEYWORDPLANIDEAERRORENUM
DESCRIPTOR.message_types_by_name['KeywordPlanIdeaErrorEnum'] = _KEYWORDPLANIDEAERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanIdeaErrorEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanIdeaErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANIDEAERRORENUM,
  '__module__' : 'google.ads.googleads.v6.errors.keyword_plan_idea_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.KeywordPlanIdeaErrorEnum)
  })
_sym_db.RegisterMessage(KeywordPlanIdeaErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
