# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.authentication.v1alpha1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.api.authentication import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_api_dot_authentication_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>kubernetes/kubernetes_io.k8s.api.authentication.v1alpha1.proto\x12+oak9.tython.k8s.api.authentication.v1alpha1\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\x1a\x38kubernetes/kubernetes_io.k8s.api.authentication.v1.proto\"\x92\x02\n\x11SelfSubjectReview\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12T\n\x06status\x18\x04 \x01(\x0b\x32\x44.oak9.tython.k8s.api.authentication.v1alpha1.SelfSubjectReviewStatus\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x96\x01\n\x17SelfSubjectReviewStatus\x12\x42\n\tuser_info\x18\x01 \x01(\x0b\x32/.oak9.tython.k8s.api.authentication.v1.UserInfo\x12\x37\n\rresource_info\x18\x02 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.authentication.v1alpha1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SELFSUBJECTREVIEW._serialized_start=257
  _SELFSUBJECTREVIEW._serialized_end=531
  _SELFSUBJECTREVIEWSTATUS._serialized_start=534
  _SELFSUBJECTREVIEWSTATUS._serialized_end=684
# @@protoc_insertion_point(module_scope)
