# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_transfer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61ws/aws_transfer.proto\x12\x18oak9.tython.aws.transfer\x1a\x13shared/shared.proto\"I\n\x0eServerProtocol\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"~\n\x1dServerIdentityProviderDetails\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0finvocation_role\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\xad\x01\n\x15ServerEndpointDetails\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16\x61\x64\x64ress_allocation_ids\x18\x02 \x03(\t\x12\x0e\n\x06vpc_id\x18\x03 \x01(\t\x12\x17\n\x0fvpc_endpoint_id\x18\x04 \x01(\t\x12\x12\n\nsubnet_ids\x18\x05 \x03(\t\"\x8c\x04\n\x06Server\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0clogging_role\x18\x02 \x01(\t\x12;\n\tprotocols\x18\x03 \x03(\x0b\x32(.oak9.tython.aws.transfer.ServerProtocol\x12Z\n\x19identity_provider_details\x18\x04 \x01(\x0b\x32\x37.oak9.tython.aws.transfer.ServerIdentityProviderDetails\x12\x15\n\rendpoint_type\x18\x05 \x01(\t\x12\x1c\n\x14security_policy_name\x18\x06 \x01(\t\x12I\n\x10\x65ndpoint_details\x18\x07 \x01(\x0b\x32/.oak9.tython.aws.transfer.ServerEndpointDetails\x12\x1e\n\x16identity_provider_type\x18\x08 \x01(\t\x12\x38\n\x04tags\x18\t \x03(\x0b\x32*.oak9.tython.aws.transfer.Server.TagsEntry\x12\x13\n\x0b\x63\x65rtificate\x18\n \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"j\n\x08Transfer\x12\x30\n\x06server\x18\x01 \x03(\x0b\x32 .oak9.tython.aws.transfer.Server\x12,\n\x04user\x18\x02 \x03(\x0b\x32\x1e.oak9.tython.aws.transfer.User\"s\n\x19UserHomeDirectoryMapEntry\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65ntry\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\"K\n\x10UserSshPublicKey\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb8\x03\n\x04User\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06policy\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\x12\x16\n\x0ehome_directory\x18\x04 \x01(\t\x12\x1b\n\x13home_directory_type\x18\x05 \x01(\t\x12\x11\n\tserver_id\x18\x06 \x01(\t\x12\x11\n\tuser_name\x18\x07 \x01(\t\x12T\n\x17home_directory_mappings\x18\x08 \x03(\x0b\x32\x33.oak9.tython.aws.transfer.UserHomeDirectoryMapEntry\x12\x43\n\x0fssh_public_keys\x18\t \x03(\x0b\x32*.oak9.tython.aws.transfer.UserSshPublicKey\x12\x36\n\x04tags\x18\n \x03(\x0b\x32(.oak9.tython.aws.transfer.User.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_transfer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVER_TAGSENTRY._options = None
  _SERVER_TAGSENTRY._serialized_options = b'8\001'
  _USER_TAGSENTRY._options = None
  _USER_TAGSENTRY._serialized_options = b'8\001'
  _SERVERPROTOCOL._serialized_start=73
  _SERVERPROTOCOL._serialized_end=146
  _SERVERIDENTITYPROVIDERDETAILS._serialized_start=148
  _SERVERIDENTITYPROVIDERDETAILS._serialized_end=274
  _SERVERENDPOINTDETAILS._serialized_start=277
  _SERVERENDPOINTDETAILS._serialized_end=450
  _SERVER._serialized_start=453
  _SERVER._serialized_end=977
  _SERVER_TAGSENTRY._serialized_start=934
  _SERVER_TAGSENTRY._serialized_end=977
  _TRANSFER._serialized_start=979
  _TRANSFER._serialized_end=1085
  _USERHOMEDIRECTORYMAPENTRY._serialized_start=1087
  _USERHOMEDIRECTORYMAPENTRY._serialized_end=1202
  _USERSSHPUBLICKEY._serialized_start=1204
  _USERSSHPUBLICKEY._serialized_end=1279
  _USER._serialized_start=1282
  _USER._serialized_end=1722
  _USER_TAGSENTRY._serialized_start=934
  _USER_TAGSENTRY._serialized_end=977
# @@protoc_insertion_point(module_scope)
