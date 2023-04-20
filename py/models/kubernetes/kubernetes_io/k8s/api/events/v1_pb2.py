# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.events.v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.api.core import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_api_dot_core_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0kubernetes/kubernetes_io.k8s.api.events.v1.proto\x12\x1doak9.tython.k8s.api.events.v1\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\x1a.kubernetes/kubernetes_io.k8s.api.core.v1.proto\"\xc0\x06\n\x05\x45vent\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65precated_count\x18\x03 \x01(\x05\x12W\n\x1a\x64\x65precated_first_timestamp\x18\x04 \x01(\x0b\x32\x33.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.Time\x12V\n\x19\x64\x65precated_last_timestamp\x18\x05 \x01(\x0b\x32\x33.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.Time\x12\x43\n\x11\x64\x65precated_source\x18\x06 \x01(\x0b\x32(.oak9.tython.k8s.api.core.v1.EventSource\x12L\n\nevent_time\x18\x07 \x01(\x0b\x32\x38.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.MicroTime\x12\x0c\n\x04kind\x18\x08 \x01(\t\x12K\n\x08metadata\x18\t \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x0c\n\x04note\x18\n \x01(\t\x12\x0e\n\x06reason\x18\x0b \x01(\t\x12?\n\tregarding\x18\x0c \x01(\x0b\x32,.oak9.tython.k8s.api.core.v1.ObjectReference\x12=\n\x07related\x18\r \x01(\x0b\x32,.oak9.tython.k8s.api.core.v1.ObjectReference\x12\x1c\n\x14reporting_controller\x18\x0e \x01(\t\x12\x1a\n\x12reporting_instance\x18\x0f \x01(\t\x12:\n\x06series\x18\x10 \x01(\x0b\x32*.oak9.tython.k8s.api.events.v1.EventSeries\x12\x0c\n\x04type\x18\x11 \x01(\t\x12\x37\n\rresource_info\x18\x12 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xe7\x01\n\tEventList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x33\n\x05items\x18\x02 \x03(\x0b\x32$.oak9.tython.k8s.api.events.v1.Event\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xab\x01\n\x0b\x45ventSeries\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12T\n\x12last_observed_time\x18\x02 \x01(\x0b\x32\x38.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.MicroTime\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.events.v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENT._serialized_start=219
  _EVENT._serialized_end=1051
  _EVENTLIST._serialized_start=1054
  _EVENTLIST._serialized_end=1285
  _EVENTSERIES._serialized_start=1288
  _EVENTSERIES._serialized_end=1459
# @@protoc_insertion_point(module_scope)