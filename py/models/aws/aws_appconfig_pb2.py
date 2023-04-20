# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_appconfig.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61ws/aws_appconfig.proto\x12\x19oak9.tython.aws.appconfig\x1a\x13shared/shared.proto\"f\n\x0f\x41pplicationTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xa3\x01\n\x0b\x41pplication\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x38\n\x04tags\x18\x03 \x03(\x0b\x32*.oak9.tython.aws.appconfig.ApplicationTags\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xb9\x03\n\tAppConfig\x12;\n\x0b\x61pplication\x18\x01 \x03(\x0b\x32&.oak9.tython.aws.appconfig.Application\x12N\n\x15\x63onfiguration_profile\x18\x02 \x03(\x0b\x32/.oak9.tython.aws.appconfig.ConfigurationProfile\x12\x39\n\ndeployment\x18\x03 \x03(\x0b\x32%.oak9.tython.aws.appconfig.Deployment\x12J\n\x13\x64\x65ployment_strategy\x18\x04 \x03(\x0b\x32-.oak9.tython.aws.appconfig.DeploymentStrategy\x12;\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32&.oak9.tython.aws.appconfig.Environment\x12[\n\x1chosted_configuration_version\x18\x06 \x03(\x0b\x32\x35.oak9.tython.aws.appconfig.HostedConfigurationVersion\"j\n\x1e\x43onfigurationProfileValidators\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"o\n\x18\x43onfigurationProfileTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xce\x02\n\x14\x43onfigurationProfile\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0clocation_uri\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12M\n\nvalidators\x18\x04 \x03(\x0b\x32\x39.oak9.tython.aws.appconfig.ConfigurationProfileValidators\x12\x1a\n\x12retrieval_role_arn\x18\x05 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x06 \x01(\t\x12\x41\n\x04tags\x18\x07 \x03(\x0b\x32\x33.oak9.tython.aws.appconfig.ConfigurationProfileTags\x12\x0c\n\x04name\x18\x08 \x01(\t\"e\n\x0e\x44\x65ploymentTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xa4\x02\n\nDeployment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16\x64\x65ployment_strategy_id\x18\x02 \x01(\t\x12 \n\x18\x63onfiguration_profile_id\x18\x03 \x01(\t\x12\x16\n\x0e\x65nvironment_id\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x1d\n\x15\x63onfiguration_version\x18\x06 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x07 \x01(\t\x12\x37\n\x04tags\x18\x08 \x03(\x0b\x32).oak9.tython.aws.appconfig.DeploymentTags\"m\n\x16\x44\x65ploymentStrategyTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xbf\x02\n\x12\x44\x65ploymentStrategy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0creplicate_to\x18\x02 \x01(\t\x12\x13\n\x0bgrowth_type\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12&\n\x1e\x64\x65ployment_duration_in_minutes\x18\x05 \x01(\x01\x12\x15\n\rgrowth_factor\x18\x06 \x01(\x01\x12\"\n\x1a\x66inal_bake_time_in_minutes\x18\x07 \x01(\x01\x12?\n\x04tags\x18\x08 \x03(\x0b\x32\x31.oak9.tython.aws.appconfig.DeploymentStrategyTags\x12\x0c\n\x04name\x18\t \x01(\t\"y\n\x13\x45nvironmentMonitors\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\talarm_arn\x18\x02 \x01(\t\x12\x16\n\x0e\x61larm_role_arn\x18\x03 \x01(\t\"f\n\x0f\x45nvironmentTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"\xfd\x01\n\x0b\x45nvironment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12@\n\x08monitors\x18\x03 \x03(\x0b\x32..oak9.tython.aws.appconfig.EnvironmentMonitors\x12\x16\n\x0e\x61pplication_id\x18\x04 \x01(\t\x12\x38\n\x04tags\x18\x05 \x03(\x0b\x32*.oak9.tython.aws.appconfig.EnvironmentTags\x12\x0c\n\x04name\x18\x06 \x01(\t\"\xea\x01\n\x1aHostedConfigurationVersion\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12 \n\x18\x63onfiguration_profile_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\t\x12\x1d\n\x15latest_version_number\x18\x05 \x01(\x01\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x07 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_appconfig_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APPLICATIONTAGS._serialized_start=75
  _APPLICATIONTAGS._serialized_end=177
  _APPLICATION._serialized_start=180
  _APPLICATION._serialized_end=343
  _APPCONFIG._serialized_start=346
  _APPCONFIG._serialized_end=787
  _CONFIGURATIONPROFILEVALIDATORS._serialized_start=789
  _CONFIGURATIONPROFILEVALIDATORS._serialized_end=895
  _CONFIGURATIONPROFILETAGS._serialized_start=897
  _CONFIGURATIONPROFILETAGS._serialized_end=1008
  _CONFIGURATIONPROFILE._serialized_start=1011
  _CONFIGURATIONPROFILE._serialized_end=1345
  _DEPLOYMENTTAGS._serialized_start=1347
  _DEPLOYMENTTAGS._serialized_end=1448
  _DEPLOYMENT._serialized_start=1451
  _DEPLOYMENT._serialized_end=1743
  _DEPLOYMENTSTRATEGYTAGS._serialized_start=1745
  _DEPLOYMENTSTRATEGYTAGS._serialized_end=1854
  _DEPLOYMENTSTRATEGY._serialized_start=1857
  _DEPLOYMENTSTRATEGY._serialized_end=2176
  _ENVIRONMENTMONITORS._serialized_start=2178
  _ENVIRONMENTMONITORS._serialized_end=2299
  _ENVIRONMENTTAGS._serialized_start=2301
  _ENVIRONMENTTAGS._serialized_end=2403
  _ENVIRONMENT._serialized_start=2406
  _ENVIRONMENT._serialized_end=2659
  _HOSTEDCONFIGURATIONVERSION._serialized_start=2662
  _HOSTEDCONFIGURATIONVERSION._serialized_end=2896
# @@protoc_insertion_point(module_scope)
