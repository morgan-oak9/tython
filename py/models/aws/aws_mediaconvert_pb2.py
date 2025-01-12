# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_mediaconvert.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61ws/aws_mediaconvert.proto\x12\x1coak9.tython.aws.mediaconvert\x1a\x13shared/shared.proto\"h\n\x1fJobTemplateAccelerationSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04mode\x18\x02 \x01(\t\"\x8b\x01\n\x19JobTemplateHopDestination\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cwait_minutes\x18\x02 \x01(\x05\x12\x10\n\x08priority\x18\x03 \x01(\x05\x12\r\n\x05queue\x18\x04 \x01(\t\"\xe6\x04\n\x0bJobTemplate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\\\n\x15\x61\x63\x63\x65leration_settings\x18\x04 \x01(\x0b\x32=.oak9.tython.aws.mediaconvert.JobTemplateAccelerationSettings\x12\x10\n\x08priority\x18\x05 \x01(\x05\x12\x1e\n\x16status_update_interval\x18\x06 \x01(\t\x12R\n\rsettings_json\x18\x07 \x03(\x0b\x32;.oak9.tython.aws.mediaconvert.JobTemplate.SettingsJsonEntry\x12\r\n\x05queue\x18\x08 \x01(\t\x12Q\n\x10hop_destinations\x18\t \x03(\x0b\x32\x37.oak9.tython.aws.mediaconvert.JobTemplateHopDestination\x12\x41\n\x04tags\x18\n \x03(\x0b\x32\x33.oak9.tython.aws.mediaconvert.JobTemplate.TagsEntry\x12\x0c\n\x04name\x18\x0b \x01(\t\x1a\x33\n\x11SettingsJsonEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb9\x01\n\x0cMediaConvert\x12?\n\x0cjob_template\x18\x01 \x03(\x0b\x32).oak9.tython.aws.mediaconvert.JobTemplate\x12\x34\n\x06preset\x18\x02 \x03(\x0b\x32$.oak9.tython.aws.mediaconvert.Preset\x12\x32\n\x05queue\x18\x03 \x03(\x0b\x32#.oak9.tython.aws.mediaconvert.Queue\"\xe5\x02\n\x06Preset\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12M\n\rsettings_json\x18\x04 \x03(\x0b\x32\x36.oak9.tython.aws.mediaconvert.Preset.SettingsJsonEntry\x12<\n\x04tags\x18\x05 \x03(\x0b\x32..oak9.tython.aws.mediaconvert.Preset.TagsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x1a\x33\n\x11SettingsJsonEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf3\x01\n\x05Queue\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cpricing_plan\x18\x04 \x01(\t\x12;\n\x04tags\x18\x05 \x03(\x0b\x32-.oak9.tython.aws.mediaconvert.Queue.TagsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_mediaconvert_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JOBTEMPLATE_SETTINGSJSONENTRY._options = None
  _JOBTEMPLATE_SETTINGSJSONENTRY._serialized_options = b'8\001'
  _JOBTEMPLATE_TAGSENTRY._options = None
  _JOBTEMPLATE_TAGSENTRY._serialized_options = b'8\001'
  _PRESET_SETTINGSJSONENTRY._options = None
  _PRESET_SETTINGSJSONENTRY._serialized_options = b'8\001'
  _PRESET_TAGSENTRY._options = None
  _PRESET_TAGSENTRY._serialized_options = b'8\001'
  _QUEUE_TAGSENTRY._options = None
  _QUEUE_TAGSENTRY._serialized_options = b'8\001'
  _JOBTEMPLATEACCELERATIONSETTINGS._serialized_start=81
  _JOBTEMPLATEACCELERATIONSETTINGS._serialized_end=185
  _JOBTEMPLATEHOPDESTINATION._serialized_start=188
  _JOBTEMPLATEHOPDESTINATION._serialized_end=327
  _JOBTEMPLATE._serialized_start=330
  _JOBTEMPLATE._serialized_end=944
  _JOBTEMPLATE_SETTINGSJSONENTRY._serialized_start=848
  _JOBTEMPLATE_SETTINGSJSONENTRY._serialized_end=899
  _JOBTEMPLATE_TAGSENTRY._serialized_start=901
  _JOBTEMPLATE_TAGSENTRY._serialized_end=944
  _MEDIACONVERT._serialized_start=947
  _MEDIACONVERT._serialized_end=1132
  _PRESET._serialized_start=1135
  _PRESET._serialized_end=1492
  _PRESET_SETTINGSJSONENTRY._serialized_start=848
  _PRESET_SETTINGSJSONENTRY._serialized_end=899
  _PRESET_TAGSENTRY._serialized_start=901
  _PRESET_TAGSENTRY._serialized_end=944
  _QUEUE._serialized_start=1495
  _QUEUE._serialized_end=1738
  _QUEUE_TAGSENTRY._serialized_start=901
  _QUEUE_TAGSENTRY._serialized_end=944
# @@protoc_insertion_point(module_scope)
