# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_autoscaling.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61ws/aws_autoscaling.proto\x12\x1boak9.tython.aws.autoscaling\x1a\x13shared/shared.proto\"\xb1\x01\n+AutoScalingGroupLaunchTemplateSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12launch_template_id\x18\x02 \x01(\t\x12\x1c\n\x14launch_template_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"\xa5\x02\n*AutoScalingGroupLifecycleHookSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x64\x65\x66\x61ult_result\x18\x02 \x01(\t\x12\x19\n\x11heartbeat_timeout\x18\x03 \x01(\x05\x12\x1b\n\x13lifecycle_hook_name\x18\x04 \x01(\t\x12\x1c\n\x14lifecycle_transition\x18\x05 \x01(\t\x12\x1d\n\x15notification_metadata\x18\x06 \x01(\t\x12\x1f\n\x17notification_target_arn\x18\x07 \x01(\t\x12\x10\n\x08role_arn\x18\x08 \x01(\t\"\x82\x01\n!AutoScalingGroupMetricsCollection\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bgranularity\x18\x02 \x01(\t\x12\x0f\n\x07metrics\x18\x03 \x03(\t\"\xb1\x02\n%AutoScalingGroupInstancesDistribution\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12%\n\x1don_demand_allocation_strategy\x18\x02 \x01(\t\x12\x1f\n\x17on_demand_base_capacity\x18\x03 \x01(\x05\x12\x30\n(on_demand_percentage_above_base_capacity\x18\x04 \x01(\x05\x12 \n\x18spot_allocation_strategy\x18\x05 \x01(\t\x12\x1b\n\x13spot_instance_pools\x18\x06 \x01(\x05\x12\x16\n\x0espot_max_price\x18\x07 \x01(\t\"\x94\x01\n\'AutoScalingGroupLaunchTemplateOverrides\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rinstance_type\x18\x02 \x01(\t\x12\x19\n\x11weighted_capacity\x18\x03 \x01(\t\"\xa3\x02\n\x1e\x41utoScalingGroupLaunchTemplate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12o\n\x1dlaunch_template_specification\x18\x02 \x01(\x0b\x32H.oak9.tython.aws.autoscaling.AutoScalingGroupLaunchTemplateSpecification\x12W\n\toverrides\x18\x03 \x03(\x0b\x32\x44.oak9.tython.aws.autoscaling.AutoScalingGroupLaunchTemplateOverrides\"\x99\x02\n$AutoScalingGroupMixedInstancesPolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x62\n\x16instances_distribution\x18\x02 \x01(\x0b\x32\x42.oak9.tython.aws.autoscaling.AutoScalingGroupInstancesDistribution\x12T\n\x0flaunch_template\x18\x03 \x01(\x0b\x32;.oak9.tython.aws.autoscaling.AutoScalingGroupLaunchTemplate\"\x93\x01\n)AutoScalingGroupNotificationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12notification_types\x18\x02 \x03(\t\x12\x11\n\ttopic_arn\x18\x03 \x01(\t\"\x8f\x01\n\x1b\x41utoScalingGroupTagProperty\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1b\n\x13propagate_at_launch\x18\x03 \x01(\x08\x12\r\n\x05value\x18\x04 \x01(\t\"\x94\t\n\x10\x41utoScalingGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x61uto_scaling_group_name\x18\x02 \x01(\t\x12\x1a\n\x12\x61vailability_zones\x18\x03 \x03(\t\x12\x10\n\x08\x63ooldown\x18\x04 \x01(\t\x12\x18\n\x10\x64\x65sired_capacity\x18\x05 \x01(\t\x12!\n\x19health_check_grace_period\x18\x06 \x01(\x05\x12\x19\n\x11health_check_type\x18\x07 \x01(\t\x12\x13\n\x0binstance_id\x18\x08 \x01(\t\x12!\n\x19launch_configuration_name\x18\t \x01(\t\x12\x61\n\x0flaunch_template\x18\n \x01(\x0b\x32H.oak9.tython.aws.autoscaling.AutoScalingGroupLaunchTemplateSpecification\x12r\n!lifecycle_hook_specification_list\x18\x0b \x03(\x0b\x32G.oak9.tython.aws.autoscaling.AutoScalingGroupLifecycleHookSpecification\x12\x1b\n\x13load_balancer_names\x18\x0c \x03(\t\x12\x1d\n\x15max_instance_lifetime\x18\r \x01(\x05\x12\x10\n\x08max_size\x18\x0e \x01(\t\x12Z\n\x12metrics_collection\x18\x0f \x03(\x0b\x32>.oak9.tython.aws.autoscaling.AutoScalingGroupMetricsCollection\x12\x10\n\x08min_size\x18\x10 \x01(\t\x12\x61\n\x16mixed_instances_policy\x18\x11 \x01(\x0b\x32\x41.oak9.tython.aws.autoscaling.AutoScalingGroupMixedInstancesPolicy\x12-\n%new_instances_protected_from_scale_in\x18\x12 \x01(\x08\x12k\n\x1bnotification_configurations\x18\x13 \x03(\x0b\x32\x46.oak9.tython.aws.autoscaling.AutoScalingGroupNotificationConfiguration\x12\x17\n\x0fplacement_group\x18\x14 \x01(\t\x12\x1f\n\x17service_linked_role_arn\x18\x15 \x01(\t\x12\x46\n\x04tags\x18\x16 \x03(\x0b\x32\x38.oak9.tython.aws.autoscaling.AutoScalingGroupTagProperty\x12\x19\n\x11target_group_arns\x18\x17 \x03(\t\x12\x1c\n\x14termination_policies\x18\x18 \x03(\t\x12\x1b\n\x13vpc_zone_identifier\x18\x19 \x03(\t\"\xf8\x02\n\x0b\x41utoScaling\x12I\n\x12\x61uto_scaling_group\x18\x01 \x03(\x0b\x32-.oak9.tython.aws.autoscaling.AutoScalingGroup\x12N\n\x14launch_configuration\x18\x02 \x03(\x0b\x32\x30.oak9.tython.aws.autoscaling.LaunchConfiguration\x12\x42\n\x0elifecycle_hook\x18\x03 \x03(\x0b\x32*.oak9.tython.aws.autoscaling.LifecycleHook\x12\x42\n\x0escaling_policy\x18\x04 \x03(\x0b\x32*.oak9.tython.aws.autoscaling.ScalingPolicy\x12\x46\n\x10scheduled_action\x18\x05 \x03(\x0b\x32,.oak9.tython.aws.autoscaling.ScheduledAction\"\xd8\x01\n\x1eLaunchConfigurationBlockDevice\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x64\x65lete_on_termination\x18\x02 \x01(\x08\x12\x11\n\tencrypted\x18\x03 \x01(\x08\x12\x0c\n\x04iops\x18\x04 \x01(\x05\x12\x13\n\x0bsnapshot_id\x18\x05 \x01(\t\x12\x13\n\x0bvolume_size\x18\x06 \x01(\x05\x12\x13\n\x0bvolume_type\x18\x07 \x01(\t\"\xe8\x01\n%LaunchConfigurationBlockDeviceMapping\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12H\n\x03\x65\x62s\x18\x03 \x01(\x0b\x32;.oak9.tython.aws.autoscaling.LaunchConfigurationBlockDevice\x12\x11\n\tno_device\x18\x04 \x01(\x08\x12\x14\n\x0cvirtual_name\x18\x05 \x01(\t\"\xe5\x04\n\x13LaunchConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12#\n\x1b\x61ssociate_public_ip_address\x18\x02 \x01(\x08\x12\x61\n\x15\x62lock_device_mappings\x18\x03 \x03(\x0b\x32\x42.oak9.tython.aws.autoscaling.LaunchConfigurationBlockDeviceMapping\x12\x1b\n\x13\x63lassic_link_vpc_id\x18\x04 \x01(\t\x12(\n classic_link_vpc_security_groups\x18\x05 \x03(\t\x12\x15\n\rebs_optimized\x18\x06 \x01(\x08\x12\x1c\n\x14iam_instance_profile\x18\x07 \x01(\t\x12\x10\n\x08image_id\x18\x08 \x01(\t\x12\x13\n\x0binstance_id\x18\t \x01(\t\x12\x1b\n\x13instance_monitoring\x18\n \x01(\x08\x12\x15\n\rinstance_type\x18\x0b \x01(\t\x12\x11\n\tkernel_id\x18\x0c \x01(\t\x12\x10\n\x08key_name\x18\r \x01(\t\x12!\n\x19launch_configuration_name\x18\x0e \x01(\t\x12\x19\n\x11placement_tenancy\x18\x0f \x01(\t\x12\x13\n\x0bram_disk_id\x18\x10 \x01(\t\x12\x17\n\x0fsecurity_groups\x18\x11 \x03(\t\x12\x12\n\nspot_price\x18\x12 \x01(\t\x12\x11\n\tuser_data\x18\x13 \x01(\t\"\xa9\x02\n\rLifecycleHook\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x61uto_scaling_group_name\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x65\x66\x61ult_result\x18\x03 \x01(\t\x12\x19\n\x11heartbeat_timeout\x18\x04 \x01(\x05\x12\x1b\n\x13lifecycle_hook_name\x18\x05 \x01(\t\x12\x1c\n\x14lifecycle_transition\x18\x06 \x01(\t\x12\x1d\n\x15notification_metadata\x18\x07 \x01(\t\x12\x1f\n\x17notification_target_arn\x18\x08 \x01(\t\x12\x10\n\x08role_arn\x18\t \x01(\t\"\xbc\x01\n\x1bScalingPolicyStepAdjustment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12#\n\x1bmetric_interval_lower_bound\x18\x02 \x01(\x01\x12#\n\x1bmetric_interval_upper_bound\x18\x03 \x01(\x01\x12\x1a\n\x12scaling_adjustment\x18\x04 \x01(\x05\"t\n\x1cScalingPolicyMetricDimension\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xfd\x01\n*ScalingPolicyCustomizedMetricSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12M\n\ndimensions\x18\x02 \x03(\x0b\x32\x39.oak9.tython.aws.autoscaling.ScalingPolicyMetricDimension\x12\x13\n\x0bmetric_name\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12\x11\n\tstatistic\x18\x05 \x01(\t\x12\x0c\n\x04unit\x18\x06 \x01(\t\"\x9d\x01\n*ScalingPolicyPredefinedMetricSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16predefined_metric_type\x18\x02 \x01(\t\x12\x16\n\x0eresource_label\x18\x03 \x01(\t\"\xf7\x02\n(ScalingPolicyTargetTrackingConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12p\n\x1f\x63ustomized_metric_specification\x18\x02 \x01(\x0b\x32G.oak9.tython.aws.autoscaling.ScalingPolicyCustomizedMetricSpecification\x12\x18\n\x10\x64isable_scale_in\x18\x03 \x01(\x08\x12p\n\x1fpredefined_metric_specification\x18\x04 \x01(\x0b\x32G.oak9.tython.aws.autoscaling.ScalingPolicyPredefinedMetricSpecification\x12\x14\n\x0ctarget_value\x18\x05 \x01(\x01\"\xed\x03\n\rScalingPolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x61\x64justment_type\x18\x02 \x01(\t\x12\x1f\n\x17\x61uto_scaling_group_name\x18\x03 \x01(\t\x12\x10\n\x08\x63ooldown\x18\x04 \x01(\t\x12!\n\x19\x65stimated_instance_warmup\x18\x05 \x01(\x05\x12\x1f\n\x17metric_aggregation_type\x18\x06 \x01(\t\x12 \n\x18min_adjustment_magnitude\x18\x07 \x01(\x05\x12\x13\n\x0bpolicy_type\x18\x08 \x01(\t\x12\x1a\n\x12scaling_adjustment\x18\t \x01(\x05\x12R\n\x10step_adjustments\x18\n \x03(\x0b\x32\x38.oak9.tython.aws.autoscaling.ScalingPolicyStepAdjustment\x12l\n\x1dtarget_tracking_configuration\x18\x0b \x01(\x0b\x32\x45.oak9.tython.aws.autoscaling.ScalingPolicyTargetTrackingConfiguration\"\xe3\x01\n\x0fScheduledAction\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x61uto_scaling_group_name\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65sired_capacity\x18\x03 \x01(\x05\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\t\x12\x10\n\x08max_size\x18\x05 \x01(\x05\x12\x10\n\x08min_size\x18\x06 \x01(\x05\x12\x12\n\nrecurrence\x18\x07 \x01(\t\x12\x12\n\nstart_time\x18\x08 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_autoscaling_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTOSCALINGGROUPLAUNCHTEMPLATESPECIFICATION._serialized_start=80
  _AUTOSCALINGGROUPLAUNCHTEMPLATESPECIFICATION._serialized_end=257
  _AUTOSCALINGGROUPLIFECYCLEHOOKSPECIFICATION._serialized_start=260
  _AUTOSCALINGGROUPLIFECYCLEHOOKSPECIFICATION._serialized_end=553
  _AUTOSCALINGGROUPMETRICSCOLLECTION._serialized_start=556
  _AUTOSCALINGGROUPMETRICSCOLLECTION._serialized_end=686
  _AUTOSCALINGGROUPINSTANCESDISTRIBUTION._serialized_start=689
  _AUTOSCALINGGROUPINSTANCESDISTRIBUTION._serialized_end=994
  _AUTOSCALINGGROUPLAUNCHTEMPLATEOVERRIDES._serialized_start=997
  _AUTOSCALINGGROUPLAUNCHTEMPLATEOVERRIDES._serialized_end=1145
  _AUTOSCALINGGROUPLAUNCHTEMPLATE._serialized_start=1148
  _AUTOSCALINGGROUPLAUNCHTEMPLATE._serialized_end=1439
  _AUTOSCALINGGROUPMIXEDINSTANCESPOLICY._serialized_start=1442
  _AUTOSCALINGGROUPMIXEDINSTANCESPOLICY._serialized_end=1723
  _AUTOSCALINGGROUPNOTIFICATIONCONFIGURATION._serialized_start=1726
  _AUTOSCALINGGROUPNOTIFICATIONCONFIGURATION._serialized_end=1873
  _AUTOSCALINGGROUPTAGPROPERTY._serialized_start=1876
  _AUTOSCALINGGROUPTAGPROPERTY._serialized_end=2019
  _AUTOSCALINGGROUP._serialized_start=2022
  _AUTOSCALINGGROUP._serialized_end=3194
  _AUTOSCALING._serialized_start=3197
  _AUTOSCALING._serialized_end=3573
  _LAUNCHCONFIGURATIONBLOCKDEVICE._serialized_start=3576
  _LAUNCHCONFIGURATIONBLOCKDEVICE._serialized_end=3792
  _LAUNCHCONFIGURATIONBLOCKDEVICEMAPPING._serialized_start=3795
  _LAUNCHCONFIGURATIONBLOCKDEVICEMAPPING._serialized_end=4027
  _LAUNCHCONFIGURATION._serialized_start=4030
  _LAUNCHCONFIGURATION._serialized_end=4643
  _LIFECYCLEHOOK._serialized_start=4646
  _LIFECYCLEHOOK._serialized_end=4943
  _SCALINGPOLICYSTEPADJUSTMENT._serialized_start=4946
  _SCALINGPOLICYSTEPADJUSTMENT._serialized_end=5134
  _SCALINGPOLICYMETRICDIMENSION._serialized_start=5136
  _SCALINGPOLICYMETRICDIMENSION._serialized_end=5252
  _SCALINGPOLICYCUSTOMIZEDMETRICSPECIFICATION._serialized_start=5255
  _SCALINGPOLICYCUSTOMIZEDMETRICSPECIFICATION._serialized_end=5508
  _SCALINGPOLICYPREDEFINEDMETRICSPECIFICATION._serialized_start=5511
  _SCALINGPOLICYPREDEFINEDMETRICSPECIFICATION._serialized_end=5668
  _SCALINGPOLICYTARGETTRACKINGCONFIGURATION._serialized_start=5671
  _SCALINGPOLICYTARGETTRACKINGCONFIGURATION._serialized_end=6046
  _SCALINGPOLICY._serialized_start=6049
  _SCALINGPOLICY._serialized_end=6542
  _SCHEDULEDACTION._serialized_start=6545
  _SCHEDULEDACTION._serialized_end=6772
# @@protoc_insertion_point(module_scope)
