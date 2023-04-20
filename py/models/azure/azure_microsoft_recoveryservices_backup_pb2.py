# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_recoveryservices_backup.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3azure/azure_microsoft_recoveryservices_backup.proto\x12\x33oak9.tython.azure.microsoft_recoveryservices_backup\x1a\x13shared/shared.proto\"\x9e\x08\n!Microsoft_RecoveryServices_Backup\x12\x64\n\x13vaults_backupconfig\x18\x01 \x03(\x0b\x32G.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupconfig\x12|\n vaults_backup_encryption_configs\x18\x02 \x03(\x0b\x32R.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupEncryptionConfigs\x12\x96\x01\n.vaults_backup_fabrics_backup_protection_intent\x18\x03 \x03(\x0b\x32^.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsBackupProtectionIntent\x12\x91\x01\n+vaults_backup_fabrics_protection_containers\x18\x04 \x03(\x0b\x32\\.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsProtectionContainers\x12i\n\x16vaults_backup_policies\x18\x05 \x03(\x0b\x32I.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupPolicies\x12\x83\x01\n$vaults_backup_resource_guard_proxies\x18\x06 \x03(\x0b\x32U.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupResourceGuardProxies\x12r\n\x1avaults_backupstorageconfig\x18\x07 \x03(\x0b\x32N.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupstorageconfig\x12\x82\x01\n#vaults_private_endpoint_connections\x18\x08 \x03(\x0b\x32U.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsPrivateEndpointConnections\"\xaa\x04\n VaultsPrivateEndpointConnections\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12^\n\x10private_endpoint\x18\x05 \x01(\x0b\x32\x44.oak9.tython.azure.microsoft_recoveryservices_backup.PrivateEndpoint\x12\x85\x01\n%private_link_service_connection_state\x18\x06 \x01(\x0b\x32V.oak9.tython.azure.microsoft_recoveryservices_backup.PrivateLinkServiceConnectionState\x12\x1a\n\x12provisioning_state\x18\x07 \x01(\t\x12m\n\x04tags\x18\x08 \x03(\x0b\x32_.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsPrivateEndpointConnections.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"a\n!PrivateLinkServiceConnectionState\x12\x17\n\x0f\x61\x63tion_required\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x1d\n\x0fPrivateEndpoint\x12\n\n\x02id\x18\x01 \x01(\t\"\xb3\x03\n\x19VaultsBackupstorageconfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12!\n\x19\x63ross_region_restore_flag\x18\x05 \x01(\x08\x12\x13\n\x0b\x64\x65\x64up_state\x18\x06 \x01(\t\x12\x1a\n\x12storage_model_type\x18\x07 \x01(\t\x12\x14\n\x0cstorage_type\x18\x08 \x01(\t\x12\x1a\n\x12storage_type_state\x18\t \x01(\t\x12\x13\n\x0bxcool_state\x18\n \x01(\t\x12\x66\n\x04tags\x18\x0b \x03(\x0b\x32X.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupstorageconfig.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"i\n VaultsBackupResourceGuardProxies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xd8\x02\n\x14VaultsBackupPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1d\n\x15protected_items_count\x18\x05 \x01(\x05\x12)\n!resource_guard_operation_requests\x18\x06 \x03(\t\x12\x61\n\x04tags\x18\x07 \x03(\x0b\x32S.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupPolicies.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x06\n5VaultsBackupFabricsProtectionContainersProtectedItems\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1e\n\x16\x62\x61\x63kup_management_type\x18\x05 \x01(\t\x12\x17\n\x0f\x62\x61\x63kup_set_name\x18\x06 \x01(\t\x12\x16\n\x0e\x63ontainer_name\x18\x07 \x01(\t\x12\x13\n\x0b\x63reate_mode\x18\x08 \x01(\t\x12%\n\x1d\x64\x65\x66\x65rred_delete_time_in_u_t_c\x18\t \x01(\t\x12&\n\x1e\x64\x65\x66\x65rred_delete_time_remaining\x18\n \x01(\t\x12\x1a\n\x12is_archive_enabled\x18\x0b \x01(\x08\x12,\n$is_deferred_delete_schedule_upcoming\x18\x0c \x01(\x08\x12\x14\n\x0cis_rehydrate\x18\r \x01(\x08\x12(\n is_scheduled_for_deferred_delete\x18\x0e \x01(\x08\x12\x1b\n\x13last_recovery_point\x18\x0f \x01(\t\x12\x11\n\tpolicy_id\x18\x10 \x01(\t\x12\x13\n\x0bpolicy_name\x18\x11 \x01(\t\x12)\n!resource_guard_operation_requests\x18\x12 \x03(\t\x12\x1a\n\x12source_resource_id\x18\x13 \x01(\t\x12\x15\n\rworkload_type\x18\x14 \x01(\t\x12\x82\x01\n\x04tags\x18\x15 \x03(\x0b\x32t.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsProtectionContainersProtectedItems.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf2\x04\n\'VaultsBackupFabricsProtectionContainers\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1e\n\x16\x62\x61\x63kup_management_type\x18\x05 \x01(\t\x12\x15\n\rfriendly_name\x18\x06 \x01(\t\x12\x15\n\rhealth_status\x18\x07 \x01(\t\x12\x1f\n\x17protectable_object_type\x18\x08 \x01(\t\x12\x1b\n\x13registration_status\x18\t \x01(\t\x12t\n\x04tags\x18\n \x03(\x0b\x32\x66.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsProtectionContainers.TagsEntry\x12\xaf\x01\n;vaults_backup_fabrics_protection_containers_protected_items\x18\x0b \x03(\x0b\x32j.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsProtectionContainersProtectedItems\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb2\x03\n)VaultsBackupFabricsBackupProtectionIntent\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1e\n\x16\x62\x61\x63kup_management_type\x18\x05 \x01(\t\x12\x0f\n\x07item_id\x18\x06 \x01(\t\x12\x11\n\tpolicy_id\x18\x07 \x01(\t\x12\x18\n\x10protection_state\x18\x08 \x01(\t\x12\x1a\n\x12source_resource_id\x18\t \x01(\t\x12v\n\x04tags\x18\n \x03(\x0b\x32h.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupFabricsBackupProtectionIntent.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb0\x03\n\x1dVaultsBackupEncryptionConfigs\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1f\n\x17\x65ncryption_at_rest_type\x18\x05 \x01(\t\x12\'\n\x1finfrastructure_encryption_state\x18\x06 \x01(\t\x12\x0f\n\x07key_uri\x18\x07 \x01(\t\x12\x1a\n\x12last_update_status\x18\x08 \x01(\t\x12\x17\n\x0fsubscription_id\x18\t \x01(\t\x12j\n\x04tags\x18\n \x03(\x0b\x32\\.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupEncryptionConfigs.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf6\x03\n\x12VaultsBackupconfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05\x65_tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1f\n\x17\x65nhanced_security_state\x18\x05 \x01(\t\x12-\n%is_soft_delete_feature_state_editable\x18\x06 \x01(\x08\x12)\n!resource_guard_operation_requests\x18\x07 \x03(\t\x12!\n\x19soft_delete_feature_state\x18\x08 \x01(\t\x12\x1a\n\x12storage_model_type\x18\t \x01(\t\x12\x14\n\x0cstorage_type\x18\n \x01(\t\x12\x1a\n\x12storage_type_state\x18\x0b \x01(\t\x12_\n\x04tags\x18\x0c \x03(\x0b\x32Q.oak9.tython.azure.microsoft_recoveryservices_backup.VaultsBackupconfig.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_recoveryservices_backup_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VAULTSPRIVATEENDPOINTCONNECTIONS_TAGSENTRY._options = None
  _VAULTSPRIVATEENDPOINTCONNECTIONS_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPSTORAGECONFIG_TAGSENTRY._options = None
  _VAULTSBACKUPSTORAGECONFIG_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPPOLICIES_TAGSENTRY._options = None
  _VAULTSBACKUPPOLICIES_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS_TAGSENTRY._options = None
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS_TAGSENTRY._options = None
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT_TAGSENTRY._options = None
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPENCRYPTIONCONFIGS_TAGSENTRY._options = None
  _VAULTSBACKUPENCRYPTIONCONFIGS_TAGSENTRY._serialized_options = b'8\001'
  _VAULTSBACKUPCONFIG_TAGSENTRY._options = None
  _VAULTSBACKUPCONFIG_TAGSENTRY._serialized_options = b'8\001'
  _MICROSOFT_RECOVERYSERVICES_BACKUP._serialized_start=130
  _MICROSOFT_RECOVERYSERVICES_BACKUP._serialized_end=1184
  _VAULTSPRIVATEENDPOINTCONNECTIONS._serialized_start=1187
  _VAULTSPRIVATEENDPOINTCONNECTIONS._serialized_end=1741
  _VAULTSPRIVATEENDPOINTCONNECTIONS_TAGSENTRY._serialized_start=1698
  _VAULTSPRIVATEENDPOINTCONNECTIONS_TAGSENTRY._serialized_end=1741
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_start=1743
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_end=1840
  _PRIVATEENDPOINT._serialized_start=1842
  _PRIVATEENDPOINT._serialized_end=1871
  _VAULTSBACKUPSTORAGECONFIG._serialized_start=1874
  _VAULTSBACKUPSTORAGECONFIG._serialized_end=2309
  _VAULTSBACKUPSTORAGECONFIG_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPSTORAGECONFIG_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPRESOURCEGUARDPROXIES._serialized_start=2311
  _VAULTSBACKUPRESOURCEGUARDPROXIES._serialized_end=2416
  _VAULTSBACKUPPOLICIES._serialized_start=2419
  _VAULTSBACKUPPOLICIES._serialized_end=2763
  _VAULTSBACKUPPOLICIES_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPPOLICIES_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS._serialized_start=2766
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS._serialized_end=3585
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERSPROTECTEDITEMS_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS._serialized_start=3588
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS._serialized_end=4214
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPFABRICSPROTECTIONCONTAINERS_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT._serialized_start=4217
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT._serialized_end=4651
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPFABRICSBACKUPPROTECTIONINTENT_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPENCRYPTIONCONFIGS._serialized_start=4654
  _VAULTSBACKUPENCRYPTIONCONFIGS._serialized_end=5086
  _VAULTSBACKUPENCRYPTIONCONFIGS_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPENCRYPTIONCONFIGS_TAGSENTRY._serialized_end=1741
  _VAULTSBACKUPCONFIG._serialized_start=5089
  _VAULTSBACKUPCONFIG._serialized_end=5591
  _VAULTSBACKUPCONFIG_TAGSENTRY._serialized_start=1698
  _VAULTSBACKUPCONFIG_TAGSENTRY._serialized_end=1741
# @@protoc_insertion_point(module_scope)
