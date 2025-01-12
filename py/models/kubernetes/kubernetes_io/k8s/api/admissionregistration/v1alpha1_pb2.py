# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.admissionregistration.v1alpha1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEkubernetes/kubernetes_io.k8s.api.admissionregistration.v1alpha1.proto\x12\x32oak9.tython.k8s.api.admissionregistration.v1alpha1\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\"\xe2\x03\n\x0eMatchResources\x12k\n\x16\x65xclude_resource_rules\x18\x01 \x03(\x0b\x32K.oak9.tython.k8s.api.admissionregistration.v1alpha1.NamedRuleWithOperations\x12\x14\n\x0cmatch_policy\x18\x02 \x01(\t\x12X\n\x12namespace_selector\x18\x03 \x01(\x0b\x32<.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector\x12U\n\x0fobject_selector\x18\x04 \x01(\x0b\x32<.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x63\n\x0eresource_rules\x18\x05 \x03(\x0b\x32K.oak9.tython.k8s.api.admissionregistration.v1alpha1.NamedRuleWithOperations\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xca\x01\n\x17NamedRuleWithOperations\x12\x12\n\napi_groups\x18\x01 \x03(\t\x12\x14\n\x0c\x61pi_versions\x18\x02 \x03(\t\x12\x12\n\noperations\x18\x03 \x03(\t\x12\x16\n\x0eresource_names\x18\x04 \x03(\t\x12\x11\n\tresources\x18\x05 \x03(\t\x12\r\n\x05scope\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"g\n\tParamKind\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"d\n\x08ParamRef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa5\x02\n\x19ValidatingAdmissionPolicy\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12_\n\x04spec\x18\x04 \x01(\x0b\x32Q.oak9.tython.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicySpec\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb3\x02\n ValidatingAdmissionPolicyBinding\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x66\n\x04spec\x18\x04 \x01(\x0b\x32X.oak9.tython.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicyBindingSpec\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb2\x02\n$ValidatingAdmissionPolicyBindingList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x63\n\x05items\x18\x02 \x03(\x0b\x32T.oak9.tython.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicyBinding\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa2\x02\n$ValidatingAdmissionPolicyBindingSpec\x12[\n\x0fmatch_resources\x18\x01 \x01(\x0b\x32\x42.oak9.tython.k8s.api.admissionregistration.v1alpha1.MatchResources\x12O\n\tparam_ref\x18\x02 \x01(\x0b\x32<.oak9.tython.k8s.api.admissionregistration.v1alpha1.ParamRef\x12\x13\n\x0bpolicy_name\x18\x03 \x01(\t\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa4\x02\n\x1dValidatingAdmissionPolicyList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\\\n\x05items\x18\x02 \x03(\x0b\x32M.oak9.tython.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicy\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xf7\x02\n\x1dValidatingAdmissionPolicySpec\x12\x16\n\x0e\x66\x61ilure_policy\x18\x01 \x01(\t\x12]\n\x11match_constraints\x18\x02 \x01(\x0b\x32\x42.oak9.tython.k8s.api.admissionregistration.v1alpha1.MatchResources\x12Q\n\nparam_kind\x18\x03 \x01(\x0b\x32=.oak9.tython.k8s.api.admissionregistration.v1alpha1.ParamKind\x12S\n\x0bvalidations\x18\x04 \x03(\x0b\x32>.oak9.tython.k8s.api.admissionregistration.v1alpha1.Validation\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"z\n\nValidation\x12\x12\n\nexpression\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.admissionregistration.v1alpha1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MATCHRESOURCES._serialized_start=213
  _MATCHRESOURCES._serialized_end=695
  _NAMEDRULEWITHOPERATIONS._serialized_start=698
  _NAMEDRULEWITHOPERATIONS._serialized_end=900
  _PARAMKIND._serialized_start=902
  _PARAMKIND._serialized_end=1005
  _PARAMREF._serialized_start=1007
  _PARAMREF._serialized_end=1107
  _VALIDATINGADMISSIONPOLICY._serialized_start=1110
  _VALIDATINGADMISSIONPOLICY._serialized_end=1403
  _VALIDATINGADMISSIONPOLICYBINDING._serialized_start=1406
  _VALIDATINGADMISSIONPOLICYBINDING._serialized_end=1713
  _VALIDATINGADMISSIONPOLICYBINDINGLIST._serialized_start=1716
  _VALIDATINGADMISSIONPOLICYBINDINGLIST._serialized_end=2022
  _VALIDATINGADMISSIONPOLICYBINDINGSPEC._serialized_start=2025
  _VALIDATINGADMISSIONPOLICYBINDINGSPEC._serialized_end=2315
  _VALIDATINGADMISSIONPOLICYLIST._serialized_start=2318
  _VALIDATINGADMISSIONPOLICYLIST._serialized_end=2610
  _VALIDATINGADMISSIONPOLICYSPEC._serialized_start=2613
  _VALIDATINGADMISSIONPOLICYSPEC._serialized_end=2988
  _VALIDATION._serialized_start=2990
  _VALIDATION._serialized_end=3112
# @@protoc_insertion_point(module_scope)
