# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_https.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgcp/gcp_compute_https.proto\x12\x1doak9.tython.gcp.compute_https\x1a\x13shared/shared.proto\"R\n ComputeHttpsHealthCheckXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xaf\x03\n\x17\x43omputeHttpsHealthCheck\x12\x1a\n\x12\x63heck_interval_sec\x18\x01 \x01(\x01\x12\x1a\n\x12\x63reation_timestamp\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11healthy_threshold\x18\x04 \x01(\x01\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0c\n\x04port\x18\x08 \x01(\x01\x12\x0f\n\x07project\x18\t \x01(\t\x12\x14\n\x0crequest_path\x18\n \x01(\t\x12\x11\n\tself_link\x18\x0b \x01(\t\x12\x13\n\x0btimeout_sec\x18\x0c \x01(\x01\x12\x1b\n\x13unhealthy_threshold\x18\r \x01(\x01\x12Q\n\x08timeouts\x18\x0e \x01(\x0b\x32?.oak9.tython.gcp.compute_https.ComputeHttpsHealthCheckXTimeouts\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_https_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEHTTPSHEALTHCHECKXTIMEOUTS._serialized_start=83
  _COMPUTEHTTPSHEALTHCHECKXTIMEOUTS._serialized_end=165
  _COMPUTEHTTPSHEALTHCHECK._serialized_start=168
  _COMPUTEHTTPSHEALTHCHECK._serialized_end=599
# @@protoc_insertion_point(module_scope)
