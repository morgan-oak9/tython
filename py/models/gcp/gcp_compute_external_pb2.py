# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_external.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egcp/gcp_compute_external.proto\x12 oak9.tython.gcp.compute_external\x1a\x13shared/shared.proto\"E\n#ComputeExternalVpnGatewayXInterface\x12\n\n\x02id\x18\x01 \x01(\x01\x12\x12\n\nip_address\x18\x02 \x01(\t\"D\n\"ComputeExternalVpnGatewayXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xf2\x02\n\x19\x43omputeExternalVpnGateway\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x17\n\x0fredundancy_type\x18\x05 \x01(\t\x12\x11\n\tself_link\x18\x06 \x01(\t\x12X\n\tinterface\x18\x07 \x03(\x0b\x32\x45.oak9.tython.gcp.compute_external.ComputeExternalVpnGatewayXInterface\x12V\n\x08timeouts\x18\x08 \x01(\x0b\x32\x44.oak9.tython.gcp.compute_external.ComputeExternalVpnGatewayXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_external_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEEXTERNALVPNGATEWAYXINTERFACE._serialized_start=89
  _COMPUTEEXTERNALVPNGATEWAYXINTERFACE._serialized_end=158
  _COMPUTEEXTERNALVPNGATEWAYXTIMEOUTS._serialized_start=160
  _COMPUTEEXTERNALVPNGATEWAYXTIMEOUTS._serialized_end=228
  _COMPUTEEXTERNALVPNGATEWAY._serialized_start=231
  _COMPUTEEXTERNALVPNGATEWAY._serialized_end=601
# @@protoc_insertion_point(module_scope)