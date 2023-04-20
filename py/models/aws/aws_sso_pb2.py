# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_sso.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_sso.proto\x12\x13oak9.tython.aws.sso\x1a\x13shared/shared.proto\"\xcd\x01\n\nAssignment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cinstance_arn\x18\x02 \x01(\t\x12\x11\n\ttarget_id\x18\x03 \x01(\t\x12\x13\n\x0btarget_type\x18\x04 \x01(\t\x12\x1a\n\x12permission_set_arn\x18\x05 \x01(\t\x12\x16\n\x0eprincipal_type\x18\x06 \x01(\t\x12\x14\n\x0cprincipal_id\x18\x07 \x01(\t\"v\n\x03SSO\x12\x33\n\nassignment\x18\x01 \x03(\x0b\x32\x1f.oak9.tython.aws.sso.Assignment\x12:\n\x0epermission_set\x18\x02 \x03(\x0b\x32\".oak9.tython.aws.sso.PermissionSet\"\xcf\x02\n\rPermissionSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cinstance_arn\x18\x04 \x01(\t\x12\x18\n\x10session_duration\x18\x05 \x01(\t\x12\x18\n\x10relay_state_type\x18\x06 \x01(\t\x12\x18\n\x10managed_policies\x18\x07 \x03(\t\x12\x15\n\rinline_policy\x18\x08 \x01(\t\x12:\n\x04tags\x18\t \x03(\x0b\x32,.oak9.tython.aws.sso.PermissionSet.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_sso_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERMISSIONSET_TAGSENTRY._options = None
  _PERMISSIONSET_TAGSENTRY._serialized_options = b'8\001'
  _ASSIGNMENT._serialized_start=64
  _ASSIGNMENT._serialized_end=269
  _SSO._serialized_start=271
  _SSO._serialized_end=389
  _PERMISSIONSET._serialized_start=392
  _PERMISSIONSET._serialized_end=727
  _PERMISSIONSET_TAGSENTRY._serialized_start=684
  _PERMISSIONSET_TAGSENTRY._serialized_end=727
# @@protoc_insertion_point(module_scope)