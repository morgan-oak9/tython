# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_ec2_dhcpoptions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61ws/aws_ec2_dhcpoptions.proto\x12\x1foak9.tython.aws.ec2_dhcpoptions\x1a\x13shared/shared.proto\"\xb9\x02\n\x0b\x44HCPOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64omain_name\x18\x02 \x01(\t\x12\x1b\n\x13\x64omain_name_servers\x18\x03 \x03(\t\x12\x1c\n\x14netbios_name_servers\x18\x04 \x03(\t\x12\x19\n\x11netbios_node_type\x18\x05 \x01(\x05\x12\x13\n\x0bntp_servers\x18\x06 \x03(\t\x12\x44\n\x04tags\x18\x07 \x03(\x0b\x32\x36.oak9.tython.aws.ec2_dhcpoptions.DHCPOptions.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"U\n\x0f\x45\x43\x32_DHCPOptions\x12\x42\n\x0c\x64hcp_options\x18\x01 \x01(\x0b\x32,.oak9.tython.aws.ec2_dhcpoptions.DHCPOptionsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_ec2_dhcpoptions_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DHCPOPTIONS_TAGSENTRY._options = None
  _DHCPOPTIONS_TAGSENTRY._serialized_options = b'8\001'
  _DHCPOPTIONS._serialized_start=88
  _DHCPOPTIONS._serialized_end=401
  _DHCPOPTIONS_TAGSENTRY._serialized_start=358
  _DHCPOPTIONS_TAGSENTRY._serialized_end=401
  _EC2_DHCPOPTIONS._serialized_start=403
  _EC2_DHCPOPTIONS._serialized_end=488
# @@protoc_insertion_point(module_scope)