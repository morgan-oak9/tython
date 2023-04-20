"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ClusterEBSStorageInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VOLUME_SIZE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    volume_size: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        volume_size: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "volume_size", b"volume_size"]) -> None: ...

global___ClusterEBSStorageInfo = ClusterEBSStorageInfo

@typing_extensions.final
class ClusterStorageInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    EBS_STORAGE_INFO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def ebs_storage_info(self) -> global___ClusterEBSStorageInfo: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        ebs_storage_info: global___ClusterEBSStorageInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ebs_storage_info", b"ebs_storage_info", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ebs_storage_info", b"ebs_storage_info", "resource_info", b"resource_info"]) -> None: ...

global___ClusterStorageInfo = ClusterStorageInfo

@typing_extensions.final
class ClusterBrokerNodeGroupInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    CLIENT_SUBNETS_FIELD_NUMBER: builtins.int
    STORAGE_INFO_FIELD_NUMBER: builtins.int
    BROKER_AZ_DISTRIBUTION_FIELD_NUMBER: builtins.int
    INSTANCE_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def client_subnets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def storage_info(self) -> global___ClusterStorageInfo: ...
    broker_az_distribution: builtins.str
    instance_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        security_groups: collections.abc.Iterable[builtins.str] | None = ...,
        client_subnets: collections.abc.Iterable[builtins.str] | None = ...,
        storage_info: global___ClusterStorageInfo | None = ...,
        broker_az_distribution: builtins.str = ...,
        instance_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "storage_info", b"storage_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_az_distribution", b"broker_az_distribution", "client_subnets", b"client_subnets", "instance_type", b"instance_type", "resource_info", b"resource_info", "security_groups", b"security_groups", "storage_info", b"storage_info"]) -> None: ...

global___ClusterBrokerNodeGroupInfo = ClusterBrokerNodeGroupInfo

@typing_extensions.final
class ClusterEncryptionAtRest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DATA_VOLUME_KMS_KEY_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    data_volume_kms_key_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        data_volume_kms_key_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_volume_kms_key_id", b"data_volume_kms_key_id", "resource_info", b"resource_info"]) -> None: ...

global___ClusterEncryptionAtRest = ClusterEncryptionAtRest

@typing_extensions.final
class ClusterEncryptionInTransit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CLIENT_BROKER_FIELD_NUMBER: builtins.int
    IN_CLUSTER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    client_broker: builtins.str
    in_cluster: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        client_broker: builtins.str = ...,
        in_cluster: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_broker", b"client_broker", "in_cluster", b"in_cluster", "resource_info", b"resource_info"]) -> None: ...

global___ClusterEncryptionInTransit = ClusterEncryptionInTransit

@typing_extensions.final
class ClusterEncryptionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENCRYPTION_AT_REST_FIELD_NUMBER: builtins.int
    ENCRYPTION_IN_TRANSIT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def encryption_at_rest(self) -> global___ClusterEncryptionAtRest: ...
    @property
    def encryption_in_transit(self) -> global___ClusterEncryptionInTransit: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        encryption_at_rest: global___ClusterEncryptionAtRest | None = ...,
        encryption_in_transit: global___ClusterEncryptionInTransit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["encryption_at_rest", b"encryption_at_rest", "encryption_in_transit", b"encryption_in_transit", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["encryption_at_rest", b"encryption_at_rest", "encryption_in_transit", b"encryption_in_transit", "resource_info", b"resource_info"]) -> None: ...

global___ClusterEncryptionInfo = ClusterEncryptionInfo

@typing_extensions.final
class ClusterJmxExporter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_IN_BROKER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled_in_broker: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled_in_broker: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled_in_broker", b"enabled_in_broker", "resource_info", b"resource_info"]) -> None: ...

global___ClusterJmxExporter = ClusterJmxExporter

@typing_extensions.final
class ClusterNodeExporter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_IN_BROKER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled_in_broker: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled_in_broker: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled_in_broker", b"enabled_in_broker", "resource_info", b"resource_info"]) -> None: ...

