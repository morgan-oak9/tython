# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_sql_managedinstances.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0azure/azure_microsoft_sql_managedinstances.proto\x12\x30oak9.tython.azure.microsoft_sql_managedinstances\x1a\x13shared/shared.proto\"\x92\x01\n\x1eMicrosoft_Sql_ManagedInstances\x12p\n\x1bmanaged_instances_databases\x18\x01 \x03(\x0b\x32K.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabases\"\xd4\x02\n(ManagedInstancesVulnerabilityAssessments\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12z\n\x0frecurring_scans\x18\x03 \x01(\x0b\x32\x61.oak9.tython.azure.microsoft_sql_managedinstances.VulnerabilityAssessmentRecurringScansProperties\x12\"\n\x1astorage_account_access_key\x18\x04 \x01(\t\x12\x1e\n\x16storage_container_path\x18\x05 \x01(\t\x12!\n\x19storage_container_sas_key\x18\x06 \x01(\t\"p\n\x18ManagedInstancesSqlAgent\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\"\x85\x01\n\'ManagedInstancesServerTrustCertificates\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpublic_blob\x18\x03 \x01(\t\"\xa3\x02\n%ManagedInstancesSecurityAlertPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0f\x64isabled_alerts\x18\x03 \x03(\t\x12\x1c\n\x14\x65mail_account_admins\x18\x04 \x01(\x08\x12\x17\n\x0f\x65mail_addresses\x18\x05 \x03(\t\x12\x16\n\x0eretention_days\x18\x06 \x01(\x05\x12\r\n\x05state\x18\x07 \x01(\t\x12\"\n\x1astorage_account_access_key\x18\x08 \x01(\t\x12\x18\n\x10storage_endpoint\x18\t \x01(\t\"\xab\x01\nJManagedInstancesRestorableDroppedDatabasesBackupShortTermRetentionPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eretention_days\x18\x03 \x01(\x05\"\x83\x03\n*ManagedInstancesPrivateEndpointConnections\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12r\n\x10private_endpoint\x18\x03 \x01(\x0b\x32X.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancePrivateEndpointProperty\x12\x99\x01\n%private_link_service_connection_state\x18\x04 \x01(\x0b\x32j.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancePrivateLinkServiceConnectionStateProperty\"_\n8ManagedInstancePrivateLinkServiceConnectionStateProperty\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"4\n&ManagedInstancePrivateEndpointProperty\x12\n\n\x02id\x18\x01 \x01(\t\"\x83\x01\n\x14ManagedInstancesKeys\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0fserver_key_type\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\"\xbd\x01\n#ManagedInstancesEncryptionProtector\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x15\x61uto_rotation_enabled\x18\x03 \x01(\x08\x12\x17\n\x0fserver_key_name\x18\x04 \x01(\t\x12\x17\n\x0fserver_key_type\x18\x05 \x01(\t\"\x96\x02\n-ManagedInstancesDistributedAvailabilityGroups\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x1fprimary_availability_group_name\x18\x03 \x01(\t\x12\x18\n\x10replication_mode\x18\x04 \x01(\t\x12)\n!secondary_availability_group_name\x18\x05 \x01(\t\x12\x17\n\x0fsource_endpoint\x18\x06 \x01(\t\x12\x17\n\x0ftarget_database\x18\x07 \x01(\t\"\x85\x02\n?ManagedInstancesDatabasesVulnerabilityAssessmentsRulesBaselines\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12{\n\x10\x62\x61seline_results\x18\x03 \x03(\x0b\x32\x61.oak9.tython.azure.microsoft_sql_managedinstances.DatabaseVulnerabilityAssessmentRuleBaselineItem\"A\n/DatabaseVulnerabilityAssessmentRuleBaselineItem\x12\x0e\n\x06result\x18\x01 \x03(\t\"\xdd\x02\n1ManagedInstancesDatabasesVulnerabilityAssessments\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12z\n\x0frecurring_scans\x18\x03 \x01(\x0b\x32\x61.oak9.tython.azure.microsoft_sql_managedinstances.VulnerabilityAssessmentRecurringScansProperties\x12\"\n\x1astorage_account_access_key\x18\x04 \x01(\t\x12\x1e\n\x16storage_container_path\x18\x05 \x01(\t\x12!\n\x19storage_container_sas_key\x18\x06 \x01(\t\"x\n/VulnerabilityAssessmentRecurringScansProperties\x12\x0e\n\x06\x65mails\x18\x01 \x03(\t\x12!\n\x19\x65mail_subscription_admins\x18\x02 \x01(\x08\x12\x12\n\nis_enabled\x18\x03 \x01(\x08\"\x8a\x01\n2ManagedInstancesDatabasesTransparentDataEncryption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\"\xac\x02\n.ManagedInstancesDatabasesSecurityAlertPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0f\x64isabled_alerts\x18\x03 \x03(\t\x12\x1c\n\x14\x65mail_account_admins\x18\x04 \x01(\x08\x12\x17\n\x0f\x65mail_addresses\x18\x05 \x03(\t\x12\x16\n\x0eretention_days\x18\x06 \x01(\x05\x12\r\n\x05state\x18\x07 \x01(\t\x12\"\n\x1astorage_account_access_key\x18\x08 \x01(\t\x12\x18\n\x10storage_endpoint\x18\t \x01(\t\"\xf2\x01\n>ManagedInstancesDatabasesSchemasTablesColumnsSensitivityLabels\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10information_type\x18\x03 \x01(\t\x12\x1b\n\x13information_type_id\x18\x04 \x01(\t\x12\x10\n\x08label_id\x18\x05 \x01(\t\x12\x12\n\nlabel_name\x18\x06 \x01(\t\x12\x0c\n\x04rank\x18\x07 \x01(\t\"\x9a\x01\n9ManagedInstancesDatabasesBackupShortTermRetentionPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eretention_days\x18\x03 \x01(\x05\"\xe6\x01\n8ManagedInstancesDatabasesBackupLongTermRetentionPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11monthly_retention\x18\x03 \x01(\t\x12\x18\n\x10weekly_retention\x18\x04 \x01(\t\x12\x14\n\x0cweek_of_year\x18\x05 \x01(\x05\x12\x18\n\x10yearly_retention\x18\x06 \x01(\t\"\xd5\x0b\n\x19ManagedInstancesDatabases\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1d\n\x15\x61uto_complete_restore\x18\x04 \x01(\x08\x12\x19\n\x11\x63\x61talog_collation\x18\x05 \x01(\t\x12\x11\n\tcollation\x18\x06 \x01(\t\x12\x13\n\x0b\x63reate_mode\x18\x07 \x01(\t\x12\x18\n\x10last_backup_name\x18\x08 \x01(\t\x12.\n&long_term_retention_backup_resource_id\x18\t \x01(\t\x12\x1f\n\x17recoverable_database_id\x18\n \x01(\t\x12&\n\x1erestorable_dropped_database_id\x18\x0b \x01(\t\x12\x1d\n\x15restore_point_in_time\x18\x0c \x01(\t\x12\x1a\n\x12source_database_id\x18\r \x01(\t\x12#\n\x1bstorage_container_sas_token\x18\x0e \x01(\t\x12\x1d\n\x15storage_container_uri\x18\x0f \x01(\t\x12\x63\n\x04tags\x18\x10 \x03(\x0b\x32U.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabases.TagsEntry\x12\xb5\x01\n@managed_instances_databases_backup_short_term_retention_policies\x18\x11 \x03(\x0b\x32k.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabasesBackupShortTermRetentionPolicies\x12\x9d\x01\n3managed_instances_databases_security_alert_policies\x18\x12 \x03(\x0b\x32`.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabasesSecurityAlertPolicies\x12\xa5\x01\n7managed_instances_databases_transparent_data_encryption\x18\x13 \x03(\x0b\x32\x64.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabasesTransparentDataEncryption\x12\xa2\x01\n5managed_instances_databases_vulnerability_assessments\x18\x14 \x03(\x0b\x32\x63.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabasesVulnerabilityAssessments\x12\xb3\x01\n?managed_instances_databases_backup_long_term_retention_policies\x18\x15 \x03(\x0b\x32j.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDatabasesBackupLongTermRetentionPolicies\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x99\x01\n*ManagedInstancesAzureADOnlyAuthentications\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x1c\x61zure_ad_only_authentication\x18\x03 \x01(\x08\"\xb2\x01\n\x1eManagedInstancesAdministrators\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x64ministrator_type\x18\x03 \x01(\t\x12\r\n\x05login\x18\x04 \x01(\t\x12\x0b\n\x03sid\x18\x05 \x01(\t\x12\x11\n\ttenant_id\x18\x06 \x01(\t\"\x95\x14\n\x10ManagedInstances\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12T\n\x08identity\x18\x02 \x01(\x0b\x32\x42.oak9.tython.azure.microsoft_sql_managedinstances.ResourceIdentity\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1b\n\x13\x61\x64ministrator_login\x18\x05 \x01(\t\x12$\n\x1c\x61\x64ministrator_login_password\x18\x06 \x01(\t\x12n\n\x0e\x61\x64ministrators\x18\x07 \x01(\x0b\x32V.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstanceExternalAdministrator\x12\x11\n\tcollation\x18\x08 \x01(\t\x12\x18\n\x10\x64ns_zone_partner\x18\t \x01(\t\x12\x18\n\x10instance_pool_id\x18\n \x01(\t\x12\x0e\n\x06key_id\x18\x0b \x01(\t\x12\x14\n\x0clicense_type\x18\x0c \x01(\t\x12$\n\x1cmaintenance_configuration_id\x18\r \x01(\t\x12$\n\x1cmanaged_instance_create_mode\x18\x0e \x01(\t\x12\x1b\n\x13minimal_tls_version\x18\x0f \x01(\t\x12)\n!primary_user_assigned_identity_id\x18\x10 \x01(\t\x12\x16\n\x0eproxy_override\x18\x11 \x01(\t\x12$\n\x1cpublic_data_endpoint_enabled\x18\x12 \x01(\x08\x12+\n#requested_backup_storage_redundancy\x18\x13 \x01(\t\x12\x1d\n\x15restore_point_in_time\x18\x14 \x01(\t\x12]\n\x11service_principal\x18\x15 \x01(\x0b\x32\x42.oak9.tython.azure.microsoft_sql_managedinstances.ServicePrincipal\x12\"\n\x1asource_managed_instance_id\x18\x16 \x01(\t\x12\x1a\n\x12storage_size_in_gb\x18\x17 \x01(\x05\x12\x11\n\tsubnet_id\x18\x18 \x01(\t\x12\x13\n\x0btimezone_id\x18\x19 \x01(\t\x12\x0f\n\x07v_cores\x18\x1a \x01(\x05\x12\x16\n\x0ezone_redundant\x18\x1b \x01(\x08\x12\x42\n\x03sku\x18\x1c \x01(\x0b\x32\x35.oak9.tython.azure.microsoft_sql_managedinstances.Sku\x12Z\n\x04tags\x18\x1d \x03(\x0b\x32L.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstances.TagsEntry\x12\x9a\x01\n1managed_instances_distributed_availability_groups\x18\x1e \x03(\x0b\x32_.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesDistributedAvailabilityGroups\x12z\n managed_instances_administrators\x18\x1f \x03(\x0b\x32P.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesAdministrators\x12\x95\x01\n/managed_instances_azure_ad_only_authentications\x18  \x03(\x0b\x32\\.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesAzureADOnlyAuthentications\x12\x85\x01\n&managed_instances_encryption_protector\x18! \x03(\x0b\x32U.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesEncryptionProtector\x12\x66\n\x16managed_instances_keys\x18\" \x03(\x0b\x32\x46.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesKeys\x12\x94\x01\n.managed_instances_private_endpoint_connections\x18# \x03(\x0b\x32\\.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesPrivateEndpointConnections\x12\x8f\x01\n+managed_instances_vulnerability_assessments\x18$ \x03(\x0b\x32Z.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesVulnerabilityAssessments\x12\x8a\x01\n)managed_instances_security_alert_policies\x18% \x03(\x0b\x32W.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesSecurityAlertPolicies\x12\x8e\x01\n+managed_instances_server_trust_certificates\x18& \x03(\x0b\x32Y.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesServerTrustCertificates\x12o\n\x1bmanaged_instances_sql_agent\x18\' \x03(\x0b\x32J.oak9.tython.azure.microsoft_sql_managedinstances.ManagedInstancesSqlAgent\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Q\n\x03Sku\x12\x10\n\x08\x63\x61pacity\x18\x01 \x01(\x05\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\t\" \n\x10ServicePrincipal\x12\x0c\n\x04type\x18\x01 \x01(\t\"\xaf\x01\n$ManagedInstanceExternalAdministrator\x12\x1a\n\x12\x61\x64ministrator_type\x18\x01 \x01(\t\x12$\n\x1c\x61zure_ad_only_authentication\x18\x02 \x01(\x08\x12\r\n\x05login\x18\x03 \x01(\t\x12\x16\n\x0eprincipal_type\x18\x04 \x01(\t\x12\x0b\n\x03sid\x18\x05 \x01(\t\x12\x11\n\ttenant_id\x18\x06 \x01(\t\"\xe2\x01\n\x10ResourceIdentity\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x80\x01\n\x18user_assigned_identities\x18\x02 \x03(\x0b\x32^.oak9.tython.azure.microsoft_sql_managedinstances.ResourceIdentity.UserAssignedIdentitiesEntry\x1a=\n\x1bUserAssignedIdentitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_sql_managedinstances_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MANAGEDINSTANCESDATABASES_TAGSENTRY._options = None
  _MANAGEDINSTANCESDATABASES_TAGSENTRY._serialized_options = b'8\001'
  _MANAGEDINSTANCES_TAGSENTRY._options = None
  _MANAGEDINSTANCES_TAGSENTRY._serialized_options = b'8\001'
  _RESOURCEIDENTITY_USERASSIGNEDIDENTITIESENTRY._options = None
  _RESOURCEIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_options = b'8\001'
  _MICROSOFT_SQL_MANAGEDINSTANCES._serialized_start=124
  _MICROSOFT_SQL_MANAGEDINSTANCES._serialized_end=270
  _MANAGEDINSTANCESVULNERABILITYASSESSMENTS._serialized_start=273
  _MANAGEDINSTANCESVULNERABILITYASSESSMENTS._serialized_end=613
  _MANAGEDINSTANCESSQLAGENT._serialized_start=615
  _MANAGEDINSTANCESSQLAGENT._serialized_end=727
  _MANAGEDINSTANCESSERVERTRUSTCERTIFICATES._serialized_start=730
  _MANAGEDINSTANCESSERVERTRUSTCERTIFICATES._serialized_end=863
  _MANAGEDINSTANCESSECURITYALERTPOLICIES._serialized_start=866
  _MANAGEDINSTANCESSECURITYALERTPOLICIES._serialized_end=1157
  _MANAGEDINSTANCESRESTORABLEDROPPEDDATABASESBACKUPSHORTTERMRETENTIONPOLICIES._serialized_start=1160
  _MANAGEDINSTANCESRESTORABLEDROPPEDDATABASESBACKUPSHORTTERMRETENTIONPOLICIES._serialized_end=1331
  _MANAGEDINSTANCESPRIVATEENDPOINTCONNECTIONS._serialized_start=1334
  _MANAGEDINSTANCESPRIVATEENDPOINTCONNECTIONS._serialized_end=1721
  _MANAGEDINSTANCEPRIVATELINKSERVICECONNECTIONSTATEPROPERTY._serialized_start=1723
  _MANAGEDINSTANCEPRIVATELINKSERVICECONNECTIONSTATEPROPERTY._serialized_end=1818
  _MANAGEDINSTANCEPRIVATEENDPOINTPROPERTY._serialized_start=1820
  _MANAGEDINSTANCEPRIVATEENDPOINTPROPERTY._serialized_end=1872
  _MANAGEDINSTANCESKEYS._serialized_start=1875
  _MANAGEDINSTANCESKEYS._serialized_end=2006
  _MANAGEDINSTANCESENCRYPTIONPROTECTOR._serialized_start=2009
  _MANAGEDINSTANCESENCRYPTIONPROTECTOR._serialized_end=2198
  _MANAGEDINSTANCESDISTRIBUTEDAVAILABILITYGROUPS._serialized_start=2201
  _MANAGEDINSTANCESDISTRIBUTEDAVAILABILITYGROUPS._serialized_end=2479
  _MANAGEDINSTANCESDATABASESVULNERABILITYASSESSMENTSRULESBASELINES._serialized_start=2482
  _MANAGEDINSTANCESDATABASESVULNERABILITYASSESSMENTSRULESBASELINES._serialized_end=2743
  _DATABASEVULNERABILITYASSESSMENTRULEBASELINEITEM._serialized_start=2745
  _DATABASEVULNERABILITYASSESSMENTRULEBASELINEITEM._serialized_end=2810
  _MANAGEDINSTANCESDATABASESVULNERABILITYASSESSMENTS._serialized_start=2813
  _MANAGEDINSTANCESDATABASESVULNERABILITYASSESSMENTS._serialized_end=3162
  _VULNERABILITYASSESSMENTRECURRINGSCANSPROPERTIES._serialized_start=3164
  _VULNERABILITYASSESSMENTRECURRINGSCANSPROPERTIES._serialized_end=3284
  _MANAGEDINSTANCESDATABASESTRANSPARENTDATAENCRYPTION._serialized_start=3287
  _MANAGEDINSTANCESDATABASESTRANSPARENTDATAENCRYPTION._serialized_end=3425
  _MANAGEDINSTANCESDATABASESSECURITYALERTPOLICIES._serialized_start=3428
  _MANAGEDINSTANCESDATABASESSECURITYALERTPOLICIES._serialized_end=3728
  _MANAGEDINSTANCESDATABASESSCHEMASTABLESCOLUMNSSENSITIVITYLABELS._serialized_start=3731
  _MANAGEDINSTANCESDATABASESSCHEMASTABLESCOLUMNSSENSITIVITYLABELS._serialized_end=3973
  _MANAGEDINSTANCESDATABASESBACKUPSHORTTERMRETENTIONPOLICIES._serialized_start=3976
  _MANAGEDINSTANCESDATABASESBACKUPSHORTTERMRETENTIONPOLICIES._serialized_end=4130
  _MANAGEDINSTANCESDATABASESBACKUPLONGTERMRETENTIONPOLICIES._serialized_start=4133
  _MANAGEDINSTANCESDATABASESBACKUPLONGTERMRETENTIONPOLICIES._serialized_end=4363
  _MANAGEDINSTANCESDATABASES._serialized_start=4366
  _MANAGEDINSTANCESDATABASES._serialized_end=5859
  _MANAGEDINSTANCESDATABASES_TAGSENTRY._serialized_start=5816
  _MANAGEDINSTANCESDATABASES_TAGSENTRY._serialized_end=5859
  _MANAGEDINSTANCESAZUREADONLYAUTHENTICATIONS._serialized_start=5862
  _MANAGEDINSTANCESAZUREADONLYAUTHENTICATIONS._serialized_end=6015
  _MANAGEDINSTANCESADMINISTRATORS._serialized_start=6018
  _MANAGEDINSTANCESADMINISTRATORS._serialized_end=6196
  _MANAGEDINSTANCES._serialized_start=6199
  _MANAGEDINSTANCES._serialized_end=8780
  _MANAGEDINSTANCES_TAGSENTRY._serialized_start=5816
  _MANAGEDINSTANCES_TAGSENTRY._serialized_end=5859
  _SKU._serialized_start=8782
  _SKU._serialized_end=8863
  _SERVICEPRINCIPAL._serialized_start=8865
  _SERVICEPRINCIPAL._serialized_end=8897
  _MANAGEDINSTANCEEXTERNALADMINISTRATOR._serialized_start=8900
  _MANAGEDINSTANCEEXTERNALADMINISTRATOR._serialized_end=9075
  _RESOURCEIDENTITY._serialized_start=9078
  _RESOURCEIDENTITY._serialized_end=9304
  _RESOURCEIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_start=9243
  _RESOURCEIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_end=9304
# @@protoc_insertion_point(module_scope)
