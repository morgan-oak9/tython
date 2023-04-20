# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_fms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_fms.proto\x12\x13oak9.tython.aws.fms\x1a\x13shared/shared.proto\"|\n\x13NotificationChannel\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rsns_role_name\x18\x02 \x01(\t\x12\x15\n\rsns_topic_arn\x18\x03 \x01(\t\"z\n\x03\x46MS\x12\x46\n\x14notification_channel\x18\x01 \x03(\x0b\x32(.oak9.tython.aws.fms.NotificationChannel\x12+\n\x06policy\x18\x02 \x03(\x0b\x32\x1b.oak9.tython.aws.fms.Policy\"h\n\x0bPolicyIEMap\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x03(\t\x12\x0f\n\x07orgunit\x18\x03 \x03(\t\"h\n\x11PolicyResourceTag\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"f\n\x0fPolicyPolicyTag\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xef\x04\n\x06Policy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x35\n\x0b\x65xclude_map\x18\x02 \x01(\x0b\x32 .oak9.tython.aws.fms.PolicyIEMap\x12\x1d\n\x15\x65xclude_resource_tags\x18\x03 \x01(\x08\x12\x35\n\x0binclude_map\x18\x04 \x01(\x0b\x32 .oak9.tython.aws.fms.PolicyIEMap\x12\x13\n\x0bpolicy_name\x18\x05 \x01(\t\x12\x1b\n\x13remediation_enabled\x18\x06 \x01(\x08\x12=\n\rresource_tags\x18\x07 \x03(\x0b\x32&.oak9.tython.aws.fms.PolicyResourceTag\x12\x15\n\rresource_type\x18\x08 \x01(\t\x12\x1a\n\x12resource_type_list\x18\t \x03(\t\x12`\n\x1csecurity_service_policy_data\x18\n \x03(\x0b\x32:.oak9.tython.aws.fms.Policy.SecurityServicePolicyDataEntry\x12#\n\x1b\x64\x65lete_all_policy_resources\x18\x0b \x01(\x08\x12\x32\n\x04tags\x18\x0c \x03(\x0b\x32$.oak9.tython.aws.fms.PolicyPolicyTag\x1a@\n\x1eSecurityServicePolicyDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_fms_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POLICY_SECURITYSERVICEPOLICYDATAENTRY._options = None
  _POLICY_SECURITYSERVICEPOLICYDATAENTRY._serialized_options = b'8\001'
  _NOTIFICATIONCHANNEL._serialized_start=63
  _NOTIFICATIONCHANNEL._serialized_end=187
  _FMS._serialized_start=189
  _FMS._serialized_end=311
  _POLICYIEMAP._serialized_start=313
  _POLICYIEMAP._serialized_end=417
  _POLICYRESOURCETAG._serialized_start=419
  _POLICYRESOURCETAG._serialized_end=523
  _POLICYPOLICYTAG._serialized_start=525
  _POLICYPOLICYTAG._serialized_end=627
  _POLICY._serialized_start=630
  _POLICY._serialized_end=1253
  _POLICY_SECURITYSERVICEPOLICYDATAENTRY._serialized_start=1189
  _POLICY_SECURITYSERVICEPOLICYDATAENTRY._serialized_end=1253
# @@protoc_insertion_point(module_scope)