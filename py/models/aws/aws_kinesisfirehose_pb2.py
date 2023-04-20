# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_kinesisfirehose.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61ws/aws_kinesisfirehose.proto\x12\x1foak9.tython.aws.kinesisfirehose\x1a\x13shared/shared.proto\"\x96\x01\n)DeliveryStreamElasticsearchBufferingHints\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13interval_in_seconds\x18\x02 \x01(\x05\x12\x13\n\x0bsize_in_mbs\x18\x03 \x01(\x05\"\xa3\x01\n&DeliveryStreamCloudWatchLoggingOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x16\n\x0elog_group_name\x18\x03 \x01(\t\x12\x17\n\x0flog_stream_name\x18\x04 \x01(\t\"\x8c\x01\n DeliveryStreamProcessorParameter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0eparameter_name\x18\x02 \x01(\t\x12\x17\n\x0fparameter_value\x18\x03 \x01(\t\"\xa9\x01\n\x17\x44\x65liveryStreamProcessor\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12U\n\nparameters\x18\x02 \x03(\x0b\x32\x41.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessorParameter\"\xbf\x01\n%DeliveryStreamProcessingConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12L\n\nprocessors\x18\x03 \x03(\x0b\x32\x38.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessor\"\x7f\n\'DeliveryStreamElasticsearchRetryOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x64uration_in_seconds\x18\x02 \x01(\x05\"\x89\x01\n\x1c\x44\x65liveryStreamBufferingHints\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13interval_in_seconds\x18\x02 \x01(\x05\x12\x13\n\x0bsize_in_mbs\x18\x03 \x01(\x05\"u\n!DeliveryStreamKMSEncryptionConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x61ws_kms_key_arn\x18\x02 \x01(\t\"\xe1\x01\n%DeliveryStreamEncryptionConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x61\n\x15kms_encryption_config\x18\x02 \x01(\x0b\x32\x42.oak9.tython.aws.kinesisfirehose.DeliveryStreamKMSEncryptionConfig\x12\x1c\n\x14no_encryption_config\x18\x03 \x01(\t\"\x82\x04\n(DeliveryStreamS3DestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nbucket_arn\x18\x02 \x01(\t\x12V\n\x0f\x62uffering_hints\x18\x03 \x01(\x0b\x32=.oak9.tython.aws.kinesisfirehose.DeliveryStreamBufferingHints\x12l\n\x1b\x63loud_watch_logging_options\x18\x04 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12\x1a\n\x12\x63ompression_format\x18\x05 \x01(\t\x12h\n\x18\x65ncryption_configuration\x18\x06 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamEncryptionConfiguration\x12\x1b\n\x13\x65rror_output_prefix\x18\x07 \x01(\t\x12\x0e\n\x06prefix\x18\x08 \x01(\t\x12\x10\n\x08role_arn\x18\t \x01(\t\"\x9b\x01\n\x1e\x44\x65liveryStreamVpcConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08role_arn\x18\x02 \x01(\t\x12\x12\n\nsubnet_ids\x18\x03 \x03(\t\x12\x1a\n\x12security_group_ids\x18\x04 \x03(\t\"\xeb\x06\n3DeliveryStreamElasticsearchDestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x63\n\x0f\x62uffering_hints\x18\x02 \x01(\x0b\x32J.oak9.tython.aws.kinesisfirehose.DeliveryStreamElasticsearchBufferingHints\x12l\n\x1b\x63loud_watch_logging_options\x18\x03 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12\x12\n\ndomain_arn\x18\x04 \x01(\t\x12\x12\n\nindex_name\x18\x05 \x01(\t\x12\x1d\n\x15index_rotation_period\x18\x06 \x01(\t\x12h\n\x18processing_configuration\x18\x07 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessingConfiguration\x12_\n\rretry_options\x18\x08 \x01(\x0b\x32H.oak9.tython.aws.kinesisfirehose.DeliveryStreamElasticsearchRetryOptions\x12\x10\n\x08role_arn\x18\t \x01(\t\x12\x16\n\x0es3_backup_mode\x18\n \x01(\t\x12\x63\n\x10s3_configuration\x18\x0b \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\x12\x18\n\x10\x63luster_endpoint\x18\x0c \x01(\t\x12\x11\n\ttype_name\x18\r \x01(\t\x12Z\n\x11vpc_configuration\x18\x0e \x01(\x0b\x32?.oak9.tython.aws.kinesisfirehose.DeliveryStreamVpcConfiguration\"q\n\x1b\x44\x65liveryStreamHiveJsonSerDe\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11timestamp_formats\x18\x02 \x03(\t\"\xe4\x02\n\x1c\x44\x65liveryStreamOpenXJsonSerDe\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x63\x61se_insensitive\x18\x02 \x01(\x08\x12\x7f\n\x1b\x63olumn_to_json_key_mappings\x18\x03 \x03(\x0b\x32Z.oak9.tython.aws.kinesisfirehose.DeliveryStreamOpenXJsonSerDe.ColumnToJsonKeyMappingsEntry\x12\x30\n(convert_dots_in_json_keys_to_underscores\x18\x04 \x01(\x08\x1a>\n\x1c\x43olumnToJsonKeyMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x88\x02\n\x1a\x44\x65liveryStreamDeserializer\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12V\n\x10hive_json_ser_de\x18\x02 \x01(\x0b\x32<.oak9.tython.aws.kinesisfirehose.DeliveryStreamHiveJsonSerDe\x12Y\n\x12open_x_json_ser_de\x18\x03 \x01(\x0b\x32=.oak9.tython.aws.kinesisfirehose.DeliveryStreamOpenXJsonSerDe\"\xb4\x01\n&DeliveryStreamInputFormatConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12Q\n\x0c\x64\x65serializer\x18\x02 \x01(\x0b\x32;.oak9.tython.aws.kinesisfirehose.DeliveryStreamDeserializer\"\xf1\x02\n\x16\x44\x65liveryStreamOrcSerDe\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x62lock_size_bytes\x18\x02 \x01(\x05\x12\x1c\n\x14\x62loom_filter_columns\x18\x03 \x03(\t\x12/\n\'bloom_filter_false_positive_probability\x18\x04 \x01(\x01\x12\x13\n\x0b\x63ompression\x18\x05 \x01(\t\x12 \n\x18\x64ictionary_key_threshold\x18\x06 \x01(\x01\x12\x16\n\x0e\x65nable_padding\x18\x07 \x01(\x08\x12\x16\n\x0e\x66ormat_version\x18\x08 \x01(\t\x12\x19\n\x11padding_tolerance\x18\t \x01(\x01\x12\x18\n\x10row_index_stride\x18\n \x01(\x05\x12\x19\n\x11stripe_size_bytes\x18\x0b \x01(\x05\"\xf7\x01\n\x1a\x44\x65liveryStreamParquetSerDe\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x62lock_size_bytes\x18\x02 \x01(\x05\x12\x13\n\x0b\x63ompression\x18\x03 \x01(\t\x12%\n\x1d\x65nable_dictionary_compression\x18\x04 \x01(\x08\x12\x19\n\x11max_padding_bytes\x18\x05 \x01(\x05\x12\x17\n\x0fpage_size_bytes\x18\x06 \x01(\x05\x12\x16\n\x0ewriter_version\x18\x07 \x01(\t\"\xf5\x01\n\x18\x44\x65liveryStreamSerializer\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\norc_ser_de\x18\x02 \x01(\x0b\x32\x37.oak9.tython.aws.kinesisfirehose.DeliveryStreamOrcSerDe\x12S\n\x0eparquet_ser_de\x18\x03 \x01(\x0b\x32;.oak9.tython.aws.kinesisfirehose.DeliveryStreamParquetSerDe\"\xb1\x01\n\'DeliveryStreamOutputFormatConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12M\n\nserializer\x18\x02 \x01(\x0b\x32\x39.oak9.tython.aws.kinesisfirehose.DeliveryStreamSerializer\"\xd1\x01\n!DeliveryStreamSchemaConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\ncatalog_id\x18\x02 \x01(\t\x12\x15\n\rdatabase_name\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x10\n\x08role_arn\x18\x05 \x01(\t\x12\x12\n\ntable_name\x18\x06 \x01(\t\x12\x12\n\nversion_id\x18\x07 \x01(\t\"\xb9\x03\n/DeliveryStreamDataFormatConversionConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12k\n\x1ainput_format_configuration\x18\x03 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamInputFormatConfiguration\x12m\n\x1boutput_format_configuration\x18\x04 \x01(\x0b\x32H.oak9.tython.aws.kinesisfirehose.DeliveryStreamOutputFormatConfiguration\x12`\n\x14schema_configuration\x18\x05 \x01(\x0b\x32\x42.oak9.tython.aws.kinesisfirehose.DeliveryStreamSchemaConfiguration\"\xf8\x06\n0DeliveryStreamExtendedS3DestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nbucket_arn\x18\x02 \x01(\t\x12V\n\x0f\x62uffering_hints\x18\x03 \x01(\x0b\x32=.oak9.tython.aws.kinesisfirehose.DeliveryStreamBufferingHints\x12l\n\x1b\x63loud_watch_logging_options\x18\x04 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12\x1a\n\x12\x63ompression_format\x18\x05 \x01(\t\x12~\n$data_format_conversion_configuration\x18\x06 \x01(\x0b\x32P.oak9.tython.aws.kinesisfirehose.DeliveryStreamDataFormatConversionConfiguration\x12h\n\x18\x65ncryption_configuration\x18\x07 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamEncryptionConfiguration\x12\x1b\n\x13\x65rror_output_prefix\x18\x08 \x01(\t\x12\x0e\n\x06prefix\x18\t \x01(\t\x12h\n\x18processing_configuration\x18\n \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessingConfiguration\x12\x10\n\x08role_arn\x18\x0b \x01(\t\x12j\n\x17s3_backup_configuration\x18\x0c \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\x12\x16\n\x0es3_backup_mode\x18\r \x01(\t\"\x97\x01\n.DeliveryStreamKinesisStreamSourceConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12kinesis_stream_arn\x18\x02 \x01(\t\x12\x10\n\x08role_arn\x18\x03 \x01(\t\"\x9f\x01\n\x19\x44\x65liveryStreamCopyCommand\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x63opy_options\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x61ta_table_columns\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x61ta_table_name\x18\x04 \x01(\t\"z\n\"DeliveryStreamRedshiftRetryOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x64uration_in_seconds\x18\x02 \x01(\x05\"\xac\x06\n.DeliveryStreamRedshiftDestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12l\n\x1b\x63loud_watch_logging_options\x18\x02 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12\x1c\n\x14\x63luster_j_db_c_u_r_l\x18\x03 \x01(\t\x12P\n\x0c\x63opy_command\x18\x04 \x01(\x0b\x32:.oak9.tython.aws.kinesisfirehose.DeliveryStreamCopyCommand\x12\x10\n\x08password\x18\x05 \x01(\t\x12h\n\x18processing_configuration\x18\x06 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessingConfiguration\x12Z\n\rretry_options\x18\x07 \x01(\x0b\x32\x43.oak9.tython.aws.kinesisfirehose.DeliveryStreamRedshiftRetryOptions\x12\x10\n\x08role_arn\x18\x08 \x01(\t\x12j\n\x17s3_backup_configuration\x18\t \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\x12\x16\n\x0es3_backup_mode\x18\n \x01(\t\x12\x63\n\x10s3_configuration\x18\x0b \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\x12\x10\n\x08username\x18\x0c \x01(\t\"x\n DeliveryStreamSplunkRetryOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x64uration_in_seconds\x18\x02 \x01(\x05\"\x88\x05\n,DeliveryStreamSplunkDestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12l\n\x1b\x63loud_watch_logging_options\x18\x02 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12,\n$hecacknowledgment_timeout_in_seconds\x18\x03 \x01(\x05\x12\x14\n\x0chec_endpoint\x18\x04 \x01(\t\x12\x19\n\x11hec_endpoint_type\x18\x05 \x01(\t\x12\x11\n\thec_token\x18\x06 \x01(\t\x12h\n\x18processing_configuration\x18\x07 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessingConfiguration\x12X\n\rretry_options\x18\x08 \x01(\x0b\x32\x41.oak9.tython.aws.kinesisfirehose.DeliveryStreamSplunkRetryOptions\x12\x16\n\x0es3_backup_mode\x18\t \x01(\t\x12\x63\n\x10s3_configuration\x18\n \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\"\x91\x01\n\'DeliveryStreamHttpEndpointConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x12\n\naccess_key\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\x95\x01\n)DeliveryStreamHttpEndpointCommonAttribute\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x61ttribute_name\x18\x02 \x01(\t\x12\x17\n\x0f\x61ttribute_value\x18\x03 \x01(\t\"\xea\x01\n.DeliveryStreamHttpEndpointRequestConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x63ontent_encoding\x18\x02 \x01(\t\x12\x65\n\x11\x63ommon_attributes\x18\x03 \x03(\x0b\x32J.oak9.tython.aws.kinesisfirehose.DeliveryStreamHttpEndpointCommonAttribute\"r\n\x1a\x44\x65liveryStreamRetryOptions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x64uration_in_seconds\x18\x02 \x01(\x05\"\xda\x06\n2DeliveryStreamHttpEndpointDestinationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08role_arn\x18\x02 \x01(\t\x12h\n\x16\x65ndpoint_configuration\x18\x03 \x01(\x0b\x32H.oak9.tython.aws.kinesisfirehose.DeliveryStreamHttpEndpointConfiguration\x12n\n\x15request_configuration\x18\x04 \x01(\x0b\x32O.oak9.tython.aws.kinesisfirehose.DeliveryStreamHttpEndpointRequestConfiguration\x12V\n\x0f\x62uffering_hints\x18\x05 \x01(\x0b\x32=.oak9.tython.aws.kinesisfirehose.DeliveryStreamBufferingHints\x12l\n\x1b\x63loud_watch_logging_options\x18\x06 \x01(\x0b\x32G.oak9.tython.aws.kinesisfirehose.DeliveryStreamCloudWatchLoggingOptions\x12h\n\x18processing_configuration\x18\x07 \x01(\x0b\x32\x46.oak9.tython.aws.kinesisfirehose.DeliveryStreamProcessingConfiguration\x12R\n\rretry_options\x18\x08 \x01(\x0b\x32;.oak9.tython.aws.kinesisfirehose.DeliveryStreamRetryOptions\x12\x16\n\x0es3_backup_mode\x18\t \x01(\t\x12\x63\n\x10s3_configuration\x18\n \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\"\xfc\x07\n\x0e\x44\x65liveryStream\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1c\n\x14\x64\x65livery_stream_name\x18\x02 \x01(\t\x12\x1c\n\x14\x64\x65livery_stream_type\x18\x03 \x01(\t\x12\x85\x01\n\'elasticsearch_destination_configuration\x18\x04 \x01(\x0b\x32T.oak9.tython.aws.kinesisfirehose.DeliveryStreamElasticsearchDestinationConfiguration\x12\x80\x01\n%extended_s3_destination_configuration\x18\x05 \x01(\x0b\x32Q.oak9.tython.aws.kinesisfirehose.DeliveryStreamExtendedS3DestinationConfiguration\x12|\n#kinesis_stream_source_configuration\x18\x06 \x01(\x0b\x32O.oak9.tython.aws.kinesisfirehose.DeliveryStreamKinesisStreamSourceConfiguration\x12{\n\"redshift_destination_configuration\x18\x07 \x01(\x0b\x32O.oak9.tython.aws.kinesisfirehose.DeliveryStreamRedshiftDestinationConfiguration\x12o\n\x1cs3_destination_configuration\x18\x08 \x01(\x0b\x32I.oak9.tython.aws.kinesisfirehose.DeliveryStreamS3DestinationConfiguration\x12w\n splunk_destination_configuration\x18\t \x01(\x0b\x32M.oak9.tython.aws.kinesisfirehose.DeliveryStreamSplunkDestinationConfiguration\x12\x84\x01\n\'http_endpoint_destination_configuration\x18\n \x01(\x0b\x32S.oak9.tython.aws.kinesisfirehose.DeliveryStreamHttpEndpointDestinationConfiguration\"[\n\x0fKinesisFirehose\x12H\n\x0f\x64\x65livery_stream\x18\x01 \x03(\x0b\x32/.oak9.tython.aws.kinesisfirehose.DeliveryStreamb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_kinesisfirehose_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DELIVERYSTREAMOPENXJSONSERDE_COLUMNTOJSONKEYMAPPINGSENTRY._options = None
  _DELIVERYSTREAMOPENXJSONSERDE_COLUMNTOJSONKEYMAPPINGSENTRY._serialized_options = b'8\001'
  _DELIVERYSTREAMELASTICSEARCHBUFFERINGHINTS._serialized_start=88
  _DELIVERYSTREAMELASTICSEARCHBUFFERINGHINTS._serialized_end=238
  _DELIVERYSTREAMCLOUDWATCHLOGGINGOPTIONS._serialized_start=241
  _DELIVERYSTREAMCLOUDWATCHLOGGINGOPTIONS._serialized_end=404
  _DELIVERYSTREAMPROCESSORPARAMETER._serialized_start=407
  _DELIVERYSTREAMPROCESSORPARAMETER._serialized_end=547
  _DELIVERYSTREAMPROCESSOR._serialized_start=550
  _DELIVERYSTREAMPROCESSOR._serialized_end=719
  _DELIVERYSTREAMPROCESSINGCONFIGURATION._serialized_start=722
  _DELIVERYSTREAMPROCESSINGCONFIGURATION._serialized_end=913
  _DELIVERYSTREAMELASTICSEARCHRETRYOPTIONS._serialized_start=915
  _DELIVERYSTREAMELASTICSEARCHRETRYOPTIONS._serialized_end=1042
  _DELIVERYSTREAMBUFFERINGHINTS._serialized_start=1045
  _DELIVERYSTREAMBUFFERINGHINTS._serialized_end=1182
  _DELIVERYSTREAMKMSENCRYPTIONCONFIG._serialized_start=1184
  _DELIVERYSTREAMKMSENCRYPTIONCONFIG._serialized_end=1301
  _DELIVERYSTREAMENCRYPTIONCONFIGURATION._serialized_start=1304
  _DELIVERYSTREAMENCRYPTIONCONFIGURATION._serialized_end=1529
  _DELIVERYSTREAMS3DESTINATIONCONFIGURATION._serialized_start=1532
  _DELIVERYSTREAMS3DESTINATIONCONFIGURATION._serialized_end=2046
  _DELIVERYSTREAMVPCCONFIGURATION._serialized_start=2049
  _DELIVERYSTREAMVPCCONFIGURATION._serialized_end=2204
  _DELIVERYSTREAMELASTICSEARCHDESTINATIONCONFIGURATION._serialized_start=2207
  _DELIVERYSTREAMELASTICSEARCHDESTINATIONCONFIGURATION._serialized_end=3082
  _DELIVERYSTREAMHIVEJSONSERDE._serialized_start=3084
  _DELIVERYSTREAMHIVEJSONSERDE._serialized_end=3197
  _DELIVERYSTREAMOPENXJSONSERDE._serialized_start=3200
  _DELIVERYSTREAMOPENXJSONSERDE._serialized_end=3556
  _DELIVERYSTREAMOPENXJSONSERDE_COLUMNTOJSONKEYMAPPINGSENTRY._serialized_start=3494
  _DELIVERYSTREAMOPENXJSONSERDE_COLUMNTOJSONKEYMAPPINGSENTRY._serialized_end=3556
  _DELIVERYSTREAMDESERIALIZER._serialized_start=3559
  _DELIVERYSTREAMDESERIALIZER._serialized_end=3823
  _DELIVERYSTREAMINPUTFORMATCONFIGURATION._serialized_start=3826
  _DELIVERYSTREAMINPUTFORMATCONFIGURATION._serialized_end=4006
  _DELIVERYSTREAMORCSERDE._serialized_start=4009
  _DELIVERYSTREAMORCSERDE._serialized_end=4378
  _DELIVERYSTREAMPARQUETSERDE._serialized_start=4381
  _DELIVERYSTREAMPARQUETSERDE._serialized_end=4628
  _DELIVERYSTREAMSERIALIZER._serialized_start=4631
  _DELIVERYSTREAMSERIALIZER._serialized_end=4876
  _DELIVERYSTREAMOUTPUTFORMATCONFIGURATION._serialized_start=4879
  _DELIVERYSTREAMOUTPUTFORMATCONFIGURATION._serialized_end=5056
  _DELIVERYSTREAMSCHEMACONFIGURATION._serialized_start=5059
  _DELIVERYSTREAMSCHEMACONFIGURATION._serialized_end=5268
  _DELIVERYSTREAMDATAFORMATCONVERSIONCONFIGURATION._serialized_start=5271
  _DELIVERYSTREAMDATAFORMATCONVERSIONCONFIGURATION._serialized_end=5712
  _DELIVERYSTREAMEXTENDEDS3DESTINATIONCONFIGURATION._serialized_start=5715
  _DELIVERYSTREAMEXTENDEDS3DESTINATIONCONFIGURATION._serialized_end=6603
  _DELIVERYSTREAMKINESISSTREAMSOURCECONFIGURATION._serialized_start=6606
  _DELIVERYSTREAMKINESISSTREAMSOURCECONFIGURATION._serialized_end=6757
  _DELIVERYSTREAMCOPYCOMMAND._serialized_start=6760
  _DELIVERYSTREAMCOPYCOMMAND._serialized_end=6919
  _DELIVERYSTREAMREDSHIFTRETRYOPTIONS._serialized_start=6921
  _DELIVERYSTREAMREDSHIFTRETRYOPTIONS._serialized_end=7043
  _DELIVERYSTREAMREDSHIFTDESTINATIONCONFIGURATION._serialized_start=7046
  _DELIVERYSTREAMREDSHIFTDESTINATIONCONFIGURATION._serialized_end=7858
  _DELIVERYSTREAMSPLUNKRETRYOPTIONS._serialized_start=7860
  _DELIVERYSTREAMSPLUNKRETRYOPTIONS._serialized_end=7980
  _DELIVERYSTREAMSPLUNKDESTINATIONCONFIGURATION._serialized_start=7983
  _DELIVERYSTREAMSPLUNKDESTINATIONCONFIGURATION._serialized_end=8631
  _DELIVERYSTREAMHTTPENDPOINTCONFIGURATION._serialized_start=8634
  _DELIVERYSTREAMHTTPENDPOINTCONFIGURATION._serialized_end=8779
  _DELIVERYSTREAMHTTPENDPOINTCOMMONATTRIBUTE._serialized_start=8782
  _DELIVERYSTREAMHTTPENDPOINTCOMMONATTRIBUTE._serialized_end=8931
  _DELIVERYSTREAMHTTPENDPOINTREQUESTCONFIGURATION._serialized_start=8934
  _DELIVERYSTREAMHTTPENDPOINTREQUESTCONFIGURATION._serialized_end=9168
  _DELIVERYSTREAMRETRYOPTIONS._serialized_start=9170
  _DELIVERYSTREAMRETRYOPTIONS._serialized_end=9284
  _DELIVERYSTREAMHTTPENDPOINTDESTINATIONCONFIGURATION._serialized_start=9287
  _DELIVERYSTREAMHTTPENDPOINTDESTINATIONCONFIGURATION._serialized_end=10145
  _DELIVERYSTREAM._serialized_start=10148
  _DELIVERYSTREAM._serialized_end=11168
  _KINESISFIREHOSE._serialized_start=11170
  _KINESISFIREHOSE._serialized_end=11261
# @@protoc_insertion_point(module_scope)
