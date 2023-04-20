# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_sourcerepo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18gcp/gcp_sourcerepo.proto\x12\x1aoak9.tython.gcp.sourcerepo\x1a\x13shared/shared.proto\"j\n\"SourcerepoRepositoryXPubsubConfigs\x12\x16\n\x0emessage_format\x18\x01 \x01(\t\x12\x1d\n\x15service_account_email\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\"O\n\x1dSourcerepoRepositoryXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xba\x02\n\x14SourcerepoRepository\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x01\x12\x0b\n\x03url\x18\x05 \x01(\t\x12V\n\x0epubsub_configs\x18\x06 \x03(\x0b\x32>.oak9.tython.gcp.sourcerepo.SourcerepoRepositoryXPubsubConfigs\x12K\n\x08timeouts\x18\x07 \x01(\x0b\x32\x39.oak9.tython.gcp.sourcerepo.SourcerepoRepositoryXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"b\n(SourcerepoRepositoryIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x90\x02\n\x1eSourcerepoRepositoryIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07members\x18\x03 \x03(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x12\n\nrepository\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12W\n\tcondition\x18\x07 \x01(\x0b\x32\x44.oak9.tython.gcp.sourcerepo.SourcerepoRepositoryIamBindingXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"a\n\'SourcerepoRepositoryIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x8d\x02\n\x1dSourcerepoRepositoryIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06member\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x12\n\nrepository\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12V\n\tcondition\x18\x07 \x01(\x0b\x32\x43.oak9.tython.gcp.sourcerepo.SourcerepoRepositoryIamMemberXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xac\x01\n\x1dSourcerepoRepositoryIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x12\n\nrepository\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_sourcerepo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOURCEREPOREPOSITORYXPUBSUBCONFIGS._serialized_start=77
  _SOURCEREPOREPOSITORYXPUBSUBCONFIGS._serialized_end=183
  _SOURCEREPOREPOSITORYXTIMEOUTS._serialized_start=185
  _SOURCEREPOREPOSITORYXTIMEOUTS._serialized_end=264
  _SOURCEREPOREPOSITORY._serialized_start=267
  _SOURCEREPOREPOSITORY._serialized_end=581
  _SOURCEREPOREPOSITORYIAMBINDINGXCONDITION._serialized_start=583
  _SOURCEREPOREPOSITORYIAMBINDINGXCONDITION._serialized_end=681
  _SOURCEREPOREPOSITORYIAMBINDING._serialized_start=684
  _SOURCEREPOREPOSITORYIAMBINDING._serialized_end=956
  _SOURCEREPOREPOSITORYIAMMEMBERXCONDITION._serialized_start=958
  _SOURCEREPOREPOSITORYIAMMEMBERXCONDITION._serialized_end=1055
  _SOURCEREPOREPOSITORYIAMMEMBER._serialized_start=1058
  _SOURCEREPOREPOSITORYIAMMEMBER._serialized_end=1327
  _SOURCEREPOREPOSITORYIAMPOLICY._serialized_start=1330
  _SOURCEREPOREPOSITORYIAMPOLICY._serialized_end=1502
# @@protoc_insertion_point(module_scope)