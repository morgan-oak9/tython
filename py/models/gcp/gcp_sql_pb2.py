# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_sql.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11gcp/gcp_sql.proto\x12\x13oak9.tython.gcp.sql\x1a\x13shared/shared.proto\"F\n\x14SqlDatabaseXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xf7\x01\n\x0bSqlDatabase\x12\x0f\n\x07\x63harset\x18\x01 \x01(\t\x12\x11\n\tcollation\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x11\n\tself_link\x18\x07 \x01(\t\x12;\n\x08timeouts\x18\x08 \x01(\x0b\x32).oak9.tython.gcp.sql.SqlDatabaseXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xbf\x02\n(SqlDatabaseInstanceXReplicaConfiguration\x12\x16\n\x0e\x63\x61_certificate\x18\x01 \x01(\t\x12\x1a\n\x12\x63lient_certificate\x18\x02 \x01(\t\x12\x12\n\nclient_key\x18\x03 \x01(\t\x12\x1e\n\x16\x63onnect_retry_interval\x18\x04 \x01(\x01\x12\x16\n\x0e\x64ump_file_path\x18\x05 \x01(\t\x12\x17\n\x0f\x66\x61ilover_target\x18\x06 \x01(\x08\x12\x1f\n\x17master_heartbeat_period\x18\x07 \x01(\x01\x12\x10\n\x08password\x18\x08 \x01(\t\x12\x12\n\nssl_cipher\x18\t \x01(\t\x12\x10\n\x08username\x18\n \x01(\t\x12!\n\x19verify_server_certificate\x18\x0b \x01(\x08\"g\n(SqlDatabaseInstanceXRestoreBackupContext\x12\x15\n\rbackup_run_id\x18\x01 \x01(\x01\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\"D\n2SqlDatabaseInstanceXSettingsXActiveDirectoryConfig\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\"|\nHSqlDatabaseInstanceXSettingsXBackupConfigurationXBackupRetentionSettings\x12\x18\n\x10retained_backups\x18\x01 \x01(\x01\x12\x16\n\x0eretention_unit\x18\x02 \x01(\t\"\xd8\x02\n0SqlDatabaseInstanceXSettingsXBackupConfiguration\x12\x1a\n\x12\x62inary_log_enabled\x18\x01 \x01(\x08\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x10\n\x08location\x18\x03 \x01(\t\x12&\n\x1epoint_in_time_recovery_enabled\x18\x04 \x01(\x08\x12\x12\n\nstart_time\x18\x05 \x01(\t\x12&\n\x1etransaction_log_retention_days\x18\x06 \x01(\x01\x12\x80\x01\n\x19\x62\x61\x63kup_retention_settings\x18\x07 \x01(\x0b\x32].oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXBackupConfigurationXBackupRetentionSettings\"I\n*SqlDatabaseInstanceXSettingsXDatabaseFlags\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xaa\x01\n+SqlDatabaseInstanceXSettingsXInsightsConfig\x12\x1e\n\x16query_insights_enabled\x18\x01 \x01(\x08\x12\x1b\n\x13query_string_length\x18\x02 \x01(\x01\x12\x1f\n\x17record_application_tags\x18\x03 \x01(\x08\x12\x1d\n\x15record_client_address\x18\x04 \x01(\x08\"w\n?SqlDatabaseInstanceXSettingsXIpConfigurationXAuthorizedNetworks\x12\x17\n\x0f\x65xpiration_time\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x81\x02\n,SqlDatabaseInstanceXSettingsXIpConfiguration\x12\x1a\n\x12\x61llocated_ip_range\x18\x01 \x01(\t\x12\x14\n\x0cipv4_enabled\x18\x02 \x01(\x08\x12\x17\n\x0fprivate_network\x18\x03 \x01(\t\x12\x13\n\x0brequire_ssl\x18\x04 \x01(\x08\x12q\n\x13\x61uthorized_networks\x18\x05 \x03(\x0b\x32T.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXIpConfigurationXAuthorizedNetworks\"w\n/SqlDatabaseInstanceXSettingsXLocationPreference\x12\x1e\n\x16\x66ollow_gae_application\x18\x01 \x01(\t\x12\x16\n\x0esecondary_zone\x18\x02 \x01(\t\x12\x0c\n\x04zone\x18\x03 \x01(\t\"a\n.SqlDatabaseInstanceXSettingsXMaintenanceWindow\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x01\x12\x0c\n\x04hour\x18\x02 \x01(\x01\x12\x14\n\x0cupdate_track\x18\x03 \x01(\t\"x\n1SqlDatabaseInstanceXSettingsXSqlServerAuditConfig\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x1a\n\x12retention_interval\x18\x02 \x01(\t\x12\x17\n\x0fupload_interval\x18\x03 \x01(\t\"\x92\t\n\x1cSqlDatabaseInstanceXSettings\x12\x19\n\x11\x61\x63tivation_policy\x18\x01 \x01(\t\x12\x19\n\x11\x61vailability_type\x18\x02 \x01(\t\x12\x11\n\tcollation\x18\x03 \x01(\t\x12\x17\n\x0f\x64isk_autoresize\x18\x04 \x01(\x08\x12\x1d\n\x15\x64isk_autoresize_limit\x18\x05 \x01(\x01\x12\x11\n\tdisk_size\x18\x06 \x01(\x01\x12\x11\n\tdisk_type\x18\x07 \x01(\t\x12\x14\n\x0cpricing_plan\x18\x08 \x01(\t\x12\x0c\n\x04tier\x18\t \x01(\t\x12V\n\x0buser_labels\x18\n \x03(\x0b\x32\x41.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettings.UserLabelsEntry\x12\x0f\n\x07version\x18\x0b \x01(\x01\x12h\n\x17\x61\x63tive_directory_config\x18\x0c \x01(\x0b\x32G.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXActiveDirectoryConfig\x12\x63\n\x14\x62\x61\x63kup_configuration\x18\r \x01(\x0b\x32\x45.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXBackupConfiguration\x12W\n\x0e\x64\x61tabase_flags\x18\x0e \x03(\x0b\x32?.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXDatabaseFlags\x12Y\n\x0finsights_config\x18\x0f \x01(\x0b\x32@.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXInsightsConfig\x12[\n\x10ip_configuration\x18\x10 \x01(\x0b\x32\x41.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXIpConfiguration\x12\x61\n\x13location_preference\x18\x11 \x01(\x0b\x32\x44.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXLocationPreference\x12_\n\x12maintenance_window\x18\x12 \x01(\x0b\x32\x43.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXMaintenanceWindow\x12g\n\x17sql_server_audit_config\x18\x13 \x01(\x0b\x32\x46.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettingsXSqlServerAuditConfig\x1a\x31\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"N\n\x1cSqlDatabaseInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x85\x08\n\x13SqlDatabaseInstance\x12\x17\n\x0f\x63onnection_name\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61tabase_version\x18\x02 \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x03 \x01(\x08\x12\x1b\n\x13\x65ncryption_key_name\x18\x04 \x01(\t\x12\x18\n\x10\x66irst_ip_address\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12K\n\nip_address\x18\x07 \x03(\x0b\x32\x37.oak9.tython.gcp.sql.SqlDatabaseInstance.IpAddressEntry\x12\x1c\n\x14master_instance_name\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x1a\n\x12private_ip_address\x18\n \x01(\t\x12\x0f\n\x07project\x18\x0b \x01(\t\x12\x19\n\x11public_ip_address\x18\x0c \x01(\t\x12\x0e\n\x06region\x18\r \x01(\t\x12\x15\n\rroot_password\x18\x0e \x01(\t\x12\x11\n\tself_link\x18\x0f \x01(\t\x12R\n\x0eserver_ca_cert\x18\x10 \x03(\x0b\x32:.oak9.tython.gcp.sql.SqlDatabaseInstance.ServerCaCertEntry\x12%\n\x1dservice_account_email_address\x18\x11 \x01(\t\x12\\\n\x15replica_configuration\x18\x12 \x01(\x0b\x32=.oak9.tython.gcp.sql.SqlDatabaseInstanceXReplicaConfiguration\x12]\n\x16restore_backup_context\x18\x13 \x01(\x0b\x32=.oak9.tython.gcp.sql.SqlDatabaseInstanceXRestoreBackupContext\x12\x43\n\x08settings\x18\x14 \x01(\x0b\x32\x31.oak9.tython.gcp.sql.SqlDatabaseInstanceXSettings\x12\x43\n\x08timeouts\x18\x15 \x01(\x0b\x32\x31.oak9.tython.gcp.sql.SqlDatabaseInstanceXTimeouts\x12\x37\n\rresource_info\x18\x16 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a\x30\n\x0eIpAddressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11ServerCaCertEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n(SqlSourceRepresentationInstanceXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\x9c\x02\n\x1fSqlSourceRepresentationInstance\x12\x18\n\x10\x64\x61tabase_version\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x01\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0e\n\x06region\x18\x07 \x01(\t\x12O\n\x08timeouts\x18\x08 \x01(\x0b\x32=.oak9.tython.gcp.sql.SqlSourceRepresentationInstanceXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"5\n\x13SqlSslCertXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xe4\x02\n\nSqlSslCert\x12\x0c\n\x04\x63\x65rt\x18\x01 \x01(\t\x12\x1a\n\x12\x63\x65rt_serial_number\x18\x02 \x01(\t\x12\x13\n\x0b\x63ommon_name\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x04 \x01(\t\x12\x17\n\x0f\x65xpiration_time\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x10\n\x08instance\x18\x07 \x01(\t\x12\x13\n\x0bprivate_key\x18\x08 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12\x16\n\x0eserver_ca_cert\x18\n \x01(\t\x12\x18\n\x10sha1_fingerprint\x18\x0b \x01(\t\x12:\n\x08timeouts\x18\x0c \x01(\x0b\x32(.oak9.tython.gcp.sql.SqlSslCertXTimeouts\x12\x37\n\rresource_info\x18\r \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"F\n\x1cSqlUserXSqlServerUserDetails\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12\x14\n\x0cserver_roles\x18\x02 \x03(\t\"B\n\x10SqlUserXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xd3\x02\n\x07SqlUser\x12\x17\n\x0f\x64\x65letion_policy\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08instance\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12R\n\x17sql_server_user_details\x18\t \x01(\x0b\x32\x31.oak9.tython.gcp.sql.SqlUserXSqlServerUserDetails\x12\x37\n\x08timeouts\x18\n \x01(\x0b\x32%.oak9.tython.gcp.sql.SqlUserXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_sql_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SQLDATABASEINSTANCEXSETTINGS_USERLABELSENTRY._options = None
  _SQLDATABASEINSTANCEXSETTINGS_USERLABELSENTRY._serialized_options = b'8\001'
  _SQLDATABASEINSTANCE_IPADDRESSENTRY._options = None
  _SQLDATABASEINSTANCE_IPADDRESSENTRY._serialized_options = b'8\001'
  _SQLDATABASEINSTANCE_SERVERCACERTENTRY._options = None
  _SQLDATABASEINSTANCE_SERVERCACERTENTRY._serialized_options = b'8\001'
  _SQLDATABASEXTIMEOUTS._serialized_start=63
  _SQLDATABASEXTIMEOUTS._serialized_end=133
  _SQLDATABASE._serialized_start=136
  _SQLDATABASE._serialized_end=383
  _SQLDATABASEINSTANCEXREPLICACONFIGURATION._serialized_start=386
  _SQLDATABASEINSTANCEXREPLICACONFIGURATION._serialized_end=705
  _SQLDATABASEINSTANCEXRESTOREBACKUPCONTEXT._serialized_start=707
  _SQLDATABASEINSTANCEXRESTOREBACKUPCONTEXT._serialized_end=810
  _SQLDATABASEINSTANCEXSETTINGSXACTIVEDIRECTORYCONFIG._serialized_start=812
  _SQLDATABASEINSTANCEXSETTINGSXACTIVEDIRECTORYCONFIG._serialized_end=880
  _SQLDATABASEINSTANCEXSETTINGSXBACKUPCONFIGURATIONXBACKUPRETENTIONSETTINGS._serialized_start=882
  _SQLDATABASEINSTANCEXSETTINGSXBACKUPCONFIGURATIONXBACKUPRETENTIONSETTINGS._serialized_end=1006
  _SQLDATABASEINSTANCEXSETTINGSXBACKUPCONFIGURATION._serialized_start=1009
  _SQLDATABASEINSTANCEXSETTINGSXBACKUPCONFIGURATION._serialized_end=1353
  _SQLDATABASEINSTANCEXSETTINGSXDATABASEFLAGS._serialized_start=1355
  _SQLDATABASEINSTANCEXSETTINGSXDATABASEFLAGS._serialized_end=1428
  _SQLDATABASEINSTANCEXSETTINGSXINSIGHTSCONFIG._serialized_start=1431
  _SQLDATABASEINSTANCEXSETTINGSXINSIGHTSCONFIG._serialized_end=1601
  _SQLDATABASEINSTANCEXSETTINGSXIPCONFIGURATIONXAUTHORIZEDNETWORKS._serialized_start=1603
  _SQLDATABASEINSTANCEXSETTINGSXIPCONFIGURATIONXAUTHORIZEDNETWORKS._serialized_end=1722
  _SQLDATABASEINSTANCEXSETTINGSXIPCONFIGURATION._serialized_start=1725
  _SQLDATABASEINSTANCEXSETTINGSXIPCONFIGURATION._serialized_end=1982
  _SQLDATABASEINSTANCEXSETTINGSXLOCATIONPREFERENCE._serialized_start=1984
  _SQLDATABASEINSTANCEXSETTINGSXLOCATIONPREFERENCE._serialized_end=2103
  _SQLDATABASEINSTANCEXSETTINGSXMAINTENANCEWINDOW._serialized_start=2105
  _SQLDATABASEINSTANCEXSETTINGSXMAINTENANCEWINDOW._serialized_end=2202
  _SQLDATABASEINSTANCEXSETTINGSXSQLSERVERAUDITCONFIG._serialized_start=2204
  _SQLDATABASEINSTANCEXSETTINGSXSQLSERVERAUDITCONFIG._serialized_end=2324
  _SQLDATABASEINSTANCEXSETTINGS._serialized_start=2327
  _SQLDATABASEINSTANCEXSETTINGS._serialized_end=3497
  _SQLDATABASEINSTANCEXSETTINGS_USERLABELSENTRY._serialized_start=3448
  _SQLDATABASEINSTANCEXSETTINGS_USERLABELSENTRY._serialized_end=3497
  _SQLDATABASEINSTANCEXTIMEOUTS._serialized_start=3499
  _SQLDATABASEINSTANCEXTIMEOUTS._serialized_end=3577
  _SQLDATABASEINSTANCE._serialized_start=3580
  _SQLDATABASEINSTANCE._serialized_end=4609
  _SQLDATABASEINSTANCE_IPADDRESSENTRY._serialized_start=4508
  _SQLDATABASEINSTANCE_IPADDRESSENTRY._serialized_end=4556
  _SQLDATABASEINSTANCE_SERVERCACERTENTRY._serialized_start=4558
  _SQLDATABASEINSTANCE_SERVERCACERTENTRY._serialized_end=4609
  _SQLSOURCEREPRESENTATIONINSTANCEXTIMEOUTS._serialized_start=4611
  _SQLSOURCEREPRESENTATIONINSTANCEXTIMEOUTS._serialized_end=4685
  _SQLSOURCEREPRESENTATIONINSTANCE._serialized_start=4688
  _SQLSOURCEREPRESENTATIONINSTANCE._serialized_end=4972
  _SQLSSLCERTXTIMEOUTS._serialized_start=4974
  _SQLSSLCERTXTIMEOUTS._serialized_end=5027
  _SQLSSLCERT._serialized_start=5030
  _SQLSSLCERT._serialized_end=5386
  _SQLUSERXSQLSERVERUSERDETAILS._serialized_start=5388
  _SQLUSERXSQLSERVERUSERDETAILS._serialized_end=5458
  _SQLUSERXTIMEOUTS._serialized_start=5460
  _SQLUSERXTIMEOUTS._serialized_end=5526
  _SQLUSER._serialized_start=5529
  _SQLUSER._serialized_end=5868
# @@protoc_insertion_point(module_scope)