# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_kms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11gcp/gcp_kms.proto\x12\x13oak9.tython.gcp.kms\x1a\x13shared/shared.proto\"G\n\x15KmsCryptoKeyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"K\n\x1cKmsCryptoKeyXVersionTemplate\x12\x11\n\talgorithm\x18\x01 \x01(\t\x12\x18\n\x10protection_level\x18\x02 \x01(\t\"\xf6\x03\n\x0cKmsCryptoKey\x12\"\n\x1a\x64\x65stroy_scheduled_duration\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bimport_only\x18\x03 \x01(\x08\x12\x10\n\x08key_ring\x18\x04 \x01(\t\x12=\n\x06labels\x18\x05 \x03(\x0b\x32-.oak9.tython.gcp.kms.KmsCryptoKey.LabelsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07purpose\x18\x07 \x01(\t\x12\x17\n\x0frotation_period\x18\x08 \x01(\t\x12%\n\x1dskip_initial_version_creation\x18\t \x01(\x08\x12<\n\x08timeouts\x18\n \x01(\x0b\x32*.oak9.tython.gcp.kms.KmsCryptoKeyXTimeouts\x12K\n\x10version_template\x18\x0b \x01(\x0b\x32\x31.oak9.tython.gcp.kms.KmsCryptoKeyXVersionTemplate\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Z\n KmsCryptoKeyIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xeb\x01\n\x16KmsCryptoKeyIamBinding\x12\x15\n\rcrypto_key_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12H\n\tcondition\x18\x06 \x01(\x0b\x32\x35.oak9.tython.gcp.kms.KmsCryptoKeyIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"Y\n\x1fKmsCryptoKeyIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xe8\x01\n\x15KmsCryptoKeyIamMember\x12\x15\n\rcrypto_key_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12G\n\tcondition\x18\x06 \x01(\x0b\x32\x34.oak9.tython.gcp.kms.KmsCryptoKeyIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x96\x01\n\x15KmsCryptoKeyIamPolicy\x12\x15\n\rcrypto_key_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"5\n\x13KmsKeyRingXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xbe\x01\n\nKmsKeyRing\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12:\n\x08timeouts\x18\x05 \x01(\x0b\x32(.oak9.tython.gcp.kms.KmsKeyRingXTimeouts\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"X\n\x1eKmsKeyRingIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xe5\x01\n\x14KmsKeyRingIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bkey_ring_id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x46\n\tcondition\x18\x06 \x01(\x0b\x32\x33.oak9.tython.gcp.kms.KmsKeyRingIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"W\n\x1dKmsKeyRingIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xe2\x01\n\x13KmsKeyRingIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bkey_ring_id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x45\n\tcondition\x18\x06 \x01(\x0b\x32\x32.oak9.tython.gcp.kms.KmsKeyRingIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x92\x01\n\x13KmsKeyRingIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0bkey_ring_id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\">\n\x1cKmsKeyRingImportJobXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xae\x04\n\x13KmsKeyRingImportJob\x12N\n\x0b\x61ttestation\x18\x01 \x03(\x0b\x32\x39.oak9.tython.gcp.kms.KmsKeyRingImportJob.AttestationEntry\x12\x13\n\x0b\x65xpire_time\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x15\n\rimport_job_id\x18\x04 \x01(\t\x12\x15\n\rimport_method\x18\x05 \x01(\t\x12\x10\n\x08key_ring\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x18\n\x10protection_level\x18\x08 \x01(\t\x12K\n\npublic_key\x18\t \x03(\x0b\x32\x37.oak9.tython.gcp.kms.KmsKeyRingImportJob.PublicKeyEntry\x12\r\n\x05state\x18\n \x01(\t\x12\x43\n\x08timeouts\x18\x0b \x01(\x0b\x32\x31.oak9.tython.gcp.kms.KmsKeyRingImportJobXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a\x32\n\x10\x41ttestationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x0ePublicKeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\">\n\x1cKmsSecretCiphertextXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\x81\x02\n\x13KmsSecretCiphertext\x12%\n\x1d\x61\x64\x64itional_authenticated_data\x18\x01 \x01(\t\x12\x12\n\nciphertext\x18\x02 \x01(\t\x12\x12\n\ncrypto_key\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x11\n\tplaintext\x18\x05 \x01(\t\x12\x43\n\x08timeouts\x18\x06 \x01(\x0b\x32\x31.oak9.tython.gcp.kms.KmsSecretCiphertextXTimeouts\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_kms_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KMSCRYPTOKEY_LABELSENTRY._options = None
  _KMSCRYPTOKEY_LABELSENTRY._serialized_options = b'8\001'
  _KMSKEYRINGIMPORTJOB_ATTESTATIONENTRY._options = None
  _KMSKEYRINGIMPORTJOB_ATTESTATIONENTRY._serialized_options = b'8\001'
  _KMSKEYRINGIMPORTJOB_PUBLICKEYENTRY._options = None
  _KMSKEYRINGIMPORTJOB_PUBLICKEYENTRY._serialized_options = b'8\001'
  _KMSCRYPTOKEYXTIMEOUTS._serialized_start=63
  _KMSCRYPTOKEYXTIMEOUTS._serialized_end=134
  _KMSCRYPTOKEYXVERSIONTEMPLATE._serialized_start=136
  _KMSCRYPTOKEYXVERSIONTEMPLATE._serialized_end=211
  _KMSCRYPTOKEY._serialized_start=214
  _KMSCRYPTOKEY._serialized_end=716
  _KMSCRYPTOKEY_LABELSENTRY._serialized_start=671
  _KMSCRYPTOKEY_LABELSENTRY._serialized_end=716
  _KMSCRYPTOKEYIAMBINDINGXCONDITION._serialized_start=718
  _KMSCRYPTOKEYIAMBINDINGXCONDITION._serialized_end=808
  _KMSCRYPTOKEYIAMBINDING._serialized_start=811
  _KMSCRYPTOKEYIAMBINDING._serialized_end=1046
  _KMSCRYPTOKEYIAMMEMBERXCONDITION._serialized_start=1048
  _KMSCRYPTOKEYIAMMEMBERXCONDITION._serialized_end=1137
  _KMSCRYPTOKEYIAMMEMBER._serialized_start=1140
  _KMSCRYPTOKEYIAMMEMBER._serialized_end=1372
  _KMSCRYPTOKEYIAMPOLICY._serialized_start=1375
  _KMSCRYPTOKEYIAMPOLICY._serialized_end=1525
  _KMSKEYRINGXTIMEOUTS._serialized_start=1527
  _KMSKEYRINGXTIMEOUTS._serialized_end=1580
  _KMSKEYRING._serialized_start=1583
  _KMSKEYRING._serialized_end=1773
  _KMSKEYRINGIAMBINDINGXCONDITION._serialized_start=1775
  _KMSKEYRINGIAMBINDINGXCONDITION._serialized_end=1863
  _KMSKEYRINGIAMBINDING._serialized_start=1866
  _KMSKEYRINGIAMBINDING._serialized_end=2095
  _KMSKEYRINGIAMMEMBERXCONDITION._serialized_start=2097
  _KMSKEYRINGIAMMEMBERXCONDITION._serialized_end=2184
  _KMSKEYRINGIAMMEMBER._serialized_start=2187
  _KMSKEYRINGIAMMEMBER._serialized_end=2413
  _KMSKEYRINGIAMPOLICY._serialized_start=2416
  _KMSKEYRINGIAMPOLICY._serialized_end=2562
  _KMSKEYRINGIMPORTJOBXTIMEOUTS._serialized_start=2564
  _KMSKEYRINGIMPORTJOBXTIMEOUTS._serialized_end=2626
  _KMSKEYRINGIMPORTJOB._serialized_start=2629
  _KMSKEYRINGIMPORTJOB._serialized_end=3187
  _KMSKEYRINGIMPORTJOB_ATTESTATIONENTRY._serialized_start=3087
  _KMSKEYRINGIMPORTJOB_ATTESTATIONENTRY._serialized_end=3137
  _KMSKEYRINGIMPORTJOB_PUBLICKEYENTRY._serialized_start=3139
  _KMSKEYRINGIMPORTJOB_PUBLICKEYENTRY._serialized_end=3187
  _KMSSECRETCIPHERTEXTXTIMEOUTS._serialized_start=3189
  _KMSSECRETCIPHERTEXTXTIMEOUTS._serialized_end=3251
  _KMSSECRETCIPHERTEXT._serialized_start=3254
  _KMSSECRETCIPHERTEXT._serialized_end=3511
# @@protoc_insertion_point(module_scope)
