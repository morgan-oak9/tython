# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_resource.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egcp/gcp_compute_resource.proto\x12 oak9.tython.gcp.compute_resource\x1a\x13shared/shared.proto\"v\n*ComputeResourcePolicyXGroupPlacementPolicy\x12!\n\x19\x61vailability_domain_count\x18\x01 \x01(\x01\x12\x13\n\x0b\x63ollocation\x18\x02 \x01(\t\x12\x10\n\x08vm_count\x18\x03 \x01(\x01\"P\n<ComputeResourcePolicyXInstanceSchedulePolicyXVmStartSchedule\x12\x10\n\x08schedule\x18\x01 \x01(\t\"O\n;ComputeResourcePolicyXInstanceSchedulePolicyXVmStopSchedule\x12\x10\n\x08schedule\x18\x01 \x01(\t\"\xe2\x02\n,ComputeResourcePolicyXInstanceSchedulePolicy\x12\x17\n\x0f\x65xpiration_time\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x11\n\ttime_zone\x18\x03 \x01(\t\x12y\n\x11vm_start_schedule\x18\x04 \x01(\x0b\x32^.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXInstanceSchedulePolicyXVmStartSchedule\x12w\n\x10vm_stop_schedule\x18\x05 \x01(\x0b\x32].oak9.tython.gcp.compute_resource.ComputeResourcePolicyXInstanceSchedulePolicyXVmStopSchedule\"y\n<ComputeResourcePolicyXSnapshotSchedulePolicyXRetentionPolicy\x12\x1a\n\x12max_retention_days\x18\x01 \x01(\x01\x12\x1d\n\x15on_source_disk_delete\x18\x02 \x01(\t\"p\nCComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXDailySchedule\x12\x15\n\rdays_in_cycle\x18\x01 \x01(\x01\x12\x12\n\nstart_time\x18\x02 \x01(\t\"r\nDComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXHourlySchedule\x12\x16\n\x0ehours_in_cycle\x18\x01 \x01(\x01\x12\x12\n\nstart_time\x18\x02 \x01(\t\"r\nOComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXWeeklyScheduleXDayOfWeeks\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\"\xd0\x01\nDComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXWeeklySchedule\x12\x87\x01\n\x0c\x64\x61y_of_weeks\x18\x01 \x03(\x0b\x32q.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXWeeklyScheduleXDayOfWeeks\"\xb8\x03\n5ComputeResourcePolicyXSnapshotSchedulePolicyXSchedule\x12}\n\x0e\x64\x61ily_schedule\x18\x01 \x01(\x0b\x32\x65.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXDailySchedule\x12\x7f\n\x0fhourly_schedule\x18\x02 \x01(\x0b\x32\x66.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXHourlySchedule\x12\x7f\n\x0fweekly_schedule\x18\x03 \x01(\x0b\x32\x66.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXScheduleXWeeklySchedule\"\x9f\x02\n?ComputeResourcePolicyXSnapshotSchedulePolicyXSnapshotProperties\x12\x13\n\x0bguest_flush\x18\x01 \x01(\x08\x12}\n\x06labels\x18\x02 \x03(\x0b\x32m.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXSnapshotProperties.LabelsEntry\x12\x19\n\x11storage_locations\x18\x03 \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x93\x03\n,ComputeResourcePolicyXSnapshotSchedulePolicy\x12x\n\x10retention_policy\x18\x01 \x01(\x0b\x32^.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXRetentionPolicy\x12i\n\x08schedule\x18\x02 \x01(\x0b\x32W.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXSchedule\x12~\n\x13snapshot_properties\x18\x03 \x01(\x0b\x32\x61.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicyXSnapshotProperties\"@\n\x1e\x43omputeResourcePolicyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xd9\x04\n\x15\x43omputeResourcePolicy\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x11\n\tself_link\x18\x06 \x01(\t\x12l\n\x16group_placement_policy\x18\x07 \x01(\x0b\x32L.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXGroupPlacementPolicy\x12p\n\x18instance_schedule_policy\x18\x08 \x01(\x0b\x32N.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXInstanceSchedulePolicy\x12p\n\x18snapshot_schedule_policy\x18\t \x01(\x0b\x32N.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXSnapshotSchedulePolicy\x12R\n\x08timeouts\x18\n \x01(\x0b\x32@.oak9.tython.gcp.compute_resource.ComputeResourcePolicyXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_resource_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES_LABELSENTRY._options = None
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES_LABELSENTRY._serialized_options = b'8\001'
  _COMPUTERESOURCEPOLICYXGROUPPLACEMENTPOLICY._serialized_start=89
  _COMPUTERESOURCEPOLICYXGROUPPLACEMENTPOLICY._serialized_end=207
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICYXVMSTARTSCHEDULE._serialized_start=209
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICYXVMSTARTSCHEDULE._serialized_end=289
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICYXVMSTOPSCHEDULE._serialized_start=291
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICYXVMSTOPSCHEDULE._serialized_end=370
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICY._serialized_start=373
  _COMPUTERESOURCEPOLICYXINSTANCESCHEDULEPOLICY._serialized_end=727
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXRETENTIONPOLICY._serialized_start=729
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXRETENTIONPOLICY._serialized_end=850
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXDAILYSCHEDULE._serialized_start=852
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXDAILYSCHEDULE._serialized_end=964
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXHOURLYSCHEDULE._serialized_start=966
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXHOURLYSCHEDULE._serialized_end=1080
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXWEEKLYSCHEDULEXDAYOFWEEKS._serialized_start=1082
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXWEEKLYSCHEDULEXDAYOFWEEKS._serialized_end=1196
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXWEEKLYSCHEDULE._serialized_start=1199
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULEXWEEKLYSCHEDULE._serialized_end=1407
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULE._serialized_start=1410
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSCHEDULE._serialized_end=1850
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES._serialized_start=1853
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES._serialized_end=2140
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES_LABELSENTRY._serialized_start=2095
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICYXSNAPSHOTPROPERTIES_LABELSENTRY._serialized_end=2140
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICY._serialized_start=2143
  _COMPUTERESOURCEPOLICYXSNAPSHOTSCHEDULEPOLICY._serialized_end=2546
  _COMPUTERESOURCEPOLICYXTIMEOUTS._serialized_start=2548
  _COMPUTERESOURCEPOLICYXTIMEOUTS._serialized_end=2612
  _COMPUTERESOURCEPOLICY._serialized_start=2615
  _COMPUTERESOURCEPOLICY._serialized_end=3216
# @@protoc_insertion_point(module_scope)