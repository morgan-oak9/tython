# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_google_spanner_bundle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.gcp import gcp_spanner_pb2 as gcp_dot_gcp__spanner__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#gcp/gcp_google_spanner_bundle.proto\x12%oak9.tython.gcp.google_spanner_bundle\x1a\x13shared/shared.proto\x1a\x15gcp/gcp_spanner.proto\"\xab\x05\n\rGoogleSpanner\x12\x42\n\x10spanner_database\x18\x01 \x03(\x0b\x32(.oak9.tython.gcp.spanner.SpannerDatabase\x12X\n\x1cspanner_database_iam_binding\x18\x02 \x03(\x0b\x32\x32.oak9.tython.gcp.spanner.SpannerDatabaseIamBinding\x12V\n\x1bspanner_database_iam_member\x18\x03 \x03(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerDatabaseIamMember\x12V\n\x1bspanner_database_iam_policy\x18\x04 \x03(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerDatabaseIamPolicy\x12\x42\n\x10spanner_instance\x18\x05 \x01(\x0b\x32(.oak9.tython.gcp.spanner.SpannerInstance\x12X\n\x1cspanner_instance_iam_binding\x18\x06 \x03(\x0b\x32\x32.oak9.tython.gcp.spanner.SpannerInstanceIamBinding\x12V\n\x1bspanner_instance_iam_member\x18\x07 \x03(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerInstanceIamMember\x12V\n\x1bspanner_instance_iam_policy\x18\x08 \x03(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerInstanceIamPolicyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_google_spanner_bundle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GOOGLESPANNER._serialized_start=123
  _GOOGLESPANNER._serialized_end=806
# @@protoc_insertion_point(module_scope)
