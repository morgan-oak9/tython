# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_datastore.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17gcp/gcp_datastore.proto\x12\x19oak9.tython.gcp.datastore\x1a\x13shared/shared.proto\"<\n\x19\x44\x61tastoreIndexXProperties\x12\x11\n\tdirection\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"9\n\x17\x44\x61tastoreIndexXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xa8\x02\n\x0e\x44\x61tastoreIndex\x12\x10\n\x08\x61ncestor\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08index_id\x18\x03 \x01(\t\x12\x0c\n\x04kind\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12H\n\nproperties\x18\x06 \x03(\x0b\x32\x34.oak9.tython.gcp.datastore.DatastoreIndexXProperties\x12\x44\n\x08timeouts\x18\x07 \x01(\x0b\x32\x32.oak9.tython.gcp.datastore.DatastoreIndexXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_datastore_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATASTOREINDEXXPROPERTIES._serialized_start=75
  _DATASTOREINDEXXPROPERTIES._serialized_end=135
  _DATASTOREINDEXXTIMEOUTS._serialized_start=137
  _DATASTOREINDEXXTIMEOUTS._serialized_end=194
  _DATASTOREINDEX._serialized_start=197
  _DATASTOREINDEX._serialized_end=493
# @@protoc_insertion_point(module_scope)