# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/campaign_draft.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import campaign_draft_status_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_campaign__draft__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/campaign_draft.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\022CampaignDraftProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v6/resources/campaign_draft.proto\x12!google.ads.googleads.v6.resources\x1a\x39google/ads/googleads/v6/enums/campaign_draft_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xad\x05\n\rCampaignDraft\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CampaignDraft\x12\x1a\n\x08\x64raft_id\x18\t \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12\x45\n\rbase_campaign\x18\n \x01(\tB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x46\n\x0e\x64raft_campaign\x18\x0c \x01(\tB)\xe0\x41\x03\xfa\x41#\n!googleads.googleapis.com/CampaignH\x03\x88\x01\x01\x12_\n\x06status\x18\x06 \x01(\x0e\x32J.google.ads.googleads.v6.enums.CampaignDraftStatusEnum.CampaignDraftStatusB\x03\xe0\x41\x03\x12(\n\x16has_experiment_running\x18\r \x01(\x08\x42\x03\xe0\x41\x03H\x04\x88\x01\x01\x12(\n\x16long_running_operation\x18\x0e \x01(\tB\x03\xe0\x41\x03H\x05\x88\x01\x01:q\xea\x41n\n&googleads.googleapis.com/CampaignDraft\x12\x44\x63ustomers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}B\x0b\n\t_draft_idB\x10\n\x0e_base_campaignB\x07\n\x05_nameB\x11\n\x0f_draft_campaignB\x19\n\x17_has_experiment_runningB\x19\n\x17_long_running_operationB\xff\x01\n%com.google.ads.googleads.v6.resourcesB\x12\x43\x61mpaignDraftProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_campaign__draft__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNDRAFT = _descriptor.Descriptor(
  name='CampaignDraft',
  full_name='google.ads.googleads.v6.resources.CampaignDraft',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.CampaignDraft.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A(\n&googleads.googleapis.com/CampaignDraft', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='draft_id', full_name='google.ads.googleads.v6.resources.CampaignDraft.draft_id', index=1,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_campaign', full_name='google.ads.googleads.v6.resources.CampaignDraft.base_campaign', index=2,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v6.resources.CampaignDraft.name', index=3,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='draft_campaign', full_name='google.ads.googleads.v6.resources.CampaignDraft.draft_campaign', index=4,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.CampaignDraft.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_experiment_running', full_name='google.ads.googleads.v6.resources.CampaignDraft.has_experiment_running', index=6,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='long_running_operation', full_name='google.ads.googleads.v6.resources.CampaignDraft.long_running_operation', index=7,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352An\n&googleads.googleapis.com/CampaignDraft\022Dcustomers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_draft_id', full_name='google.ads.googleads.v6.resources.CampaignDraft._draft_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_base_campaign', full_name='google.ads.googleads.v6.resources.CampaignDraft._base_campaign',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v6.resources.CampaignDraft._name',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_draft_campaign', full_name='google.ads.googleads.v6.resources.CampaignDraft._draft_campaign',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_experiment_running', full_name='google.ads.googleads.v6.resources.CampaignDraft._has_experiment_running',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_long_running_operation', full_name='google.ads.googleads.v6.resources.CampaignDraft._long_running_operation',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=243,
  serialized_end=928,
)

_CAMPAIGNDRAFT.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v6_dot_enums_dot_campaign__draft__status__pb2._CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS
_CAMPAIGNDRAFT.oneofs_by_name['_draft_id'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['draft_id'])
_CAMPAIGNDRAFT.fields_by_name['draft_id'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_draft_id']
_CAMPAIGNDRAFT.oneofs_by_name['_base_campaign'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['base_campaign'])
_CAMPAIGNDRAFT.fields_by_name['base_campaign'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_base_campaign']
_CAMPAIGNDRAFT.oneofs_by_name['_name'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['name'])
_CAMPAIGNDRAFT.fields_by_name['name'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_name']
_CAMPAIGNDRAFT.oneofs_by_name['_draft_campaign'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['draft_campaign'])
_CAMPAIGNDRAFT.fields_by_name['draft_campaign'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_draft_campaign']
_CAMPAIGNDRAFT.oneofs_by_name['_has_experiment_running'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['has_experiment_running'])
_CAMPAIGNDRAFT.fields_by_name['has_experiment_running'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_has_experiment_running']
_CAMPAIGNDRAFT.oneofs_by_name['_long_running_operation'].fields.append(
  _CAMPAIGNDRAFT.fields_by_name['long_running_operation'])
_CAMPAIGNDRAFT.fields_by_name['long_running_operation'].containing_oneof = _CAMPAIGNDRAFT.oneofs_by_name['_long_running_operation']
DESCRIPTOR.message_types_by_name['CampaignDraft'] = _CAMPAIGNDRAFT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignDraft = _reflection.GeneratedProtocolMessageType('CampaignDraft', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNDRAFT,
  '__module__' : 'google.ads.googleads.v6.resources.campaign_draft_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.CampaignDraft)
  })
_sym_db.RegisterMessage(CampaignDraft)


DESCRIPTOR._options = None
_CAMPAIGNDRAFT.fields_by_name['resource_name']._options = None
_CAMPAIGNDRAFT.fields_by_name['draft_id']._options = None
_CAMPAIGNDRAFT.fields_by_name['base_campaign']._options = None
_CAMPAIGNDRAFT.fields_by_name['draft_campaign']._options = None
_CAMPAIGNDRAFT.fields_by_name['status']._options = None
_CAMPAIGNDRAFT.fields_by_name['has_experiment_running']._options = None
_CAMPAIGNDRAFT.fields_by_name['long_running_operation']._options = None
_CAMPAIGNDRAFT._options = None
# @@protoc_insertion_point(module_scope)
