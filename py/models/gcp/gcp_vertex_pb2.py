# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_vertex.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gcp/gcp_vertex.proto\x12\x16oak9.tython.gcp.vertex\x1a\x13shared/shared.proto\"6\n\x1eVertexAiDatasetXEncryptionSpec\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\"J\n\x18VertexAiDatasetXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xeb\x03\n\x0fVertexAiDataset\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x43\n\x06labels\x18\x04 \x03(\x0b\x32\x33.oak9.tython.gcp.vertex.VertexAiDataset.LabelsEntry\x12\x1b\n\x13metadata_schema_uri\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x0e\n\x06region\x18\x08 \x01(\t\x12\x13\n\x0bupdate_time\x18\t \x01(\t\x12O\n\x0f\x65ncryption_spec\x18\n \x01(\x0b\x32\x36.oak9.tython.gcp.vertex.VertexAiDatasetXEncryptionSpec\x12\x42\n\x08timeouts\x18\x0b \x01(\x0b\x32\x30.oak9.tython.gcp.vertex.VertexAiDatasetXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_vertex_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VERTEXAIDATASET_LABELSENTRY._options = None
  _VERTEXAIDATASET_LABELSENTRY._serialized_options = b'8\001'
  _VERTEXAIDATASETXENCRYPTIONSPEC._serialized_start=69
  _VERTEXAIDATASETXENCRYPTIONSPEC._serialized_end=123
  _VERTEXAIDATASETXTIMEOUTS._serialized_start=125
  _VERTEXAIDATASETXTIMEOUTS._serialized_end=199
  _VERTEXAIDATASET._serialized_start=202
  _VERTEXAIDATASET._serialized_end=693
  _VERTEXAIDATASET_LABELSENTRY._serialized_start=648
  _VERTEXAIDATASET_LABELSENTRY._serialized_end=693
# @@protoc_insertion_point(module_scope)
