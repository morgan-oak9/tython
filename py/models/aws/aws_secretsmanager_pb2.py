# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_secretsmanager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61ws/aws_secretsmanager.proto\x12\x1eoak9.tython.aws.secretsmanager\x1a\x13shared/shared.proto\"u\n\x0eResourcePolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x17\n\x0fresource_policy\x18\x03 \x01(\t\"\xb8\x02\n\x0eSecretsManager\x12G\n\x0fresource_policy\x18\x01 \x01(\x0b\x32..oak9.tython.aws.secretsmanager.ResourcePolicy\x12K\n\x11rotation_schedule\x18\x02 \x01(\x0b\x32\x30.oak9.tython.aws.secretsmanager.RotationSchedule\x12\x36\n\x06secret\x18\x03 \x01(\x0b\x32&.oak9.tython.aws.secretsmanager.Secret\x12X\n\x18secret_target_attachment\x18\x04 \x03(\x0b\x32\x36.oak9.tython.aws.secretsmanager.SecretTargetAttachment\"\x9f\x02\n$RotationScheduleHostedRotationLambda\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rrotation_type\x18\x02 \x01(\t\x12\x1c\n\x14rotation_lambda_name\x18\x03 \x01(\t\x12\x13\n\x0bkms_key_arn\x18\x04 \x01(\t\x12\x19\n\x11master_secret_arn\x18\x05 \x01(\t\x12\x1e\n\x16vpc_security_group_ids\x18\x06 \x01(\t\x12!\n\x19master_secret_kms_key_arn\x18\x07 \x01(\t\x12\x16\n\x0evpc_subnet_ids\x18\x08 \x01(\t\"z\n\x1dRotationScheduleRotationRules\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12 \n\x18\x61utomatically_after_days\x18\x02 \x01(\x05\"\xb8\x02\n\x10RotationSchedule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x64\n\x16hosted_rotation_lambda\x18\x03 \x01(\x0b\x32\x44.oak9.tython.aws.secretsmanager.RotationScheduleHostedRotationLambda\x12\x1b\n\x13rotation_lambda_arn\x18\x04 \x01(\t\x12U\n\x0erotation_rules\x18\x05 \x01(\x0b\x32=.oak9.tython.aws.secretsmanager.RotationScheduleRotationRules\"\xee\x02\n\x1aSecretGenerateSecretString\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11\x65xclude_uppercase\x18\x02 \x01(\x08\x12\"\n\x1arequire_each_included_type\x18\x03 \x01(\x08\x12\x15\n\rinclude_space\x18\x04 \x01(\x08\x12\x1a\n\x12\x65xclude_characters\x18\x05 \x01(\t\x12\x1b\n\x13generate_string_key\x18\x06 \x01(\t\x12\x17\n\x0fpassword_length\x18\x07 \x01(\x05\x12\x1b\n\x13\x65xclude_punctuation\x18\x08 \x01(\x08\x12\x19\n\x11\x65xclude_lowercase\x18\t \x01(\x08\x12\x1e\n\x16secret_string_template\x18\n \x01(\t\x12\x17\n\x0f\x65xclude_numbers\x18\x0b \x01(\x08\"\xd8\x02\n\x06Secret\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nkms_key_id\x18\x03 \x01(\t\x12\x15\n\rsecret_string\x18\x04 \x01(\t\x12Z\n\x16generate_secret_string\x18\x05 \x01(\x0b\x32:.oak9.tython.aws.secretsmanager.SecretGenerateSecretString\x12>\n\x04tags\x18\x06 \x03(\x0b\x32\x30.oak9.tython.aws.secretsmanager.Secret.TagsEntry\x12\x0c\n\x04name\x18\x07 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x16SecretTargetAttachment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x13\n\x0btarget_type\x18\x03 \x01(\t\x12\x11\n\ttarget_id\x18\x04 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_secretsmanager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SECRET_TAGSENTRY._options = None
  _SECRET_TAGSENTRY._serialized_options = b'8\001'
  _RESOURCEPOLICY._serialized_start=85
  _RESOURCEPOLICY._serialized_end=202
  _SECRETSMANAGER._serialized_start=205
  _SECRETSMANAGER._serialized_end=517
  _ROTATIONSCHEDULEHOSTEDROTATIONLAMBDA._serialized_start=520
  _ROTATIONSCHEDULEHOSTEDROTATIONLAMBDA._serialized_end=807
  _ROTATIONSCHEDULEROTATIONRULES._serialized_start=809
  _ROTATIONSCHEDULEROTATIONRULES._serialized_end=931
  _ROTATIONSCHEDULE._serialized_start=934
  _ROTATIONSCHEDULE._serialized_end=1246
  _SECRETGENERATESECRETSTRING._serialized_start=1249
  _SECRETGENERATESECRETSTRING._serialized_end=1615
  _SECRET._serialized_start=1618
  _SECRET._serialized_end=1962
  _SECRET_TAGSENTRY._serialized_start=1919
  _SECRET_TAGSENTRY._serialized_end=1962
  _SECRETTARGETATTACHMENT._serialized_start=1965
  _SECRETTARGETATTACHMENT._serialized_end=2105
# @@protoc_insertion_point(module_scope)