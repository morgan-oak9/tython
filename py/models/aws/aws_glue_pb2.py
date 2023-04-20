# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_glue.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61ws/aws_glue.proto\x12\x14oak9.tython.aws.glue\x1a\x13shared/shared.proto\"\x89\x01\n\x17\x43lassifierXMLClassifier\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07row_tag\x18\x02 \x01(\t\x12\x16\n\x0e\x63lassification\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"t\n\x18\x43lassifierJsonClassifier\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tjson_path\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xef\x01\n\x17\x43lassifierCsvClassifier\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cquote_symbol\x18\x02 \x01(\t\x12\x17\n\x0f\x63ontains_header\x18\x03 \x01(\t\x12\x11\n\tdelimiter\x18\x04 \x01(\t\x12\x0e\n\x06header\x18\x05 \x03(\t\x12\x1b\n\x13\x61llow_single_column\x18\x06 \x01(\x08\x12\x1e\n\x16\x64isable_value_trimming\x18\x07 \x01(\x08\x12\x0c\n\x04name\x18\x08 \x01(\t\"\xa8\x01\n\x18\x43lassifierGrokClassifier\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63ustom_patterns\x18\x02 \x01(\t\x12\x14\n\x0cgrok_pattern\x18\x03 \x01(\t\x12\x16\n\x0e\x63lassification\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\"\xe5\x02\n\nClassifier\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x45\n\x0exml_classifier\x18\x02 \x01(\x0b\x32-.oak9.tython.aws.glue.ClassifierXMLClassifier\x12G\n\x0fjson_classifier\x18\x03 \x01(\x0b\x32..oak9.tython.aws.glue.ClassifierJsonClassifier\x12\x45\n\x0e\x63sv_classifier\x18\x04 \x01(\x0b\x32-.oak9.tython.aws.glue.ClassifierCsvClassifier\x12G\n\x0fgrok_classifier\x18\x05 \x01(\x0b\x32..oak9.tython.aws.glue.ClassifierGrokClassifier\"\xc3\x06\n\x04Glue\x12\x34\n\nclassifier\x18\x01 \x03(\x0b\x32 .oak9.tython.aws.glue.Classifier\x12\x34\n\nconnection\x18\x02 \x03(\x0b\x32 .oak9.tython.aws.glue.Connection\x12.\n\x07\x63rawler\x18\x03 \x03(\x0b\x32\x1d.oak9.tython.aws.glue.Crawler\x12]\n data_catalog_encryption_settings\x18\x04 \x03(\x0b\x32\x33.oak9.tython.aws.glue.DataCatalogEncryptionSettings\x12\x30\n\x08\x64\x61tabase\x18\x05 \x03(\x0b\x32\x1e.oak9.tython.aws.glue.Database\x12\x37\n\x0c\x64\x65v_endpoint\x18\x06 \x03(\x0b\x32!.oak9.tython.aws.glue.DevEndpoint\x12&\n\x03job\x18\x07 \x03(\x0b\x32\x19.oak9.tython.aws.glue.Job\x12\x37\n\x0cml_transform\x18\x08 \x03(\x0b\x32!.oak9.tython.aws.glue.MLTransform\x12\x32\n\tpartition\x18\t \x03(\x0b\x32\x1f.oak9.tython.aws.glue.Partition\x12K\n\x16security_configuration\x18\n \x03(\x0b\x32+.oak9.tython.aws.glue.SecurityConfiguration\x12*\n\x05table\x18\x0b \x03(\x0b\x32\x1b.oak9.tython.aws.glue.Table\x12.\n\x07trigger\x18\x0c \x03(\x0b\x32\x1d.oak9.tython.aws.glue.Trigger\x12\x30\n\x08workflow\x18\r \x03(\x0b\x32\x1e.oak9.tython.aws.glue.Workflow\x12\x65\n$security_configuration_s3_encryption\x18\x0e \x03(\x0b\x32\x37.oak9.tython.aws.glue.SecurityConfigurationS3Encryption\"\xb1\x01\n(ConnectionPhysicalConnectionRequirements\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11\x61vailability_zone\x18\x02 \x01(\t\x12\x1e\n\x16security_group_id_list\x18\x03 \x03(\t\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\"\xb9\x03\n\x19\x43onnectionConnectionInput\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\x0f\x63onnection_type\x18\x03 \x01(\t\x12\x16\n\x0ematch_criteria\x18\x04 \x03(\t\x12h\n physical_connection_requirements\x18\x05 \x01(\x0b\x32>.oak9.tython.aws.glue.ConnectionPhysicalConnectionRequirements\x12h\n\x15\x63onnection_properties\x18\x06 \x03(\x0b\x32I.oak9.tython.aws.glue.ConnectionConnectionInput.ConnectionPropertiesEntry\x12\x0c\n\x04name\x18\x07 \x01(\t\x1a;\n\x19\x43onnectionPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa4\x01\n\nConnection\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12I\n\x10\x63onnection_input\x18\x02 \x01(\x0b\x32/.oak9.tython.aws.glue.ConnectionConnectionInput\x12\x12\n\ncatalog_id\x18\x03 \x01(\t\"\x86\x01\n\x19\x43rawlerSchemaChangePolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0fupdate_behavior\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65lete_behavior\x18\x03 \x01(\t\"g\n\x0f\x43rawlerSchedule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13schedule_expression\x18\x02 \x01(\t\"l\n\x0f\x43rawlerS3Target\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\nexclusions\x18\x03 \x03(\t\"v\n\x14\x43rawlerCatalogTarget\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rdatabase_name\x18\x02 \x01(\t\x12\x0e\n\x06tables\x18\x03 \x03(\t\"\x87\x01\n\x11\x43rawlerJdbcTarget\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x12\n\nexclusions\x18\x04 \x03(\t\"^\n\x15\x43rawlerDynamoDBTarget\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04path\x18\x02 \x01(\t\"\xd0\x02\n\x0e\x43rawlerTargets\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x39\n\ns3_targets\x18\x02 \x03(\x0b\x32%.oak9.tython.aws.glue.CrawlerS3Target\x12\x43\n\x0f\x63\x61talog_targets\x18\x03 \x03(\x0b\x32*.oak9.tython.aws.glue.CrawlerCatalogTarget\x12=\n\x0cjdbc_targets\x18\x04 \x03(\x0b\x32\'.oak9.tython.aws.glue.CrawlerJdbcTarget\x12\x46\n\x11\x64ynamo_db_targets\x18\x05 \x03(\x0b\x32+.oak9.tython.aws.glue.CrawlerDynamoDBTarget\"\x97\x04\n\x07\x43rawler\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x13\n\x0b\x63lassifiers\x18\x03 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12M\n\x14schema_change_policy\x18\x05 \x01(\x0b\x32/.oak9.tython.aws.glue.CrawlerSchemaChangePolicy\x12\x15\n\rconfiguration\x18\x06 \x01(\t\x12\x37\n\x08schedule\x18\x07 \x01(\x0b\x32%.oak9.tython.aws.glue.CrawlerSchedule\x12\x15\n\rdatabase_name\x18\x08 \x01(\t\x12\x35\n\x07targets\x18\t \x01(\x0b\x32$.oak9.tython.aws.glue.CrawlerTargets\x12&\n\x1e\x63rawler_security_configuration\x18\n \x01(\t\x12\x14\n\x0ctable_prefix\x18\x0b \x01(\t\x12\x35\n\x04tags\x18\x0c \x03(\x0b\x32\'.oak9.tython.aws.glue.Crawler.TagsEntry\x12\x0c\n\x04name\x18\r \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb6\x01\n9DataCatalogEncryptionSettingsConnectionPasswordEncryption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12,\n$return_connection_password_encrypted\x18\x02 \x01(\x08\x12\x12\n\nkms_key_id\x18\x03 \x01(\t\"\xa5\x01\n-DataCatalogEncryptionSettingsEncryptionAtRest\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17\x63\x61talog_encryption_mode\x18\x02 \x01(\t\x12\x1a\n\x12sse_aws_kms_key_id\x18\x03 \x01(\t\"\xcf\x02\n:DataCatalogEncryptionSettingsDataCatalogEncryptionSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12w\n\x1e\x63onnection_password_encryption\x18\x02 \x01(\x0b\x32O.oak9.tython.aws.glue.DataCatalogEncryptionSettingsConnectionPasswordEncryption\x12_\n\x12\x65ncryption_at_rest\x18\x03 \x01(\x0b\x32\x43.oak9.tython.aws.glue.DataCatalogEncryptionSettingsEncryptionAtRest\"\xe8\x01\n\x1d\x44\x61taCatalogEncryptionSettings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12z\n data_catalog_encryption_settings\x18\x02 \x01(\x0b\x32P.oak9.tython.aws.glue.DataCatalogEncryptionSettingsDataCatalogEncryptionSettings\x12\x12\n\ncatalog_id\x18\x03 \x01(\t\"\x8d\x02\n\x15\x44\x61tabaseDatabaseInput\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0clocation_uri\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12O\n\nparameters\x18\x04 \x03(\x0b\x32;.oak9.tython.aws.glue.DatabaseDatabaseInput.ParametersEntry\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9c\x01\n\x08\x44\x61tabase\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x43\n\x0e\x64\x61tabase_input\x18\x02 \x01(\x0b\x32+.oak9.tython.aws.glue.DatabaseDatabaseInput\x12\x12\n\ncatalog_id\x18\x03 \x01(\t\"\xe4\x04\n\x0b\x44\x65vEndpoint\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12\x65xtra_jars_s3_path\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t\x12\x17\n\x0fnumber_of_nodes\x18\x04 \x01(\x05\x12\x43\n\targuments\x18\x05 \x03(\x0b\x32\x30.oak9.tython.aws.glue.DevEndpoint.ArgumentsEntry\x12\x11\n\tsubnet_id\x18\x06 \x01(\t\x12\x13\n\x0bpublic_keys\x18\x07 \x03(\t\x12\x1a\n\x12security_group_ids\x18\x08 \x03(\t\x12\x10\n\x08role_arn\x18\t \x01(\t\x12\x13\n\x0bworker_type\x18\n \x01(\t\x12\x15\n\rendpoint_name\x18\x0b \x01(\t\x12\x14\n\x0cglue_version\x18\x0c \x01(\t\x12!\n\x19\x65xtra_python_libs_s3_path\x18\r \x01(\t\x12\x1e\n\x16security_configuration\x18\x0e \x01(\t\x12\x19\n\x11number_of_workers\x18\x0f \x01(\x05\x12\x39\n\x04tags\x18\x10 \x03(\x0b\x32+.oak9.tython.aws.glue.DevEndpoint.TagsEntry\x1a\x30\n\x0e\x41rgumentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n\x12JobConnectionsList\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x63onnections\x18\x02 \x03(\t\"n\n\x17JobNotificationProperty\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12notify_delay_after\x18\x02 \x01(\x05\"\x87\x01\n\rJobJobCommand\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0epython_version\x18\x02 \x01(\t\x12\x17\n\x0fscript_location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"l\n\x14JobExecutionProperty\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13max_concurrent_runs\x18\x02 \x01(\x01\"\xae\x06\n\x03Job\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12=\n\x0b\x63onnections\x18\x02 \x01(\x0b\x32(.oak9.tython.aws.glue.JobConnectionsList\x12\x13\n\x0bmax_retries\x18\x03 \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07timeout\x18\x05 \x01(\x05\x12\x1a\n\x12\x61llocated_capacity\x18\x06 \x01(\x01\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0c\n\x04role\x18\x08 \x01(\t\x12J\n\x11\x64\x65\x66\x61ult_arguments\x18\t \x03(\x0b\x32/.oak9.tython.aws.glue.Job.DefaultArgumentsEntry\x12L\n\x15notification_property\x18\n \x01(\x0b\x32-.oak9.tython.aws.glue.JobNotificationProperty\x12\x13\n\x0bworker_type\x18\x0b \x01(\t\x12\x0f\n\x07log_uri\x18\x0c \x01(\t\x12\x34\n\x07\x63ommand\x18\r \x01(\x0b\x32#.oak9.tython.aws.glue.JobJobCommand\x12\x14\n\x0cglue_version\x18\x0e \x01(\t\x12\x46\n\x12\x65xecution_property\x18\x0f \x01(\x0b\x32*.oak9.tython.aws.glue.JobExecutionProperty\x12\x1e\n\x16security_configuration\x18\x10 \x01(\t\x12\x19\n\x11number_of_workers\x18\x11 \x01(\x05\x12\x31\n\x04tags\x18\x12 \x03(\x0b\x32#.oak9.tython.aws.glue.Job.TagsEntry\x12\x14\n\x0cmax_capacity\x18\x13 \x01(\x01\x1a\x37\n\x15\x44\x65\x66\x61ultArgumentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe0\x01\n MLTransformFindMatchesParameters\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12!\n\x19precision_recall_tradeoff\x18\x02 \x01(\x01\x12\x1f\n\x17\x65nforce_provided_labels\x18\x03 \x01(\x08\x12\x1f\n\x17primary_key_column_name\x18\x04 \x01(\t\x12\x1e\n\x16\x61\x63\x63uracy_cost_tradeoff\x18\x05 \x01(\x01\"\xca\x01\n\x1eMLTransformTransformParameters\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0etransform_type\x18\x02 \x01(\t\x12W\n\x17\x66ind_matches_parameters\x18\x03 \x01(\x0b\x32\x36.oak9.tython.aws.glue.MLTransformFindMatchesParameters\"\xa8\x01\n\x15MLTransformGlueTables\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x15\n\rdatabase_name\x18\x04 \x01(\t\x12\x12\n\ncatalog_id\x18\x05 \x01(\t\"\x99\x01\n\x1cMLTransformInputRecordTables\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12@\n\x0bglue_tables\x18\x02 \x03(\x0b\x32+.oak9.tython.aws.glue.MLTransformGlueTables\"\x86\x04\n\x0bMLTransform\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x13\n\x0bmax_retries\x18\x03 \x01(\x05\x12\x13\n\x0bworker_type\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07timeout\x18\x06 \x01(\x05\x12\x14\n\x0cglue_version\x18\x07 \x01(\t\x12R\n\x14transform_parameters\x18\x08 \x01(\x0b\x32\x34.oak9.tython.aws.glue.MLTransformTransformParameters\x12O\n\x13input_record_tables\x18\t \x01(\x0b\x32\x32.oak9.tython.aws.glue.MLTransformInputRecordTables\x12\x19\n\x11number_of_workers\x18\n \x01(\x05\x12\x39\n\x04tags\x18\x0b \x03(\x0b\x32+.oak9.tython.aws.glue.MLTransform.TagsEntry\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x14\n\x0cmax_capacity\x18\r \x01(\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc8\x02\n\x13PartitionSkewedInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13skewed_column_names\x18\x02 \x03(\t\x12\x1c\n\x14skewed_column_values\x18\x03 \x03(\t\x12w\n!skewed_column_value_location_maps\x18\x04 \x03(\x0b\x32L.oak9.tython.aws.glue.PartitionSkewedInfo.SkewedColumnValueLocationMapsEntry\x1a\x44\n\"SkewedColumnValueLocationMapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"i\n\x0fPartitionColumn\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xfb\x01\n\x12PartitionSerdeInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12L\n\nparameters\x18\x02 \x03(\x0b\x32\x38.oak9.tython.aws.glue.PartitionSerdeInfo.ParametersEntry\x12\x1d\n\x15serialization_library\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"m\n\x0ePartitionOrder\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\t\x12\x12\n\nsort_order\x18\x03 \x01(\x05\"\xf9\x04\n\x1aPartitionStorageDescriptor\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12!\n\x19stored_as_sub_directories\x18\x02 \x01(\x08\x12T\n\nparameters\x18\x03 \x03(\x0b\x32@.oak9.tython.aws.glue.PartitionStorageDescriptor.ParametersEntry\x12\x16\n\x0e\x62ucket_columns\x18\x04 \x03(\t\x12>\n\x0bskewed_info\x18\x05 \x01(\x0b\x32).oak9.tython.aws.glue.PartitionSkewedInfo\x12\x14\n\x0cinput_format\x18\x06 \x01(\t\x12\x19\n\x11number_of_buckets\x18\x07 \x01(\x05\x12\x15\n\routput_format\x18\x08 \x01(\t\x12\x36\n\x07\x63olumns\x18\t \x03(\x0b\x32%.oak9.tython.aws.glue.PartitionColumn\x12<\n\nserde_info\x18\n \x01(\x0b\x32(.oak9.tython.aws.glue.PartitionSerdeInfo\x12:\n\x0csort_columns\x18\x0b \x03(\x0b\x32$.oak9.tython.aws.glue.PartitionOrder\x12\x12\n\ncompressed\x18\x0c \x01(\x08\x12\x10\n\x08location\x18\r \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb6\x02\n\x17PartitionPartitionInput\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12Q\n\nparameters\x18\x02 \x03(\x0b\x32=.oak9.tython.aws.glue.PartitionPartitionInput.ParametersEntry\x12L\n\x12storage_descriptor\x18\x03 \x01(\x0b\x32\x30.oak9.tython.aws.glue.PartitionStorageDescriptor\x12\x0e\n\x06values\x18\x04 \x03(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcb\x01\n\tPartition\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x15\n\rdatabase_name\x18\x03 \x01(\t\x12\x12\n\ncatalog_id\x18\x04 \x01(\t\x12\x46\n\x0fpartition_input\x18\x05 \x01(\x0b\x32-.oak9.tython.aws.glue.PartitionPartitionInput\"]\n\"SecurityConfigurationS3Encryptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x9e\x01\n)SecurityConfigurationCloudWatchEncryption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bkms_key_arn\x18\x02 \x01(\t\x12#\n\x1b\x63loud_watch_encryption_mode\x18\x03 \x01(\t\"\xa2\x01\n+SecurityConfigurationJobBookmarksEncryption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bkms_key_arn\x18\x02 \x01(\t\x12%\n\x1djob_bookmarks_encryption_mode\x18\x03 \x01(\t\"\xff\x02\n,SecurityConfigurationEncryptionConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12P\n\x0es3_encryptions\x18\x02 \x01(\x0b\x32\x38.oak9.tython.aws.glue.SecurityConfigurationS3Encryptions\x12_\n\x16\x63loud_watch_encryption\x18\x03 \x01(\x0b\x32?.oak9.tython.aws.glue.SecurityConfigurationCloudWatchEncryption\x12\x63\n\x18job_bookmarks_encryption\x18\x04 \x01(\x0b\x32\x41.oak9.tython.aws.glue.SecurityConfigurationJobBookmarksEncryption\"\xc4\x01\n\x15SecurityConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x64\n\x18\x65ncryption_configuration\x18\x02 \x01(\x0b\x32\x42.oak9.tython.aws.glue.SecurityConfigurationEncryptionConfiguration\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xc0\x02\n\x0fTableSkewedInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13skewed_column_names\x18\x02 \x03(\t\x12\x1c\n\x14skewed_column_values\x18\x03 \x03(\t\x12s\n!skewed_column_value_location_maps\x18\x04 \x03(\x0b\x32H.oak9.tython.aws.glue.TableSkewedInfo.SkewedColumnValueLocationMapsEntry\x1a\x44\n\"SkewedColumnValueLocationMapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"e\n\x0bTableColumn\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xf3\x01\n\x0eTableSerdeInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12H\n\nparameters\x18\x02 \x03(\x0b\x32\x34.oak9.tython.aws.glue.TableSerdeInfo.ParametersEntry\x12\x1d\n\x15serialization_library\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"i\n\nTableOrder\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\t\x12\x12\n\nsort_order\x18\x03 \x01(\x05\"\xe1\x04\n\x16TableStorageDescriptor\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12!\n\x19stored_as_sub_directories\x18\x02 \x01(\x08\x12P\n\nparameters\x18\x03 \x03(\x0b\x32<.oak9.tython.aws.glue.TableStorageDescriptor.ParametersEntry\x12\x16\n\x0e\x62ucket_columns\x18\x04 \x03(\t\x12:\n\x0bskewed_info\x18\x05 \x01(\x0b\x32%.oak9.tython.aws.glue.TableSkewedInfo\x12\x14\n\x0cinput_format\x18\x06 \x01(\t\x12\x19\n\x11number_of_buckets\x18\x07 \x01(\x05\x12\x15\n\routput_format\x18\x08 \x01(\t\x12\x32\n\x07\x63olumns\x18\t \x03(\x0b\x32!.oak9.tython.aws.glue.TableColumn\x12\x38\n\nserde_info\x18\n \x01(\x0b\x32$.oak9.tython.aws.glue.TableSerdeInfo\x12\x36\n\x0csort_columns\x18\x0b \x03(\x0b\x32 .oak9.tython.aws.glue.TableOrder\x12\x12\n\ncompressed\x18\x0c \x01(\x08\x12\x10\n\x08location\x18\r \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xde\x03\n\x0fTableTableInput\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x1a\n\x12view_original_text\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ntable_type\x18\x05 \x01(\t\x12I\n\nparameters\x18\x06 \x03(\x0b\x32\x35.oak9.tython.aws.glue.TableTableInput.ParametersEntry\x12\x1a\n\x12view_expanded_text\x18\x07 \x01(\t\x12H\n\x12storage_descriptor\x18\x08 \x01(\x0b\x32,.oak9.tython.aws.glue.TableStorageDescriptor\x12\x39\n\x0epartition_keys\x18\t \x03(\x0b\x32!.oak9.tython.aws.glue.TableColumn\x12\x11\n\tretention\x18\n \x01(\x05\x12\x0c\n\x04name\x18\x0b \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa7\x01\n\x05Table\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12:\n\x0btable_input\x18\x02 \x01(\x0b\x32%.oak9.tython.aws.glue.TableTableInput\x12\x15\n\rdatabase_name\x18\x03 \x01(\t\x12\x12\n\ncatalog_id\x18\x04 \x01(\t\"r\n\x1bTriggerNotificationProperty\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12notify_delay_after\x18\x02 \x01(\x05\"\xec\x02\n\rTriggerAction\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12P\n\x15notification_property\x18\x02 \x01(\x0b\x32\x31.oak9.tython.aws.glue.TriggerNotificationProperty\x12\x14\n\x0c\x63rawler_name\x18\x03 \x01(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\x12\x10\n\x08job_name\x18\x05 \x01(\t\x12\x45\n\targuments\x18\x06 \x03(\x0b\x32\x32.oak9.tython.aws.glue.TriggerAction.ArgumentsEntry\x12\x1e\n\x16security_configuration\x18\x07 \x01(\t\x1a\x30\n\x0e\x41rgumentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x01\n\x10TriggerCondition\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x63rawler_name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x13\n\x0b\x63rawl_state\x18\x04 \x01(\t\x12\x18\n\x10logical_operator\x18\x05 \x01(\t\x12\x10\n\x08job_name\x18\x06 \x01(\t\"\x98\x01\n\x10TriggerPredicate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07logical\x18\x02 \x01(\t\x12:\n\nconditions\x18\x03 \x03(\x0b\x32&.oak9.tython.aws.glue.TriggerCondition\"\x8c\x03\n\x07Trigger\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x19\n\x11start_on_creation\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x34\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32#.oak9.tython.aws.glue.TriggerAction\x12\x15\n\rworkflow_name\x18\x06 \x01(\t\x12\x10\n\x08schedule\x18\x07 \x01(\t\x12\x35\n\x04tags\x18\x08 \x03(\x0b\x32\'.oak9.tython.aws.glue.Trigger.TagsEntry\x12\x0c\n\x04name\x18\t \x01(\t\x12\x39\n\tpredicate\x18\n \x01(\x0b\x32&.oak9.tython.aws.glue.TriggerPredicate\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe2\x02\n\x08Workflow\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12X\n\x16\x64\x65\x66\x61ult_run_properties\x18\x03 \x03(\x0b\x32\x38.oak9.tython.aws.glue.Workflow.DefaultRunPropertiesEntry\x12\x36\n\x04tags\x18\x04 \x03(\x0b\x32(.oak9.tython.aws.glue.Workflow.TagsEntry\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a;\n\x19\x44\x65\x66\x61ultRunPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8d\x01\n!SecurityConfigurationS3Encryption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bkms_key_arn\x18\x02 \x01(\t\x12\x1a\n\x12s3_encryption_mode\x18\x03 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_glue_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONNECTIONCONNECTIONINPUT_CONNECTIONPROPERTIESENTRY._options = None
  _CONNECTIONCONNECTIONINPUT_CONNECTIONPROPERTIESENTRY._serialized_options = b'8\001'
  _CRAWLER_TAGSENTRY._options = None
  _CRAWLER_TAGSENTRY._serialized_options = b'8\001'
  _DATABASEDATABASEINPUT_PARAMETERSENTRY._options = None
  _DATABASEDATABASEINPUT_PARAMETERSENTRY._serialized_options = b'8\001'
  _DEVENDPOINT_ARGUMENTSENTRY._options = None
  _DEVENDPOINT_ARGUMENTSENTRY._serialized_options = b'8\001'
  _DEVENDPOINT_TAGSENTRY._options = None
  _DEVENDPOINT_TAGSENTRY._serialized_options = b'8\001'
  _JOB_DEFAULTARGUMENTSENTRY._options = None
  _JOB_DEFAULTARGUMENTSENTRY._serialized_options = b'8\001'
  _JOB_TAGSENTRY._options = None
  _JOB_TAGSENTRY._serialized_options = b'8\001'
  _MLTRANSFORM_TAGSENTRY._options = None
  _MLTRANSFORM_TAGSENTRY._serialized_options = b'8\001'
  _PARTITIONSKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._options = None
  _PARTITIONSKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_options = b'8\001'
  _PARTITIONSERDEINFO_PARAMETERSENTRY._options = None
  _PARTITIONSERDEINFO_PARAMETERSENTRY._serialized_options = b'8\001'
  _PARTITIONSTORAGEDESCRIPTOR_PARAMETERSENTRY._options = None
  _PARTITIONSTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_options = b'8\001'
  _PARTITIONPARTITIONINPUT_PARAMETERSENTRY._options = None
  _PARTITIONPARTITIONINPUT_PARAMETERSENTRY._serialized_options = b'8\001'
  _TABLESKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._options = None
  _TABLESKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_options = b'8\001'
  _TABLESERDEINFO_PARAMETERSENTRY._options = None
  _TABLESERDEINFO_PARAMETERSENTRY._serialized_options = b'8\001'
  _TABLESTORAGEDESCRIPTOR_PARAMETERSENTRY._options = None
  _TABLESTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_options = b'8\001'
  _TABLETABLEINPUT_PARAMETERSENTRY._options = None
  _TABLETABLEINPUT_PARAMETERSENTRY._serialized_options = b'8\001'
  _TRIGGERACTION_ARGUMENTSENTRY._options = None
  _TRIGGERACTION_ARGUMENTSENTRY._serialized_options = b'8\001'
  _TRIGGER_TAGSENTRY._options = None
  _TRIGGER_TAGSENTRY._serialized_options = b'8\001'
  _WORKFLOW_DEFAULTRUNPROPERTIESENTRY._options = None
  _WORKFLOW_DEFAULTRUNPROPERTIESENTRY._serialized_options = b'8\001'
  _WORKFLOW_TAGSENTRY._options = None
  _WORKFLOW_TAGSENTRY._serialized_options = b'8\001'
  _CLASSIFIERXMLCLASSIFIER._serialized_start=66
  _CLASSIFIERXMLCLASSIFIER._serialized_end=203
  _CLASSIFIERJSONCLASSIFIER._serialized_start=205
  _CLASSIFIERJSONCLASSIFIER._serialized_end=321
  _CLASSIFIERCSVCLASSIFIER._serialized_start=324
  _CLASSIFIERCSVCLASSIFIER._serialized_end=563
  _CLASSIFIERGROKCLASSIFIER._serialized_start=566
  _CLASSIFIERGROKCLASSIFIER._serialized_end=734
  _CLASSIFIER._serialized_start=737
  _CLASSIFIER._serialized_end=1094
  _GLUE._serialized_start=1097
  _GLUE._serialized_end=1932
  _CONNECTIONPHYSICALCONNECTIONREQUIREMENTS._serialized_start=1935
  _CONNECTIONPHYSICALCONNECTIONREQUIREMENTS._serialized_end=2112
  _CONNECTIONCONNECTIONINPUT._serialized_start=2115
  _CONNECTIONCONNECTIONINPUT._serialized_end=2556
  _CONNECTIONCONNECTIONINPUT_CONNECTIONPROPERTIESENTRY._serialized_start=2497
  _CONNECTIONCONNECTIONINPUT_CONNECTIONPROPERTIESENTRY._serialized_end=2556
  _CONNECTION._serialized_start=2559
  _CONNECTION._serialized_end=2723
  _CRAWLERSCHEMACHANGEPOLICY._serialized_start=2726
  _CRAWLERSCHEMACHANGEPOLICY._serialized_end=2860
  _CRAWLERSCHEDULE._serialized_start=2862
  _CRAWLERSCHEDULE._serialized_end=2965
  _CRAWLERS3TARGET._serialized_start=2967
  _CRAWLERS3TARGET._serialized_end=3075
  _CRAWLERCATALOGTARGET._serialized_start=3077
  _CRAWLERCATALOGTARGET._serialized_end=3195
  _CRAWLERJDBCTARGET._serialized_start=3198
  _CRAWLERJDBCTARGET._serialized_end=3333
  _CRAWLERDYNAMODBTARGET._serialized_start=3335
  _CRAWLERDYNAMODBTARGET._serialized_end=3429
  _CRAWLERTARGETS._serialized_start=3432
  _CRAWLERTARGETS._serialized_end=3768
  _CRAWLER._serialized_start=3771
  _CRAWLER._serialized_end=4306
  _CRAWLER_TAGSENTRY._serialized_start=4263
  _CRAWLER_TAGSENTRY._serialized_end=4306
  _DATACATALOGENCRYPTIONSETTINGSCONNECTIONPASSWORDENCRYPTION._serialized_start=4309
  _DATACATALOGENCRYPTIONSETTINGSCONNECTIONPASSWORDENCRYPTION._serialized_end=4491
  _DATACATALOGENCRYPTIONSETTINGSENCRYPTIONATREST._serialized_start=4494
  _DATACATALOGENCRYPTIONSETTINGSENCRYPTIONATREST._serialized_end=4659
  _DATACATALOGENCRYPTIONSETTINGSDATACATALOGENCRYPTIONSETTINGS._serialized_start=4662
  _DATACATALOGENCRYPTIONSETTINGSDATACATALOGENCRYPTIONSETTINGS._serialized_end=4997
  _DATACATALOGENCRYPTIONSETTINGS._serialized_start=5000
  _DATACATALOGENCRYPTIONSETTINGS._serialized_end=5232
  _DATABASEDATABASEINPUT._serialized_start=5235
  _DATABASEDATABASEINPUT._serialized_end=5504
  _DATABASEDATABASEINPUT_PARAMETERSENTRY._serialized_start=5455
  _DATABASEDATABASEINPUT_PARAMETERSENTRY._serialized_end=5504
  _DATABASE._serialized_start=5507
  _DATABASE._serialized_end=5663
  _DEVENDPOINT._serialized_start=5666
  _DEVENDPOINT._serialized_end=6278
  _DEVENDPOINT_ARGUMENTSENTRY._serialized_start=6185
  _DEVENDPOINT_ARGUMENTSENTRY._serialized_end=6233
  _DEVENDPOINT_TAGSENTRY._serialized_start=4263
  _DEVENDPOINT_TAGSENTRY._serialized_end=4306
  _JOBCONNECTIONSLIST._serialized_start=6280
  _JOBCONNECTIONSLIST._serialized_end=6378
  _JOBNOTIFICATIONPROPERTY._serialized_start=6380
  _JOBNOTIFICATIONPROPERTY._serialized_end=6490
  _JOBJOBCOMMAND._serialized_start=6493
  _JOBJOBCOMMAND._serialized_end=6628
  _JOBEXECUTIONPROPERTY._serialized_start=6630
  _JOBEXECUTIONPROPERTY._serialized_end=6738
  _JOB._serialized_start=6741
  _JOB._serialized_end=7555
  _JOB_DEFAULTARGUMENTSENTRY._serialized_start=7455
  _JOB_DEFAULTARGUMENTSENTRY._serialized_end=7510
  _JOB_TAGSENTRY._serialized_start=4263
  _JOB_TAGSENTRY._serialized_end=4306
  _MLTRANSFORMFINDMATCHESPARAMETERS._serialized_start=7558
  _MLTRANSFORMFINDMATCHESPARAMETERS._serialized_end=7782
  _MLTRANSFORMTRANSFORMPARAMETERS._serialized_start=7785
  _MLTRANSFORMTRANSFORMPARAMETERS._serialized_end=7987
  _MLTRANSFORMGLUETABLES._serialized_start=7990
  _MLTRANSFORMGLUETABLES._serialized_end=8158
  _MLTRANSFORMINPUTRECORDTABLES._serialized_start=8161
  _MLTRANSFORMINPUTRECORDTABLES._serialized_end=8314
  _MLTRANSFORM._serialized_start=8317
  _MLTRANSFORM._serialized_end=8835
  _MLTRANSFORM_TAGSENTRY._serialized_start=4263
  _MLTRANSFORM_TAGSENTRY._serialized_end=4306
  _PARTITIONSKEWEDINFO._serialized_start=8838
  _PARTITIONSKEWEDINFO._serialized_end=9166
  _PARTITIONSKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_start=9098
  _PARTITIONSKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_end=9166
  _PARTITIONCOLUMN._serialized_start=9168
  _PARTITIONCOLUMN._serialized_end=9273
  _PARTITIONSERDEINFO._serialized_start=9276
  _PARTITIONSERDEINFO._serialized_end=9527
  _PARTITIONSERDEINFO_PARAMETERSENTRY._serialized_start=5455
  _PARTITIONSERDEINFO_PARAMETERSENTRY._serialized_end=5504
  _PARTITIONORDER._serialized_start=9529
  _PARTITIONORDER._serialized_end=9638
  _PARTITIONSTORAGEDESCRIPTOR._serialized_start=9641
  _PARTITIONSTORAGEDESCRIPTOR._serialized_end=10274
  _PARTITIONSTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_start=5455
  _PARTITIONSTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_end=5504
  _PARTITIONPARTITIONINPUT._serialized_start=10277
  _PARTITIONPARTITIONINPUT._serialized_end=10587
  _PARTITIONPARTITIONINPUT_PARAMETERSENTRY._serialized_start=5455
  _PARTITIONPARTITIONINPUT_PARAMETERSENTRY._serialized_end=5504
  _PARTITION._serialized_start=10590
  _PARTITION._serialized_end=10793
  _SECURITYCONFIGURATIONS3ENCRYPTIONS._serialized_start=10795
  _SECURITYCONFIGURATIONS3ENCRYPTIONS._serialized_end=10888
  _SECURITYCONFIGURATIONCLOUDWATCHENCRYPTION._serialized_start=10891
  _SECURITYCONFIGURATIONCLOUDWATCHENCRYPTION._serialized_end=11049
  _SECURITYCONFIGURATIONJOBBOOKMARKSENCRYPTION._serialized_start=11052
  _SECURITYCONFIGURATIONJOBBOOKMARKSENCRYPTION._serialized_end=11214
  _SECURITYCONFIGURATIONENCRYPTIONCONFIGURATION._serialized_start=11217
  _SECURITYCONFIGURATIONENCRYPTIONCONFIGURATION._serialized_end=11600
  _SECURITYCONFIGURATION._serialized_start=11603
  _SECURITYCONFIGURATION._serialized_end=11799
  _TABLESKEWEDINFO._serialized_start=11802
  _TABLESKEWEDINFO._serialized_end=12122
  _TABLESKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_start=9098
  _TABLESKEWEDINFO_SKEWEDCOLUMNVALUELOCATIONMAPSENTRY._serialized_end=9166
  _TABLECOLUMN._serialized_start=12124
  _TABLECOLUMN._serialized_end=12225
  _TABLESERDEINFO._serialized_start=12228
  _TABLESERDEINFO._serialized_end=12471
  _TABLESERDEINFO_PARAMETERSENTRY._serialized_start=5455
  _TABLESERDEINFO_PARAMETERSENTRY._serialized_end=5504
  _TABLEORDER._serialized_start=12473
  _TABLEORDER._serialized_end=12578
  _TABLESTORAGEDESCRIPTOR._serialized_start=12581
  _TABLESTORAGEDESCRIPTOR._serialized_end=13190
  _TABLESTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_start=5455
  _TABLESTORAGEDESCRIPTOR_PARAMETERSENTRY._serialized_end=5504
  _TABLETABLEINPUT._serialized_start=13193
  _TABLETABLEINPUT._serialized_end=13671
  _TABLETABLEINPUT_PARAMETERSENTRY._serialized_start=5455
  _TABLETABLEINPUT_PARAMETERSENTRY._serialized_end=5504
  _TABLE._serialized_start=13674
  _TABLE._serialized_end=13841
  _TRIGGERNOTIFICATIONPROPERTY._serialized_start=13843
  _TRIGGERNOTIFICATIONPROPERTY._serialized_end=13957
  _TRIGGERACTION._serialized_start=13960
  _TRIGGERACTION._serialized_end=14324
  _TRIGGERACTION_ARGUMENTSENTRY._serialized_start=6185
  _TRIGGERACTION_ARGUMENTSENTRY._serialized_end=6233
  _TRIGGERCONDITION._serialized_start=14327
  _TRIGGERCONDITION._serialized_end=14504
  _TRIGGERPREDICATE._serialized_start=14507
  _TRIGGERPREDICATE._serialized_end=14659
  _TRIGGER._serialized_start=14662
  _TRIGGER._serialized_end=15058
  _TRIGGER_TAGSENTRY._serialized_start=4263
  _TRIGGER_TAGSENTRY._serialized_end=4306
  _WORKFLOW._serialized_start=15061
  _WORKFLOW._serialized_end=15415
  _WORKFLOW_DEFAULTRUNPROPERTIESENTRY._serialized_start=15311
  _WORKFLOW_DEFAULTRUNPROPERTIESENTRY._serialized_end=15370
  _WORKFLOW_TAGSENTRY._serialized_start=4263
  _WORKFLOW_TAGSENTRY._serialized_end=4306
  _SECURITYCONFIGURATIONS3ENCRYPTION._serialized_start=15418
  _SECURITYCONFIGURATIONS3ENCRYPTION._serialized_end=15559
# @@protoc_insertion_point(module_scope)
