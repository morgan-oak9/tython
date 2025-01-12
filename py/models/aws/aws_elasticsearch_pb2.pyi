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
class DomainMasterUserOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    MASTER_USER_ARN_FIELD_NUMBER: builtins.int
    MASTER_USER_NAME_FIELD_NUMBER: builtins.int
    MASTER_USER_PASSWORD_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    master_user_arn: builtins.str
    master_user_name: builtins.str
    master_user_password: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        master_user_arn: builtins.str = ...,
        master_user_name: builtins.str = ...,
        master_user_password: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["master_user_arn", b"master_user_arn", "master_user_name", b"master_user_name", "master_user_password", b"master_user_password", "resource_info", b"resource_info"]) -> None: ...

global___DomainMasterUserOptions = DomainMasterUserOptions

@typing_extensions.final
class DomainAdvancedSecurityOptionsInput(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    INTERNAL_USER_DATABASE_ENABLED_FIELD_NUMBER: builtins.int
    MASTER_USER_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    internal_user_database_enabled: builtins.bool
    @property
    def master_user_options(self) -> global___DomainMasterUserOptions: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
        internal_user_database_enabled: builtins.bool = ...,
        master_user_options: global___DomainMasterUserOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["master_user_options", b"master_user_options", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "internal_user_database_enabled", b"internal_user_database_enabled", "master_user_options", b"master_user_options", "resource_info", b"resource_info"]) -> None: ...

global___DomainAdvancedSecurityOptionsInput = DomainAdvancedSecurityOptionsInput

@typing_extensions.final
class DomainCognitoOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    IDENTITY_POOL_ID_FIELD_NUMBER: builtins.int
    ROLE_ARN_FIELD_NUMBER: builtins.int
    USER_POOL_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    identity_pool_id: builtins.str
    role_arn: builtins.str
    user_pool_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
        identity_pool_id: builtins.str = ...,
        role_arn: builtins.str = ...,
        user_pool_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "identity_pool_id", b"identity_pool_id", "resource_info", b"resource_info", "role_arn", b"role_arn", "user_pool_id", b"user_pool_id"]) -> None: ...

global___DomainCognitoOptions = DomainCognitoOptions

@typing_extensions.final
class DomainDomainEndpointOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENFORCE_HTTP_S_FIELD_NUMBER: builtins.int
    TLS_SECURITY_POLICY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enforce_http_s: builtins.bool
    tls_security_policy: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enforce_http_s: builtins.bool = ...,
        tls_security_policy: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enforce_http_s", b"enforce_http_s", "resource_info", b"resource_info", "tls_security_policy", b"tls_security_policy"]) -> None: ...

global___DomainDomainEndpointOptions = DomainDomainEndpointOptions

@typing_extensions.final
class DomainEBSOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    EBS_ENABLED_FIELD_NUMBER: builtins.int
    IOPS_FIELD_NUMBER: builtins.int
    VOLUME_SIZE_FIELD_NUMBER: builtins.int
    VOLUME_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    ebs_enabled: builtins.bool
    iops: builtins.int
    volume_size: builtins.int
    volume_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        ebs_enabled: builtins.bool = ...,
        iops: builtins.int = ...,
        volume_size: builtins.int = ...,
        volume_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ebs_enabled", b"ebs_enabled", "iops", b"iops", "resource_info", b"resource_info", "volume_size", b"volume_size", "volume_type", b"volume_type"]) -> None: ...

global___DomainEBSOptions = DomainEBSOptions

@typing_extensions.final
class DomainZoneAwarenessConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    AVAILABILITY_ZONE_COUNT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    availability_zone_count: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        availability_zone_count: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["availability_zone_count", b"availability_zone_count", "resource_info", b"resource_info"]) -> None: ...

global___DomainZoneAwarenessConfig = DomainZoneAwarenessConfig

