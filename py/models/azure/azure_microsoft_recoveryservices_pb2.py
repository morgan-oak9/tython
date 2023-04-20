# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_recoveryservices.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,azure/azure_microsoft_recoveryservices.proto\x12,oak9.tython.azure.microsoft_recoveryservices\x1a\x13shared/shared.proto\"b\n\x1aMicrosoft_RecoveryServices\x12\x44\n\x06vaults\x18\x01 \x03(\x0b\x32\x34.oak9.tython.azure.microsoft_recoveryservices.Vaults\"\xd5\x01\n\x19VaultsExtendedInformation\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12\x16\n\x0e\x65ncryption_key\x18\x05 \x01(\t\x12!\n\x19\x65ncryption_key_thumbprint\x18\x06 \x01(\t\x12\x15\n\rintegrity_key\x18\x07 \x01(\t\"\x83\x01\n\x12VaultsCertificates\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tauth_type\x18\x03 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x04 \x01(\t\"\xa8\x07\n\x06Vaults\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12L\n\x08identity\x18\x03 \x01(\x0b\x32:.oak9.tython.azure.microsoft_recoveryservices.IdentityData\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12[\n\nencryption\x18\x06 \x01(\x0b\x32G.oak9.tython.azure.microsoft_recoveryservices.VaultPropertiesEncryption\x12^\n\x0cmove_details\x18\x07 \x01(\x0b\x32H.oak9.tython.azure.microsoft_recoveryservices.VaultPropertiesMoveDetails\x12U\n\x0fupgrade_details\x18\x08 \x01(\x0b\x32<.oak9.tython.azure.microsoft_recoveryservices.UpgradeDetails\x12>\n\x03sku\x18\t \x01(\x0b\x32\x31.oak9.tython.azure.microsoft_recoveryservices.Sku\x12M\n\x0bsystem_data\x18\n \x01(\x0b\x32\x38.oak9.tython.azure.microsoft_recoveryservices.SystemData\x12L\n\x04tags\x18\x0b \x03(\x0b\x32>.oak9.tython.azure.microsoft_recoveryservices.Vaults.TagsEntry\x12]\n\x13vaults_certificates\x18\x0c \x03(\x0b\x32@.oak9.tython.azure.microsoft_recoveryservices.VaultsCertificates\x12l\n\x1bvaults_extended_information\x18\r \x03(\x0b\x32G.oak9.tython.azure.microsoft_recoveryservices.VaultsExtendedInformation\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa0\x01\n\nSystemData\x12\x12\n\ncreated_at\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12\x17\n\x0f\x63reated_by_type\x18\x03 \x01(\t\x12\x18\n\x10last_modified_at\x18\x04 \x01(\t\x12\x18\n\x10last_modified_by\x18\x05 \x01(\t\x12\x1d\n\x15last_modified_by_type\x18\x06 \x01(\t\"Q\n\x03Sku\x12\x10\n\x08\x63\x61pacity\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\t\"\x1e\n\x0eUpgradeDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x1aVaultPropertiesMoveDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf5\x01\n\x19VaultPropertiesEncryption\x12!\n\x19infrastructure_encryption\x18\x01 \x01(\t\x12R\n\x0ckek_identity\x18\x02 \x01(\x0b\x32<.oak9.tython.azure.microsoft_recoveryservices.CmkKekIdentity\x12\x61\n\x14key_vault_properties\x18\x03 \x01(\x0b\x32\x43.oak9.tython.azure.microsoft_recoveryservices.CmkKeyVaultProperties\"(\n\x15\x43mkKeyVaultProperties\x12\x0f\n\x07key_uri\x18\x01 \x01(\t\"V\n\x0e\x43mkKekIdentity\x12\x1e\n\x16user_assigned_identity\x18\x01 \x01(\t\x12$\n\x1cuse_system_assigned_identity\x18\x02 \x01(\x08\"\xd5\x01\n\x0cIdentityData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12x\n\x18user_assigned_identities\x18\x02 \x03(\x0b\x32V.oak9.tython.azure.microsoft_recoveryservices.IdentityData.UserAssignedIdentitiesEntry\x1a=\n\x1bUserAssignedIdentitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_recoveryservices_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VAULTS_TAGSENTRY._options = None
  _VAULTS_TAGSENTRY._serialized_options = b'8\001'
  _IDENTITYDATA_USERASSIGNEDIDENTITIESENTRY._options = None
  _IDENTITYDATA_USERASSIGNEDIDENTITIESENTRY._serialized_options = b'8\001'
  _MICROSOFT_RECOVERYSERVICES._serialized_start=115
  _MICROSOFT_RECOVERYSERVICES._serialized_end=213
  _VAULTSEXTENDEDINFORMATION._serialized_start=216
  _VAULTSEXTENDEDINFORMATION._serialized_end=429
  _VAULTSCERTIFICATES._serialized_start=432
  _VAULTSCERTIFICATES._serialized_end=563
  _VAULTS._serialized_start=566
  _VAULTS._serialized_end=1502
  _VAULTS_TAGSENTRY._serialized_start=1459
  _VAULTS_TAGSENTRY._serialized_end=1502
  _SYSTEMDATA._serialized_start=1505
  _SYSTEMDATA._serialized_end=1665
  _SKU._serialized_start=1667
  _SKU._serialized_end=1748
  _UPGRADEDETAILS._serialized_start=1750
  _UPGRADEDETAILS._serialized_end=1780
  _VAULTPROPERTIESMOVEDETAILS._serialized_start=1782
  _VAULTPROPERTIESMOVEDETAILS._serialized_end=1824
  _VAULTPROPERTIESENCRYPTION._serialized_start=1827
  _VAULTPROPERTIESENCRYPTION._serialized_end=2072
  _CMKKEYVAULTPROPERTIES._serialized_start=2074
  _CMKKEYVAULTPROPERTIES._serialized_end=2114
  _CMKKEKIDENTITY._serialized_start=2116
  _CMKKEKIDENTITY._serialized_end=2202
  _IDENTITYDATA._serialized_start=2205
  _IDENTITYDATA._serialized_end=2418
  _IDENTITYDATA_USERASSIGNEDIDENTITIESENTRY._serialized_start=2357
  _IDENTITYDATA_USERASSIGNEDIDENTITIESENTRY._serialized_end=2418
# @@protoc_insertion_point(module_scope)