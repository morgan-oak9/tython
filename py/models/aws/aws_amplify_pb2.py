# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_amplify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ws/aws_amplify.proto\x12\x17oak9.tython.aws.amplify\x1a\x13shared/shared.proto\"n\n\x16\x41ppEnvironmentVariable\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x8c\x01\n\x12\x41ppBasicAuthConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x19\n\x11\x65nable_basic_auth\x18\x03 \x01(\x08\x12\x10\n\x08password\x18\x04 \x01(\t\"\xe5\x03\n\x1b\x41ppAutoBranchCreationConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12N\n\x15\x65nvironment_variables\x18\x02 \x03(\x0b\x32/.oak9.tython.aws.amplify.AppEnvironmentVariable\x12#\n\x1b\x65nable_auto_branch_creation\x18\x03 \x01(\x08\x12%\n\x1dpull_request_environment_name\x18\x04 \x01(\t\x12%\n\x1d\x61uto_branch_creation_patterns\x18\x05 \x03(\t\x12#\n\x1b\x65nable_pull_request_preview\x18\x06 \x01(\x08\x12\x19\n\x11\x65nable_auto_build\x18\x07 \x01(\x08\x12\x1f\n\x17\x65nable_performance_mode\x18\x08 \x01(\x08\x12\x12\n\nbuild_spec\x18\t \x01(\t\x12\r\n\x05stage\x18\n \x01(\t\x12\x46\n\x11\x62\x61sic_auth_config\x18\x0b \x01(\x0b\x32+.oak9.tython.aws.amplify.AppBasicAuthConfig\"\x8b\x01\n\rAppCustomRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tcondition\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\"\x87\x05\n\x03\x41pp\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12Y\n\x1b\x61uto_branch_creation_config\x18\x02 \x01(\x0b\x32\x34.oak9.tython.aws.amplify.AppAutoBranchCreationConfig\x12\x13\n\x0boauth_token\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12#\n\x1b\x65nable_branch_auto_deletion\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x12\n\nrepository\x18\x07 \x01(\t\x12N\n\x15\x65nvironment_variables\x18\x08 \x03(\x0b\x32/.oak9.tython.aws.amplify.AppEnvironmentVariable\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\t \x01(\t\x12\x12\n\nbuild_spec\x18\n \x01(\t\x12<\n\x0c\x63ustom_rules\x18\x0b \x03(\x0b\x32&.oak9.tython.aws.amplify.AppCustomRule\x12\x46\n\x11\x62\x61sic_auth_config\x18\x0c \x01(\x0b\x32+.oak9.tython.aws.amplify.AppBasicAuthConfig\x12\x34\n\x04tags\x18\r \x03(\x0b\x32&.oak9.tython.aws.amplify.App.TagsEntry\x12\x18\n\x10iam_service_role\x18\x0e \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x96\x01\n\x07\x41mplify\x12)\n\x03\x61pp\x18\x01 \x03(\x0b\x32\x1c.oak9.tython.aws.amplify.App\x12/\n\x06\x62ranch\x18\x02 \x03(\x0b\x32\x1f.oak9.tython.aws.amplify.Branch\x12/\n\x06\x64omain\x18\x03 \x03(\x0b\x32\x1f.oak9.tython.aws.amplify.Domain\"q\n\x19\x42ranchEnvironmentVariable\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x8f\x01\n\x15\x42ranchBasicAuthConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x19\n\x11\x65nable_basic_auth\x18\x03 \x01(\x08\x12\x10\n\x08password\x18\x04 \x01(\t\"\xaa\x04\n\x06\x42ranch\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12Q\n\x15\x65nvironment_variables\x18\x03 \x03(\x0b\x32\x32.oak9.tython.aws.amplify.BranchEnvironmentVariable\x12\x0e\n\x06\x61pp_id\x18\x04 \x01(\t\x12%\n\x1dpull_request_environment_name\x18\x05 \x01(\t\x12#\n\x1b\x65nable_pull_request_preview\x18\x06 \x01(\x08\x12\x19\n\x11\x65nable_auto_build\x18\x07 \x01(\x08\x12\x1f\n\x17\x65nable_performance_mode\x18\x08 \x01(\x08\x12\x12\n\nbuild_spec\x18\t \x01(\t\x12\r\n\x05stage\x18\n \x01(\t\x12\x13\n\x0b\x62ranch_name\x18\x0b \x01(\t\x12I\n\x11\x62\x61sic_auth_config\x18\x0c \x01(\x0b\x32..oak9.tython.aws.amplify.BranchBasicAuthConfig\x12\x37\n\x04tags\x18\r \x03(\x0b\x32).oak9.tython.aws.amplify.Branch.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"v\n\x16\x44omainSubDomainSetting\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06prefix\x18\x02 \x01(\t\x12\x13\n\x0b\x62ranch_name\x18\x03 \x01(\t\"\xa1\x02\n\x06\x44omain\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12L\n\x13sub_domain_settings\x18\x02 \x03(\x0b\x32/.oak9.tython.aws.amplify.DomainSubDomainSetting\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\t\x12 \n\x18\x61uto_sub_domain_iam_role\x18\x04 \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x05 \x01(\t\x12\x1e\n\x16\x65nable_auto_sub_domain\x18\x06 \x01(\x08\x12)\n!auto_sub_domain_creation_patterns\x18\x07 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_amplify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APP_TAGSENTRY._options = None
  _APP_TAGSENTRY._serialized_options = b'8\001'
  _BRANCH_TAGSENTRY._options = None
  _BRANCH_TAGSENTRY._serialized_options = b'8\001'
  _APPENVIRONMENTVARIABLE._serialized_start=71
  _APPENVIRONMENTVARIABLE._serialized_end=181
  _APPBASICAUTHCONFIG._serialized_start=184
  _APPBASICAUTHCONFIG._serialized_end=324
  _APPAUTOBRANCHCREATIONCONFIG._serialized_start=327
  _APPAUTOBRANCHCREATIONCONFIG._serialized_end=812
  _APPCUSTOMRULE._serialized_start=815
  _APPCUSTOMRULE._serialized_end=954
  _APP._serialized_start=957
  _APP._serialized_end=1604
  _APP_TAGSENTRY._serialized_start=1561
  _APP_TAGSENTRY._serialized_end=1604
  _AMPLIFY._serialized_start=1607
  _AMPLIFY._serialized_end=1757
  _BRANCHENVIRONMENTVARIABLE._serialized_start=1759
  _BRANCHENVIRONMENTVARIABLE._serialized_end=1872
  _BRANCHBASICAUTHCONFIG._serialized_start=1875
  _BRANCHBASICAUTHCONFIG._serialized_end=2018
  _BRANCH._serialized_start=2021
  _BRANCH._serialized_end=2575
  _BRANCH_TAGSENTRY._serialized_start=1561
  _BRANCH_TAGSENTRY._serialized_end=1604
  _DOMAINSUBDOMAINSETTING._serialized_start=2577
  _DOMAINSUBDOMAINSETTING._serialized_end=2695
  _DOMAIN._serialized_start=2698
  _DOMAIN._serialized_end=2987
# @@protoc_insertion_point(module_scope)
