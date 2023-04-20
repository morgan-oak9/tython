# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_msk.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_msk.proto\x12\x13oak9.tython.aws.msk\x1a\x13shared/shared.proto\"e\n\x15\x43lusterEBSStorageInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bvolume_size\x18\x02 \x01(\x05\"\x93\x01\n\x12\x43lusterStorageInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x44\n\x10\x65\x62s_storage_info\x18\x02 \x01(\x0b\x32*.oak9.tython.aws.msk.ClusterEBSStorageInfo\"\xfc\x01\n\x1a\x43lusterBrokerNodeGroupInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0fsecurity_groups\x18\x02 \x03(\t\x12\x16\n\x0e\x63lient_subnets\x18\x03 \x03(\t\x12=\n\x0cstorage_info\x18\x04 \x01(\x0b\x32\'.oak9.tython.aws.msk.ClusterStorageInfo\x12\x1e\n\x16\x62roker_az_distribution\x18\x05 \x01(\t\x12\x15\n\rinstance_type\x18\x06 \x01(\t\"r\n\x17\x43lusterEncryptionAtRest\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16\x64\x61ta_volume_kms_key_id\x18\x02 \x01(\t\"\x80\x01\n\x1a\x43lusterEncryptionInTransit\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rclient_broker\x18\x02 \x01(\t\x12\x12\n\nin_cluster\x18\x03 \x01(\x08\"\xea\x01\n\x15\x43lusterEncryptionInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12H\n\x12\x65ncryption_at_rest\x18\x02 \x01(\x0b\x32,.oak9.tython.aws.msk.ClusterEncryptionAtRest\x12N\n\x15\x65ncryption_in_transit\x18\x03 \x01(\x0b\x32/.oak9.tython.aws.msk.ClusterEncryptionInTransit\"h\n\x12\x43lusterJmxExporter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11\x65nabled_in_broker\x18\x02 \x01(\x08\"i\n\x13\x43lusterNodeExporter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11\x65nabled_in_broker\x18\x02 \x01(\x08\"\xcc\x01\n\x11\x43lusterPrometheus\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12=\n\x0cjmx_exporter\x18\x02 \x01(\x0b\x32\'.oak9.tython.aws.msk.ClusterJmxExporter\x12?\n\rnode_exporter\x18\x03 \x01(\x0b\x32(.oak9.tython.aws.msk.ClusterNodeExporter\"\x8c\x01\n\x15\x43lusterOpenMonitoring\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12:\n\nprometheus\x18\x02 \x01(\x0b\x32&.oak9.tython.aws.msk.ClusterPrometheus\"X\n\x0c\x43lusterScram\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"x\n\x0b\x43lusterSasl\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x30\n\x05scram\x18\x02 \x01(\x0b\x32!.oak9.tython.aws.msk.ClusterScram\"m\n\nClusterTls\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12&\n\x1e\x63\x65rtificate_authority_arn_list\x18\x02 \x03(\t\"\xb4\x01\n\x1b\x43lusterClientAuthentication\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12.\n\x04sasl\x18\x02 \x01(\x0b\x32 .oak9.tython.aws.msk.ClusterSasl\x12,\n\x03tls\x18\x03 \x01(\x0b\x32\x1f.oak9.tython.aws.msk.ClusterTls\"u\n\tClusterS3\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x0e\n\x06prefix\x18\x04 \x01(\t\"t\n\x0f\x43lusterFirehose\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x64\x65livery_stream\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"t\n\x15\x43lusterCloudWatchLogs\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tlog_group\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"\xf6\x01\n\x11\x43lusterBrokerLogs\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12*\n\x02s3\x18\x02 \x01(\x0b\x32\x1e.oak9.tython.aws.msk.ClusterS3\x12\x36\n\x08\x66irehose\x18\x03 \x01(\x0b\x32$.oak9.tython.aws.msk.ClusterFirehose\x12\x44\n\x10\x63loud_watch_logs\x18\x04 \x01(\x0b\x32*.oak9.tython.aws.msk.ClusterCloudWatchLogs\"\x8a\x01\n\x12\x43lusterLoggingInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12;\n\x0b\x62roker_logs\x18\x02 \x01(\x0b\x32&.oak9.tython.aws.msk.ClusterBrokerLogs\"r\n\x18\x43lusterConfigurationInfo\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08revision\x18\x02 \x01(\x05\x12\x0b\n\x03\x61rn\x18\x03 \x01(\t\"\xc5\x05\n\x07\x43luster\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12O\n\x16\x62roker_node_group_info\x18\x02 \x01(\x0b\x32/.oak9.tython.aws.msk.ClusterBrokerNodeGroupInfo\x12\x1b\n\x13\x65nhanced_monitoring\x18\x03 \x01(\t\x12\x15\n\rkafka_version\x18\x04 \x01(\t\x12\x1e\n\x16number_of_broker_nodes\x18\x05 \x01(\x05\x12\x43\n\x0f\x65ncryption_info\x18\x06 \x01(\x0b\x32*.oak9.tython.aws.msk.ClusterEncryptionInfo\x12\x43\n\x0fopen_monitoring\x18\x07 \x01(\x0b\x32*.oak9.tython.aws.msk.ClusterOpenMonitoring\x12\x14\n\x0c\x63luster_name\x18\x08 \x01(\t\x12O\n\x15\x63lient_authentication\x18\t \x01(\x0b\x32\x30.oak9.tython.aws.msk.ClusterClientAuthentication\x12=\n\x0clogging_info\x18\n \x01(\x0b\x32\'.oak9.tython.aws.msk.ClusterLoggingInfo\x12\x34\n\x04tags\x18\x0b \x03(\x0b\x32&.oak9.tython.aws.msk.Cluster.TagsEntry\x12I\n\x12\x63onfiguration_info\x18\x0c \x01(\x0b\x32-.oak9.tython.aws.msk.ClusterConfigurationInfo\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x03MSK\x12-\n\x07\x63luster\x18\x01 \x03(\x0b\x32\x1c.oak9.tython.aws.msk.Clusterb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_msk_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLUSTER_TAGSENTRY._options = None
  _CLUSTER_TAGSENTRY._serialized_options = b'8\001'
  _CLUSTEREBSSTORAGEINFO._serialized_start=63
  _CLUSTEREBSSTORAGEINFO._serialized_end=164
  _CLUSTERSTORAGEINFO._serialized_start=167
  _CLUSTERSTORAGEINFO._serialized_end=314
  _CLUSTERBROKERNODEGROUPINFO._serialized_start=317
  _CLUSTERBROKERNODEGROUPINFO._serialized_end=569
  _CLUSTERENCRYPTIONATREST._serialized_start=571
  _CLUSTERENCRYPTIONATREST._serialized_end=685
  _CLUSTERENCRYPTIONINTRANSIT._serialized_start=688
  _CLUSTERENCRYPTIONINTRANSIT._serialized_end=816
  _CLUSTERENCRYPTIONINFO._serialized_start=819
  _CLUSTERENCRYPTIONINFO._serialized_end=1053
  _CLUSTERJMXEXPORTER._serialized_start=1055
  _CLUSTERJMXEXPORTER._serialized_end=1159
  _CLUSTERNODEEXPORTER._serialized_start=1161
  _CLUSTERNODEEXPORTER._serialized_end=1266
  _CLUSTERPROMETHEUS._serialized_start=1269
  _CLUSTERPROMETHEUS._serialized_end=1473
  _CLUSTEROPENMONITORING._serialized_start=1476
  _CLUSTEROPENMONITORING._serialized_end=1616
  _CLUSTERSCRAM._serialized_start=1618
  _CLUSTERSCRAM._serialized_end=1706
  _CLUSTERSASL._serialized_start=1708
  _CLUSTERSASL._serialized_end=1828
  _CLUSTERTLS._serialized_start=1830
  _CLUSTERTLS._serialized_end=1939
  _CLUSTERCLIENTAUTHENTICATION._serialized_start=1942
  _CLUSTERCLIENTAUTHENTICATION._serialized_end=2122
  _CLUSTERS3._serialized_start=2124
  _CLUSTERS3._serialized_end=2241
  _CLUSTERFIREHOSE._serialized_start=2243
  _CLUSTERFIREHOSE._serialized_end=2359
  _CLUSTERCLOUDWATCHLOGS._serialized_start=2361
  _CLUSTERCLOUDWATCHLOGS._serialized_end=2477
  _CLUSTERBROKERLOGS._serialized_start=2480
  _CLUSTERBROKERLOGS._serialized_end=2726
  _CLUSTERLOGGINGINFO._serialized_start=2729
  _CLUSTERLOGGINGINFO._serialized_end=2867
  _CLUSTERCONFIGURATIONINFO._serialized_start=2869
  _CLUSTERCONFIGURATIONINFO._serialized_end=2983
  _CLUSTER._serialized_start=2986
  _CLUSTER._serialized_end=3695
  _CLUSTER_TAGSENTRY._serialized_start=3652
  _CLUSTER_TAGSENTRY._serialized_end=3695
  _MSK._serialized_start=3697
  _MSK._serialized_end=3749
# @@protoc_insertion_point(module_scope)
