# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_artifact.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gcp/gcp_artifact.proto\x12\x18oak9.tython.gcp.artifact\x1a\x13shared/shared.proto\"c\n&ArtifactRegistryRepositoryXMavenConfig\x12!\n\x19\x61llow_snapshot_overwrites\x18\x01 \x01(\x08\x12\x16\n\x0eversion_policy\x18\x02 \x01(\t\"U\n#ArtifactRegistryRepositoryXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xb8\x04\n\x1a\x41rtifactRegistryRepository\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x14\n\x0ckms_key_name\x18\x05 \x01(\t\x12P\n\x06labels\x18\x06 \x03(\x0b\x32@.oak9.tython.gcp.artifact.ArtifactRegistryRepository.LabelsEntry\x12\x10\n\x08location\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12\x15\n\rrepository_id\x18\n \x01(\t\x12\x13\n\x0bupdate_time\x18\x0b \x01(\t\x12V\n\x0cmaven_config\x18\x0c \x01(\x0b\x32@.oak9.tython.gcp.artifact.ArtifactRegistryRepositoryXMavenConfig\x12O\n\x08timeouts\x18\r \x01(\x0b\x32=.oak9.tython.gcp.artifact.ArtifactRegistryRepositoryXTimeouts\x12\x37\n\rresource_info\x18\x0e \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n.ArtifactRegistryRepositoryIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xac\x02\n$ArtifactRegistryRepositoryIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x12\n\nrepository\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12[\n\tcondition\x18\x08 \x01(\x0b\x32H.oak9.tython.gcp.artifact.ArtifactRegistryRepositoryIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"g\n-ArtifactRegistryRepositoryIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xa9\x02\n#ArtifactRegistryRepositoryIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x12\n\nrepository\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12Z\n\tcondition\x18\x08 \x01(\x0b\x32G.oak9.tython.gcp.artifact.ArtifactRegistryRepositoryIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xc4\x01\n#ArtifactRegistryRepositoryIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x12\n\nrepository\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_artifact_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ARTIFACTREGISTRYREPOSITORY_LABELSENTRY._options = None
  _ARTIFACTREGISTRYREPOSITORY_LABELSENTRY._serialized_options = b'8\001'
  _ARTIFACTREGISTRYREPOSITORYXMAVENCONFIG._serialized_start=73
  _ARTIFACTREGISTRYREPOSITORYXMAVENCONFIG._serialized_end=172
  _ARTIFACTREGISTRYREPOSITORYXTIMEOUTS._serialized_start=174
  _ARTIFACTREGISTRYREPOSITORYXTIMEOUTS._serialized_end=259
  _ARTIFACTREGISTRYREPOSITORY._serialized_start=262
  _ARTIFACTREGISTRYREPOSITORY._serialized_end=830
  _ARTIFACTREGISTRYREPOSITORY_LABELSENTRY._serialized_start=785
  _ARTIFACTREGISTRYREPOSITORY_LABELSENTRY._serialized_end=830
  _ARTIFACTREGISTRYREPOSITORYIAMBINDINGXCONDITION._serialized_start=832
  _ARTIFACTREGISTRYREPOSITORYIAMBINDINGXCONDITION._serialized_end=936
  _ARTIFACTREGISTRYREPOSITORYIAMBINDING._serialized_start=939
  _ARTIFACTREGISTRYREPOSITORYIAMBINDING._serialized_end=1239
  _ARTIFACTREGISTRYREPOSITORYIAMMEMBERXCONDITION._serialized_start=1241
  _ARTIFACTREGISTRYREPOSITORYIAMMEMBERXCONDITION._serialized_end=1344
  _ARTIFACTREGISTRYREPOSITORYIAMMEMBER._serialized_start=1347
  _ARTIFACTREGISTRYREPOSITORYIAMMEMBER._serialized_end=1644
  _ARTIFACTREGISTRYREPOSITORYIAMPOLICY._serialized_start=1647
  _ARTIFACTREGISTRYREPOSITORYIAMPOLICY._serialized_end=1843
# @@protoc_insertion_point(module_scope)
