# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_folder.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gcp/gcp_folder.proto\x12\x16oak9.tython.gcp.folder\x1a\x13shared/shared.proto\"O\n\x0f\x46olderXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0c\n\x04read\x18\x03 \x01(\t\x12\x0e\n\x06update\x18\x04 \x01(\t\"\xfd\x01\n\x06\x46older\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x11\n\tfolder_id\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x17\n\x0flifecycle_state\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0e\n\x06parent\x18\x07 \x01(\t\x12\x39\n\x08timeouts\x18\x08 \x01(\x0b\x32\'.oak9.tython.gcp.folder.FolderXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"`\n-FolderAccessApprovalSettingsXEnrolledServices\x12\x15\n\rcloud_product\x18\x01 \x01(\t\x12\x18\n\x10\x65nrollment_level\x18\x02 \x01(\t\"W\n%FolderAccessApprovalSettingsXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xd1\x03\n\x1c\x46olderAccessApprovalSettings\x12\x1a\n\x12\x61\x63tive_key_version\x18\x01 \x01(\t\x12\'\n\x1f\x61ncestor_has_active_key_version\x18\x02 \x01(\x08\x12\x19\n\x11\x65nrolled_ancestor\x18\x03 \x01(\x08\x12\x11\n\tfolder_id\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x1b\n\x13invalid_key_version\x18\x06 \x01(\x08\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x1b\n\x13notification_emails\x18\x08 \x03(\t\x12`\n\x11\x65nrolled_services\x18\t \x03(\x0b\x32\x45.oak9.tython.gcp.folder.FolderAccessApprovalSettingsXEnrolledServices\x12O\n\x08timeouts\x18\n \x01(\x0b\x32=.oak9.tython.gcp.folder.FolderAccessApprovalSettingsXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"Q\n#FolderIamAuditConfigXAuditLogConfig\x12\x18\n\x10\x65xempted_members\x18\x01 \x03(\t\x12\x10\n\x08log_type\x18\x02 \x01(\t\"\xe1\x01\n\x14\x46olderIamAuditConfig\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x0e\n\x06\x66older\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07service\x18\x04 \x01(\t\x12U\n\x10\x61udit_log_config\x18\x05 \x03(\x0b\x32;.oak9.tython.gcp.folder.FolderIamAuditConfigXAuditLogConfig\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"T\n\x1a\x46olderIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xdb\x01\n\x10\x46olderIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x0e\n\x06\x66older\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x45\n\tcondition\x18\x06 \x01(\x0b\x32\x32.oak9.tython.gcp.folder.FolderIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"S\n\x19\x46olderIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xd8\x01\n\x0f\x46olderIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x0e\n\x06\x66older\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x44\n\tcondition\x18\x06 \x01(\x0b\x32\x31.oak9.tython.gcp.folder.FolderIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x89\x01\n\x0f\x46olderIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x0e\n\x06\x66older\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\":\n&FolderOrganizationPolicyXBooleanPolicy\x12\x10\n\x08\x65nforced\x18\x01 \x01(\x08\"H\n)FolderOrganizationPolicyXListPolicyXAllow\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x08\x12\x0e\n\x06values\x18\x02 \x03(\t\"G\n(FolderOrganizationPolicyXListPolicyXDeny\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x08\x12\x0e\n\x06values\x18\x02 \x03(\t\"\xfd\x01\n#FolderOrganizationPolicyXListPolicy\x12\x1b\n\x13inherit_from_parent\x18\x01 \x01(\x08\x12\x17\n\x0fsuggested_value\x18\x02 \x01(\t\x12P\n\x05\x61llow\x18\x03 \x01(\x0b\x32\x41.oak9.tython.gcp.folder.FolderOrganizationPolicyXListPolicyXAllow\x12N\n\x04\x64\x65ny\x18\x04 \x01(\x0b\x32@.oak9.tython.gcp.folder.FolderOrganizationPolicyXListPolicyXDeny\"9\n&FolderOrganizationPolicyXRestorePolicy\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x08\"a\n!FolderOrganizationPolicyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0c\n\x04read\x18\x03 \x01(\t\x12\x0e\n\x06update\x18\x04 \x01(\t\"\x86\x04\n\x18\x46olderOrganizationPolicy\x12\x12\n\nconstraint\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x0e\n\x06\x66older\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x13\n\x0bupdate_time\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x06 \x01(\x01\x12V\n\x0e\x62oolean_policy\x18\x07 \x01(\x0b\x32>.oak9.tython.gcp.folder.FolderOrganizationPolicyXBooleanPolicy\x12P\n\x0blist_policy\x18\x08 \x01(\x0b\x32;.oak9.tython.gcp.folder.FolderOrganizationPolicyXListPolicy\x12V\n\x0erestore_policy\x18\t \x01(\x0b\x32>.oak9.tython.gcp.folder.FolderOrganizationPolicyXRestorePolicy\x12K\n\x08timeouts\x18\n \x01(\x0b\x32\x39.oak9.tython.gcp.folder.FolderOrganizationPolicyXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_folder_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FOLDERXTIMEOUTS._serialized_start=69
  _FOLDERXTIMEOUTS._serialized_end=148
  _FOLDER._serialized_start=151
  _FOLDER._serialized_end=404
  _FOLDERACCESSAPPROVALSETTINGSXENROLLEDSERVICES._serialized_start=406
  _FOLDERACCESSAPPROVALSETTINGSXENROLLEDSERVICES._serialized_end=502
  _FOLDERACCESSAPPROVALSETTINGSXTIMEOUTS._serialized_start=504
  _FOLDERACCESSAPPROVALSETTINGSXTIMEOUTS._serialized_end=591
  _FOLDERACCESSAPPROVALSETTINGS._serialized_start=594
  _FOLDERACCESSAPPROVALSETTINGS._serialized_end=1059
  _FOLDERIAMAUDITCONFIGXAUDITLOGCONFIG._serialized_start=1061
  _FOLDERIAMAUDITCONFIGXAUDITLOGCONFIG._serialized_end=1142
  _FOLDERIAMAUDITCONFIG._serialized_start=1145
  _FOLDERIAMAUDITCONFIG._serialized_end=1370
  _FOLDERIAMBINDINGXCONDITION._serialized_start=1372
  _FOLDERIAMBINDINGXCONDITION._serialized_end=1456
  _FOLDERIAMBINDING._serialized_start=1459
  _FOLDERIAMBINDING._serialized_end=1678
  _FOLDERIAMMEMBERXCONDITION._serialized_start=1680
  _FOLDERIAMMEMBERXCONDITION._serialized_end=1763
  _FOLDERIAMMEMBER._serialized_start=1766
  _FOLDERIAMMEMBER._serialized_end=1982
  _FOLDERIAMPOLICY._serialized_start=1985
  _FOLDERIAMPOLICY._serialized_end=2122
  _FOLDERORGANIZATIONPOLICYXBOOLEANPOLICY._serialized_start=2124
  _FOLDERORGANIZATIONPOLICYXBOOLEANPOLICY._serialized_end=2182
  _FOLDERORGANIZATIONPOLICYXLISTPOLICYXALLOW._serialized_start=2184
  _FOLDERORGANIZATIONPOLICYXLISTPOLICYXALLOW._serialized_end=2256
  _FOLDERORGANIZATIONPOLICYXLISTPOLICYXDENY._serialized_start=2258
  _FOLDERORGANIZATIONPOLICYXLISTPOLICYXDENY._serialized_end=2329
  _FOLDERORGANIZATIONPOLICYXLISTPOLICY._serialized_start=2332
  _FOLDERORGANIZATIONPOLICYXLISTPOLICY._serialized_end=2585
  _FOLDERORGANIZATIONPOLICYXRESTOREPOLICY._serialized_start=2587
  _FOLDERORGANIZATIONPOLICYXRESTOREPOLICY._serialized_end=2644
  _FOLDERORGANIZATIONPOLICYXTIMEOUTS._serialized_start=2646
  _FOLDERORGANIZATIONPOLICYXTIMEOUTS._serialized_end=2743
  _FOLDERORGANIZATIONPOLICY._serialized_start=2746
  _FOLDERORGANIZATIONPOLICY._serialized_end=3264
# @@protoc_insertion_point(module_scope)
