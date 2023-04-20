# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_bigquery.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gcp/gcp_bigquery.proto\x12\x18oak9.tython.gcp.bigquery\x1a\x13shared/shared.proto\"J\n!BigqueryConnectionXAwsXAccessRole\x12\x13\n\x0biam_role_id\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\"j\n\x16\x42igqueryConnectionXAws\x12P\n\x0b\x61\x63\x63\x65ss_role\x18\x01 \x01(\x0b\x32;.oak9.tython.gcp.bigquery.BigqueryConnectionXAwsXAccessRole\"\x87\x01\n\x18\x42igqueryConnectionXAzure\x12\x13\n\x0b\x61pplication\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x1a\n\x12\x63ustomer_tenant_id\x18\x03 \x01(\t\x12\x11\n\tobject_id\x18\x04 \x01(\t\x12\x14\n\x0credirect_uri\x18\x05 \x01(\t\">\n BigqueryConnectionXCloudResource\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"L\n\x1f\x42igqueryConnectionXCloudSpanner\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x17\n\x0fuse_parallelism\x18\x02 \x01(\x08\"L\n&BigqueryConnectionXCloudSqlXCredential\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"\xa8\x01\n\x1b\x42igqueryConnectionXCloudSql\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12T\n\ncredential\x18\x04 \x01(\x0b\x32@.oak9.tython.gcp.bigquery.BigqueryConnectionXCloudSqlXCredential\"M\n\x1b\x42igqueryConnectionXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xa0\x05\n\x12\x42igqueryConnection\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x15\n\rfriendly_name\x18\x03 \x01(\t\x12\x16\n\x0ehas_credential\x18\x04 \x01(\x08\x12\n\n\x02id\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07project\x18\x08 \x01(\t\x12=\n\x03\x61ws\x18\t \x01(\x0b\x32\x30.oak9.tython.gcp.bigquery.BigqueryConnectionXAws\x12\x41\n\x05\x61zure\x18\n \x01(\x0b\x32\x32.oak9.tython.gcp.bigquery.BigqueryConnectionXAzure\x12R\n\x0e\x63loud_resource\x18\x0b \x01(\x0b\x32:.oak9.tython.gcp.bigquery.BigqueryConnectionXCloudResource\x12P\n\rcloud_spanner\x18\x0c \x01(\x0b\x32\x39.oak9.tython.gcp.bigquery.BigqueryConnectionXCloudSpanner\x12H\n\tcloud_sql\x18\r \x01(\x0b\x32\x35.oak9.tython.gcp.bigquery.BigqueryConnectionXCloudSql\x12G\n\x08timeouts\x18\x0e \x01(\x0b\x32\x35.oak9.tython.gcp.bigquery.BigqueryConnectionXTimeouts\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"`\n&BigqueryConnectionIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x9f\x02\n\x1c\x42igqueryConnectionIamBinding\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0f\n\x07members\x18\x05 \x03(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12S\n\tcondition\x18\x08 \x01(\x0b\x32@.oak9.tython.gcp.bigquery.BigqueryConnectionIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"_\n%BigqueryConnectionIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x9c\x02\n\x1b\x42igqueryConnectionIamMember\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0e\n\x06member\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12R\n\tcondition\x18\x08 \x01(\x0b\x32?.oak9.tython.gcp.bigquery.BigqueryConnectionIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xbf\x01\n\x1b\x42igqueryConnectionIamPolicy\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"K\n+BigqueryDataTransferConfigXEmailPreferences\x12\x1c\n\x14\x65nable_failure_email\x18\x01 \x01(\x08\"s\n*BigqueryDataTransferConfigXScheduleOptions\x12\x1f\n\x17\x64isable_auto_scheduling\x18\x01 \x01(\x08\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\"G\n*BigqueryDataTransferConfigXSensitiveParams\x12\x19\n\x11secret_access_key\x18\x01 \x01(\t\"U\n#BigqueryDataTransferConfigXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xdb\x06\n\x1a\x42igqueryDataTransferConfig\x12 \n\x18\x64\x61ta_refresh_window_days\x18\x01 \x01(\x01\x12\x16\n\x0e\x64\x61ta_source_id\x18\x02 \x01(\t\x12\x1e\n\x16\x64\x65stination_dataset_id\x18\x03 \x01(\t\x12\x10\n\x08\x64isabled\x18\x04 \x01(\x08\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x10\n\x08location\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12!\n\x19notification_pubsub_topic\x18\t \x01(\t\x12P\n\x06params\x18\n \x03(\x0b\x32@.oak9.tython.gcp.bigquery.BigqueryDataTransferConfig.ParamsEntry\x12\x0f\n\x07project\x18\x0b \x01(\t\x12\x10\n\x08schedule\x18\x0c \x01(\t\x12\x1c\n\x14service_account_name\x18\r \x01(\t\x12`\n\x11\x65mail_preferences\x18\x0e \x01(\x0b\x32\x45.oak9.tython.gcp.bigquery.BigqueryDataTransferConfigXEmailPreferences\x12^\n\x10schedule_options\x18\x0f \x01(\x0b\x32\x44.oak9.tython.gcp.bigquery.BigqueryDataTransferConfigXScheduleOptions\x12^\n\x10sensitive_params\x18\x10 \x01(\x0b\x32\x44.oak9.tython.gcp.bigquery.BigqueryDataTransferConfigXSensitiveParams\x12O\n\x08timeouts\x18\x11 \x01(\x0b\x32=.oak9.tython.gcp.bigquery.BigqueryDataTransferConfigXTimeouts\x12\x37\n\rresource_info\x18\x12 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"P\n&BigqueryDatasetXAccessXDatasetXDataset\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\"\x89\x01\n\x1e\x42igqueryDatasetXAccessXDataset\x12\x14\n\x0ctarget_types\x18\x01 \x03(\t\x12Q\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32@.oak9.tython.gcp.bigquery.BigqueryDatasetXAccessXDatasetXDataset\"W\n\x1b\x42igqueryDatasetXAccessXView\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"\x8c\x02\n\x16\x42igqueryDatasetXAccess\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x16\n\x0egroup_by_email\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\x12\x15\n\rspecial_group\x18\x04 \x01(\t\x12\x15\n\ruser_by_email\x18\x05 \x01(\t\x12I\n\x07\x64\x61taset\x18\x06 \x01(\x0b\x32\x38.oak9.tython.gcp.bigquery.BigqueryDatasetXAccessXDataset\x12\x43\n\x04view\x18\x07 \x01(\x0b\x32\x35.oak9.tython.gcp.bigquery.BigqueryDatasetXAccessXView\"F\n.BigqueryDatasetXDefaultEncryptionConfiguration\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\"J\n\x18\x42igqueryDatasetXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xf1\x05\n\x0f\x42igqueryDataset\x12\x15\n\rcreation_time\x18\x01 \x01(\x01\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\'\n\x1f\x64\x65\x66\x61ult_partition_expiration_ms\x18\x03 \x01(\x01\x12#\n\x1b\x64\x65\x66\x61ult_table_expiration_ms\x18\x04 \x01(\x01\x12\"\n\x1a\x64\x65lete_contents_on_destroy\x18\x05 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04\x65tag\x18\x07 \x01(\t\x12\x15\n\rfriendly_name\x18\x08 \x01(\t\x12\n\n\x02id\x18\t \x01(\t\x12\x45\n\x06labels\x18\n \x03(\x0b\x32\x35.oak9.tython.gcp.bigquery.BigqueryDataset.LabelsEntry\x12\x1a\n\x12last_modified_time\x18\x0b \x01(\x01\x12\x10\n\x08location\x18\x0c \x01(\t\x12\x0f\n\x07project\x18\r \x01(\t\x12\x11\n\tself_link\x18\x0e \x01(\t\x12@\n\x06\x61\x63\x63\x65ss\x18\x0f \x03(\x0b\x32\x30.oak9.tython.gcp.bigquery.BigqueryDatasetXAccess\x12r\n default_encryption_configuration\x18\x10 \x01(\x0b\x32H.oak9.tython.gcp.bigquery.BigqueryDatasetXDefaultEncryptionConfiguration\x12\x44\n\x08timeouts\x18\x11 \x01(\x0b\x32\x32.oak9.tython.gcp.bigquery.BigqueryDatasetXTimeouts\x12\x37\n\rresource_info\x18\x12 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"O\n%BigqueryDatasetAccessXDatasetXDataset\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\"\x87\x01\n\x1d\x42igqueryDatasetAccessXDataset\x12\x14\n\x0ctarget_types\x18\x01 \x03(\t\x12P\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32?.oak9.tython.gcp.bigquery.BigqueryDatasetAccessXDatasetXDataset\"@\n\x1e\x42igqueryDatasetAccessXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"V\n\x1a\x42igqueryDatasetAccessXView\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"\xef\x03\n\x15\x42igqueryDatasetAccess\x12\x1a\n\x12\x61pi_updated_member\x18\x01 \x01(\x08\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x16\n\x0egroup_by_email\x18\x04 \x01(\t\x12\x12\n\niam_member\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x0c\n\x04role\x18\x08 \x01(\t\x12\x15\n\rspecial_group\x18\t \x01(\t\x12\x15\n\ruser_by_email\x18\n \x01(\t\x12H\n\x07\x64\x61taset\x18\x0b \x01(\x0b\x32\x37.oak9.tython.gcp.bigquery.BigqueryDatasetAccessXDataset\x12J\n\x08timeouts\x18\x0c \x01(\x0b\x32\x38.oak9.tython.gcp.bigquery.BigqueryDatasetAccessXTimeouts\x12\x42\n\x04view\x18\r \x01(\x0b\x32\x34.oak9.tython.gcp.bigquery.BigqueryDatasetAccessXView\x12\x37\n\rresource_info\x18\x0e \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"]\n#BigqueryDatasetIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x84\x02\n\x19\x42igqueryDatasetIamBinding\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12P\n\tcondition\x18\x07 \x01(\x0b\x32=.oak9.tython.gcp.bigquery.BigqueryDatasetIamBindingXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\\\n\"BigqueryDatasetIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x81\x02\n\x18\x42igqueryDatasetIamMember\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12O\n\tcondition\x18\x07 \x01(\x0b\x32<.oak9.tython.gcp.bigquery.BigqueryDatasetIamMemberXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa7\x01\n\x18\x42igqueryDatasetIamPolicy\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"d\n3BigqueryJobXCopyXDestinationEncryptionConfiguration\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x12\x17\n\x0fkms_key_version\x18\x02 \x01(\t\"]\n!BigqueryJobXCopyXDestinationTable\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"Y\n\x1d\x42igqueryJobXCopyXSourceTables\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"\xee\x02\n\x10\x42igqueryJobXCopy\x12\x1a\n\x12\x63reate_disposition\x18\x01 \x01(\t\x12\x19\n\x11write_disposition\x18\x02 \x01(\t\x12{\n$destination_encryption_configuration\x18\x03 \x01(\x0b\x32M.oak9.tython.gcp.bigquery.BigqueryJobXCopyXDestinationEncryptionConfiguration\x12V\n\x11\x64\x65stination_table\x18\x04 \x01(\x0b\x32;.oak9.tython.gcp.bigquery.BigqueryJobXCopyXDestinationTable\x12N\n\rsource_tables\x18\x05 \x03(\x0b\x32\x37.oak9.tython.gcp.bigquery.BigqueryJobXCopyXSourceTables\"[\n\x1f\x42igqueryJobXExtractXSourceModel\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\"[\n\x1f\x42igqueryJobXExtractXSourceTable\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"\xd1\x02\n\x13\x42igqueryJobXExtract\x12\x13\n\x0b\x63ompression\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65stination_format\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_uris\x18\x03 \x03(\t\x12\x17\n\x0f\x66ield_delimiter\x18\x04 \x01(\t\x12\x14\n\x0cprint_header\x18\x05 \x01(\x08\x12\x1e\n\x16use_avro_logical_types\x18\x06 \x01(\x08\x12O\n\x0csource_model\x18\x07 \x01(\x0b\x32\x39.oak9.tython.gcp.bigquery.BigqueryJobXExtractXSourceModel\x12O\n\x0csource_table\x18\x08 \x01(\x0b\x32\x39.oak9.tython.gcp.bigquery.BigqueryJobXExtractXSourceTable\"d\n3BigqueryJobXLoadXDestinationEncryptionConfiguration\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x12\x17\n\x0fkms_key_version\x18\x02 \x01(\t\"]\n!BigqueryJobXLoadXDestinationTable\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"W\n!BigqueryJobXLoadXTimePartitioning\x12\x15\n\rexpiration_ms\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\xcc\x05\n\x10\x42igqueryJobXLoad\x12\x19\n\x11\x61llow_jagged_rows\x18\x01 \x01(\x08\x12\x1d\n\x15\x61llow_quoted_newlines\x18\x02 \x01(\x08\x12\x12\n\nautodetect\x18\x03 \x01(\x08\x12\x1a\n\x12\x63reate_disposition\x18\x04 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x05 \x01(\t\x12\x17\n\x0f\x66ield_delimiter\x18\x06 \x01(\t\x12\x1d\n\x15ignore_unknown_values\x18\x07 \x01(\x08\x12\x17\n\x0fmax_bad_records\x18\x08 \x01(\x01\x12\x13\n\x0bnull_marker\x18\t \x01(\t\x12\x19\n\x11projection_fields\x18\n \x03(\t\x12\r\n\x05quote\x18\x0b \x01(\t\x12\x1d\n\x15schema_update_options\x18\x0c \x03(\t\x12\x19\n\x11skip_leading_rows\x18\r \x01(\x01\x12\x15\n\rsource_format\x18\x0e \x01(\t\x12\x13\n\x0bsource_uris\x18\x0f \x03(\t\x12\x19\n\x11write_disposition\x18\x10 \x01(\t\x12{\n$destination_encryption_configuration\x18\x11 \x01(\x0b\x32M.oak9.tython.gcp.bigquery.BigqueryJobXLoadXDestinationEncryptionConfiguration\x12V\n\x11\x64\x65stination_table\x18\x12 \x01(\x0b\x32;.oak9.tython.gcp.bigquery.BigqueryJobXLoadXDestinationTable\x12V\n\x11time_partitioning\x18\x13 \x01(\x0b\x32;.oak9.tython.gcp.bigquery.BigqueryJobXLoadXTimePartitioning\"J\n BigqueryJobXQueryXDefaultDataset\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\"e\n4BigqueryJobXQueryXDestinationEncryptionConfiguration\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x12\x17\n\x0fkms_key_version\x18\x02 \x01(\t\"^\n\"BigqueryJobXQueryXDestinationTable\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t\"|\n\x1f\x42igqueryJobXQueryXScriptOptions\x12\x1c\n\x14key_result_statement\x18\x01 \x01(\t\x12\x1d\n\x15statement_byte_budget\x18\x02 \x01(\t\x12\x1c\n\x14statement_timeout_ms\x18\x03 \x01(\t\"[\n.BigqueryJobXQueryXUserDefinedFunctionResources\x12\x13\n\x0binline_code\x18\x01 \x01(\t\x12\x14\n\x0cresource_uri\x18\x02 \x01(\t\"\xb7\x06\n\x11\x42igqueryJobXQuery\x12\x1b\n\x13\x61llow_large_results\x18\x01 \x01(\x08\x12\x1a\n\x12\x63reate_disposition\x18\x02 \x01(\t\x12\x17\n\x0f\x66latten_results\x18\x03 \x01(\x08\x12\x1c\n\x14maximum_billing_tier\x18\x04 \x01(\x01\x12\x1c\n\x14maximum_bytes_billed\x18\x05 \x01(\t\x12\x16\n\x0eparameter_mode\x18\x06 \x01(\t\x12\x10\n\x08priority\x18\x07 \x01(\t\x12\r\n\x05query\x18\x08 \x01(\t\x12\x1d\n\x15schema_update_options\x18\t \x03(\t\x12\x16\n\x0euse_legacy_sql\x18\n \x01(\x08\x12\x17\n\x0fuse_query_cache\x18\x0b \x01(\x08\x12\x19\n\x11write_disposition\x18\x0c \x01(\t\x12S\n\x0f\x64\x65\x66\x61ult_dataset\x18\r \x01(\x0b\x32:.oak9.tython.gcp.bigquery.BigqueryJobXQueryXDefaultDataset\x12|\n$destination_encryption_configuration\x18\x0e \x01(\x0b\x32N.oak9.tython.gcp.bigquery.BigqueryJobXQueryXDestinationEncryptionConfiguration\x12W\n\x11\x64\x65stination_table\x18\x0f \x01(\x0b\x32<.oak9.tython.gcp.bigquery.BigqueryJobXQueryXDestinationTable\x12Q\n\x0escript_options\x18\x10 \x01(\x0b\x32\x39.oak9.tython.gcp.bigquery.BigqueryJobXQueryXScriptOptions\x12q\n\x1fuser_defined_function_resources\x18\x11 \x03(\x0b\x32H.oak9.tython.gcp.bigquery.BigqueryJobXQueryXUserDefinedFunctionResources\"6\n\x14\x42igqueryJobXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xd9\x05\n\x0b\x42igqueryJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x16\n\x0ejob_timeout_ms\x18\x03 \x01(\t\x12\x10\n\x08job_type\x18\x04 \x01(\t\x12\x41\n\x06labels\x18\x05 \x03(\x0b\x32\x31.oak9.tython.gcp.bigquery.BigqueryJob.LabelsEntry\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x41\n\x06status\x18\x08 \x03(\x0b\x32\x31.oak9.tython.gcp.bigquery.BigqueryJob.StatusEntry\x12\x12\n\nuser_email\x18\t \x01(\t\x12\x38\n\x04\x63opy\x18\n \x01(\x0b\x32*.oak9.tython.gcp.bigquery.BigqueryJobXCopy\x12>\n\x07\x65xtract\x18\x0b \x01(\x0b\x32-.oak9.tython.gcp.bigquery.BigqueryJobXExtract\x12\x38\n\x04load\x18\x0c \x01(\x0b\x32*.oak9.tython.gcp.bigquery.BigqueryJobXLoad\x12:\n\x05query\x18\r \x01(\x0b\x32+.oak9.tython.gcp.bigquery.BigqueryJobXQuery\x12@\n\x08timeouts\x18\x0e \x01(\x0b\x32..oak9.tython.gcp.bigquery.BigqueryJobXTimeouts\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"N\n\x1c\x42igqueryReservationXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x87\x02\n\x13\x42igqueryReservation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11ignore_idle_slots\x18\x02 \x01(\x08\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x15\n\rslot_capacity\x18\x06 \x01(\x01\x12H\n\x08timeouts\x18\x07 \x01(\x0b\x32\x36.oak9.tython.gcp.bigquery.BigqueryReservationXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"H\n&BigqueryReservationAssignmentXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xb1\x02\n\x1d\x42igqueryReservationAssignment\x12\x10\n\x08\x61ssignee\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x13\n\x0breservation\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12R\n\x08timeouts\x18\t \x01(\x0b\x32@.oak9.tython.gcp.bigquery.BigqueryReservationAssignmentXTimeouts\x12\x37\n\rresource_info\x18\n \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"a\n\x19\x42igqueryRoutineXArguments\x12\x15\n\rargument_kind\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\x0c\n\x04mode\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"J\n\x18\x42igqueryRoutineXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x8d\x04\n\x0f\x42igqueryRoutine\x12\x15\n\rcreation_time\x18\x01 \x01(\x01\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66inition_body\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x19\n\x11\x64\x65terminism_level\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x1a\n\x12imported_libraries\x18\x07 \x03(\t\x12\x10\n\x08language\x18\x08 \x01(\t\x12\x1a\n\x12last_modified_time\x18\t \x01(\x01\x12\x0f\n\x07project\x18\n \x01(\t\x12\x19\n\x11return_table_type\x18\x0b \x01(\t\x12\x13\n\x0breturn_type\x18\x0c \x01(\t\x12\x12\n\nroutine_id\x18\r \x01(\t\x12\x14\n\x0croutine_type\x18\x0e \x01(\t\x12\x46\n\targuments\x18\x0f \x03(\x0b\x32\x33.oak9.tython.gcp.bigquery.BigqueryRoutineXArguments\x12\x44\n\x08timeouts\x18\x10 \x01(\x0b\x32\x32.oak9.tython.gcp.bigquery.BigqueryRoutineXTimeouts\x12\x37\n\rresource_info\x18\x11 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"V\n%BigqueryTableXEncryptionConfiguration\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x12\x17\n\x0fkms_key_version\x18\x02 \x01(\t\"\xc3\x01\n2BigqueryTableXExternalDataConfigurationXCsvOptions\x12\x19\n\x11\x61llow_jagged_rows\x18\x01 \x01(\x08\x12\x1d\n\x15\x61llow_quoted_newlines\x18\x02 \x01(\x08\x12\x10\n\x08\x65ncoding\x18\x03 \x01(\t\x12\x17\n\x0f\x66ield_delimiter\x18\x04 \x01(\t\x12\r\n\x05quote\x18\x05 \x01(\t\x12\x19\n\x11skip_leading_rows\x18\x06 \x01(\x01\"a\n5BigqueryTableXExternalDataConfigurationXSheetsOptions\x12\r\n\x05range\x18\x01 \x01(\t\x12\x19\n\x11skip_leading_rows\x18\x02 \x01(\x01\"\x8c\x01\n?BigqueryTableXExternalDataConfigurationXHivePartitioningOptions\x12\x0c\n\x04mode\x18\x01 \x01(\t\x12 \n\x18require_partition_filter\x18\x02 \x01(\x08\x12\x19\n\x11source_uri_prefix\x18\x03 \x01(\t\"\xae\x04\n\'BigqueryTableXExternalDataConfiguration\x12\x12\n\nautodetect\x18\x01 \x01(\x08\x12\x13\n\x0b\x63ompression\x18\x02 \x01(\t\x12\x15\n\rconnection_id\x18\x03 \x01(\t\x12\x1d\n\x15ignore_unknown_values\x18\x04 \x01(\x08\x12\x17\n\x0fmax_bad_records\x18\x05 \x01(\x01\x12\x0e\n\x06schema\x18\x06 \x01(\t\x12\x15\n\rsource_format\x18\x07 \x01(\t\x12\x13\n\x0bsource_uris\x18\x08 \x03(\t\x12\x61\n\x0b\x63sv_options\x18\t \x01(\x0b\x32L.oak9.tython.gcp.bigquery.BigqueryTableXExternalDataConfigurationXCsvOptions\x12n\n\x15google_sheets_options\x18\n \x01(\x0b\x32O.oak9.tython.gcp.bigquery.BigqueryTableXExternalDataConfigurationXSheetsOptions\x12|\n\x19hive_partitioning_options\x18\x0b \x01(\x0b\x32Y.oak9.tython.gcp.bigquery.BigqueryTableXExternalDataConfigurationXHivePartitioningOptions\"d\n\x1e\x42igqueryTableXMaterializedView\x12\x16\n\x0e\x65nable_refresh\x18\x01 \x01(\x08\x12\r\n\x05query\x18\x02 \x01(\t\x12\x1b\n\x13refresh_interval_ms\x18\x03 \x01(\x01\"U\n%BigqueryTableXRangePartitioningXRange\x12\x0b\n\x03\x65nd\x18\x01 \x01(\x01\x12\x10\n\x08interval\x18\x02 \x01(\x01\x12\r\n\x05start\x18\x03 \x01(\x01\"\x80\x01\n\x1f\x42igqueryTableXRangePartitioning\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12N\n\x05range\x18\x02 \x01(\x0b\x32?.oak9.tython.gcp.bigquery.BigqueryTableXRangePartitioningXRange\"v\n\x1e\x42igqueryTableXTimePartitioning\x12\x15\n\rexpiration_ms\x18\x01 \x01(\x01\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12 \n\x18require_partition_filter\x18\x03 \x01(\x08\x12\x0c\n\x04type\x18\x04 \x01(\t\";\n\x12\x42igqueryTableXView\x12\r\n\x05query\x18\x01 \x01(\t\x12\x16\n\x0euse_legacy_sql\x18\x02 \x01(\x08\"\xc3\x08\n\rBigqueryTable\x12\x12\n\nclustering\x18\x01 \x03(\t\x12\x15\n\rcreation_time\x18\x02 \x01(\x01\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04\x65tag\x18\x06 \x01(\t\x12\x17\n\x0f\x65xpiration_time\x18\x07 \x01(\x01\x12\x15\n\rfriendly_name\x18\x08 \x01(\t\x12\n\n\x02id\x18\t \x01(\t\x12\x43\n\x06labels\x18\n \x03(\x0b\x32\x33.oak9.tython.gcp.bigquery.BigqueryTable.LabelsEntry\x12\x1a\n\x12last_modified_time\x18\x0b \x01(\x01\x12\x10\n\x08location\x18\x0c \x01(\t\x12\x11\n\tnum_bytes\x18\r \x01(\x01\x12\x1b\n\x13num_long_term_bytes\x18\x0e \x01(\x01\x12\x10\n\x08num_rows\x18\x0f \x01(\x01\x12\x0f\n\x07project\x18\x10 \x01(\t\x12\x0e\n\x06schema\x18\x11 \x01(\t\x12\x11\n\tself_link\x18\x12 \x01(\t\x12\x10\n\x08table_id\x18\x13 \x01(\t\x12\x0c\n\x04type\x18\x14 \x01(\t\x12\x61\n\x18\x65ncryption_configuration\x18\x15 \x01(\x0b\x32?.oak9.tython.gcp.bigquery.BigqueryTableXEncryptionConfiguration\x12\x66\n\x1b\x65xternal_data_configuration\x18\x16 \x01(\x0b\x32\x41.oak9.tython.gcp.bigquery.BigqueryTableXExternalDataConfiguration\x12S\n\x11materialized_view\x18\x17 \x01(\x0b\x32\x38.oak9.tython.gcp.bigquery.BigqueryTableXMaterializedView\x12U\n\x12range_partitioning\x18\x18 \x01(\x0b\x32\x39.oak9.tython.gcp.bigquery.BigqueryTableXRangePartitioning\x12S\n\x11time_partitioning\x18\x19 \x01(\x0b\x32\x38.oak9.tython.gcp.bigquery.BigqueryTableXTimePartitioning\x12:\n\x04view\x18\x1a \x01(\x0b\x32,.oak9.tython.gcp.bigquery.BigqueryTableXView\x12\x37\n\rresource_info\x18\x1b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"[\n!BigqueryTableIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x92\x02\n\x17\x42igqueryTableIamBinding\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x10\n\x08table_id\x18\x07 \x01(\t\x12N\n\tcondition\x18\x08 \x01(\x0b\x32;.oak9.tython.gcp.bigquery.BigqueryTableIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"Z\n BigqueryTableIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x8f\x02\n\x16\x42igqueryTableIamMember\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x10\n\x08table_id\x18\x07 \x01(\t\x12M\n\tcondition\x18\x08 \x01(\x0b\x32:.oak9.tython.gcp.bigquery.BigqueryTableIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb7\x01\n\x16\x42igqueryTableIamPolicy\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x10\n\x08table_id\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_bigquery_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BIGQUERYDATATRANSFERCONFIG_PARAMSENTRY._options = None
  _BIGQUERYDATATRANSFERCONFIG_PARAMSENTRY._serialized_options = b'8\001'
  _BIGQUERYDATASET_LABELSENTRY._options = None
  _BIGQUERYDATASET_LABELSENTRY._serialized_options = b'8\001'
  _BIGQUERYJOB_LABELSENTRY._options = None
  _BIGQUERYJOB_LABELSENTRY._serialized_options = b'8\001'
  _BIGQUERYJOB_STATUSENTRY._options = None
  _BIGQUERYJOB_STATUSENTRY._serialized_options = b'8\001'
  _BIGQUERYTABLE_LABELSENTRY._options = None
  _BIGQUERYTABLE_LABELSENTRY._serialized_options = b'8\001'
  _BIGQUERYCONNECTIONXAWSXACCESSROLE._serialized_start=73
  _BIGQUERYCONNECTIONXAWSXACCESSROLE._serialized_end=147
  _BIGQUERYCONNECTIONXAWS._serialized_start=149
  _BIGQUERYCONNECTIONXAWS._serialized_end=255
  _BIGQUERYCONNECTIONXAZURE._serialized_start=258
  _BIGQUERYCONNECTIONXAZURE._serialized_end=393
  _BIGQUERYCONNECTIONXCLOUDRESOURCE._serialized_start=395
  _BIGQUERYCONNECTIONXCLOUDRESOURCE._serialized_end=457
  _BIGQUERYCONNECTIONXCLOUDSPANNER._serialized_start=459
  _BIGQUERYCONNECTIONXCLOUDSPANNER._serialized_end=535
  _BIGQUERYCONNECTIONXCLOUDSQLXCREDENTIAL._serialized_start=537
  _BIGQUERYCONNECTIONXCLOUDSQLXCREDENTIAL._serialized_end=613
  _BIGQUERYCONNECTIONXCLOUDSQL._serialized_start=616
  _BIGQUERYCONNECTIONXCLOUDSQL._serialized_end=784
  _BIGQUERYCONNECTIONXTIMEOUTS._serialized_start=786
  _BIGQUERYCONNECTIONXTIMEOUTS._serialized_end=863
  _BIGQUERYCONNECTION._serialized_start=866
  _BIGQUERYCONNECTION._serialized_end=1538
  _BIGQUERYCONNECTIONIAMBINDINGXCONDITION._serialized_start=1540
  _BIGQUERYCONNECTIONIAMBINDINGXCONDITION._serialized_end=1636
  _BIGQUERYCONNECTIONIAMBINDING._serialized_start=1639
  _BIGQUERYCONNECTIONIAMBINDING._serialized_end=1926
  _BIGQUERYCONNECTIONIAMMEMBERXCONDITION._serialized_start=1928
  _BIGQUERYCONNECTIONIAMMEMBERXCONDITION._serialized_end=2023
  _BIGQUERYCONNECTIONIAMMEMBER._serialized_start=2026
  _BIGQUERYCONNECTIONIAMMEMBER._serialized_end=2310
  _BIGQUERYCONNECTIONIAMPOLICY._serialized_start=2313
  _BIGQUERYCONNECTIONIAMPOLICY._serialized_end=2504
  _BIGQUERYDATATRANSFERCONFIGXEMAILPREFERENCES._serialized_start=2506
  _BIGQUERYDATATRANSFERCONFIGXEMAILPREFERENCES._serialized_end=2581
  _BIGQUERYDATATRANSFERCONFIGXSCHEDULEOPTIONS._serialized_start=2583
  _BIGQUERYDATATRANSFERCONFIGXSCHEDULEOPTIONS._serialized_end=2698
  _BIGQUERYDATATRANSFERCONFIGXSENSITIVEPARAMS._serialized_start=2700
  _BIGQUERYDATATRANSFERCONFIGXSENSITIVEPARAMS._serialized_end=2771
  _BIGQUERYDATATRANSFERCONFIGXTIMEOUTS._serialized_start=2773
  _BIGQUERYDATATRANSFERCONFIGXTIMEOUTS._serialized_end=2858
  _BIGQUERYDATATRANSFERCONFIG._serialized_start=2861
  _BIGQUERYDATATRANSFERCONFIG._serialized_end=3720
  _BIGQUERYDATATRANSFERCONFIG_PARAMSENTRY._serialized_start=3675
  _BIGQUERYDATATRANSFERCONFIG_PARAMSENTRY._serialized_end=3720
  _BIGQUERYDATASETXACCESSXDATASETXDATASET._serialized_start=3722
  _BIGQUERYDATASETXACCESSXDATASETXDATASET._serialized_end=3802
  _BIGQUERYDATASETXACCESSXDATASET._serialized_start=3805
  _BIGQUERYDATASETXACCESSXDATASET._serialized_end=3942
  _BIGQUERYDATASETXACCESSXVIEW._serialized_start=3944
  _BIGQUERYDATASETXACCESSXVIEW._serialized_end=4031
  _BIGQUERYDATASETXACCESS._serialized_start=4034
  _BIGQUERYDATASETXACCESS._serialized_end=4302
  _BIGQUERYDATASETXDEFAULTENCRYPTIONCONFIGURATION._serialized_start=4304
  _BIGQUERYDATASETXDEFAULTENCRYPTIONCONFIGURATION._serialized_end=4374
  _BIGQUERYDATASETXTIMEOUTS._serialized_start=4376
  _BIGQUERYDATASETXTIMEOUTS._serialized_end=4450
  _BIGQUERYDATASET._serialized_start=4453
  _BIGQUERYDATASET._serialized_end=5206
  _BIGQUERYDATASET_LABELSENTRY._serialized_start=5161
  _BIGQUERYDATASET_LABELSENTRY._serialized_end=5206
  _BIGQUERYDATASETACCESSXDATASETXDATASET._serialized_start=5208
  _BIGQUERYDATASETACCESSXDATASETXDATASET._serialized_end=5287
  _BIGQUERYDATASETACCESSXDATASET._serialized_start=5290
  _BIGQUERYDATASETACCESSXDATASET._serialized_end=5425
  _BIGQUERYDATASETACCESSXTIMEOUTS._serialized_start=5427
  _BIGQUERYDATASETACCESSXTIMEOUTS._serialized_end=5491
  _BIGQUERYDATASETACCESSXVIEW._serialized_start=5493
  _BIGQUERYDATASETACCESSXVIEW._serialized_end=5579
  _BIGQUERYDATASETACCESS._serialized_start=5582
  _BIGQUERYDATASETACCESS._serialized_end=6077
  _BIGQUERYDATASETIAMBINDINGXCONDITION._serialized_start=6079
  _BIGQUERYDATASETIAMBINDINGXCONDITION._serialized_end=6172
  _BIGQUERYDATASETIAMBINDING._serialized_start=6175
  _BIGQUERYDATASETIAMBINDING._serialized_end=6435
  _BIGQUERYDATASETIAMMEMBERXCONDITION._serialized_start=6437
  _BIGQUERYDATASETIAMMEMBERXCONDITION._serialized_end=6529
  _BIGQUERYDATASETIAMMEMBER._serialized_start=6532
  _BIGQUERYDATASETIAMMEMBER._serialized_end=6789
  _BIGQUERYDATASETIAMPOLICY._serialized_start=6792
  _BIGQUERYDATASETIAMPOLICY._serialized_end=6959
  _BIGQUERYJOBXCOPYXDESTINATIONENCRYPTIONCONFIGURATION._serialized_start=6961
  _BIGQUERYJOBXCOPYXDESTINATIONENCRYPTIONCONFIGURATION._serialized_end=7061
  _BIGQUERYJOBXCOPYXDESTINATIONTABLE._serialized_start=7063
  _BIGQUERYJOBXCOPYXDESTINATIONTABLE._serialized_end=7156
  _BIGQUERYJOBXCOPYXSOURCETABLES._serialized_start=7158
  _BIGQUERYJOBXCOPYXSOURCETABLES._serialized_end=7247
  _BIGQUERYJOBXCOPY._serialized_start=7250
  _BIGQUERYJOBXCOPY._serialized_end=7616
  _BIGQUERYJOBXEXTRACTXSOURCEMODEL._serialized_start=7618
  _BIGQUERYJOBXEXTRACTXSOURCEMODEL._serialized_end=7709
  _BIGQUERYJOBXEXTRACTXSOURCETABLE._serialized_start=7711
  _BIGQUERYJOBXEXTRACTXSOURCETABLE._serialized_end=7802
  _BIGQUERYJOBXEXTRACT._serialized_start=7805
  _BIGQUERYJOBXEXTRACT._serialized_end=8142
  _BIGQUERYJOBXLOADXDESTINATIONENCRYPTIONCONFIGURATION._serialized_start=8144
  _BIGQUERYJOBXLOADXDESTINATIONENCRYPTIONCONFIGURATION._serialized_end=8244
  _BIGQUERYJOBXLOADXDESTINATIONTABLE._serialized_start=8246
  _BIGQUERYJOBXLOADXDESTINATIONTABLE._serialized_end=8339
  _BIGQUERYJOBXLOADXTIMEPARTITIONING._serialized_start=8341
  _BIGQUERYJOBXLOADXTIMEPARTITIONING._serialized_end=8428
  _BIGQUERYJOBXLOAD._serialized_start=8431
  _BIGQUERYJOBXLOAD._serialized_end=9147
  _BIGQUERYJOBXQUERYXDEFAULTDATASET._serialized_start=9149
  _BIGQUERYJOBXQUERYXDEFAULTDATASET._serialized_end=9223
  _BIGQUERYJOBXQUERYXDESTINATIONENCRYPTIONCONFIGURATION._serialized_start=9225
  _BIGQUERYJOBXQUERYXDESTINATIONENCRYPTIONCONFIGURATION._serialized_end=9326
  _BIGQUERYJOBXQUERYXDESTINATIONTABLE._serialized_start=9328
  _BIGQUERYJOBXQUERYXDESTINATIONTABLE._serialized_end=9422
  _BIGQUERYJOBXQUERYXSCRIPTOPTIONS._serialized_start=9424
  _BIGQUERYJOBXQUERYXSCRIPTOPTIONS._serialized_end=9548
  _BIGQUERYJOBXQUERYXUSERDEFINEDFUNCTIONRESOURCES._serialized_start=9550
  _BIGQUERYJOBXQUERYXUSERDEFINEDFUNCTIONRESOURCES._serialized_end=9641
  _BIGQUERYJOBXQUERY._serialized_start=9644
  _BIGQUERYJOBXQUERY._serialized_end=10467
  _BIGQUERYJOBXTIMEOUTS._serialized_start=10469
  _BIGQUERYJOBXTIMEOUTS._serialized_end=10523
  _BIGQUERYJOB._serialized_start=10526
  _BIGQUERYJOB._serialized_end=11255
  _BIGQUERYJOB_LABELSENTRY._serialized_start=5161
  _BIGQUERYJOB_LABELSENTRY._serialized_end=5206
  _BIGQUERYJOB_STATUSENTRY._serialized_start=11210
  _BIGQUERYJOB_STATUSENTRY._serialized_end=11255
  _BIGQUERYRESERVATIONXTIMEOUTS._serialized_start=11257
  _BIGQUERYRESERVATIONXTIMEOUTS._serialized_end=11335
  _BIGQUERYRESERVATION._serialized_start=11338
  _BIGQUERYRESERVATION._serialized_end=11601
  _BIGQUERYRESERVATIONASSIGNMENTXTIMEOUTS._serialized_start=11603
  _BIGQUERYRESERVATIONASSIGNMENTXTIMEOUTS._serialized_end=11675
  _BIGQUERYRESERVATIONASSIGNMENT._serialized_start=11678
  _BIGQUERYRESERVATIONASSIGNMENT._serialized_end=11983
  _BIGQUERYROUTINEXARGUMENTS._serialized_start=11985
  _BIGQUERYROUTINEXARGUMENTS._serialized_end=12082
  _BIGQUERYROUTINEXTIMEOUTS._serialized_start=12084
  _BIGQUERYROUTINEXTIMEOUTS._serialized_end=12158
  _BIGQUERYROUTINE._serialized_start=12161
  _BIGQUERYROUTINE._serialized_end=12686
  _BIGQUERYTABLEXENCRYPTIONCONFIGURATION._serialized_start=12688
  _BIGQUERYTABLEXENCRYPTIONCONFIGURATION._serialized_end=12774
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXCSVOPTIONS._serialized_start=12777
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXCSVOPTIONS._serialized_end=12972
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXSHEETSOPTIONS._serialized_start=12974
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXSHEETSOPTIONS._serialized_end=13071
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXHIVEPARTITIONINGOPTIONS._serialized_start=13074
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATIONXHIVEPARTITIONINGOPTIONS._serialized_end=13214
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATION._serialized_start=13217
  _BIGQUERYTABLEXEXTERNALDATACONFIGURATION._serialized_end=13775
  _BIGQUERYTABLEXMATERIALIZEDVIEW._serialized_start=13777
  _BIGQUERYTABLEXMATERIALIZEDVIEW._serialized_end=13877
  _BIGQUERYTABLEXRANGEPARTITIONINGXRANGE._serialized_start=13879
  _BIGQUERYTABLEXRANGEPARTITIONINGXRANGE._serialized_end=13964
  _BIGQUERYTABLEXRANGEPARTITIONING._serialized_start=13967
  _BIGQUERYTABLEXRANGEPARTITIONING._serialized_end=14095
  _BIGQUERYTABLEXTIMEPARTITIONING._serialized_start=14097
  _BIGQUERYTABLEXTIMEPARTITIONING._serialized_end=14215
  _BIGQUERYTABLEXVIEW._serialized_start=14217
  _BIGQUERYTABLEXVIEW._serialized_end=14276
  _BIGQUERYTABLE._serialized_start=14279
  _BIGQUERYTABLE._serialized_end=15370
  _BIGQUERYTABLE_LABELSENTRY._serialized_start=5161
  _BIGQUERYTABLE_LABELSENTRY._serialized_end=5206
  _BIGQUERYTABLEIAMBINDINGXCONDITION._serialized_start=15372
  _BIGQUERYTABLEIAMBINDINGXCONDITION._serialized_end=15463
  _BIGQUERYTABLEIAMBINDING._serialized_start=15466
  _BIGQUERYTABLEIAMBINDING._serialized_end=15740
  _BIGQUERYTABLEIAMMEMBERXCONDITION._serialized_start=15742
  _BIGQUERYTABLEIAMMEMBERXCONDITION._serialized_end=15832
  _BIGQUERYTABLEIAMMEMBER._serialized_start=15835
  _BIGQUERYTABLEIAMMEMBER._serialized_end=16106
  _BIGQUERYTABLEIAMPOLICY._serialized_start=16109
  _BIGQUERYTABLEIAMPOLICY._serialized_end=16292
# @@protoc_insertion_point(module_scope)