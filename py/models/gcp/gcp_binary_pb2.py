# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_binary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gcp/gcp_binary.proto\x12\x16oak9.tython.gcp.binary\x1a\x13shared/shared.proto\"\x84\x01\nMBinaryAuthorizationAttestorXAttestationAuthorityNoteXPublicKeysXPkixPublicKey\x12\x16\n\x0epublic_key_pem\x18\x01 \x01(\t\x12\x1b\n\x13signature_algorithm\x18\x02 \x01(\t\"\x84\x02\n?BinaryAuthorizationAttestorXAttestationAuthorityNoteXPublicKeys\x12$\n\x1c\x61scii_armored_pgp_public_key\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12~\n\x0fpkix_public_key\x18\x04 \x01(\x0b\x32\x65.oak9.tython.gcp.binary.BinaryAuthorizationAttestorXAttestationAuthorityNoteXPublicKeysXPkixPublicKey\"\xe6\x01\n4BinaryAuthorizationAttestorXAttestationAuthorityNote\x12(\n delegation_service_account_email\x18\x01 \x01(\t\x12\x16\n\x0enote_reference\x18\x02 \x01(\t\x12l\n\x0bpublic_keys\x18\x03 \x03(\x0b\x32W.oak9.tython.gcp.binary.BinaryAuthorizationAttestorXAttestationAuthorityNoteXPublicKeys\"V\n$BinaryAuthorizationAttestorXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xd8\x02\n\x1b\x42inaryAuthorizationAttestor\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12p\n\x1a\x61ttestation_authority_note\x18\x05 \x01(\x0b\x32L.oak9.tython.gcp.binary.BinaryAuthorizationAttestorXAttestationAuthorityNote\x12N\n\x08timeouts\x18\x06 \x01(\x0b\x32<.oak9.tython.gcp.binary.BinaryAuthorizationAttestorXTimeouts\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"i\n/BinaryAuthorizationAttestorIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x98\x02\n%BinaryAuthorizationAttestorIamBinding\x12\x10\n\x08\x61ttestor\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12Z\n\tcondition\x18\x07 \x01(\x0b\x32G.oak9.tython.gcp.binary.BinaryAuthorizationAttestorIamBindingXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"h\n.BinaryAuthorizationAttestorIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x95\x02\n$BinaryAuthorizationAttestorIamMember\x12\x10\n\x08\x61ttestor\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12Y\n\tcondition\x18\x07 \x01(\x0b\x32\x46.oak9.tython.gcp.binary.BinaryAuthorizationAttestorIamMemberXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb1\x01\n$BinaryAuthorizationAttestorIamPolicy\x12\x10\n\x08\x61ttestor\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"L\n4BinaryAuthorizationPolicyXAdmissionWhitelistPatterns\x12\x14\n\x0cname_pattern\x18\x01 \x01(\t\"\x96\x01\n/BinaryAuthorizationPolicyXClusterAdmissionRules\x12\x0f\n\x07\x63luster\x18\x01 \x01(\t\x12\x18\n\x10\x65nforcement_mode\x18\x02 \x01(\t\x12\x17\n\x0f\x65valuation_mode\x18\x03 \x01(\t\x12\x1f\n\x17require_attestations_by\x18\x04 \x03(\t\"\x84\x01\n.BinaryAuthorizationPolicyXDefaultAdmissionRule\x12\x18\n\x10\x65nforcement_mode\x18\x01 \x01(\t\x12\x17\n\x0f\x65valuation_mode\x18\x02 \x01(\t\x12\x1f\n\x17require_attestations_by\x18\x03 \x03(\t\"T\n\"BinaryAuthorizationPolicyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xc1\x04\n\x19\x42inaryAuthorizationPolicy\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12%\n\x1dglobal_policy_evaluation_mode\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12r\n\x1c\x61\x64mission_whitelist_patterns\x18\x05 \x03(\x0b\x32L.oak9.tython.gcp.binary.BinaryAuthorizationPolicyXAdmissionWhitelistPatterns\x12h\n\x17\x63luster_admission_rules\x18\x06 \x03(\x0b\x32G.oak9.tython.gcp.binary.BinaryAuthorizationPolicyXClusterAdmissionRules\x12\x66\n\x16\x64\x65\x66\x61ult_admission_rule\x18\x07 \x01(\x0b\x32\x46.oak9.tython.gcp.binary.BinaryAuthorizationPolicyXDefaultAdmissionRule\x12L\n\x08timeouts\x18\x08 \x01(\x0b\x32:.oak9.tython.gcp.binary.BinaryAuthorizationPolicyXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_binary_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTEXPUBLICKEYSXPKIXPUBLICKEY._serialized_start=70
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTEXPUBLICKEYSXPKIXPUBLICKEY._serialized_end=202
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTEXPUBLICKEYS._serialized_start=205
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTEXPUBLICKEYS._serialized_end=465
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTE._serialized_start=468
  _BINARYAUTHORIZATIONATTESTORXATTESTATIONAUTHORITYNOTE._serialized_end=698
  _BINARYAUTHORIZATIONATTESTORXTIMEOUTS._serialized_start=700
  _BINARYAUTHORIZATIONATTESTORXTIMEOUTS._serialized_end=786
  _BINARYAUTHORIZATIONATTESTOR._serialized_start=789
  _BINARYAUTHORIZATIONATTESTOR._serialized_end=1133
  _BINARYAUTHORIZATIONATTESTORIAMBINDINGXCONDITION._serialized_start=1135
  _BINARYAUTHORIZATIONATTESTORIAMBINDINGXCONDITION._serialized_end=1240
  _BINARYAUTHORIZATIONATTESTORIAMBINDING._serialized_start=1243
  _BINARYAUTHORIZATIONATTESTORIAMBINDING._serialized_end=1523
  _BINARYAUTHORIZATIONATTESTORIAMMEMBERXCONDITION._serialized_start=1525
  _BINARYAUTHORIZATIONATTESTORIAMMEMBERXCONDITION._serialized_end=1629
  _BINARYAUTHORIZATIONATTESTORIAMMEMBER._serialized_start=1632
  _BINARYAUTHORIZATIONATTESTORIAMMEMBER._serialized_end=1909
  _BINARYAUTHORIZATIONATTESTORIAMPOLICY._serialized_start=1912
  _BINARYAUTHORIZATIONATTESTORIAMPOLICY._serialized_end=2089
  _BINARYAUTHORIZATIONPOLICYXADMISSIONWHITELISTPATTERNS._serialized_start=2091
  _BINARYAUTHORIZATIONPOLICYXADMISSIONWHITELISTPATTERNS._serialized_end=2167
  _BINARYAUTHORIZATIONPOLICYXCLUSTERADMISSIONRULES._serialized_start=2170
  _BINARYAUTHORIZATIONPOLICYXCLUSTERADMISSIONRULES._serialized_end=2320
  _BINARYAUTHORIZATIONPOLICYXDEFAULTADMISSIONRULE._serialized_start=2323
  _BINARYAUTHORIZATIONPOLICYXDEFAULTADMISSIONRULE._serialized_end=2455
  _BINARYAUTHORIZATIONPOLICYXTIMEOUTS._serialized_start=2457
  _BINARYAUTHORIZATIONPOLICYXTIMEOUTS._serialized_end=2541
  _BINARYAUTHORIZATIONPOLICY._serialized_start=2544
  _BINARYAUTHORIZATIONPOLICY._serialized_end=3121
# @@protoc_insertion_point(module_scope)