# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.apiserverinternal.v1alpha1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAkubernetes/kubernetes_io.k8s.api.apiserverinternal.v1alpha1.proto\x12.oak9.tython.k8s.api.apiserverinternal.v1alpha1\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\"\x9c\x01\n\x14ServerStorageVersion\x12\x15\n\rapi_server_id\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65\x63odable_versions\x18\x02 \x03(\t\x12\x18\n\x10\x65ncoding_version\x18\x03 \x01(\t\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xe1\x02\n\x0eStorageVersion\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12P\n\x04spec\x18\x04 \x01(\x0b\x32\x42.oak9.tython.k8s.api.apiserverinternal.v1alpha1.StorageVersionSpec\x12T\n\x06status\x18\x05 \x01(\x0b\x32\x44.oak9.tython.k8s.api.apiserverinternal.v1alpha1.StorageVersionStatus\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x81\x02\n\x17StorageVersionCondition\x12Q\n\x14last_transition_time\x18\x01 \x01(\x0b\x32\x33.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.Time\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1b\n\x13observed_generation\x18\x03 \x01(\x05\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x8a\x02\n\x12StorageVersionList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12M\n\x05items\x18\x02 \x03(\x0b\x32>.oak9.tython.k8s.api.apiserverinternal.v1alpha1.StorageVersion\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"M\n\x12StorageVersionSpec\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xad\x02\n\x14StorageVersionStatus\x12\x1f\n\x17\x63ommon_encoding_version\x18\x01 \x01(\t\x12[\n\nconditions\x18\x02 \x03(\x0b\x32G.oak9.tython.k8s.api.apiserverinternal.v1alpha1.StorageVersionCondition\x12^\n\x10storage_versions\x18\x03 \x03(\x0b\x32\x44.oak9.tython.k8s.api.apiserverinternal.v1alpha1.ServerStorageVersion\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.apiserverinternal.v1alpha1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVERSTORAGEVERSION._serialized_start=205
  _SERVERSTORAGEVERSION._serialized_end=361
  _STORAGEVERSION._serialized_start=364
  _STORAGEVERSION._serialized_end=717
  _STORAGEVERSIONCONDITION._serialized_start=720
  _STORAGEVERSIONCONDITION._serialized_end=977
  _STORAGEVERSIONLIST._serialized_start=980
  _STORAGEVERSIONLIST._serialized_end=1246
  _STORAGEVERSIONSPEC._serialized_start=1248
  _STORAGEVERSIONSPEC._serialized_end=1325
  _STORAGEVERSIONSTATUS._serialized_start=1328
  _STORAGEVERSIONSTATUS._serialized_end=1629
# @@protoc_insertion_point(module_scope)