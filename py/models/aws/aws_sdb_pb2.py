# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_sdb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_sdb.proto\x12\x13oak9.tython.aws.sdb\x1a\x13shared/shared.proto\"V\n\x06\x44omain\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"2\n\x03SDB\x12+\n\x06\x64omain\x18\x01 \x03(\x0b\x32\x1b.oak9.tython.aws.sdb.Domainb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_sdb_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOMAIN._serialized_start=63
  _DOMAIN._serialized_end=149
  _SDB._serialized_start=151
  _SDB._serialized_end=201
# @@protoc_insertion_point(module_scope)
