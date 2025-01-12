# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_kms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_kms.proto\x12\x13oak9.tython.aws.kms\x1a\x13shared/shared.proto\"k\n\x05\x41lias\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nalias_name\x18\x02 \x01(\t\x12\x15\n\rtarget_key_id\x18\x03 \x01(\t\"\xc1\x01\n\x03KMS\x12)\n\x05\x61lias\x18\x01 \x03(\x0b\x32\x1a.oak9.tython.aws.kms.Alias\x12%\n\x03key\x18\x02 \x01(\x0b\x32\x18.oak9.tython.aws.kms.Key\x12=\n\x10\x63ustom_key_store\x18\x03 \x01(\x0b\x32#.oak9.tython.aws.kms.CustomKeyStore\x12)\n\x05grant\x18\x04 \x03(\x0b\x32\x1a.oak9.tython.aws.kms.Grant\"\x8b\x01\n\x0e\x43ustomKeyStore\x12\x1c\n\x14\x63loud_hsm_cluster_id\x18\x01 \x01(\t\x12\x1d\n\x15\x63ustom_key_store_name\x18\x02 \x01(\t\x12\x1a\n\x12key_store_password\x18\x03 \x01(\t\x12 \n\x18trust_anchor_certificate\x18\x04 \x01(\t\"\xfc\x01\n\x05Grant\x12\x19\n\x11grantee_principal\x18\x01 \x01(\t\x12\x1a\n\x12retiring_principal\x18\x02 \x01(\t\x12\x14\n\x0cgrant_tokens\x18\x03 \x03(\t\x12\x0e\n\x06key_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x12\n\noperations\x18\x06 \x03(\t\x12@\n\x0b\x63onstraints\x18\x07 \x03(\x0b\x32+.oak9.tython.aws.kms.Grant.ConstraintsEntry\x1a\x32\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa8\x03\n\x03Key\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x1b\n\x13\x65nable_key_rotation\x18\x04 \x01(\x08\x12\x11\n\tkey_usage\x18\x05 \x01(\t\x12\x1e\n\x16pending_window_in_days\x18\x06 \x01(\x05\x12\x30\n\x04tags\x18\x07 \x03(\x0b\x32\".oak9.tython.aws.kms.Key.TagsEntry\x12\x1b\n\x13\x63ustom_key_store_id\x18\x08 \x01(\t\x12*\n\"bypass_policy_lockout_safety_check\x18\t \x01(\x08\x12\x10\n\x08key_spec\x18\n \x01(\t\x12\x14\n\x0cmulti_region\x18\x0b \x01(\x08\x12\x0e\n\x06origin\x18\x0c \x01(\t\x12\x12\n\nkey_policy\x18\r \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_kms_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GRANT_CONSTRAINTSENTRY._options = None
  _GRANT_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _KEY_TAGSENTRY._options = None
  _KEY_TAGSENTRY._serialized_options = b'8\001'
  _ALIAS._serialized_start=63
  _ALIAS._serialized_end=170
  _KMS._serialized_start=173
  _KMS._serialized_end=366
  _CUSTOMKEYSTORE._serialized_start=369
  _CUSTOMKEYSTORE._serialized_end=508
  _GRANT._serialized_start=511
  _GRANT._serialized_end=763
  _GRANT_CONSTRAINTSENTRY._serialized_start=713
  _GRANT_CONSTRAINTSENTRY._serialized_end=763
  _KEY._serialized_start=766
  _KEY._serialized_end=1190
  _KEY_TAGSENTRY._serialized_start=1147
  _KEY_TAGSENTRY._serialized_end=1190
# @@protoc_insertion_point(module_scope)
