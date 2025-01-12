# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_health.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgcp/gcp_compute_health.proto\x12\x1eoak9.tython.gcp.compute_health\x1a\x13shared/shared.proto\"|\n\"ComputeHealthCheckXGrpcHealthCheck\x12\x19\n\x11grpc_service_name\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x01\x12\x11\n\tport_name\x18\x03 \x01(\t\x12\x1a\n\x12port_specification\x18\x04 \x01(\t\"\xae\x01\n#ComputeHealthCheckXHttp2HealthCheck\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x01\x12\x11\n\tport_name\x18\x03 \x01(\t\x12\x1a\n\x12port_specification\x18\x04 \x01(\t\x12\x14\n\x0cproxy_header\x18\x05 \x01(\t\x12\x14\n\x0crequest_path\x18\x06 \x01(\t\x12\x10\n\x08response\x18\x07 \x01(\t\"\xad\x01\n\"ComputeHealthCheckXHttpHealthCheck\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x01\x12\x11\n\tport_name\x18\x03 \x01(\t\x12\x1a\n\x12port_specification\x18\x04 \x01(\t\x12\x14\n\x0cproxy_header\x18\x05 \x01(\t\x12\x14\n\x0crequest_path\x18\x06 \x01(\t\x12\x10\n\x08response\x18\x07 \x01(\t\"\xae\x01\n#ComputeHealthCheckXHttpsHealthCheck\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x01\x12\x11\n\tport_name\x18\x03 \x01(\t\x12\x1a\n\x12port_specification\x18\x04 \x01(\t\x12\x14\n\x0cproxy_header\x18\x05 \x01(\t\x12\x14\n\x0crequest_path\x18\x06 \x01(\t\x12\x10\n\x08response\x18\x07 \x01(\t\".\n\x1c\x43omputeHealthCheckXLogConfig\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\x99\x01\n!ComputeHealthCheckXSslHealthCheck\x12\x0c\n\x04port\x18\x01 \x01(\x01\x12\x11\n\tport_name\x18\x02 \x01(\t\x12\x1a\n\x12port_specification\x18\x03 \x01(\t\x12\x14\n\x0cproxy_header\x18\x04 \x01(\t\x12\x0f\n\x07request\x18\x05 \x01(\t\x12\x10\n\x08response\x18\x06 \x01(\t\"\x99\x01\n!ComputeHealthCheckXTcpHealthCheck\x12\x0c\n\x04port\x18\x01 \x01(\x01\x12\x11\n\tport_name\x18\x02 \x01(\t\x12\x1a\n\x12port_specification\x18\x03 \x01(\t\x12\x14\n\x0cproxy_header\x18\x04 \x01(\t\x12\x0f\n\x07request\x18\x05 \x01(\t\x12\x10\n\x08response\x18\x06 \x01(\t\"M\n\x1b\x43omputeHealthCheckXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x8e\x08\n\x12\x43omputeHealthCheck\x12\x1a\n\x12\x63heck_interval_sec\x18\x01 \x01(\x01\x12\x1a\n\x12\x63reation_timestamp\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11healthy_threshold\x18\x04 \x01(\x01\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x11\n\tself_link\x18\x08 \x01(\t\x12\x13\n\x0btimeout_sec\x18\t \x01(\x01\x12\x0c\n\x04type\x18\n \x01(\t\x12\x1b\n\x13unhealthy_threshold\x18\x0b \x01(\x01\x12]\n\x11grpc_health_check\x18\x0c \x01(\x0b\x32\x42.oak9.tython.gcp.compute_health.ComputeHealthCheckXGrpcHealthCheck\x12_\n\x12http2_health_check\x18\r \x01(\x0b\x32\x43.oak9.tython.gcp.compute_health.ComputeHealthCheckXHttp2HealthCheck\x12]\n\x11http_health_check\x18\x0e \x01(\x0b\x32\x42.oak9.tython.gcp.compute_health.ComputeHealthCheckXHttpHealthCheck\x12_\n\x12https_health_check\x18\x0f \x01(\x0b\x32\x43.oak9.tython.gcp.compute_health.ComputeHealthCheckXHttpsHealthCheck\x12P\n\nlog_config\x18\x10 \x01(\x0b\x32<.oak9.tython.gcp.compute_health.ComputeHealthCheckXLogConfig\x12[\n\x10ssl_health_check\x18\x11 \x01(\x0b\x32\x41.oak9.tython.gcp.compute_health.ComputeHealthCheckXSslHealthCheck\x12[\n\x10tcp_health_check\x18\x12 \x01(\x0b\x32\x41.oak9.tython.gcp.compute_health.ComputeHealthCheckXTcpHealthCheck\x12M\n\x08timeouts\x18\x13 \x01(\x0b\x32;.oak9.tython.gcp.compute_health.ComputeHealthCheckXTimeouts\x12\x37\n\rresource_info\x18\x14 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_health_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEHEALTHCHECKXGRPCHEALTHCHECK._serialized_start=85
  _COMPUTEHEALTHCHECKXGRPCHEALTHCHECK._serialized_end=209
  _COMPUTEHEALTHCHECKXHTTP2HEALTHCHECK._serialized_start=212
  _COMPUTEHEALTHCHECKXHTTP2HEALTHCHECK._serialized_end=386
  _COMPUTEHEALTHCHECKXHTTPHEALTHCHECK._serialized_start=389
  _COMPUTEHEALTHCHECKXHTTPHEALTHCHECK._serialized_end=562
  _COMPUTEHEALTHCHECKXHTTPSHEALTHCHECK._serialized_start=565
  _COMPUTEHEALTHCHECKXHTTPSHEALTHCHECK._serialized_end=739
  _COMPUTEHEALTHCHECKXLOGCONFIG._serialized_start=741
  _COMPUTEHEALTHCHECKXLOGCONFIG._serialized_end=787
  _COMPUTEHEALTHCHECKXSSLHEALTHCHECK._serialized_start=790
  _COMPUTEHEALTHCHECKXSSLHEALTHCHECK._serialized_end=943
  _COMPUTEHEALTHCHECKXTCPHEALTHCHECK._serialized_start=946
  _COMPUTEHEALTHCHECKXTCPHEALTHCHECK._serialized_end=1099
  _COMPUTEHEALTHCHECKXTIMEOUTS._serialized_start=1101
  _COMPUTEHEALTHCHECKXTIMEOUTS._serialized_end=1178
  _COMPUTEHEALTHCHECK._serialized_start=1181
  _COMPUTEHEALTHCHECK._serialized_end=2219
# @@protoc_insertion_point(module_scope)