global___ClusterNodeExporter = ClusterNodeExporter

@typing_extensions.final
class ClusterPrometheus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    JMX_EXPORTER_FIELD_NUMBER: builtins.int
    NODE_EXPORTER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def jmx_exporter(self) -> global___ClusterJmxExporter: ...
    @property
    def node_exporter(self) -> global___ClusterNodeExporter: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        jmx_exporter: global___ClusterJmxExporter | None = ...,
        node_exporter: global___ClusterNodeExporter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["jmx_exporter", b"jmx_exporter", "node_exporter", b"node_exporter", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["jmx_exporter", b"jmx_exporter", "node_exporter", b"node_exporter", "resource_info", b"resource_info"]) -> None: ...

global___ClusterPrometheus = ClusterPrometheus

@typing_extensions.final
class ClusterOpenMonitoring(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    PROMETHEUS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def prometheus(self) -> global___ClusterPrometheus: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        prometheus: global___ClusterPrometheus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "resource_info", b"resource_info"]) -> None: ...

global___ClusterOpenMonitoring = ClusterOpenMonitoring

@typing_extensions.final
class ClusterScram(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "resource_info", b"resource_info"]) -> None: ...

global___ClusterScram = ClusterScram

@typing_extensions.final
class ClusterSasl(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SCRAM_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def scram(self) -> global___ClusterScram: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        scram: global___ClusterScram | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "scram", b"scram"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "scram", b"scram"]) -> None: ...

global___ClusterSasl = ClusterSasl

@typing_extensions.final
class ClusterTls(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CERTIFICATE_AUTHORITY_ARN_LIST_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def certificate_authority_arn_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        certificate_authority_arn_list: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_authority_arn_list", b"certificate_authority_arn_list", "resource_info", b"resource_info"]) -> None: ...

global___ClusterTls = ClusterTls

@typing_extensions.final
class ClusterClientAuthentication(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SASL_FIELD_NUMBER: builtins.int
    TLS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def sasl(self) -> global___ClusterSasl: ...
    @property
    def tls(self) -> global___ClusterTls: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        sasl: global___ClusterSasl | None = ...,
        tls: global___ClusterTls | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sasl", b"sasl", "tls", b"tls"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sasl", b"sasl", "tls", b"tls"]) -> None: ...

global___ClusterClientAuthentication = ClusterClientAuthentication

@typing_extensions.final
class ClusterS3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    PREFIX_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    bucket: builtins.str
    enabled: builtins.bool
    prefix: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        bucket: builtins.str = ...,
        enabled: builtins.bool = ...,
        prefix: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket", "enabled", b"enabled", "prefix", b"prefix", "resource_info", b"resource_info"]) -> None: ...

global___ClusterS3 = ClusterS3

@typing_extensions.final
class ClusterFirehose(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DELIVERY_STREAM_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    delivery_stream: builtins.str
    enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        delivery_stream: builtins.str = ...,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delivery_stream", b"delivery_stream", "enabled", b"enabled", "resource_info", b"resource_info"]) -> None: ...

global___ClusterFirehose = ClusterFirehose

@typing_extensions.final
class ClusterCloudWatchLogs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LOG_GROUP_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    log_group: builtins.str
    enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        log_group: builtins.str = ...,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "log_group", b"log_group", "resource_info", b"resource_info"]) -> None: ...

global___ClusterCloudWatchLogs = ClusterCloudWatchLogs

@typing_extensions.final
class ClusterBrokerLogs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    S3_FIELD_NUMBER: builtins.int
    FIREHOSE_FIELD_NUMBER: builtins.int
    CLOUD_WATCH_LOGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def s3(self) -> global___ClusterS3: ...
    @property
    def firehose(self) -> global___ClusterFirehose: ...
    @property
    def cloud_watch_logs(self) -> global___ClusterCloudWatchLogs: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        s3: global___ClusterS3 | None = ...,
        firehose: global___ClusterFirehose | None = ...,
        cloud_watch_logs: global___ClusterCloudWatchLogs | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cloud_watch_logs", b"cloud_watch_logs", "firehose", b"firehose", "resource_info", b"resource_info", "s3", b"s3"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_watch_logs", b"cloud_watch_logs", "firehose", b"firehose", "resource_info", b"resource_info", "s3", b"s3"]) -> None: ...

