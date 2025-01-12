# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_neptune.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ws/aws_neptune.proto\x12\x17oak9.tython.aws.neptune\x1a\x13shared/shared.proto\"y\n\x16\x44\x42\x43lusterDBClusterRole\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08role_arn\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\"\xcc\x06\n\tDBCluster\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11storage_encrypted\x18\x02 \x01(\x08\x12\x17\n\x0frestore_to_time\x18\x03 \x01(\t\x12\x16\n\x0e\x65ngine_version\x18\x04 \x01(\t\x12\x12\n\nkms_key_id\x18\x05 \x01(\t\x12I\n\x10\x61ssociated_roles\x18\x06 \x03(\x0b\x32/.oak9.tython.aws.neptune.DBClusterDBClusterRole\x12\x1a\n\x12\x61vailability_zones\x18\x07 \x03(\t\x12\x1b\n\x13snapshot_identifier\x18\x08 \x01(\t\x12\x0c\n\x04port\x18\t \x01(\x05\x12\x1d\n\x15\x64\x62_cluster_identifier\x18\n \x01(\t\x12$\n\x1cpreferred_maintenance_window\x18\x0b \x01(\t\x12\x18\n\x10iam_auth_enabled\x18\x0c \x01(\x08\x12\x1c\n\x14\x64\x62_subnet_group_name\x18\r \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x0e \x01(\x08\x12\x1f\n\x17preferred_backup_window\x18\x0f \x01(\t\x12\"\n\x1ause_latest_restorable_time\x18\x10 \x01(\x08\x12\x1e\n\x16vpc_security_group_ids\x18\x11 \x03(\t\x12$\n\x1csource_db_cluster_identifier\x18\x12 \x01(\t\x12\'\n\x1f\x64\x62_cluster_parameter_group_name\x18\x13 \x01(\t\x12\x1f\n\x17\x62\x61\x63kup_retention_period\x18\x14 \x01(\x05\x12\x14\n\x0crestore_type\x18\x15 \x01(\t\x12:\n\x04tags\x18\x16 \x03(\x0b\x32,.oak9.tython.aws.neptune.DBCluster.TagsEntry\x12&\n\x1e\x65nable_cloudwatch_logs_exports\x18\x17 \x03(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd9\x02\n\x07Neptune\x12\x36\n\ndb_cluster\x18\x01 \x03(\x0b\x32\".oak9.tython.aws.neptune.DBCluster\x12T\n\x1a\x64\x62_cluster_parameter_group\x18\x02 \x03(\x0b\x32\x30.oak9.tython.aws.neptune.DBClusterParameterGroup\x12\x38\n\x0b\x64\x62_instance\x18\x03 \x03(\x0b\x32#.oak9.tython.aws.neptune.DBInstance\x12\x45\n\x12\x64\x62_parameter_group\x18\x04 \x03(\x0b\x32).oak9.tython.aws.neptune.DBParameterGroup\x12?\n\x0f\x64\x62_subnet_group\x18\x05 \x03(\x0b\x32&.oak9.tython.aws.neptune.DBSubnetGroup\"\x85\x03\n\x17\x44\x42\x43lusterParameterGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12T\n\nparameters\x18\x03 \x03(\x0b\x32@.oak9.tython.aws.neptune.DBClusterParameterGroup.ParametersEntry\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12H\n\x04tags\x18\x05 \x03(\x0b\x32:.oak9.tython.aws.neptune.DBClusterParameterGroup.TagsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf2\x03\n\nDBInstance\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x64\x62_parameter_group_name\x18\x02 \x01(\t\x12\x19\n\x11\x64\x62_instance_class\x18\x03 \x01(\t\x12#\n\x1b\x61llow_major_version_upgrade\x18\x04 \x01(\x08\x12\x1d\n\x15\x64\x62_cluster_identifier\x18\x05 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x06 \x01(\t\x12$\n\x1cpreferred_maintenance_window\x18\x07 \x01(\t\x12\"\n\x1a\x61uto_minor_version_upgrade\x18\x08 \x01(\x08\x12\x1c\n\x14\x64\x62_subnet_group_name\x18\t \x01(\t\x12\x1e\n\x16\x64\x62_instance_identifier\x18\n \x01(\t\x12\x1e\n\x16\x64\x62_snapshot_identifier\x18\x0b \x01(\t\x12;\n\x04tags\x18\x0c \x03(\x0b\x32-.oak9.tython.aws.neptune.DBInstance.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf0\x02\n\x10\x44\x42ParameterGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12M\n\nparameters\x18\x03 \x03(\x0b\x32\x39.oak9.tython.aws.neptune.DBParameterGroup.ParametersEntry\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x41\n\x04tags\x18\x05 \x03(\x0b\x32\x33.oak9.tython.aws.neptune.DBParameterGroup.TagsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x02\n\rDBSubnetGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1c\n\x14\x64\x62_subnet_group_name\x18\x02 \x01(\t\x12#\n\x1b\x64\x62_subnet_group_description\x18\x03 \x01(\t\x12\x12\n\nsubnet_ids\x18\x04 \x03(\t\x12>\n\x04tags\x18\x05 \x03(\x0b\x32\x30.oak9.tython.aws.neptune.DBSubnetGroup.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_neptune_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DBCLUSTER_TAGSENTRY._options = None
  _DBCLUSTER_TAGSENTRY._serialized_options = b'8\001'
  _DBCLUSTERPARAMETERGROUP_PARAMETERSENTRY._options = None
  _DBCLUSTERPARAMETERGROUP_PARAMETERSENTRY._serialized_options = b'8\001'
  _DBCLUSTERPARAMETERGROUP_TAGSENTRY._options = None
  _DBCLUSTERPARAMETERGROUP_TAGSENTRY._serialized_options = b'8\001'
  _DBINSTANCE_TAGSENTRY._options = None
  _DBINSTANCE_TAGSENTRY._serialized_options = b'8\001'
  _DBPARAMETERGROUP_PARAMETERSENTRY._options = None
  _DBPARAMETERGROUP_PARAMETERSENTRY._serialized_options = b'8\001'
  _DBPARAMETERGROUP_TAGSENTRY._options = None
  _DBPARAMETERGROUP_TAGSENTRY._serialized_options = b'8\001'
  _DBSUBNETGROUP_TAGSENTRY._options = None
  _DBSUBNETGROUP_TAGSENTRY._serialized_options = b'8\001'
  _DBCLUSTERDBCLUSTERROLE._serialized_start=71
  _DBCLUSTERDBCLUSTERROLE._serialized_end=192
  _DBCLUSTER._serialized_start=195
  _DBCLUSTER._serialized_end=1039
  _DBCLUSTER_TAGSENTRY._serialized_start=996
  _DBCLUSTER_TAGSENTRY._serialized_end=1039
  _NEPTUNE._serialized_start=1042
  _NEPTUNE._serialized_end=1387
  _DBCLUSTERPARAMETERGROUP._serialized_start=1390
  _DBCLUSTERPARAMETERGROUP._serialized_end=1779
  _DBCLUSTERPARAMETERGROUP_PARAMETERSENTRY._serialized_start=1685
  _DBCLUSTERPARAMETERGROUP_PARAMETERSENTRY._serialized_end=1734
  _DBCLUSTERPARAMETERGROUP_TAGSENTRY._serialized_start=996
  _DBCLUSTERPARAMETERGROUP_TAGSENTRY._serialized_end=1039
  _DBINSTANCE._serialized_start=1782
  _DBINSTANCE._serialized_end=2280
  _DBINSTANCE_TAGSENTRY._serialized_start=996
  _DBINSTANCE_TAGSENTRY._serialized_end=1039
  _DBPARAMETERGROUP._serialized_start=2283
  _DBPARAMETERGROUP._serialized_end=2651
  _DBPARAMETERGROUP_PARAMETERSENTRY._serialized_start=1685
  _DBPARAMETERGROUP_PARAMETERSENTRY._serialized_end=1734
  _DBPARAMETERGROUP_TAGSENTRY._serialized_start=996
  _DBPARAMETERGROUP_TAGSENTRY._serialized_end=1039
  _DBSUBNETGROUP._serialized_start=2654
  _DBSUBNETGROUP._serialized_end=2922
  _DBSUBNETGROUP_TAGSENTRY._serialized_start=996
  _DBSUBNETGROUP_TAGSENTRY._serialized_end=1039
# @@protoc_insertion_point(module_scope)
