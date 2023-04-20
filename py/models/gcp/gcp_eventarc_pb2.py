# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_eventarc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gcp/gcp_eventarc.proto\x12\x18oak9.tython.gcp.eventarc\x1a\x13shared/shared.proto\"\\\n+EventarcTriggerXDestinationXCloudRunService\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\"v\n\x1f\x45ventarcTriggerXDestinationXGke\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\"\xf1\x01\n\x1b\x45ventarcTriggerXDestination\x12\x16\n\x0e\x63loud_function\x18\x01 \x01(\t\x12\x10\n\x08workflow\x18\x02 \x01(\t\x12`\n\x11\x63loud_run_service\x18\x03 \x01(\x0b\x32\x45.oak9.tython.gcp.eventarc.EventarcTriggerXDestinationXCloudRunService\x12\x46\n\x03gke\x18\x04 \x01(\x0b\x32\x39.oak9.tython.gcp.eventarc.EventarcTriggerXDestinationXGke\"V\n EventarcTriggerXMatchingCriteria\x12\x11\n\tattribute\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"J\n\x18\x45ventarcTriggerXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"G\n EventarcTriggerXTransportXPubsub\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\"g\n\x19\x45ventarcTriggerXTransport\x12J\n\x06pubsub\x18\x01 \x01(\x0b\x32:.oak9.tython.gcp.eventarc.EventarcTriggerXTransportXPubsub\"\x8c\x05\n\x0f\x45ventarcTrigger\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x45\n\x06labels\x18\x04 \x03(\x0b\x32\x35.oak9.tython.gcp.eventarc.EventarcTrigger.LabelsEntry\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x17\n\x0fservice_account\x18\x08 \x01(\t\x12\x0b\n\x03uid\x18\t \x01(\t\x12\x13\n\x0bupdate_time\x18\n \x01(\t\x12J\n\x0b\x64\x65stination\x18\x0b \x01(\x0b\x32\x35.oak9.tython.gcp.eventarc.EventarcTriggerXDestination\x12U\n\x11matching_criteria\x18\x0c \x03(\x0b\x32:.oak9.tython.gcp.eventarc.EventarcTriggerXMatchingCriteria\x12\x44\n\x08timeouts\x18\r \x01(\x0b\x32\x32.oak9.tython.gcp.eventarc.EventarcTriggerXTimeouts\x12\x46\n\ttransport\x18\x0e \x01(\x0b\x32\x33.oak9.tython.gcp.eventarc.EventarcTriggerXTransport\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_eventarc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTARCTRIGGER_LABELSENTRY._options = None
  _EVENTARCTRIGGER_LABELSENTRY._serialized_options = b'8\001'
  _EVENTARCTRIGGERXDESTINATIONXCLOUDRUNSERVICE._serialized_start=73
  _EVENTARCTRIGGERXDESTINATIONXCLOUDRUNSERVICE._serialized_end=165
  _EVENTARCTRIGGERXDESTINATIONXGKE._serialized_start=167
  _EVENTARCTRIGGERXDESTINATIONXGKE._serialized_end=285
  _EVENTARCTRIGGERXDESTINATION._serialized_start=288
  _EVENTARCTRIGGERXDESTINATION._serialized_end=529
  _EVENTARCTRIGGERXMATCHINGCRITERIA._serialized_start=531
  _EVENTARCTRIGGERXMATCHINGCRITERIA._serialized_end=617
  _EVENTARCTRIGGERXTIMEOUTS._serialized_start=619
  _EVENTARCTRIGGERXTIMEOUTS._serialized_end=693
  _EVENTARCTRIGGERXTRANSPORTXPUBSUB._serialized_start=695
  _EVENTARCTRIGGERXTRANSPORTXPUBSUB._serialized_end=766
  _EVENTARCTRIGGERXTRANSPORT._serialized_start=768
  _EVENTARCTRIGGERXTRANSPORT._serialized_end=871
  _EVENTARCTRIGGER._serialized_start=874
  _EVENTARCTRIGGER._serialized_end=1526
  _EVENTARCTRIGGER_LABELSENTRY._serialized_start=1481
  _EVENTARCTRIGGER_LABELSENTRY._serialized_end=1526
# @@protoc_insertion_point(module_scope)
