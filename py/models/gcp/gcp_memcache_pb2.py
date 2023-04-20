# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_memcache.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gcp/gcp_memcache.proto\x12\x18oak9.tython.gcp.memcache\x1a\x13shared/shared.proto\"\x86\x01\nDMemcacheInstanceXMaintenancePolicyXWeeklyMaintenanceWindowXStartTime\x12\r\n\x05hours\x18\x01 \x01(\x01\x12\x0f\n\x07minutes\x18\x02 \x01(\x01\x12\r\n\x05nanos\x18\x03 \x01(\x01\x12\x0f\n\x07seconds\x18\x04 \x01(\x01\"\xcf\x01\n:MemcacheInstanceXMaintenancePolicyXWeeklyMaintenanceWindow\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\t\x12r\n\nstart_time\x18\x03 \x01(\x0b\x32^.oak9.tython.gcp.memcache.MemcacheInstanceXMaintenancePolicyXWeeklyMaintenanceWindowXStartTime\"\xdc\x01\n\"MemcacheInstanceXMaintenancePolicy\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0bupdate_time\x18\x03 \x01(\t\x12w\n\x19weekly_maintenance_window\x18\x04 \x03(\x0b\x32T.oak9.tython.gcp.memcache.MemcacheInstanceXMaintenancePolicyXWeeklyMaintenanceWindow\"\xbb\x01\n#MemcacheInstanceXMemcacheParameters\x12\n\n\x02id\x18\x01 \x01(\t\x12Y\n\x06params\x18\x02 \x03(\x0b\x32I.oak9.tython.gcp.memcache.MemcacheInstanceXMemcacheParameters.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x1bMemcacheInstanceXNodeConfig\x12\x11\n\tcpu_count\x18\x01 \x01(\x01\x12\x16\n\x0ememory_size_mb\x18\x02 \x01(\x01\"K\n\x19MemcacheInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xb1\x08\n\x10MemcacheInstance\x12\x1a\n\x12\x61uthorized_network\x18\x01 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\t\x12\x1a\n\x12\x64iscovery_endpoint\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x46\n\x06labels\x18\x06 \x03(\x0b\x32\x36.oak9.tython.gcp.memcache.MemcacheInstance.LabelsEntry\x12\x61\n\x14maintenance_schedule\x18\x07 \x03(\x0b\x32\x43.oak9.tython.gcp.memcache.MemcacheInstance.MaintenanceScheduleEntry\x12\x1d\n\x15memcache_full_version\x18\x08 \x01(\t\x12U\n\x0ememcache_nodes\x18\t \x03(\x0b\x32=.oak9.tython.gcp.memcache.MemcacheInstance.MemcacheNodesEntry\x12\x18\n\x10memcache_version\x18\n \x01(\t\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x12\n\nnode_count\x18\x0c \x01(\x01\x12\x0f\n\x07project\x18\r \x01(\t\x12\x0e\n\x06region\x18\x0e \x01(\t\x12\r\n\x05zones\x18\x0f \x03(\t\x12X\n\x12maintenance_policy\x18\x10 \x01(\x0b\x32<.oak9.tython.gcp.memcache.MemcacheInstanceXMaintenancePolicy\x12Z\n\x13memcache_parameters\x18\x11 \x01(\x0b\x32=.oak9.tython.gcp.memcache.MemcacheInstanceXMemcacheParameters\x12J\n\x0bnode_config\x18\x12 \x01(\x0b\x32\x35.oak9.tython.gcp.memcache.MemcacheInstanceXNodeConfig\x12\x45\n\x08timeouts\x18\x13 \x01(\x0b\x32\x33.oak9.tython.gcp.memcache.MemcacheInstanceXTimeouts\x12\x37\n\rresource_info\x18\x14 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a:\n\x18MaintenanceScheduleEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12MemcacheNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_memcache_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS_PARAMSENTRY._options = None
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS_PARAMSENTRY._serialized_options = b'8\001'
  _MEMCACHEINSTANCE_LABELSENTRY._options = None
  _MEMCACHEINSTANCE_LABELSENTRY._serialized_options = b'8\001'
  _MEMCACHEINSTANCE_MAINTENANCESCHEDULEENTRY._options = None
  _MEMCACHEINSTANCE_MAINTENANCESCHEDULEENTRY._serialized_options = b'8\001'
  _MEMCACHEINSTANCE_MEMCACHENODESENTRY._options = None
  _MEMCACHEINSTANCE_MEMCACHENODESENTRY._serialized_options = b'8\001'
  _MEMCACHEINSTANCEXMAINTENANCEPOLICYXWEEKLYMAINTENANCEWINDOWXSTARTTIME._serialized_start=74
  _MEMCACHEINSTANCEXMAINTENANCEPOLICYXWEEKLYMAINTENANCEWINDOWXSTARTTIME._serialized_end=208
  _MEMCACHEINSTANCEXMAINTENANCEPOLICYXWEEKLYMAINTENANCEWINDOW._serialized_start=211
  _MEMCACHEINSTANCEXMAINTENANCEPOLICYXWEEKLYMAINTENANCEWINDOW._serialized_end=418
  _MEMCACHEINSTANCEXMAINTENANCEPOLICY._serialized_start=421
  _MEMCACHEINSTANCEXMAINTENANCEPOLICY._serialized_end=641
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS._serialized_start=644
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS._serialized_end=831
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS_PARAMSENTRY._serialized_start=786
  _MEMCACHEINSTANCEXMEMCACHEPARAMETERS_PARAMSENTRY._serialized_end=831
  _MEMCACHEINSTANCEXNODECONFIG._serialized_start=833
  _MEMCACHEINSTANCEXNODECONFIG._serialized_end=905
  _MEMCACHEINSTANCEXTIMEOUTS._serialized_start=907
  _MEMCACHEINSTANCEXTIMEOUTS._serialized_end=982
  _MEMCACHEINSTANCE._serialized_start=985
  _MEMCACHEINSTANCE._serialized_end=2058
  _MEMCACHEINSTANCE_LABELSENTRY._serialized_start=1899
  _MEMCACHEINSTANCE_LABELSENTRY._serialized_end=1944
  _MEMCACHEINSTANCE_MAINTENANCESCHEDULEENTRY._serialized_start=1946
  _MEMCACHEINSTANCE_MAINTENANCESCHEDULEENTRY._serialized_end=2004
  _MEMCACHEINSTANCE_MEMCACHENODESENTRY._serialized_start=2006
  _MEMCACHEINSTANCE_MEMCACHENODESENTRY._serialized_end=2058
# @@protoc_insertion_point(module_scope)
