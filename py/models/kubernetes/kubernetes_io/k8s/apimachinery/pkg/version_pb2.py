# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.apimachinery.pkg.version.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;kubernetes/kubernetes_io.k8s.apimachinery.pkg.version.proto\x12(oak9.tython.k8s.apimachinery.pkg.version\x1a\x13shared/shared.proto\"\xea\x01\n\x04Info\x12\x12\n\nbuild_date\x18\x01 \x01(\t\x12\x10\n\x08\x63ompiler\x18\x02 \x01(\t\x12\x12\n\ngit_commit\x18\x03 \x01(\t\x12\x16\n\x0egit_tree_state\x18\x04 \x01(\t\x12\x13\n\x0bgit_version\x18\x05 \x01(\t\x12\x12\n\ngo_version\x18\x06 \x01(\t\x12\r\n\x05major\x18\x07 \x01(\t\x12\r\n\x05minor\x18\x08 \x01(\t\x12\x10\n\x08platform\x18\t \x01(\t\x12\x37\n\rresource_info\x18\n \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.apimachinery.pkg.version_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INFO._serialized_start=127
  _INFO._serialized_end=361
# @@protoc_insertion_point(module_scope)