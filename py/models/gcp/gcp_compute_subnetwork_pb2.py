# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_subnetwork.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n gcp/gcp_compute_subnetwork.proto\x12\"oak9.tython.gcp.compute_subnetwork\x1a\x13shared/shared.proto\"\x92\x01\n\x1b\x43omputeSubnetworkXLogConfig\x12\x1c\n\x14\x61ggregation_interval\x18\x01 \x01(\t\x12\x13\n\x0b\x66ilter_expr\x18\x02 \x01(\t\x12\x15\n\rflow_sampling\x18\x03 \x01(\x01\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x17\n\x0fmetadata_fields\x18\x05 \x03(\t\"L\n\x1a\x43omputeSubnetworkXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xb4\x06\n\x11\x43omputeSubnetwork\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1c\n\x14\x65xternal_ipv6_prefix\x18\x03 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x04 \x01(\t\x12\x17\n\x0fgateway_address\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x15\n\rip_cidr_range\x18\x07 \x01(\t\x12\x18\n\x10ipv6_access_type\x18\x08 \x01(\t\x12\x17\n\x0fipv6_cidr_range\x18\t \x01(\t\x12\x0c\n\x04name\x18\n \x01(\t\x12\x0f\n\x07network\x18\x0b \x01(\t\x12 \n\x18private_ip_google_access\x18\x0c \x01(\x08\x12\"\n\x1aprivate_ipv6_google_access\x18\r \x01(\t\x12\x0f\n\x07project\x18\x0e \x01(\t\x12\x0f\n\x07purpose\x18\x0f \x01(\t\x12\x0e\n\x06region\x18\x10 \x01(\t\x12\x0c\n\x04role\x18\x11 \x01(\t\x12g\n\x12secondary_ip_range\x18\x12 \x03(\x0b\x32K.oak9.tython.gcp.compute_subnetwork.ComputeSubnetwork.SecondaryIpRangeEntry\x12\x11\n\tself_link\x18\x13 \x01(\t\x12\x12\n\nstack_type\x18\x14 \x01(\t\x12S\n\nlog_config\x18\x15 \x01(\x0b\x32?.oak9.tython.gcp.compute_subnetwork.ComputeSubnetworkXLogConfig\x12P\n\x08timeouts\x18\x16 \x01(\x0b\x32>.oak9.tython.gcp.compute_subnetwork.ComputeSubnetworkXTimeouts\x12\x37\n\rresource_info\x18\x17 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a\x37\n\x15SecondaryIpRangeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"_\n%ComputeSubnetworkIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xa2\x02\n\x1b\x43omputeSubnetworkIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07members\x18\x03 \x03(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x12\n\nsubnetwork\x18\x07 \x01(\t\x12\\\n\tcondition\x18\x08 \x01(\x0b\x32I.oak9.tython.gcp.compute_subnetwork.ComputeSubnetworkIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"^\n$ComputeSubnetworkIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x9f\x02\n\x1a\x43omputeSubnetworkIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06member\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x12\n\nsubnetwork\x18\x07 \x01(\t\x12[\n\tcondition\x18\x08 \x01(\x0b\x32H.oak9.tython.gcp.compute_subnetwork.ComputeSubnetworkIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb9\x01\n\x1a\x43omputeSubnetworkIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x12\n\nsubnetwork\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_subnetwork_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTESUBNETWORK_SECONDARYIPRANGEENTRY._options = None
  _COMPUTESUBNETWORK_SECONDARYIPRANGEENTRY._serialized_options = b'8\001'
  _COMPUTESUBNETWORKXLOGCONFIG._serialized_start=94
  _COMPUTESUBNETWORKXLOGCONFIG._serialized_end=240
  _COMPUTESUBNETWORKXTIMEOUTS._serialized_start=242
  _COMPUTESUBNETWORKXTIMEOUTS._serialized_end=318
  _COMPUTESUBNETWORK._serialized_start=321
  _COMPUTESUBNETWORK._serialized_end=1141
  _COMPUTESUBNETWORK_SECONDARYIPRANGEENTRY._serialized_start=1086
  _COMPUTESUBNETWORK_SECONDARYIPRANGEENTRY._serialized_end=1141
  _COMPUTESUBNETWORKIAMBINDINGXCONDITION._serialized_start=1143
  _COMPUTESUBNETWORKIAMBINDINGXCONDITION._serialized_end=1238
  _COMPUTESUBNETWORKIAMBINDING._serialized_start=1241
  _COMPUTESUBNETWORKIAMBINDING._serialized_end=1531
  _COMPUTESUBNETWORKIAMMEMBERXCONDITION._serialized_start=1533
  _COMPUTESUBNETWORKIAMMEMBERXCONDITION._serialized_end=1627
  _COMPUTESUBNETWORKIAMMEMBER._serialized_start=1630
  _COMPUTESUBNETWORKIAMMEMBER._serialized_end=1917
  _COMPUTESUBNETWORKIAMPOLICY._serialized_start=1920
  _COMPUTESUBNETWORKIAMPOLICY._serialized_end=2105
# @@protoc_insertion_point(module_scope)