@typing_extensions.final
class DomainElasticsearchClusterConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DEDICATED_MASTER_COUNT_FIELD_NUMBER: builtins.int
    DEDICATED_MASTER_ENABLED_FIELD_NUMBER: builtins.int
    DEDICATED_MASTER_TYPE_FIELD_NUMBER: builtins.int
    INSTANCE_COUNT_FIELD_NUMBER: builtins.int
    INSTANCE_TYPE_FIELD_NUMBER: builtins.int
    ZONE_AWARENESS_CONFIG_FIELD_NUMBER: builtins.int
    ZONE_AWARENESS_ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    dedicated_master_count: builtins.int
    dedicated_master_enabled: builtins.bool
    dedicated_master_type: builtins.str
    instance_count: builtins.int
    instance_type: builtins.str
    @property
    def zone_awareness_config(self) -> global___DomainZoneAwarenessConfig: ...
    zone_awareness_enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        dedicated_master_count: builtins.int = ...,
        dedicated_master_enabled: builtins.bool = ...,
        dedicated_master_type: builtins.str = ...,
        instance_count: builtins.int = ...,
        instance_type: builtins.str = ...,
        zone_awareness_config: global___DomainZoneAwarenessConfig | None = ...,
        zone_awareness_enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "zone_awareness_config", b"zone_awareness_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dedicated_master_count", b"dedicated_master_count", "dedicated_master_enabled", b"dedicated_master_enabled", "dedicated_master_type", b"dedicated_master_type", "instance_count", b"instance_count", "instance_type", b"instance_type", "resource_info", b"resource_info", "zone_awareness_config", b"zone_awareness_config", "zone_awareness_enabled", b"zone_awareness_enabled"]) -> None: ...

global___DomainElasticsearchClusterConfig = DomainElasticsearchClusterConfig

@typing_extensions.final
class DomainEncryptionAtRestOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    KMS_KEY_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    kms_key_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
        kms_key_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "kms_key_id", b"kms_key_id", "resource_info", b"resource_info"]) -> None: ...

global___DomainEncryptionAtRestOptions = DomainEncryptionAtRestOptions

@typing_extensions.final
class DomainNodeToNodeEncryptionOptions(google.protobuf.message.Message):
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

global___DomainNodeToNodeEncryptionOptions = DomainNodeToNodeEncryptionOptions

@typing_extensions.final
class DomainSnapshotOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    AUTOMATED_SNAPSHOT_START_HOUR_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    automated_snapshot_start_hour: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        automated_snapshot_start_hour: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["automated_snapshot_start_hour", b"automated_snapshot_start_hour", "resource_info", b"resource_info"]) -> None: ...

global___DomainSnapshotOptions = DomainSnapshotOptions

@typing_extensions.final
class DomainVPCOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "security_group_ids", b"security_group_ids", "subnet_ids", b"subnet_ids"]) -> None: ...

global___DomainVPCOptions = DomainVPCOptions

