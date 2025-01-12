# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_spanner.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gcp/gcp_spanner.proto\x12\x17oak9.tython.gcp.spanner\x1a\x13shared/shared.proto\"8\n SpannerDatabaseXEncryptionConfig\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\"J\n\x18SpannerDatabaseXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x97\x03\n\x0fSpannerDatabase\x12\x18\n\x10\x64\x61tabase_dialect\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x64l\x18\x02 \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x03 \x01(\x08\x12\n\n\x02id\x18\x04 \x01(\t\x12\x10\n\x08instance\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12 \n\x18version_retention_period\x18\t \x01(\t\x12T\n\x11\x65ncryption_config\x18\n \x01(\x0b\x32\x39.oak9.tython.gcp.spanner.SpannerDatabaseXEncryptionConfig\x12\x43\n\x08timeouts\x18\x0b \x01(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerDatabaseXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"]\n#SpannerDatabaseIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x93\x02\n\x19SpannerDatabaseIamBinding\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0f\n\x07members\x18\x05 \x03(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12O\n\tcondition\x18\x08 \x01(\x0b\x32<.oak9.tython.gcp.spanner.SpannerDatabaseIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\\\n\"SpannerDatabaseIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x90\x02\n\x18SpannerDatabaseIamMember\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0e\n\x06member\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12N\n\tcondition\x18\x08 \x01(\x0b\x32;.oak9.tython.gcp.spanner.SpannerDatabaseIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb7\x01\n\x18SpannerDatabaseIamPolicy\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"J\n\x18SpannerInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xa8\x03\n\x0fSpannerInstance\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x15\n\rforce_destroy\x18\x03 \x01(\x08\x12\n\n\x02id\x18\x04 \x01(\t\x12\x44\n\x06labels\x18\x05 \x03(\x0b\x32\x34.oak9.tython.gcp.spanner.SpannerInstance.LabelsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x11\n\tnum_nodes\x18\x07 \x01(\x01\x12\x18\n\x10processing_units\x18\x08 \x01(\x01\x12\x0f\n\x07project\x18\t \x01(\t\x12\r\n\x05state\x18\n \x01(\t\x12\x43\n\x08timeouts\x18\x0b \x01(\x0b\x32\x31.oak9.tython.gcp.spanner.SpannerInstanceXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n#SpannerInstanceIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x81\x02\n\x19SpannerInstanceIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12O\n\tcondition\x18\x07 \x01(\x0b\x32<.oak9.tython.gcp.spanner.SpannerInstanceIamBindingXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\\\n\"SpannerInstanceIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xfe\x01\n\x18SpannerInstanceIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12N\n\tcondition\x18\x07 \x01(\x0b\x32;.oak9.tython.gcp.spanner.SpannerInstanceIamMemberXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa5\x01\n\x18SpannerInstanceIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_spanner_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SPANNERINSTANCE_LABELSENTRY._options = None
  _SPANNERINSTANCE_LABELSENTRY._serialized_options = b'8\001'
  _SPANNERDATABASEXENCRYPTIONCONFIG._serialized_start=71
  _SPANNERDATABASEXENCRYPTIONCONFIG._serialized_end=127
  _SPANNERDATABASEXTIMEOUTS._serialized_start=129
  _SPANNERDATABASEXTIMEOUTS._serialized_end=203
  _SPANNERDATABASE._serialized_start=206
  _SPANNERDATABASE._serialized_end=613
  _SPANNERDATABASEIAMBINDINGXCONDITION._serialized_start=615
  _SPANNERDATABASEIAMBINDINGXCONDITION._serialized_end=708
  _SPANNERDATABASEIAMBINDING._serialized_start=711
  _SPANNERDATABASEIAMBINDING._serialized_end=986
  _SPANNERDATABASEIAMMEMBERXCONDITION._serialized_start=988
  _SPANNERDATABASEIAMMEMBERXCONDITION._serialized_end=1080
  _SPANNERDATABASEIAMMEMBER._serialized_start=1083
  _SPANNERDATABASEIAMMEMBER._serialized_end=1355
  _SPANNERDATABASEIAMPOLICY._serialized_start=1358
  _SPANNERDATABASEIAMPOLICY._serialized_end=1541
  _SPANNERINSTANCEXTIMEOUTS._serialized_start=1543
  _SPANNERINSTANCEXTIMEOUTS._serialized_end=1617
  _SPANNERINSTANCE._serialized_start=1620
  _SPANNERINSTANCE._serialized_end=2044
  _SPANNERINSTANCE_LABELSENTRY._serialized_start=1999
  _SPANNERINSTANCE_LABELSENTRY._serialized_end=2044
  _SPANNERINSTANCEIAMBINDINGXCONDITION._serialized_start=2046
  _SPANNERINSTANCEIAMBINDINGXCONDITION._serialized_end=2139
  _SPANNERINSTANCEIAMBINDING._serialized_start=2142
  _SPANNERINSTANCEIAMBINDING._serialized_end=2399
  _SPANNERINSTANCEIAMMEMBERXCONDITION._serialized_start=2401
  _SPANNERINSTANCEIAMMEMBERXCONDITION._serialized_end=2493
  _SPANNERINSTANCEIAMMEMBER._serialized_start=2496
  _SPANNERINSTANCEIAMMEMBER._serialized_end=2750
  _SPANNERINSTANCEIAMPOLICY._serialized_start=2753
  _SPANNERINSTANCEIAMPOLICY._serialized_end=2918
# @@protoc_insertion_point(module_scope)
