# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_directoryservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61ws/aws_directoryservice.proto\x12 oak9.tython.aws.directoryservice\x1a\x13shared/shared.proto\"u\n\x16MicrosoftADVpcSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nsubnet_ids\x18\x02 \x03(\t\x12\x0e\n\x06vpc_id\x18\x03 \x01(\t\"\x85\x02\n\x0bMicrosoftAD\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x63reate_alias\x18\x02 \x01(\x08\x12\x0f\n\x07\x65\x64ition\x18\x03 \x01(\t\x12\x12\n\nenable_sso\x18\x04 \x01(\x08\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x12\n\nshort_name\x18\x07 \x01(\t\x12N\n\x0cvpc_settings\x18\x08 \x01(\x0b\x32\x38.oak9.tython.aws.directoryservice.MicrosoftADVpcSettings\"\x96\x01\n\x10\x44irectoryService\x12\x43\n\x0cmicrosoft_ad\x18\x01 \x03(\x0b\x32-.oak9.tython.aws.directoryservice.MicrosoftAD\x12=\n\tsimple_ad\x18\x02 \x03(\x0b\x32*.oak9.tython.aws.directoryservice.SimpleAD\"r\n\x13SimpleADVpcSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nsubnet_ids\x18\x02 \x03(\t\x12\x0e\n\x06vpc_id\x18\x03 \x01(\t\"\x91\x02\n\x08SimpleAD\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x63reate_alias\x18\x02 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nenable_sso\x18\x04 \x01(\x08\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x12\n\nshort_name\x18\x07 \x01(\t\x12\x0c\n\x04size\x18\x08 \x01(\t\x12K\n\x0cvpc_settings\x18\t \x01(\x0b\x32\x35.oak9.tython.aws.directoryservice.SimpleADVpcSettingsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_directoryservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MICROSOFTADVPCSETTINGS._serialized_start=89
  _MICROSOFTADVPCSETTINGS._serialized_end=206
  _MICROSOFTAD._serialized_start=209
  _MICROSOFTAD._serialized_end=470
  _DIRECTORYSERVICE._serialized_start=473
  _DIRECTORYSERVICE._serialized_end=623
  _SIMPLEADVPCSETTINGS._serialized_start=625
  _SIMPLEADVPCSETTINGS._serialized_end=739
  _SIMPLEAD._serialized_start=742
  _SIMPLEAD._serialized_end=1015
# @@protoc_insertion_point(module_scope)