global___ClusterBrokerLogs = ClusterBrokerLogs

@typing_extensions.final
class ClusterLoggingInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BROKER_LOGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def broker_logs(self) -> global___ClusterBrokerLogs: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        broker_logs: global___ClusterBrokerLogs | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["broker_logs", b"broker_logs", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_logs", b"broker_logs", "resource_info", b"resource_info"]) -> None: ...

global___ClusterLoggingInfo = ClusterLoggingInfo

@typing_extensions.final
class ClusterConfigurationInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int
    ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    revision: builtins.int
    arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        revision: builtins.int = ...,
        arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arn", b"arn", "resource_info", b"resource_info", "revision", b"revision"]) -> None: ...

global___ClusterConfigurationInfo = ClusterConfigurationInfo

@typing_extensions.final
class Cluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BROKER_NODE_GROUP_INFO_FIELD_NUMBER: builtins.int
    ENHANCED_MONITORING_FIELD_NUMBER: builtins.int
    KAFKA_VERSION_FIELD_NUMBER: builtins.int
    NUMBER_OF_BROKER_NODES_FIELD_NUMBER: builtins.int
    ENCRYPTION_INFO_FIELD_NUMBER: builtins.int
    OPEN_MONITORING_FIELD_NUMBER: builtins.int
    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    CLIENT_AUTHENTICATION_FIELD_NUMBER: builtins.int
    LOGGING_INFO_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    CONFIGURATION_INFO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def broker_node_group_info(self) -> global___ClusterBrokerNodeGroupInfo: ...
    enhanced_monitoring: builtins.str
    kafka_version: builtins.str
    number_of_broker_nodes: builtins.int
    @property
    def encryption_info(self) -> global___ClusterEncryptionInfo: ...
    @property
    def open_monitoring(self) -> global___ClusterOpenMonitoring: ...
    cluster_name: builtins.str
    @property
    def client_authentication(self) -> global___ClusterClientAuthentication: ...
    @property
    def logging_info(self) -> global___ClusterLoggingInfo: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def configuration_info(self) -> global___ClusterConfigurationInfo: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        broker_node_group_info: global___ClusterBrokerNodeGroupInfo | None = ...,
        enhanced_monitoring: builtins.str = ...,
        kafka_version: builtins.str = ...,
        number_of_broker_nodes: builtins.int = ...,
        encryption_info: global___ClusterEncryptionInfo | None = ...,
        open_monitoring: global___ClusterOpenMonitoring | None = ...,
        cluster_name: builtins.str = ...,
        client_authentication: global___ClusterClientAuthentication | None = ...,
        logging_info: global___ClusterLoggingInfo | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        configuration_info: global___ClusterConfigurationInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["broker_node_group_info", b"broker_node_group_info", "client_authentication", b"client_authentication", "configuration_info", b"configuration_info", "encryption_info", b"encryption_info", "logging_info", b"logging_info", "open_monitoring", b"open_monitoring", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["broker_node_group_info", b"broker_node_group_info", "client_authentication", b"client_authentication", "cluster_name", b"cluster_name", "configuration_info", b"configuration_info", "encryption_info", b"encryption_info", "enhanced_monitoring", b"enhanced_monitoring", "kafka_version", b"kafka_version", "logging_info", b"logging_info", "number_of_broker_nodes", b"number_of_broker_nodes", "open_monitoring", b"open_monitoring", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___Cluster = Cluster

@typing_extensions.final
class MSK(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_FIELD_NUMBER: builtins.int
    @property
    def cluster(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Cluster]: ...
    def __init__(
        self,
        *,
        cluster: collections.abc.Iterable[global___Cluster] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster", b"cluster"]) -> None: ...

global___MSK = MSK