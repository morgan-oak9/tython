# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_google_load_balancer_bundle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.gcp import gcp_compute_backend_pb2 as gcp_dot_gcp__compute__backend__pb2
from oak9.tython.models.gcp import gcp_compute_forwarding_pb2 as gcp_dot_gcp__compute__forwarding__pb2
from oak9.tython.models.gcp import gcp_compute_global_pb2 as gcp_dot_gcp__compute__global__pb2
from oak9.tython.models.gcp import gcp_compute_health_pb2 as gcp_dot_gcp__compute__health__pb2
from oak9.tython.models.gcp import gcp_compute_http_pb2 as gcp_dot_gcp__compute__http__pb2
from oak9.tython.models.gcp import gcp_compute_https_pb2 as gcp_dot_gcp__compute__https__pb2
from oak9.tython.models.gcp import gcp_compute_region_pb2 as gcp_dot_gcp__compute__region__pb2
from oak9.tython.models.gcp import gcp_compute_ssl_pb2 as gcp_dot_gcp__compute__ssl__pb2
from oak9.tython.models.gcp import gcp_compute_target_pb2 as gcp_dot_gcp__compute__target__pb2
from oak9.tython.models.gcp import gcp_compute_url_pb2 as gcp_dot_gcp__compute__url__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)gcp/gcp_google_load_balancer_bundle.proto\x12+oak9.tython.gcp.google_load_balancer_bundle\x1a\x13shared/shared.proto\x1a\x1dgcp/gcp_compute_backend.proto\x1a gcp/gcp_compute_forwarding.proto\x1a\x1cgcp/gcp_compute_global.proto\x1a\x1cgcp/gcp_compute_health.proto\x1a\x1agcp/gcp_compute_http.proto\x1a\x1bgcp/gcp_compute_https.proto\x1a\x1cgcp/gcp_compute_region.proto\x1a\x19gcp/gcp_compute_ssl.proto\x1a\x1cgcp/gcp_compute_target.proto\x1a\x19gcp/gcp_compute_url.proto\"\xbc\x11\n\x12GoogleLoadBalancer\x12U\n\x16\x63ompute_backend_bucket\x18\x01 \x01(\x0b\x32\x35.oak9.tython.gcp.compute_backend.ComputeBackendBucket\x12p\n%compute_backend_bucket_signed_url_key\x18\x02 \x01(\x0b\x32\x41.oak9.tython.gcp.compute_backend.ComputeBackendBucketSignedUrlKey\x12W\n\x17\x63ompute_backend_service\x18\x03 \x01(\x0b\x32\x36.oak9.tython.gcp.compute_backend.ComputeBackendService\x12r\n&compute_backend_service_signed_url_key\x18\x04 \x01(\x0b\x32\x42.oak9.tython.gcp.compute_backend.ComputeBackendServiceSignedUrlKey\x12Z\n\x17\x63ompute_forwarding_rule\x18\x05 \x01(\x0b\x32\x39.oak9.tython.gcp.compute_forwarding.ComputeForwardingRule\x12\x63\n\x1e\x63ompute_global_forwarding_rule\x18\x06 \x01(\x0b\x32;.oak9.tython.gcp.compute_global.ComputeGlobalForwardingRule\x12P\n\x14\x63ompute_health_check\x18\x07 \x01(\x0b\x32\x32.oak9.tython.gcp.compute_health.ComputeHealthCheck\x12W\n\x19\x63ompute_http_health_check\x18\x08 \x01(\x0b\x32\x34.oak9.tython.gcp.compute_http.ComputeHttpHealthCheck\x12Z\n\x1a\x63ompute_https_health_check\x18\t \x01(\x0b\x32\x36.oak9.tython.gcp.compute_https.ComputeHttpsHealthCheck\x12\x63\n\x1e\x63ompute_region_backend_service\x18\n \x01(\x0b\x32;.oak9.tython.gcp.compute_region.ComputeRegionBackendService\x12]\n\x1b\x63ompute_region_health_check\x18\x0b \x01(\x0b\x32\x38.oak9.tython.gcp.compute_region.ComputeRegionHealthCheck\x12\x63\n\x1e\x63ompute_region_ssl_certificate\x18\x0c \x01(\x0b\x32;.oak9.tython.gcp.compute_region.ComputeRegionSslCertificate\x12\x66\n compute_region_target_http_proxy\x18\r \x01(\x0b\x32<.oak9.tython.gcp.compute_region.ComputeRegionTargetHttpProxy\x12h\n!compute_region_target_https_proxy\x18\x0e \x01(\x0b\x32=.oak9.tython.gcp.compute_region.ComputeRegionTargetHttpsProxy\x12S\n\x16\x63ompute_region_url_map\x18\x0f \x01(\x0b\x32\x33.oak9.tython.gcp.compute_region.ComputeRegionUrlMap\x12S\n\x17\x63ompute_ssl_certificate\x18\x10 \x01(\x0b\x32\x32.oak9.tython.gcp.compute_ssl.ComputeSslCertificate\x12I\n\x12\x63ompute_ssl_policy\x18\x11 \x01(\x0b\x32-.oak9.tython.gcp.compute_ssl.ComputeSslPolicy\x12Y\n\x19\x63ompute_target_grpc_proxy\x18\x12 \x01(\x0b\x32\x36.oak9.tython.gcp.compute_target.ComputeTargetGrpcProxy\x12Y\n\x19\x63ompute_target_http_proxy\x18\x13 \x01(\x0b\x32\x36.oak9.tython.gcp.compute_target.ComputeTargetHttpProxy\x12[\n\x1a\x63ompute_target_https_proxy\x18\x14 \x01(\x0b\x32\x37.oak9.tython.gcp.compute_target.ComputeTargetHttpsProxy\x12N\n\x13\x63ompute_target_pool\x18\x15 \x01(\x0b\x32\x31.oak9.tython.gcp.compute_target.ComputeTargetPool\x12W\n\x18\x63ompute_target_ssl_proxy\x18\x16 \x01(\x0b\x32\x35.oak9.tython.gcp.compute_target.ComputeTargetSslProxy\x12W\n\x18\x63ompute_target_tcp_proxy\x18\x17 \x01(\x0b\x32\x35.oak9.tython.gcp.compute_target.ComputeTargetTcpProxy\x12\x43\n\x0f\x63ompute_url_map\x18\x18 \x01(\x0b\x32*.oak9.tython.gcp.compute_url.ComputeUrlMapb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_google_load_balancer_bundle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GOOGLELOADBALANCER._serialized_start=408
  _GOOGLELOADBALANCER._serialized_end=2644
# @@protoc_insertion_point(module_scope)
