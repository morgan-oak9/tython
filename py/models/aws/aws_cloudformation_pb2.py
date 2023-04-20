# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_cloudformation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61ws/aws_cloudformation.proto\x12\x1eoak9.tython.aws.cloudformation\x1a\x13shared/shared.proto\"`\n\x0e\x43ustomResource\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rservice_token\x18\x02 \x01(\t\"\x9d\x03\n\x0e\x43loudFormation\x12G\n\x0f\x63ustom_resource\x18\x01 \x03(\x0b\x32..oak9.tython.aws.cloudformation.CustomResource\x12\x34\n\x05macro\x18\x02 \x03(\x0b\x32%.oak9.tython.aws.cloudformation.Macro\x12\x34\n\x05stack\x18\x03 \x03(\x0b\x32%.oak9.tython.aws.cloudformation.Stack\x12;\n\tstack_set\x18\x04 \x03(\x0b\x32(.oak9.tython.aws.cloudformation.StackSet\x12\x45\n\x0ewait_condition\x18\x05 \x03(\x0b\x32-.oak9.tython.aws.cloudformation.WaitCondition\x12R\n\x15wait_condition_handle\x18\x06 \x03(\x0b\x32\x33.oak9.tython.aws.cloudformation.WaitConditionHandle\"\xa8\x01\n\x05Macro\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x15\n\rfunction_name\x18\x03 \x01(\t\x12\x16\n\x0elog_group_name\x18\x04 \x01(\t\x12\x14\n\x0clog_role_arn\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\"\xf9\x02\n\x05Stack\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11notification_arns\x18\x02 \x03(\t\x12I\n\nparameters\x18\x03 \x03(\x0b\x32\x35.oak9.tython.aws.cloudformation.Stack.ParametersEntry\x12=\n\x04tags\x18\x04 \x03(\x0b\x32/.oak9.tython.aws.cloudformation.Stack.TagsEntry\x12\x16\n\x0etemplate_u_r_l\x18\x05 \x01(\t\x12\x1a\n\x12timeout_in_minutes\x18\x06 \x01(\x05\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x16StackSetAutoDeployment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12(\n retain_stacks_on_account_removal\x18\x03 \x01(\x08\"\xf5\x01\n\x1cStackSetOperationPreferences\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x66\x61ilure_tolerance_count\x18\x02 \x01(\x05\x12$\n\x1c\x66\x61ilure_tolerance_percentage\x18\x03 \x01(\x05\x12\x1c\n\x14max_concurrent_count\x18\x04 \x01(\x05\x12!\n\x19max_concurrent_percentage\x18\x05 \x01(\x05\x12\x14\n\x0cregion_order\x18\x06 \x03(\t\"\x87\x01\n\x19StackSetDeploymentTargets\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x61\x63\x63ounts\x18\x02 \x03(\t\x12\x1f\n\x17organizational_unit_ids\x18\x03 \x03(\t\"|\n\x11StackSetParameter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rparameter_key\x18\x02 \x01(\t\x12\x17\n\x0fparameter_value\x18\x03 \x01(\t\"\x89\x02\n\x16StackSetStackInstances\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12U\n\x12\x64\x65ployment_targets\x18\x02 \x01(\x0b\x32\x39.oak9.tython.aws.cloudformation.StackSetDeploymentTargets\x12\x0f\n\x07regions\x18\x03 \x03(\t\x12N\n\x13parameter_overrides\x18\x04 \x03(\x0b\x32\x31.oak9.tython.aws.cloudformation.StackSetParameter\"\xc8\x05\n\x08StackSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0estack_set_name\x18\x02 \x01(\t\x12\x1f\n\x17\x61\x64ministration_role_arn\x18\x03 \x01(\t\x12O\n\x0f\x61uto_deployment\x18\x04 \x01(\x0b\x32\x36.oak9.tython.aws.cloudformation.StackSetAutoDeployment\x12\x14\n\x0c\x63\x61pabilities\x18\x05 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x1b\n\x13\x65xecution_role_name\x18\x07 \x01(\t\x12[\n\x15operation_preferences\x18\x08 \x01(\x0b\x32<.oak9.tython.aws.cloudformation.StackSetOperationPreferences\x12U\n\x15stack_instances_group\x18\t \x03(\x0b\x32\x36.oak9.tython.aws.cloudformation.StackSetStackInstances\x12\x45\n\nparameters\x18\n \x03(\x0b\x32\x31.oak9.tython.aws.cloudformation.StackSetParameter\x12\x18\n\x10permission_model\x18\x0b \x01(\t\x12@\n\x04tags\x18\x0c \x03(\x0b\x32\x32.oak9.tython.aws.cloudformation.StackSet.TagsEntry\x12\x15\n\rtemplate_body\x18\r \x01(\t\x12\x16\n\x0etemplate_u_r_l\x18\x0e \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\rWaitCondition\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0e\n\x06handle\x18\x03 \x01(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\t\"N\n\x13WaitConditionHandle\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_cloudformation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STACK_PARAMETERSENTRY._options = None
  _STACK_PARAMETERSENTRY._serialized_options = b'8\001'
  _STACK_TAGSENTRY._options = None
  _STACK_TAGSENTRY._serialized_options = b'8\001'
  _STACKSET_TAGSENTRY._options = None
  _STACKSET_TAGSENTRY._serialized_options = b'8\001'
  _CUSTOMRESOURCE._serialized_start=85
  _CUSTOMRESOURCE._serialized_end=181
  _CLOUDFORMATION._serialized_start=184
  _CLOUDFORMATION._serialized_end=597
  _MACRO._serialized_start=600
  _MACRO._serialized_end=768
  _STACK._serialized_start=771
  _STACK._serialized_end=1148
  _STACK_PARAMETERSENTRY._serialized_start=1054
  _STACK_PARAMETERSENTRY._serialized_end=1103
  _STACK_TAGSENTRY._serialized_start=1105
  _STACK_TAGSENTRY._serialized_end=1148
  _STACKSETAUTODEPLOYMENT._serialized_start=1151
  _STACKSETAUTODEPLOYMENT._serialized_end=1291
  _STACKSETOPERATIONPREFERENCES._serialized_start=1294
  _STACKSETOPERATIONPREFERENCES._serialized_end=1539
  _STACKSETDEPLOYMENTTARGETS._serialized_start=1542
  _STACKSETDEPLOYMENTTARGETS._serialized_end=1677
  _STACKSETPARAMETER._serialized_start=1679
  _STACKSETPARAMETER._serialized_end=1803
  _STACKSETSTACKINSTANCES._serialized_start=1806
  _STACKSETSTACKINSTANCES._serialized_end=2071
  _STACKSET._serialized_start=2074
  _STACKSET._serialized_end=2786
  _STACKSET_TAGSENTRY._serialized_start=1105
  _STACKSET_TAGSENTRY._serialized_end=1148
  _WAITCONDITION._serialized_start=2788
  _WAITCONDITION._serialized_end=2908
  _WAITCONDITIONHANDLE._serialized_start=2910
  _WAITCONDITIONHANDLE._serialized_end=2988
# @@protoc_insertion_point(module_scope)
