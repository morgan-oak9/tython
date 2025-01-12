# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_filestore.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17gcp/gcp_filestore.proto\x12\x19oak9.tython.gcp.filestore\x1a\x13shared/shared.proto\"\x90\x01\n-FilestoreInstanceXFileSharesXNfsExportOptions\x12\x13\n\x0b\x61\x63\x63\x65ss_mode\x18\x01 \x01(\t\x12\x10\n\x08\x61non_gid\x18\x02 \x01(\x01\x12\x10\n\x08\x61non_uid\x18\x03 \x01(\x01\x12\x11\n\tip_ranges\x18\x04 \x03(\t\x12\x13\n\x0bsquash_mode\x18\x05 \x01(\t\"\xa7\x01\n\x1c\x46ilestoreInstanceXFileShares\x12\x13\n\x0b\x63\x61pacity_gb\x18\x01 \x01(\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x64\n\x12nfs_export_options\x18\x03 \x03(\x0b\x32H.oak9.tython.gcp.filestore.FilestoreInstanceXFileSharesXNfsExportOptions\"\x83\x01\n\x1a\x46ilestoreInstanceXNetworks\x12\x14\n\x0c\x63onnect_mode\x18\x01 \x01(\t\x12\x14\n\x0cip_addresses\x18\x02 \x03(\t\x12\r\n\x05modes\x18\x03 \x03(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x19\n\x11reserved_ip_range\x18\x05 \x01(\t\"L\n\x1a\x46ilestoreInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xcc\x04\n\x11\x46ilestoreInstance\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x14\n\x0ckms_key_name\x18\x05 \x01(\t\x12H\n\x06labels\x18\x06 \x03(\x0b\x32\x38.oak9.tython.gcp.filestore.FilestoreInstance.LabelsEntry\x12\x10\n\x08location\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12\x0c\n\x04tier\x18\n \x01(\t\x12\x0c\n\x04zone\x18\x0b \x01(\t\x12L\n\x0b\x66ile_shares\x18\x0c \x01(\x0b\x32\x37.oak9.tython.gcp.filestore.FilestoreInstanceXFileShares\x12G\n\x08networks\x18\r \x03(\x0b\x32\x35.oak9.tython.gcp.filestore.FilestoreInstanceXNetworks\x12G\n\x08timeouts\x18\x0e \x01(\x0b\x32\x35.oak9.tython.gcp.filestore.FilestoreInstanceXTimeouts\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_filestore_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILESTOREINSTANCE_LABELSENTRY._options = None
  _FILESTOREINSTANCE_LABELSENTRY._serialized_options = b'8\001'
  _FILESTOREINSTANCEXFILESHARESXNFSEXPORTOPTIONS._serialized_start=76
  _FILESTOREINSTANCEXFILESHARESXNFSEXPORTOPTIONS._serialized_end=220
  _FILESTOREINSTANCEXFILESHARES._serialized_start=223
  _FILESTOREINSTANCEXFILESHARES._serialized_end=390
  _FILESTOREINSTANCEXNETWORKS._serialized_start=393
  _FILESTOREINSTANCEXNETWORKS._serialized_end=524
  _FILESTOREINSTANCEXTIMEOUTS._serialized_start=526
  _FILESTOREINSTANCEXTIMEOUTS._serialized_end=602
  _FILESTOREINSTANCE._serialized_start=605
  _FILESTOREINSTANCE._serialized_end=1193
  _FILESTOREINSTANCE_LABELSENTRY._serialized_start=1148
  _FILESTOREINSTANCE_LABELSENTRY._serialized_end=1193
# @@protoc_insertion_point(module_scope)
