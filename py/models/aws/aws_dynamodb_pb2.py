# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_dynamodb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61ws/aws_dynamodb.proto\x12\x18oak9.tython.aws.dynamodb\x1a\x13shared/shared.proto\"\x83\x01\n\x18TableAttributeDefinition\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x61ttribute_name\x18\x02 \x01(\t\x12\x16\n\x0e\x61ttribute_type\x18\x03 \x01(\t\"\x97\x05\n\x08\x44ynamoDB\x12V\n\x1atable_attribute_definition\x18\x01 \x03(\x0b\x32\x32.oak9.tython.aws.dynamodb.TableAttributeDefinition\x12Y\n\x1ctable_global_secondary_index\x18\x02 \x03(\x0b\x32\x33.oak9.tython.aws.dynamodb.TableGlobalSecondaryIndex\x12W\n\x1btable_local_secondary_index\x18\x03 \x03(\x0b\x32\x32.oak9.tython.aws.dynamodb.TableLocalSecondaryIndex\x12s\n*table_point_in_time_recovery_specification\x18\x04 \x03(\x0b\x32?.oak9.tython.aws.dynamodb.TablePointInTimeRecoverySpecification\x12P\n\x17table_sse_specification\x18\x05 \x03(\x0b\x32/.oak9.tython.aws.dynamodb.TableSSESpecification\x12V\n\x1atable_stream_specification\x18\x06 \x03(\x0b\x32\x32.oak9.tython.aws.dynamodb.TableStreamSpecification\x12`\n table_time_to_live_specification\x18\x07 \x03(\x0b\x32\x36.oak9.tython.aws.dynamodb.TableTimeToLiveSpecification\"s\n\x0eTableKeySchema\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x61ttribute_name\x18\x02 \x01(\t\x12\x10\n\x08key_type\x18\x03 \x01(\t\"\x7f\n\x0fTableProjection\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12non_key_attributes\x18\x02 \x03(\t\x12\x17\n\x0fprojection_type\x18\x03 \x01(\t\"\x90\x01\n\x1aTableProvisionedThroughput\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13read_capacity_units\x18\x02 \x01(\x05\x12\x1c\n\x14write_capacity_units\x18\x03 \x01(\x05\"\xbb\x02\n\x19TableGlobalSecondaryIndex\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12<\n\nkey_schema\x18\x03 \x03(\x0b\x32(.oak9.tython.aws.dynamodb.TableKeySchema\x12=\n\nprojection\x18\x04 \x01(\x0b\x32).oak9.tython.aws.dynamodb.TableProjection\x12T\n\x16provisioned_throughput\x18\x05 \x01(\x0b\x32\x34.oak9.tython.aws.dynamodb.TableProvisionedThroughput\"\xe4\x01\n\x18TableLocalSecondaryIndex\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12<\n\nkey_schema\x18\x03 \x03(\x0b\x32(.oak9.tython.aws.dynamodb.TableKeySchema\x12=\n\nprojection\x18\x04 \x01(\x0b\x32).oak9.tython.aws.dynamodb.TableProjection\"\x88\x01\n%TablePointInTimeRecoverySpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12&\n\x1epoint_in_time_recovery_enabled\x18\x02 \x01(\x08\"\x92\x01\n\x15TableSSESpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11kms_master_key_id\x18\x02 \x01(\t\x12\x13\n\x0bsse_enabled\x18\x03 \x01(\x08\x12\x10\n\x08sse_type\x18\x04 \x01(\t\"m\n\x18TableStreamSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10stream_view_type\x18\x02 \x01(\t\"\x80\x01\n\x1cTableTimeToLiveSpecification\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x61ttribute_name\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_dynamodb_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TABLEATTRIBUTEDEFINITION._serialized_start=74
  _TABLEATTRIBUTEDEFINITION._serialized_end=205
  _DYNAMODB._serialized_start=208
  _DYNAMODB._serialized_end=871
  _TABLEKEYSCHEMA._serialized_start=873
  _TABLEKEYSCHEMA._serialized_end=988
  _TABLEPROJECTION._serialized_start=990
  _TABLEPROJECTION._serialized_end=1117
  _TABLEPROVISIONEDTHROUGHPUT._serialized_start=1120
  _TABLEPROVISIONEDTHROUGHPUT._serialized_end=1264
  _TABLEGLOBALSECONDARYINDEX._serialized_start=1267
  _TABLEGLOBALSECONDARYINDEX._serialized_end=1582
  _TABLELOCALSECONDARYINDEX._serialized_start=1585
  _TABLELOCALSECONDARYINDEX._serialized_end=1813
  _TABLEPOINTINTIMERECOVERYSPECIFICATION._serialized_start=1816
  _TABLEPOINTINTIMERECOVERYSPECIFICATION._serialized_end=1952
  _TABLESSESPECIFICATION._serialized_start=1955
  _TABLESSESPECIFICATION._serialized_end=2101
  _TABLESTREAMSPECIFICATION._serialized_start=2103
  _TABLESTREAMSPECIFICATION._serialized_end=2212
  _TABLETIMETOLIVESPECIFICATION._serialized_start=2215
  _TABLETIMETOLIVESPECIFICATION._serialized_end=2343
# @@protoc_insertion_point(module_scope)
