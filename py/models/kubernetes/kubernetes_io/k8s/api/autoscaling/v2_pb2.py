# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes/kubernetes_io.k8s.api.autoscaling.v2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta import v1_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1__pb2
from oak9.tython.models.kubernetes.kubernetes_io.k8s.apimachinery.pkg.api import resource_pb2 as kubernetes_dot_kubernetes__io_dot_k8s_dot_apimachinery_dot_pkg_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5kubernetes/kubernetes_io.k8s.api.autoscaling.v2.proto\x12\"oak9.tython.k8s.api.autoscaling.v2\x1a\x13shared/shared.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1.proto\x1a@kubernetes/kubernetes_io.k8s.apimachinery.pkg.api.resource.proto\"\xbb\x01\n\x1d\x43ontainerResourceMetricSource\x12\x11\n\tcontainer\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12@\n\x06target\x18\x03 \x01(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricTarget\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xc1\x01\n\x1d\x43ontainerResourceMetricStatus\x12\x11\n\tcontainer\x18\x01 \x01(\t\x12\x46\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x35.oak9.tython.k8s.api.autoscaling.v2.MetricValueStatus\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x87\x01\n\x1b\x43rossVersionObjectReference\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xd7\x01\n\x14\x45xternalMetricSource\x12\x44\n\x06metric\x18\x01 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12@\n\x06target\x18\x02 \x01(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricTarget\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xdd\x01\n\x14\x45xternalMetricStatus\x12\x46\n\x07\x63urrent\x18\x01 \x01(\x0b\x32\x35.oak9.tython.k8s.api.autoscaling.v2.MetricValueStatus\x12\x44\n\x06metric\x18\x02 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x80\x01\n\x10HPAScalingPolicy\x12\x16\n\x0eperiod_seconds\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xcf\x01\n\x0fHPAScalingRules\x12\x46\n\x08policies\x18\x01 \x03(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.HPAScalingPolicy\x12\x15\n\rselect_policy\x18\x02 \x01(\t\x12$\n\x1cstabilization_window_seconds\x18\x03 \x01(\x05\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xe4\x02\n\x17HorizontalPodAutoscaler\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12K\n\x08metadata\x18\x03 \x01(\x0b\x32\x39.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12M\n\x04spec\x18\x04 \x01(\x0b\x32?.oak9.tython.k8s.api.autoscaling.v2.HorizontalPodAutoscalerSpec\x12Q\n\x06status\x18\x05 \x01(\x0b\x32\x41.oak9.tython.k8s.api.autoscaling.v2.HorizontalPodAutoscalerStatus\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xea\x01\n\x1fHorizontalPodAutoscalerBehavior\x12G\n\nscale_down\x18\x01 \x01(\x0b\x32\x33.oak9.tython.k8s.api.autoscaling.v2.HPAScalingRules\x12\x45\n\x08scale_up\x18\x02 \x01(\x0b\x32\x33.oak9.tython.k8s.api.autoscaling.v2.HPAScalingRules\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xed\x01\n HorizontalPodAutoscalerCondition\x12Q\n\x14last_transition_time\x18\x01 \x01(\x0b\x32\x33.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.Time\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x90\x02\n\x1bHorizontalPodAutoscalerList\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12J\n\x05items\x18\x02 \x03(\x0b\x32;.oak9.tython.k8s.api.autoscaling.v2.HorizontalPodAutoscaler\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12I\n\x08metadata\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xf5\x02\n\x1bHorizontalPodAutoscalerSpec\x12U\n\x08\x62\x65havior\x18\x01 \x01(\x0b\x32\x43.oak9.tython.k8s.api.autoscaling.v2.HorizontalPodAutoscalerBehavior\x12\x14\n\x0cmax_replicas\x18\x02 \x01(\x05\x12?\n\x07metrics\x18\x03 \x03(\x0b\x32..oak9.tython.k8s.api.autoscaling.v2.MetricSpec\x12\x14\n\x0cmin_replicas\x18\x04 \x01(\x05\x12Y\n\x10scale_target_ref\x18\x05 \x01(\x0b\x32?.oak9.tython.k8s.api.autoscaling.v2.CrossVersionObjectReference\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x9c\x03\n\x1dHorizontalPodAutoscalerStatus\x12X\n\nconditions\x18\x01 \x03(\x0b\x32\x44.oak9.tython.k8s.api.autoscaling.v2.HorizontalPodAutoscalerCondition\x12I\n\x0f\x63urrent_metrics\x18\x02 \x03(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricStatus\x12\x18\n\x10\x63urrent_replicas\x18\x03 \x01(\x05\x12\x18\n\x10\x64\x65sired_replicas\x18\x04 \x01(\x05\x12L\n\x0flast_scale_time\x18\x05 \x01(\x0b\x32\x33.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.Time\x12\x1b\n\x13observed_generation\x18\x06 \x01(\x05\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa9\x01\n\x10MetricIdentifier\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x08selector\x18\x02 \x01(\x0b\x32<.oak9.tython.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xd6\x03\n\nMetricSpec\x12]\n\x12\x63ontainer_resource\x18\x01 \x01(\x0b\x32\x41.oak9.tython.k8s.api.autoscaling.v2.ContainerResourceMetricSource\x12J\n\x08\x65xternal\x18\x02 \x01(\x0b\x32\x38.oak9.tython.k8s.api.autoscaling.v2.ExternalMetricSource\x12\x46\n\x06object\x18\x03 \x01(\x0b\x32\x36.oak9.tython.k8s.api.autoscaling.v2.ObjectMetricSource\x12\x42\n\x04pods\x18\x04 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.PodsMetricSource\x12J\n\x08resource\x18\x05 \x01(\x0b\x32\x38.oak9.tython.k8s.api.autoscaling.v2.ResourceMetricSource\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xd8\x03\n\x0cMetricStatus\x12]\n\x12\x63ontainer_resource\x18\x01 \x01(\x0b\x32\x41.oak9.tython.k8s.api.autoscaling.v2.ContainerResourceMetricStatus\x12J\n\x08\x65xternal\x18\x02 \x01(\x0b\x32\x38.oak9.tython.k8s.api.autoscaling.v2.ExternalMetricStatus\x12\x46\n\x06object\x18\x03 \x01(\x0b\x32\x36.oak9.tython.k8s.api.autoscaling.v2.ObjectMetricStatus\x12\x42\n\x04pods\x18\x04 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.PodsMetricStatus\x12J\n\x08resource\x18\x05 \x01(\x0b\x32\x38.oak9.tython.k8s.api.autoscaling.v2.ResourceMetricStatus\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x8a\x02\n\x0cMetricTarget\x12\x1b\n\x13\x61verage_utilization\x18\x01 \x01(\x05\x12N\n\raverage_value\x18\x02 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.api.resource.Quantity\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x46\n\x05value\x18\x04 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.api.resource.Quantity\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x81\x02\n\x11MetricValueStatus\x12\x1b\n\x13\x61verage_utilization\x18\x01 \x01(\x05\x12N\n\raverage_value\x18\x02 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.api.resource.Quantity\x12\x46\n\x05value\x18\x03 \x01(\x0b\x32\x37.oak9.tython.k8s.apimachinery.pkg.api.resource.Quantity\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb0\x02\n\x12ObjectMetricSource\x12Y\n\x10\x64\x65scribed_object\x18\x01 \x01(\x0b\x32?.oak9.tython.k8s.api.autoscaling.v2.CrossVersionObjectReference\x12\x44\n\x06metric\x18\x02 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12@\n\x06target\x18\x03 \x01(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricTarget\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb6\x02\n\x12ObjectMetricStatus\x12\x46\n\x07\x63urrent\x18\x01 \x01(\x0b\x32\x35.oak9.tython.k8s.api.autoscaling.v2.MetricValueStatus\x12Y\n\x10\x64\x65scribed_object\x18\x02 \x01(\x0b\x32?.oak9.tython.k8s.api.autoscaling.v2.CrossVersionObjectReference\x12\x44\n\x06metric\x18\x03 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12\x37\n\rresource_info\x18\x04 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xd3\x01\n\x10PodsMetricSource\x12\x44\n\x06metric\x18\x01 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12@\n\x06target\x18\x02 \x01(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricTarget\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xd9\x01\n\x10PodsMetricStatus\x12\x46\n\x07\x63urrent\x18\x01 \x01(\x0b\x32\x35.oak9.tython.k8s.api.autoscaling.v2.MetricValueStatus\x12\x44\n\x06metric\x18\x02 \x01(\x0b\x32\x34.oak9.tython.k8s.api.autoscaling.v2.MetricIdentifier\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x9f\x01\n\x14ResourceMetricSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x06target\x18\x02 \x01(\x0b\x32\x30.oak9.tython.k8s.api.autoscaling.v2.MetricTarget\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa5\x01\n\x14ResourceMetricStatus\x12\x46\n\x07\x63urrent\x18\x01 \x01(\x0b\x32\x35.oak9.tython.k8s.api.autoscaling.v2.MetricValueStatus\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\rresource_info\x18\x03 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes.kubernetes_io.k8s.api.autoscaling.v2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTAINERRESOURCEMETRICSOURCE._serialized_start=247
  _CONTAINERRESOURCEMETRICSOURCE._serialized_end=434
  _CONTAINERRESOURCEMETRICSTATUS._serialized_start=437
  _CONTAINERRESOURCEMETRICSTATUS._serialized_end=630
  _CROSSVERSIONOBJECTREFERENCE._serialized_start=633
  _CROSSVERSIONOBJECTREFERENCE._serialized_end=768
  _EXTERNALMETRICSOURCE._serialized_start=771
  _EXTERNALMETRICSOURCE._serialized_end=986
  _EXTERNALMETRICSTATUS._serialized_start=989
  _EXTERNALMETRICSTATUS._serialized_end=1210
  _HPASCALINGPOLICY._serialized_start=1213
  _HPASCALINGPOLICY._serialized_end=1341
  _HPASCALINGRULES._serialized_start=1344
  _HPASCALINGRULES._serialized_end=1551
  _HORIZONTALPODAUTOSCALER._serialized_start=1554
  _HORIZONTALPODAUTOSCALER._serialized_end=1910
  _HORIZONTALPODAUTOSCALERBEHAVIOR._serialized_start=1913
  _HORIZONTALPODAUTOSCALERBEHAVIOR._serialized_end=2147
  _HORIZONTALPODAUTOSCALERCONDITION._serialized_start=2150
  _HORIZONTALPODAUTOSCALERCONDITION._serialized_end=2387
  _HORIZONTALPODAUTOSCALERLIST._serialized_start=2390
  _HORIZONTALPODAUTOSCALERLIST._serialized_end=2662
  _HORIZONTALPODAUTOSCALERSPEC._serialized_start=2665
  _HORIZONTALPODAUTOSCALERSPEC._serialized_end=3038
  _HORIZONTALPODAUTOSCALERSTATUS._serialized_start=3041
  _HORIZONTALPODAUTOSCALERSTATUS._serialized_end=3453
  _METRICIDENTIFIER._serialized_start=3456
  _METRICIDENTIFIER._serialized_end=3625
  _METRICSPEC._serialized_start=3628
  _METRICSPEC._serialized_end=4098
  _METRICSTATUS._serialized_start=4101
  _METRICSTATUS._serialized_end=4573
  _METRICTARGET._serialized_start=4576
  _METRICTARGET._serialized_end=4842
  _METRICVALUESTATUS._serialized_start=4845
  _METRICVALUESTATUS._serialized_end=5102
  _OBJECTMETRICSOURCE._serialized_start=5105
  _OBJECTMETRICSOURCE._serialized_end=5409
  _OBJECTMETRICSTATUS._serialized_start=5412
  _OBJECTMETRICSTATUS._serialized_end=5722
  _PODSMETRICSOURCE._serialized_start=5725
  _PODSMETRICSOURCE._serialized_end=5936
  _PODSMETRICSTATUS._serialized_start=5939
  _PODSMETRICSTATUS._serialized_end=6156
  _RESOURCEMETRICSOURCE._serialized_start=6159
  _RESOURCEMETRICSOURCE._serialized_end=6318
  _RESOURCEMETRICSTATUS._serialized_start=6321
  _RESOURCEMETRICSTATUS._serialized_end=6486
# @@protoc_insertion_point(module_scope)
