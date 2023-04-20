# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.coordination.v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6kubernetes/kubernetes_io.k8s.api.coordination.v1.proto\x12#oak9.tython.k8s.api.coordination.v1\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\"\xee\x01\n\x05Lease\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12<\n\x04spec\x18\x04 \x01(\x0b\x32..oak9.tython.k8s.api.coordination.v1.LeaseSpec\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xed\x01\n\tLeaseList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x39\n\x05items\x18\x02 \x03(\x0b\x32*.oak9.tython.k8s.api.coordination.v1.Lease\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb6\x02\n\tLeaseSpec\x12N\n\x0c\x61\x63quire_time\x18\x01 \x01(\x0b\x32\x38.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.MicroTime\x12\x17\n\x0fholder_identity\x18\x02 \x01(\t\x12\x1e\n\x16lease_duration_seconds\x18\x03 \x01(\x05\x12\x19\n\x11lease_transitions\x18\x04 \x01(\x05\x12L\n\nrenew_time\x18\x05 \x01(\x0b\x32\x38.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.MicroTime\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.coordination.v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LEASE._serialized_start=183
  _LEASE._serialized_end=421
  _LEASELIST._serialized_start=424
  _LEASELIST._serialized_end=661
  _LEASESPEC._serialized_start=664
  _LEASESPEC._serialized_end=974
# @@protoc_insertion_point(module_scope)