@typing_extensions.final
class Domain(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AccessPoliciesEntry(google.protobuf.message.Message):
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

    @typing_extensions.final
    class AdvancedOptionsEntry(google.protobuf.message.Message):
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
    ACCESS_POLICIES_FIELD_NUMBER: builtins.int
    ADVANCED_OPTIONS_FIELD_NUMBER: builtins.int
    ADVANCED_SECURITY_OPTIONS_FIELD_NUMBER: builtins.int
    COGNITO_OPTIONS_FIELD_NUMBER: builtins.int
    DOMAIN_ENDPOINT_OPTIONS_FIELD_NUMBER: builtins.int
    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    EBS_OPTIONS_FIELD_NUMBER: builtins.int
    ELASTICSEARCH_CLUSTER_CONFIG_FIELD_NUMBER: builtins.int
    ELASTICSEARCH_VERSION_FIELD_NUMBER: builtins.int
    ENCRYPTION_AT_REST_OPTIONS_FIELD_NUMBER: builtins.int
    NODE_TO_NODE_ENCRYPTION_OPTIONS_FIELD_NUMBER: builtins.int
    SNAPSHOT_OPTIONS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    VPC_OPTIONS_FIELD_NUMBER: builtins.int
    LOG_PUBLISHING_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def access_policies(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def advanced_options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def advanced_security_options(self) -> global___DomainAdvancedSecurityOptionsInput: ...
    @property
    def cognito_options(self) -> global___DomainCognitoOptions: ...
    @property
    def domain_endpoint_options(self) -> global___DomainDomainEndpointOptions: ...
    domain_name: builtins.str
    @property
    def ebs_options(self) -> global___DomainEBSOptions: ...
    @property
    def elasticsearch_cluster_config(self) -> global___DomainElasticsearchClusterConfig: ...
    elasticsearch_version: builtins.str
    @property
    def encryption_at_rest_options(self) -> global___DomainEncryptionAtRestOptions: ...
    @property
    def node_to_node_encryption_options(self) -> global___DomainNodeToNodeEncryptionOptions: ...
    @property
    def snapshot_options(self) -> global___DomainSnapshotOptions: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def vpc_options(self) -> global___DomainVPCOptions: ...
    @property
    def log_publishing_options(self) -> global___LogPublishingOptions: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        access_policies: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        advanced_options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        advanced_security_options: global___DomainAdvancedSecurityOptionsInput | None = ...,
        cognito_options: global___DomainCognitoOptions | None = ...,
        domain_endpoint_options: global___DomainDomainEndpointOptions | None = ...,
        domain_name: builtins.str = ...,
        ebs_options: global___DomainEBSOptions | None = ...,
        elasticsearch_cluster_config: global___DomainElasticsearchClusterConfig | None = ...,
        elasticsearch_version: builtins.str = ...,
        encryption_at_rest_options: global___DomainEncryptionAtRestOptions | None = ...,
        node_to_node_encryption_options: global___DomainNodeToNodeEncryptionOptions | None = ...,
        snapshot_options: global___DomainSnapshotOptions | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        vpc_options: global___DomainVPCOptions | None = ...,
        log_publishing_options: global___LogPublishingOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["advanced_security_options", b"advanced_security_options", "cognito_options", b"cognito_options", "domain_endpoint_options", b"domain_endpoint_options", "ebs_options", b"ebs_options", "elasticsearch_cluster_config", b"elasticsearch_cluster_config", "encryption_at_rest_options", b"encryption_at_rest_options", "log_publishing_options", b"log_publishing_options", "node_to_node_encryption_options", b"node_to_node_encryption_options", "resource_info", b"resource_info", "snapshot_options", b"snapshot_options", "vpc_options", b"vpc_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_policies", b"access_policies", "advanced_options", b"advanced_options", "advanced_security_options", b"advanced_security_options", "cognito_options", b"cognito_options", "domain_endpoint_options", b"domain_endpoint_options", "domain_name", b"domain_name", "ebs_options", b"ebs_options", "elasticsearch_cluster_config", b"elasticsearch_cluster_config", "elasticsearch_version", b"elasticsearch_version", "encryption_at_rest_options", b"encryption_at_rest_options", "log_publishing_options", b"log_publishing_options", "node_to_node_encryption_options", b"node_to_node_encryption_options", "resource_info", b"resource_info", "snapshot_options", b"snapshot_options", "tags", b"tags", "vpc_options", b"vpc_options"]) -> None: ...

global___Domain = Domain

@typing_extensions.final
class Elasticsearch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_FIELD_NUMBER: builtins.int
    @property
    def domain(self) -> global___Domain: ...
    def __init__(
        self,
        *,
        domain: global___Domain | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["domain", b"domain"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain", b"domain"]) -> None: ...

global___Elasticsearch = Elasticsearch

@typing_extensions.final
class LogPublishingOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    CLOUDWATCHLOGS_LOG_GROUP_ARN_FIELD_NUMBER: builtins.int
    LOG_TYPE_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    cloudwatchlogs_log_group_arn: builtins.str
    log_type: builtins.str
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        cloudwatchlogs_log_group_arn: builtins.str = ...,
        log_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloudwatchlogs_log_group_arn", b"cloudwatchlogs_log_group_arn", "enabled", b"enabled", "log_type", b"log_type"]) -> None: ...

global___LogPublishingOptions = LogPublishingOptions
