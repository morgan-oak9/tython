# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_attached.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egcp/gcp_compute_attached.proto\x12 oak9.tython.gcp.compute_attached\x1a\x13shared/shared.proto\">\n\x1c\x43omputeAttachedDiskXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\x8e\x02\n\x13\x43omputeAttachedDisk\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12\x0c\n\x04\x64isk\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0c\n\x04mode\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12P\n\x08timeouts\x18\x08 \x01(\x0b\x32>.oak9.tython.gcp.compute_attached.ComputeAttachedDiskXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_attached_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEATTACHEDDISKXTIMEOUTS._serialized_start=89
  _COMPUTEATTACHEDDISKXTIMEOUTS._serialized_end=151
  _COMPUTEATTACHEDDISK._serialized_start=154
  _COMPUTEATTACHEDDISK._serialized_end=424
# @@protoc_insertion_point(module_scope)
