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
class DBClusterDBClusterRole(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FEATURE_NAME_FIELD_NUMBER: builtins.int
    ROLE_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    feature_name: builtins.str
    role_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        feature_name: builtins.str = ...,
        role_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_name", b"feature_name", "resource_info", b"resource_info", "role_arn", b"role_arn"]) -> None: ...

global___DBClusterDBClusterRole = DBClusterDBClusterRole

@typing_extensions.final
class RDS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_CLUSTER_DB_CLUSTER_ROLE_FIELD_NUMBER: builtins.int
    DB_CLUSTER_SCALING_CONFIGURATION_FIELD_NUMBER: builtins.int
    DB_INSTANCE_DB_INSTANCE_ROLE_FIELD_NUMBER: builtins.int
    DB_INSTANCE_PROCESSOR_FEATURE_FIELD_NUMBER: builtins.int
    DB_PROXY_AUTH_FORMAT_FIELD_NUMBER: builtins.int
    DB_PROXY_TAG_FORMAT_FIELD_NUMBER: builtins.int
    DB_PROXY_TARGET_GROUP_CONNECTION_POOL_CONFIGURATION_INFO_FORMAT_FIELD_NUMBER: builtins.int
    DB_SECURITY_GROUP_INGRESS_FIELD_NUMBER: builtins.int
    OPTION_GROUP_OPTION_CONFIGURATION_FIELD_NUMBER: builtins.int
    @property
    def db_cluster_db_cluster_role(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBClusterDBClusterRole]: ...
    @property
    def db_cluster_scaling_configuration(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBClusterScalingConfiguration]: ...
    @property
    def db_instance_db_instance_role(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBInstanceDBInstanceRole]: ...
    @property
    def db_instance_processor_feature(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBInstanceProcessorFeature]: ...
    @property
    def db_proxy_auth_format(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBProxyAuthFormat]: ...
    @property
    def db_proxy_tag_format(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBProxyTagFormat]: ...
    @property
    def db_proxy_target_group_connection_pool_configuration_info_format(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBProxyTargetGroupConnectionPoolConfigurationInfoFormat]: ...
    @property
    def db_security_group_ingress(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DBSecurityGroupIngress]: ...
    @property
    def option_group_option_configuration(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OptionGroupOptionConfiguration]: ...
    def __init__(
        self,
        *,
        db_cluster_db_cluster_role: collections.abc.Iterable[global___DBClusterDBClusterRole] | None = ...,
        db_cluster_scaling_configuration: collections.abc.Iterable[global___DBClusterScalingConfiguration] | None = ...,
        db_instance_db_instance_role: collections.abc.Iterable[global___DBInstanceDBInstanceRole] | None = ...,
        db_instance_processor_feature: collections.abc.Iterable[global___DBInstanceProcessorFeature] | None = ...,
        db_proxy_auth_format: collections.abc.Iterable[global___DBProxyAuthFormat] | None = ...,
        db_proxy_tag_format: collections.abc.Iterable[global___DBProxyTagFormat] | None = ...,
        db_proxy_target_group_connection_pool_configuration_info_format: collections.abc.Iterable[global___DBProxyTargetGroupConnectionPoolConfigurationInfoFormat] | None = ...,
        db_security_group_ingress: collections.abc.Iterable[global___DBSecurityGroupIngress] | None = ...,
        option_group_option_configuration: collections.abc.Iterable[global___OptionGroupOptionConfiguration] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_cluster_db_cluster_role", b"db_cluster_db_cluster_role", "db_cluster_scaling_configuration", b"db_cluster_scaling_configuration", "db_instance_db_instance_role", b"db_instance_db_instance_role", "db_instance_processor_feature", b"db_instance_processor_feature", "db_proxy_auth_format", b"db_proxy_auth_format", "db_proxy_tag_format", b"db_proxy_tag_format", "db_proxy_target_group_connection_pool_configuration_info_format", b"db_proxy_target_group_connection_pool_configuration_info_format", "db_security_group_ingress", b"db_security_group_ingress", "option_group_option_configuration", b"option_group_option_configuration"]) -> None: ...

global___RDS = RDS

@typing_extensions.final
class DBClusterScalingConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    AUTO_PAUSE_FIELD_NUMBER: builtins.int
    MAX_CAPACITY_FIELD_NUMBER: builtins.int
    MIN_CAPACITY_FIELD_NUMBER: builtins.int
    SECONDS_UNTIL_AUTO_PAUSE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    auto_pause: builtins.bool
    max_capacity: builtins.int
    min_capacity: builtins.int
    seconds_until_auto_pause: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        auto_pause: builtins.bool = ...,
        max_capacity: builtins.int = ...,
        min_capacity: builtins.int = ...,
        seconds_until_auto_pause: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_pause", b"auto_pause", "max_capacity", b"max_capacity", "min_capacity", b"min_capacity", "resource_info", b"resource_info", "seconds_until_auto_pause", b"seconds_until_auto_pause"]) -> None: ...

global___DBClusterScalingConfiguration = DBClusterScalingConfiguration

@typing_extensions.final
class DBInstanceDBInstanceRole(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FEATURE_NAME_FIELD_NUMBER: builtins.int
    ROLE_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    feature_name: builtins.str
    role_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        feature_name: builtins.str = ...,
        role_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_name", b"feature_name", "resource_info", b"resource_info", "role_arn", b"role_arn"]) -> None: ...

global___DBInstanceDBInstanceRole = DBInstanceDBInstanceRole

@typing_extensions.final
class DBInstanceProcessorFeature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___DBInstanceProcessorFeature = DBInstanceProcessorFeature

@typing_extensions.final
class DBProxyAuthFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    AUTH_SCHEME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    IAM_AUTH_FIELD_NUMBER: builtins.int
    SECRET_ARN_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    auth_scheme: builtins.str
    description: builtins.str
    iam_auth: builtins.str
    secret_arn: builtins.str
    user_name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        auth_scheme: builtins.str = ...,
        description: builtins.str = ...,
        iam_auth: builtins.str = ...,
        secret_arn: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auth_scheme", b"auth_scheme", "description", b"description", "iam_auth", b"iam_auth", "resource_info", b"resource_info", "secret_arn", b"secret_arn", "user_name", b"user_name"]) -> None: ...

global___DBProxyAuthFormat = DBProxyAuthFormat

@typing_extensions.final
class DBProxyTagFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___DBProxyTagFormat = DBProxyTagFormat

@typing_extensions.final
class DBProxyTargetGroupConnectionPoolConfigurationInfoFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    MAX_CONNECTIONS_PERCENT_FIELD_NUMBER: builtins.int
    MAX_IDLE_CONNECTIONS_PERCENT_FIELD_NUMBER: builtins.int
    CONNECTION_BORROW_TIMEOUT_FIELD_NUMBER: builtins.int
    SESSION_PINNING_FILTERS_FIELD_NUMBER: builtins.int
    INIT_QUERY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    max_connections_percent: builtins.int
    max_idle_connections_percent: builtins.int
    connection_borrow_timeout: builtins.int
    @property
    def session_pinning_filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    init_query: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        max_connections_percent: builtins.int = ...,
        max_idle_connections_percent: builtins.int = ...,
        connection_borrow_timeout: builtins.int = ...,
        session_pinning_filters: collections.abc.Iterable[builtins.str] | None = ...,
        init_query: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection_borrow_timeout", b"connection_borrow_timeout", "init_query", b"init_query", "max_connections_percent", b"max_connections_percent", "max_idle_connections_percent", b"max_idle_connections_percent", "resource_info", b"resource_info", "session_pinning_filters", b"session_pinning_filters"]) -> None: ...

global___DBProxyTargetGroupConnectionPoolConfigurationInfoFormat = DBProxyTargetGroupConnectionPoolConfigurationInfoFormat

@typing_extensions.final
class DBSecurityGroupIngress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CIDR_IP_FIELD_NUMBER: builtins.int
    E_C2_SECURITY_GROUP_ID_FIELD_NUMBER: builtins.int
    E_C2_SECURITY_GROUP_NAME_FIELD_NUMBER: builtins.int
    E_C2_SECURITY_GROUP_OWNER_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    cidr_ip: builtins.str
    e_c2_security_group_id: builtins.str
    e_c2_security_group_name: builtins.str
    e_c2_security_group_owner_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        cidr_ip: builtins.str = ...,
        e_c2_security_group_id: builtins.str = ...,
        e_c2_security_group_name: builtins.str = ...,
        e_c2_security_group_owner_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cidr_ip", b"cidr_ip", "e_c2_security_group_id", b"e_c2_security_group_id", "e_c2_security_group_name", b"e_c2_security_group_name", "e_c2_security_group_owner_id", b"e_c2_security_group_owner_id", "resource_info", b"resource_info"]) -> None: ...

global___DBSecurityGroupIngress = DBSecurityGroupIngress

@typing_extensions.final
class OptionGroupOptionSetting(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___OptionGroupOptionSetting = OptionGroupOptionSetting

@typing_extensions.final
class OptionGroupOptionConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DB_SECURITY_GROUP_MEMBERSHIPS_FIELD_NUMBER: builtins.int
    OPTION_NAME_FIELD_NUMBER: builtins.int
    OPTION_SETTINGS_FIELD_NUMBER: builtins.int
    OPTION_VERSION_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    VPC_SECURITY_GROUP_MEMBERSHIPS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def db_security_group_memberships(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    option_name: builtins.str
    @property
    def option_settings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OptionGroupOptionSetting]: ...
    option_version: builtins.str
    port: builtins.int
    @property
    def vpc_security_group_memberships(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        db_security_group_memberships: collections.abc.Iterable[builtins.str] | None = ...,
        option_name: builtins.str = ...,
        option_settings: collections.abc.Iterable[global___OptionGroupOptionSetting] | None = ...,
        option_version: builtins.str = ...,
        port: builtins.int = ...,
        vpc_security_group_memberships: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_security_group_memberships", b"db_security_group_memberships", "option_name", b"option_name", "option_settings", b"option_settings", "option_version", b"option_version", "port", b"port", "resource_info", b"resource_info", "vpc_security_group_memberships", b"vpc_security_group_memberships"]) -> None: ...

global___OptionGroupOptionConfiguration = OptionGroupOptionConfiguration
