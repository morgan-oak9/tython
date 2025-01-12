# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_dlm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_dlm.proto\x12\x13oak9.tython.aws.dlm\x1a\x13shared/shared.proto\"\xa5\x01\n\x19LifecyclePolicyCreateRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rinterval_unit\x18\x02 \x01(\t\x12\r\n\x05times\x18\x03 \x03(\t\x12\x17\n\x0f\x63ron_expression\x18\x04 \x01(\t\x12\x10\n\x08interval\x18\x05 \x01(\x05\"\xad\x01\n\x1eLifecyclePolicyFastRestoreRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rinterval_unit\x18\x02 \x01(\t\x12\x1a\n\x12\x61vailability_zones\x18\x03 \x03(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x10\n\x08interval\x18\x05 \x01(\x05\"\x8c\x01\n\x19LifecyclePolicyRetainRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rinterval_unit\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x10\n\x08interval\x18\x04 \x01(\x05\"\x8c\x01\n(LifecyclePolicyCrossRegionCopyRetainRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rinterval_unit\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x05\"\xff\x01\n\"LifecyclePolicyCrossRegionCopyRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rtarget_region\x18\x02 \x01(\t\x12\x11\n\tencrypted\x18\x03 \x01(\x08\x12\x0f\n\x07\x63mk_arn\x18\x04 \x01(\t\x12R\n\x0bretain_rule\x18\x05 \x01(\x0b\x32=.oak9.tython.aws.dlm.LifecyclePolicyCrossRegionCopyRetainRule\x12\x11\n\tcopy_tags\x18\x06 \x01(\x08\"\xb7\x05\n\x17LifecyclePolicySchedule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12P\n\x0btags_to_add\x18\x02 \x03(\x0b\x32;.oak9.tython.aws.dlm.LifecyclePolicySchedule.TagsToAddEntry\x12\x43\n\x0b\x63reate_rule\x18\x03 \x01(\x0b\x32..oak9.tython.aws.dlm.LifecyclePolicyCreateRule\x12U\n\rvariable_tags\x18\x04 \x03(\x0b\x32>.oak9.tython.aws.dlm.LifecyclePolicySchedule.VariableTagsEntry\x12N\n\x11\x66\x61st_restore_rule\x18\x05 \x01(\x0b\x32\x33.oak9.tython.aws.dlm.LifecyclePolicyFastRestoreRule\x12\x43\n\x0bretain_rule\x18\x06 \x01(\x0b\x32..oak9.tython.aws.dlm.LifecyclePolicyRetainRule\x12X\n\x17\x63ross_region_copy_rules\x18\x07 \x03(\x0b\x32\x37.oak9.tython.aws.dlm.LifecyclePolicyCrossRegionCopyRule\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x11\n\tcopy_tags\x18\t \x01(\x08\x1a\x30\n\x0eTagsToAddEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11VariableTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"q\n\x19LifecyclePolicyParameters\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x65xclude_boot_volume\x18\x02 \x01(\x08\"\x94\x03\n\x1cLifecyclePolicyPolicyDetails\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0eresource_types\x18\x02 \x03(\t\x12?\n\tschedules\x18\x03 \x03(\x0b\x32,.oak9.tython.aws.dlm.LifecyclePolicySchedule\x12\x13\n\x0bpolicy_type\x18\x04 \x01(\t\x12\x42\n\nparameters\x18\x05 \x01(\x0b\x32..oak9.tython.aws.dlm.LifecyclePolicyParameters\x12V\n\x0btarget_tags\x18\x06 \x03(\x0b\x32\x41.oak9.tython.aws.dlm.LifecyclePolicyPolicyDetails.TargetTagsEntry\x1a\x31\n\x0fTargetTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd5\x01\n\x0fLifecyclePolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12\x65xecution_role_arn\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12I\n\x0epolicy_details\x18\x05 \x01(\x0b\x32\x31.oak9.tython.aws.dlm.LifecyclePolicyPolicyDetails\"E\n\x03\x44LM\x12>\n\x10lifecycle_policy\x18\x01 \x03(\x0b\x32$.oak9.tython.aws.dlm.LifecyclePolicyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_dlm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIFECYCLEPOLICYSCHEDULE_TAGSTOADDENTRY._options = None
  _LIFECYCLEPOLICYSCHEDULE_TAGSTOADDENTRY._serialized_options = b'8\001'
  _LIFECYCLEPOLICYSCHEDULE_VARIABLETAGSENTRY._options = None
  _LIFECYCLEPOLICYSCHEDULE_VARIABLETAGSENTRY._serialized_options = b'8\001'
  _LIFECYCLEPOLICYPOLICYDETAILS_TARGETTAGSENTRY._options = None
  _LIFECYCLEPOLICYPOLICYDETAILS_TARGETTAGSENTRY._serialized_options = b'8\001'
  _LIFECYCLEPOLICYCREATERULE._serialized_start=64
  _LIFECYCLEPOLICYCREATERULE._serialized_end=229
  _LIFECYCLEPOLICYFASTRESTORERULE._serialized_start=232
  _LIFECYCLEPOLICYFASTRESTORERULE._serialized_end=405
  _LIFECYCLEPOLICYRETAINRULE._serialized_start=408
  _LIFECYCLEPOLICYRETAINRULE._serialized_end=548
  _LIFECYCLEPOLICYCROSSREGIONCOPYRETAINRULE._serialized_start=551
  _LIFECYCLEPOLICYCROSSREGIONCOPYRETAINRULE._serialized_end=691
  _LIFECYCLEPOLICYCROSSREGIONCOPYRULE._serialized_start=694
  _LIFECYCLEPOLICYCROSSREGIONCOPYRULE._serialized_end=949
  _LIFECYCLEPOLICYSCHEDULE._serialized_start=952
  _LIFECYCLEPOLICYSCHEDULE._serialized_end=1647
  _LIFECYCLEPOLICYSCHEDULE_TAGSTOADDENTRY._serialized_start=1546
  _LIFECYCLEPOLICYSCHEDULE_TAGSTOADDENTRY._serialized_end=1594
  _LIFECYCLEPOLICYSCHEDULE_VARIABLETAGSENTRY._serialized_start=1596
  _LIFECYCLEPOLICYSCHEDULE_VARIABLETAGSENTRY._serialized_end=1647
  _LIFECYCLEPOLICYPARAMETERS._serialized_start=1649
  _LIFECYCLEPOLICYPARAMETERS._serialized_end=1762
  _LIFECYCLEPOLICYPOLICYDETAILS._serialized_start=1765
  _LIFECYCLEPOLICYPOLICYDETAILS._serialized_end=2169
  _LIFECYCLEPOLICYPOLICYDETAILS_TARGETTAGSENTRY._serialized_start=2120
  _LIFECYCLEPOLICYPOLICYDETAILS_TARGETTAGSENTRY._serialized_end=2169
  _LIFECYCLEPOLICY._serialized_start=2172
  _LIFECYCLEPOLICY._serialized_end=2385
  _DLM._serialized_start=2387
  _DLM._serialized_end=2456
# @@protoc_insertion_point(module_scope)
