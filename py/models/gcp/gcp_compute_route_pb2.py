# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_route.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgcp/gcp_compute_route.proto\x12\x1doak9.tython.gcp.compute_route\x1a\x13shared/shared.proto\"7\n\x15\x43omputeRouteXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xde\x03\n\x0c\x43omputeRoute\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\ndest_range\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07network\x18\x05 \x01(\t\x12\x18\n\x10next_hop_gateway\x18\x06 \x01(\t\x12\x14\n\x0cnext_hop_ilb\x18\x07 \x01(\t\x12\x19\n\x11next_hop_instance\x18\x08 \x01(\t\x12\x1e\n\x16next_hop_instance_zone\x18\t \x01(\t\x12\x13\n\x0bnext_hop_ip\x18\n \x01(\t\x12\x18\n\x10next_hop_network\x18\x0b \x01(\t\x12\x1b\n\x13next_hop_vpn_tunnel\x18\x0c \x01(\t\x12\x10\n\x08priority\x18\r \x01(\x01\x12\x0f\n\x07project\x18\x0e \x01(\t\x12\x11\n\tself_link\x18\x0f \x01(\t\x12\x0c\n\x04tags\x18\x10 \x03(\t\x12\x46\n\x08timeouts\x18\x11 \x01(\x0b\x32\x34.oak9.tython.gcp.compute_route.ComputeRouteXTimeouts\x12\x37\n\rresource_info\x18\x12 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_route_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEROUTEXTIMEOUTS._serialized_start=83
  _COMPUTEROUTEXTIMEOUTS._serialized_end=138
  _COMPUTEROUTE._serialized_start=141
  _COMPUTEROUTE._serialized_end=619
# @@protoc_insertion_point(module_scope)
