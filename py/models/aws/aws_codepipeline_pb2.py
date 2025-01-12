# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_codepipeline.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61ws/aws_codepipeline.proto\x12\x1coak9.tython.aws.codepipeline\x1a\x13shared/shared.proto\"\xc7\x01\n\'CustomActionTypeConfigurationProperties\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\tqueryable\x18\x05 \x01(\x08\x12\x10\n\x08required\x18\x06 \x01(\x08\x12\x0e\n\x06secret\x18\x07 \x01(\x08\"\x88\x01\n\x1f\x43ustomActionTypeArtifactDetails\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rmaximum_count\x18\x02 \x01(\x05\x12\x15\n\rminimum_count\x18\x03 \x01(\x05\"\xd6\x01\n\x18\x43ustomActionTypeSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x65ntity_url_template\x18\x02 \x01(\t\x12\x1e\n\x16\x65xecution_url_template\x18\x03 \x01(\t\x12\x1d\n\x15revision_url_template\x18\x04 \x01(\t\x12%\n\x1dthird_party_configuration_url\x18\x05 \x01(\t\"\xe7\x04\n\x10\x43ustomActionType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12g\n\x18\x63onfiguration_properties\x18\x03 \x03(\x0b\x32\x45.oak9.tython.aws.codepipeline.CustomActionTypeConfigurationProperties\x12]\n\x16input_artifact_details\x18\x04 \x01(\x0b\x32=.oak9.tython.aws.codepipeline.CustomActionTypeArtifactDetails\x12^\n\x17output_artifact_details\x18\x05 \x01(\x0b\x32=.oak9.tython.aws.codepipeline.CustomActionTypeArtifactDetails\x12\x10\n\x08provider\x18\x06 \x01(\t\x12H\n\x08settings\x18\x07 \x01(\x0b\x32\x36.oak9.tython.aws.codepipeline.CustomActionTypeSettings\x12\x46\n\x04tags\x18\x08 \x03(\x0b\x32\x38.oak9.tython.aws.codepipeline.CustomActionType.TagsEntry\x12\x0f\n\x07version\x18\t \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcc\x01\n\x0c\x43odePipeline\x12J\n\x12\x63ustom_action_type\x18\x01 \x03(\x0b\x32..oak9.tython.aws.codepipeline.CustomActionType\x12\x38\n\x08pipeline\x18\x02 \x03(\x0b\x32&.oak9.tython.aws.codepipeline.Pipeline\x12\x36\n\x07webhook\x18\x03 \x03(\x0b\x32%.oak9.tython.aws.codepipeline.Webhook\"\\\n\x15PipelineEncryptionKey\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\n\n\x02id\x18\x02 \x01(\t\"\xaf\x01\n\x15PipelineArtifactStore\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\x0e\x65ncryption_key\x18\x02 \x01(\x0b\x32\x33.oak9.tython.aws.codepipeline.PipelineEncryptionKey\x12\x10\n\x08location\x18\x03 \x01(\t\"\xb0\x01\n\x18PipelineArtifactStoreMap\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\x0e\x61rtifact_store\x18\x02 \x01(\x0b\x32\x33.oak9.tython.aws.codepipeline.PipelineArtifactStore\x12\x0e\n\x06region\x18\x03 \x01(\t\"v\n\x17PipelineStageTransition\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x12\n\nstage_name\x18\x03 \x01(\t\"\x93\x01\n\x14PipelineActionTypeId\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"^\n\x15PipelineInputArtifact\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\"_\n\x16PipelineOutputArtifact\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xad\x04\n\x19PipelineActionDeclaration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12J\n\x0e\x61\x63tion_type_id\x18\x02 \x01(\x0b\x32\x32.oak9.tython.aws.codepipeline.PipelineActionTypeId\x12\x61\n\rconfiguration\x18\x03 \x03(\x0b\x32J.oak9.tython.aws.codepipeline.PipelineActionDeclaration.ConfigurationEntry\x12L\n\x0finput_artifacts\x18\x04 \x03(\x0b\x32\x33.oak9.tython.aws.codepipeline.PipelineInputArtifact\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\tnamespace\x18\x06 \x01(\t\x12N\n\x10output_artifacts\x18\x07 \x03(\x0b\x32\x34.oak9.tython.aws.codepipeline.PipelineOutputArtifact\x12\x0e\n\x06region\x18\x08 \x01(\t\x12\x10\n\x08role_arn\x18\t \x01(\t\x12\x11\n\trun_order\x18\n \x01(\x05\x1a\x34\n\x12\x43onfigurationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"c\n\x1aPipelineBlockerDeclaration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xf7\x01\n\x18PipelineStageDeclaration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12H\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x37.oak9.tython.aws.codepipeline.PipelineActionDeclaration\x12J\n\x08\x62lockers\x18\x03 \x03(\x0b\x32\x38.oak9.tython.aws.codepipeline.PipelineBlockerDeclaration\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xbd\x04\n\x08Pipeline\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\x0e\x61rtifact_store\x18\x02 \x01(\x0b\x32\x33.oak9.tython.aws.codepipeline.PipelineArtifactStore\x12O\n\x0f\x61rtifact_stores\x18\x03 \x03(\x0b\x32\x36.oak9.tython.aws.codepipeline.PipelineArtifactStoreMap\x12`\n!disable_inbound_stage_transitions\x18\x04 \x03(\x0b\x32\x35.oak9.tython.aws.codepipeline.PipelineStageTransition\x12\x0c\n\x04name\x18\x05 \x01(\t\x12#\n\x1brestart_execution_on_update\x18\x06 \x01(\x08\x12\x10\n\x08role_arn\x18\x07 \x01(\t\x12\x46\n\x06stages\x18\x08 \x03(\x0b\x32\x36.oak9.tython.aws.codepipeline.PipelineStageDeclaration\x12>\n\x04tags\x18\t \x03(\x0b\x32\x30.oak9.tython.aws.codepipeline.Pipeline.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8a\x01\n\x1fWebhookWebhookAuthConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x61llowed_ip_range\x18\x02 \x01(\t\x12\x14\n\x0csecret_token\x18\x03 \x01(\t\"|\n\x18WebhookWebhookFilterRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tjson_path\x18\x02 \x01(\t\x12\x14\n\x0cmatch_equals\x18\x03 \x01(\t\"\x8a\x03\n\x07Webhook\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x63\n\x1c\x61uthentication_configuration\x18\x02 \x01(\x0b\x32=.oak9.tython.aws.codepipeline.WebhookWebhookAuthConfiguration\x12G\n\x07\x66ilters\x18\x03 \x03(\x0b\x32\x36.oak9.tython.aws.codepipeline.WebhookWebhookFilterRule\x12\x16\n\x0e\x61uthentication\x18\x04 \x01(\t\x12\x17\n\x0ftarget_pipeline\x18\x05 \x01(\t\x12\x15\n\rtarget_action\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x1f\n\x17target_pipeline_version\x18\x08 \x01(\x05\x12!\n\x19register_with_third_party\x18\t \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_codepipeline_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUSTOMACTIONTYPE_TAGSENTRY._options = None
  _CUSTOMACTIONTYPE_TAGSENTRY._serialized_options = b'8\001'
  _PIPELINEACTIONDECLARATION_CONFIGURATIONENTRY._options = None
  _PIPELINEACTIONDECLARATION_CONFIGURATIONENTRY._serialized_options = b'8\001'
  _PIPELINE_TAGSENTRY._options = None
  _PIPELINE_TAGSENTRY._serialized_options = b'8\001'
  _CUSTOMACTIONTYPECONFIGURATIONPROPERTIES._serialized_start=82
  _CUSTOMACTIONTYPECONFIGURATIONPROPERTIES._serialized_end=281
  _CUSTOMACTIONTYPEARTIFACTDETAILS._serialized_start=284
  _CUSTOMACTIONTYPEARTIFACTDETAILS._serialized_end=420
  _CUSTOMACTIONTYPESETTINGS._serialized_start=423
  _CUSTOMACTIONTYPESETTINGS._serialized_end=637
  _CUSTOMACTIONTYPE._serialized_start=640
  _CUSTOMACTIONTYPE._serialized_end=1255
  _CUSTOMACTIONTYPE_TAGSENTRY._serialized_start=1212
  _CUSTOMACTIONTYPE_TAGSENTRY._serialized_end=1255
  _CODEPIPELINE._serialized_start=1258
  _CODEPIPELINE._serialized_end=1462
  _PIPELINEENCRYPTIONKEY._serialized_start=1464
  _PIPELINEENCRYPTIONKEY._serialized_end=1556
  _PIPELINEARTIFACTSTORE._serialized_start=1559
  _PIPELINEARTIFACTSTORE._serialized_end=1734
  _PIPELINEARTIFACTSTOREMAP._serialized_start=1737
  _PIPELINEARTIFACTSTOREMAP._serialized_end=1913
  _PIPELINESTAGETRANSITION._serialized_start=1915
  _PIPELINESTAGETRANSITION._serialized_end=2033
  _PIPELINEACTIONTYPEID._serialized_start=2036
  _PIPELINEACTIONTYPEID._serialized_end=2183
  _PIPELINEINPUTARTIFACT._serialized_start=2185
  _PIPELINEINPUTARTIFACT._serialized_end=2279
  _PIPELINEOUTPUTARTIFACT._serialized_start=2281
  _PIPELINEOUTPUTARTIFACT._serialized_end=2376
  _PIPELINEACTIONDECLARATION._serialized_start=2379
  _PIPELINEACTIONDECLARATION._serialized_end=2936
  _PIPELINEACTIONDECLARATION_CONFIGURATIONENTRY._serialized_start=2884
  _PIPELINEACTIONDECLARATION_CONFIGURATIONENTRY._serialized_end=2936
  _PIPELINEBLOCKERDECLARATION._serialized_start=2938
  _PIPELINEBLOCKERDECLARATION._serialized_end=3037
  _PIPELINESTAGEDECLARATION._serialized_start=3040
  _PIPELINESTAGEDECLARATION._serialized_end=3287
  _PIPELINE._serialized_start=3290
  _PIPELINE._serialized_end=3863
  _PIPELINE_TAGSENTRY._serialized_start=1212
  _PIPELINE_TAGSENTRY._serialized_end=1255
  _WEBHOOKWEBHOOKAUTHCONFIGURATION._serialized_start=3866
  _WEBHOOKWEBHOOKAUTHCONFIGURATION._serialized_end=4004
  _WEBHOOKWEBHOOKFILTERRULE._serialized_start=4006
  _WEBHOOKWEBHOOKFILTERRULE._serialized_end=4130
  _WEBHOOK._serialized_start=4133
  _WEBHOOK._serialized_end=4527
# @@protoc_insertion_point(module_scope)
