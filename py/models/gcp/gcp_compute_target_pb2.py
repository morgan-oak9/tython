# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_target.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgcp/gcp_compute_target.proto\x12\x1eoak9.tython.gcp.compute_target\x1a\x13shared/shared.proto\"Q\n\x1f\x43omputeTargetGrpcProxyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xf4\x02\n\x16\x43omputeTargetGrpcProxy\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x11\n\tself_link\x18\x07 \x01(\t\x12\x19\n\x11self_link_with_id\x18\x08 \x01(\t\x12\x0f\n\x07url_map\x18\t \x01(\t\x12\x1e\n\x16validate_for_proxyless\x18\n \x01(\x08\x12Q\n\x08timeouts\x18\x0b \x01(\x0b\x32?.oak9.tython.gcp.compute_target.ComputeTargetGrpcProxyXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"Q\n\x1f\x43omputeTargetHttpProxyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xca\x02\n\x16\x43omputeTargetHttpProxy\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x12\n\nproxy_bind\x18\x06 \x01(\x08\x12\x10\n\x08proxy_id\x18\x07 \x01(\x01\x12\x11\n\tself_link\x18\x08 \x01(\t\x12\x0f\n\x07url_map\x18\t \x01(\t\x12Q\n\x08timeouts\x18\n \x01(\x0b\x32?.oak9.tython.gcp.compute_target.ComputeTargetHttpProxyXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"R\n ComputeTargetHttpsProxyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x91\x03\n\x17\x43omputeTargetHttpsProxy\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x12\n\nproxy_bind\x18\x06 \x01(\x08\x12\x10\n\x08proxy_id\x18\x07 \x01(\x01\x12\x15\n\rquic_override\x18\x08 \x01(\t\x12\x11\n\tself_link\x18\t \x01(\t\x12\x18\n\x10ssl_certificates\x18\n \x03(\t\x12\x12\n\nssl_policy\x18\x0b \x01(\t\x12\x0f\n\x07url_map\x18\x0c \x01(\t\x12R\n\x08timeouts\x18\r \x01(\x0b\x32@.oak9.tython.gcp.compute_target.ComputeTargetHttpsProxyXTimeouts\x12\x37\n\rresource_info\x18\x0e \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"@\n\x1e\x43omputeTargetInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xc5\x02\n\x15\x43omputeTargetInstance\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x12\n\nnat_policy\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x11\n\tself_link\x18\x08 \x01(\t\x12\x0c\n\x04zone\x18\t \x01(\t\x12P\n\x08timeouts\x18\n \x01(\x0b\x32>.oak9.tython.gcp.compute_target.ComputeTargetInstanceXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"L\n\x1a\x43omputeTargetPoolXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xee\x02\n\x11\x43omputeTargetPool\x12\x13\n\x0b\x62\x61\x63kup_pool\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x16\n\x0e\x66\x61ilover_ratio\x18\x03 \x01(\x01\x12\x15\n\rhealth_checks\x18\x04 \x03(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x11\n\tinstances\x18\x06 \x03(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07project\x18\x08 \x01(\t\x12\x0e\n\x06region\x18\t \x01(\t\x12\x11\n\tself_link\x18\n \x01(\t\x12\x18\n\x10session_affinity\x18\x0b \x01(\t\x12L\n\x08timeouts\x18\x0c \x01(\x0b\x32:.oak9.tython.gcp.compute_target.ComputeTargetPoolXTimeouts\x12\x37\n\rresource_info\x18\r \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"P\n\x1e\x43omputeTargetSslProxyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x80\x03\n\x15\x43omputeTargetSslProxy\x12\x17\n\x0f\x62\x61\x63kend_service\x18\x01 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x14\n\x0cproxy_header\x18\x07 \x01(\t\x12\x10\n\x08proxy_id\x18\x08 \x01(\x01\x12\x11\n\tself_link\x18\t \x01(\t\x12\x18\n\x10ssl_certificates\x18\n \x03(\t\x12\x12\n\nssl_policy\x18\x0b \x01(\t\x12P\n\x08timeouts\x18\x0c \x01(\x0b\x32>.oak9.tython.gcp.compute_target.ComputeTargetSslProxyXTimeouts\x12\x37\n\rresource_info\x18\r \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"P\n\x1e\x43omputeTargetTcpProxyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xe6\x02\n\x15\x43omputeTargetTcpProxy\x12\x17\n\x0f\x62\x61\x63kend_service\x18\x01 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x12\n\nproxy_bind\x18\x07 \x01(\x08\x12\x14\n\x0cproxy_header\x18\x08 \x01(\t\x12\x10\n\x08proxy_id\x18\t \x01(\x01\x12\x11\n\tself_link\x18\n \x01(\t\x12P\n\x08timeouts\x18\x0b \x01(\x0b\x32>.oak9.tython.gcp.compute_target.ComputeTargetTcpProxyXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_target_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTETARGETGRPCPROXYXTIMEOUTS._serialized_start=85
  _COMPUTETARGETGRPCPROXYXTIMEOUTS._serialized_end=166
  _COMPUTETARGETGRPCPROXY._serialized_start=169
  _COMPUTETARGETGRPCPROXY._serialized_end=541
  _COMPUTETARGETHTTPPROXYXTIMEOUTS._serialized_start=543
  _COMPUTETARGETHTTPPROXYXTIMEOUTS._serialized_end=624
  _COMPUTETARGETHTTPPROXY._serialized_start=627
  _COMPUTETARGETHTTPPROXY._serialized_end=957
  _COMPUTETARGETHTTPSPROXYXTIMEOUTS._serialized_start=959
  _COMPUTETARGETHTTPSPROXYXTIMEOUTS._serialized_end=1041
  _COMPUTETARGETHTTPSPROXY._serialized_start=1044
  _COMPUTETARGETHTTPSPROXY._serialized_end=1445
  _COMPUTETARGETINSTANCEXTIMEOUTS._serialized_start=1447
  _COMPUTETARGETINSTANCEXTIMEOUTS._serialized_end=1511
  _COMPUTETARGETINSTANCE._serialized_start=1514
  _COMPUTETARGETINSTANCE._serialized_end=1839
  _COMPUTETARGETPOOLXTIMEOUTS._serialized_start=1841
  _COMPUTETARGETPOOLXTIMEOUTS._serialized_end=1917
  _COMPUTETARGETPOOL._serialized_start=1920
  _COMPUTETARGETPOOL._serialized_end=2286
  _COMPUTETARGETSSLPROXYXTIMEOUTS._serialized_start=2288
  _COMPUTETARGETSSLPROXYXTIMEOUTS._serialized_end=2368
  _COMPUTETARGETSSLPROXY._serialized_start=2371
  _COMPUTETARGETSSLPROXY._serialized_end=2755
  _COMPUTETARGETTCPPROXYXTIMEOUTS._serialized_start=2757
  _COMPUTETARGETTCPPROXYXTIMEOUTS._serialized_end=2837
  _COMPUTETARGETTCPPROXY._serialized_start=2840
  _COMPUTETARGETTCPPROXY._serialized_end=3198
# @@protoc_insertion_point(module_scope)
