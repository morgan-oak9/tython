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
class ComposerEnvironmentXConfigXDatabaseConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MACHINE_TYPE_FIELD_NUMBER: builtins.int
    machine_type: builtins.str
    def __init__(
        self,
        *,
        machine_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["machine_type", b"machine_type"]) -> None: ...

global___ComposerEnvironmentXConfigXDatabaseConfig = ComposerEnvironmentXConfigXDatabaseConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXEncryptionConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KMS_KEY_NAME_FIELD_NUMBER: builtins.int
    kms_key_name: builtins.str
    def __init__(
        self,
        *,
        kms_key_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["kms_key_name", b"kms_key_name"]) -> None: ...

global___ComposerEnvironmentXConfigXEncryptionConfig = ComposerEnvironmentXConfigXEncryptionConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    END_TIME_FIELD_NUMBER: builtins.int
    RECURRENCE_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    end_time: builtins.str
    recurrence: builtins.str
    start_time: builtins.str
    def __init__(
        self,
        *,
        end_time: builtins.str = ...,
        recurrence: builtins.str = ...,
        start_time: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_time", b"end_time", "recurrence", b"recurrence", "start_time", b"start_time"]) -> None: ...

global___ComposerEnvironmentXConfigXMaintenanceWindow = ComposerEnvironmentXConfigXMaintenanceWindow

@typing_extensions.final
class ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfigXCidrBlocks(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CIDR_BLOCK_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    cidr_block: builtins.str
    display_name: builtins.str
    def __init__(
        self,
        *,
        cidr_block: builtins.str = ...,
        display_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cidr_block", b"cidr_block", "display_name", b"display_name"]) -> None: ...

global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfigXCidrBlocks = ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfigXCidrBlocks

@typing_extensions.final
class ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    CIDR_BLOCKS_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    @property
    def cidr_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfigXCidrBlocks]: ...
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        cidr_blocks: collections.abc.Iterable[global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfigXCidrBlocks] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cidr_blocks", b"cidr_blocks", "enabled", b"enabled"]) -> None: ...

global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfig = ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXNodeConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class IpAllocationPolicyEntry(google.protobuf.message.Message):
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

    DISK_SIZE_GB_FIELD_NUMBER: builtins.int
    ENABLE_IP_MASQ_AGENT_FIELD_NUMBER: builtins.int
    IP_ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    MACHINE_TYPE_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    OAUTH_SCOPES_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    SUBNETWORK_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ZONE_FIELD_NUMBER: builtins.int
    disk_size_gb: builtins.float
    enable_ip_masq_agent: builtins.bool
    @property
    def ip_allocation_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    machine_type: builtins.str
    network: builtins.str
    @property
    def oauth_scopes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    service_account: builtins.str
    subnetwork: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    zone: builtins.str
    def __init__(
        self,
        *,
        disk_size_gb: builtins.float = ...,
        enable_ip_masq_agent: builtins.bool = ...,
        ip_allocation_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        machine_type: builtins.str = ...,
        network: builtins.str = ...,
        oauth_scopes: collections.abc.Iterable[builtins.str] | None = ...,
        service_account: builtins.str = ...,
        subnetwork: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        zone: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disk_size_gb", b"disk_size_gb", "enable_ip_masq_agent", b"enable_ip_masq_agent", "ip_allocation_policy", b"ip_allocation_policy", "machine_type", b"machine_type", "network", b"network", "oauth_scopes", b"oauth_scopes", "service_account", b"service_account", "subnetwork", b"subnetwork", "tags", b"tags", "zone", b"zone"]) -> None: ...

global___ComposerEnvironmentXConfigXNodeConfig = ComposerEnvironmentXConfigXNodeConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXPrivateEnvironmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_COMPOSER_CONNECTION_SUBNETWORK_FIELD_NUMBER: builtins.int
    CLOUD_COMPOSER_NETWORK_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    CLOUD_SQL_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    ENABLE_PRIVATE_ENDPOINT_FIELD_NUMBER: builtins.int
    ENABLE_PRIVATELY_USED_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    MASTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    WEB_SERVER_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    cloud_composer_connection_subnetwork: builtins.str
    cloud_composer_network_ipv4_cidr_block: builtins.str
    cloud_sql_ipv4_cidr_block: builtins.str
    enable_private_endpoint: builtins.bool
    enable_privately_used_public_ips: builtins.bool
    master_ipv4_cidr_block: builtins.str
    web_server_ipv4_cidr_block: builtins.str
    def __init__(
        self,
        *,
        cloud_composer_connection_subnetwork: builtins.str = ...,
        cloud_composer_network_ipv4_cidr_block: builtins.str = ...,
        cloud_sql_ipv4_cidr_block: builtins.str = ...,
        enable_private_endpoint: builtins.bool = ...,
        enable_privately_used_public_ips: builtins.bool = ...,
        master_ipv4_cidr_block: builtins.str = ...,
        web_server_ipv4_cidr_block: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_composer_connection_subnetwork", b"cloud_composer_connection_subnetwork", "cloud_composer_network_ipv4_cidr_block", b"cloud_composer_network_ipv4_cidr_block", "cloud_sql_ipv4_cidr_block", b"cloud_sql_ipv4_cidr_block", "enable_private_endpoint", b"enable_private_endpoint", "enable_privately_used_public_ips", b"enable_privately_used_public_ips", "master_ipv4_cidr_block", b"master_ipv4_cidr_block", "web_server_ipv4_cidr_block", b"web_server_ipv4_cidr_block"]) -> None: ...

global___ComposerEnvironmentXConfigXPrivateEnvironmentConfig = ComposerEnvironmentXConfigXPrivateEnvironmentConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXSoftwareConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AirflowConfigOverridesEntry(google.protobuf.message.Message):
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
    class EnvVariablesEntry(google.protobuf.message.Message):
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
    class PypiPackagesEntry(google.protobuf.message.Message):
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

    AIRFLOW_CONFIG_OVERRIDES_FIELD_NUMBER: builtins.int
    ENV_VARIABLES_FIELD_NUMBER: builtins.int
    IMAGE_VERSION_FIELD_NUMBER: builtins.int
    PYPI_PACKAGES_FIELD_NUMBER: builtins.int
    PYTHON_VERSION_FIELD_NUMBER: builtins.int
    SCHEDULER_COUNT_FIELD_NUMBER: builtins.int
    @property
    def airflow_config_overrides(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def env_variables(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    image_version: builtins.str
    @property
    def pypi_packages(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    python_version: builtins.str
    scheduler_count: builtins.float
    def __init__(
        self,
        *,
        airflow_config_overrides: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        env_variables: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        image_version: builtins.str = ...,
        pypi_packages: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        python_version: builtins.str = ...,
        scheduler_count: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["airflow_config_overrides", b"airflow_config_overrides", "env_variables", b"env_variables", "image_version", b"image_version", "pypi_packages", b"pypi_packages", "python_version", b"python_version", "scheduler_count", b"scheduler_count"]) -> None: ...

global___ComposerEnvironmentXConfigXSoftwareConfig = ComposerEnvironmentXConfigXSoftwareConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXWebServerConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MACHINE_TYPE_FIELD_NUMBER: builtins.int
    machine_type: builtins.str
    def __init__(
        self,
        *,
        machine_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["machine_type", b"machine_type"]) -> None: ...

global___ComposerEnvironmentXConfigXWebServerConfig = ComposerEnvironmentXConfigXWebServerConfig

@typing_extensions.final
class ComposerEnvironmentXConfigXWebServerNetworkAccessControlXAllowedIpRange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    description: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "value", b"value"]) -> None: ...

global___ComposerEnvironmentXConfigXWebServerNetworkAccessControlXAllowedIpRange = ComposerEnvironmentXConfigXWebServerNetworkAccessControlXAllowedIpRange

@typing_extensions.final
class ComposerEnvironmentXConfigXWebServerNetworkAccessControl(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOWED_IP_RANGE_FIELD_NUMBER: builtins.int
    @property
    def allowed_ip_range(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComposerEnvironmentXConfigXWebServerNetworkAccessControlXAllowedIpRange]: ...
    def __init__(
        self,
        *,
        allowed_ip_range: collections.abc.Iterable[global___ComposerEnvironmentXConfigXWebServerNetworkAccessControlXAllowedIpRange] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_ip_range", b"allowed_ip_range"]) -> None: ...

global___ComposerEnvironmentXConfigXWebServerNetworkAccessControl = ComposerEnvironmentXConfigXWebServerNetworkAccessControl

@typing_extensions.final
class ComposerEnvironmentXConfigXWorkloadsConfigXScheduler(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNT_FIELD_NUMBER: builtins.int
    CPU_FIELD_NUMBER: builtins.int
    MEMORY_GB_FIELD_NUMBER: builtins.int
    STORAGE_GB_FIELD_NUMBER: builtins.int
    count: builtins.float
    cpu: builtins.float
    memory_gb: builtins.float
    storage_gb: builtins.float
    def __init__(
        self,
        *,
        count: builtins.float = ...,
        cpu: builtins.float = ...,
        memory_gb: builtins.float = ...,
        storage_gb: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "cpu", b"cpu", "memory_gb", b"memory_gb", "storage_gb", b"storage_gb"]) -> None: ...

global___ComposerEnvironmentXConfigXWorkloadsConfigXScheduler = ComposerEnvironmentXConfigXWorkloadsConfigXScheduler

@typing_extensions.final
class ComposerEnvironmentXConfigXWorkloadsConfigXWebServer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CPU_FIELD_NUMBER: builtins.int
    MEMORY_GB_FIELD_NUMBER: builtins.int
    STORAGE_GB_FIELD_NUMBER: builtins.int
    cpu: builtins.float
    memory_gb: builtins.float
    storage_gb: builtins.float
    def __init__(
        self,
        *,
        cpu: builtins.float = ...,
        memory_gb: builtins.float = ...,
        storage_gb: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpu", b"cpu", "memory_gb", b"memory_gb", "storage_gb", b"storage_gb"]) -> None: ...

global___ComposerEnvironmentXConfigXWorkloadsConfigXWebServer = ComposerEnvironmentXConfigXWorkloadsConfigXWebServer

@typing_extensions.final
class ComposerEnvironmentXConfigXWorkloadsConfigXWorker(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CPU_FIELD_NUMBER: builtins.int
    MAX_COUNT_FIELD_NUMBER: builtins.int
    MEMORY_GB_FIELD_NUMBER: builtins.int
    MIN_COUNT_FIELD_NUMBER: builtins.int
    STORAGE_GB_FIELD_NUMBER: builtins.int
    cpu: builtins.float
    max_count: builtins.float
    memory_gb: builtins.float
    min_count: builtins.float
    storage_gb: builtins.float
    def __init__(
        self,
        *,
        cpu: builtins.float = ...,
        max_count: builtins.float = ...,
        memory_gb: builtins.float = ...,
        min_count: builtins.float = ...,
        storage_gb: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpu", b"cpu", "max_count", b"max_count", "memory_gb", b"memory_gb", "min_count", b"min_count", "storage_gb", b"storage_gb"]) -> None: ...

global___ComposerEnvironmentXConfigXWorkloadsConfigXWorker = ComposerEnvironmentXConfigXWorkloadsConfigXWorker

@typing_extensions.final
class ComposerEnvironmentXConfigXWorkloadsConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEDULER_FIELD_NUMBER: builtins.int
    WEB_SERVER_FIELD_NUMBER: builtins.int
    WORKER_FIELD_NUMBER: builtins.int
    @property
    def scheduler(self) -> global___ComposerEnvironmentXConfigXWorkloadsConfigXScheduler: ...
    @property
    def web_server(self) -> global___ComposerEnvironmentXConfigXWorkloadsConfigXWebServer: ...
    @property
    def worker(self) -> global___ComposerEnvironmentXConfigXWorkloadsConfigXWorker: ...
    def __init__(
        self,
        *,
        scheduler: global___ComposerEnvironmentXConfigXWorkloadsConfigXScheduler | None = ...,
        web_server: global___ComposerEnvironmentXConfigXWorkloadsConfigXWebServer | None = ...,
        worker: global___ComposerEnvironmentXConfigXWorkloadsConfigXWorker | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["scheduler", b"scheduler", "web_server", b"web_server", "worker", b"worker"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["scheduler", b"scheduler", "web_server", b"web_server", "worker", b"worker"]) -> None: ...

global___ComposerEnvironmentXConfigXWorkloadsConfig = ComposerEnvironmentXConfigXWorkloadsConfig

@typing_extensions.final
class ComposerEnvironmentXConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AIRFLOW_URI_FIELD_NUMBER: builtins.int
    DAG_GCS_PREFIX_FIELD_NUMBER: builtins.int
    ENVIRONMENT_SIZE_FIELD_NUMBER: builtins.int
    GKE_CLUSTER_FIELD_NUMBER: builtins.int
    NODE_COUNT_FIELD_NUMBER: builtins.int
    DATABASE_CONFIG_FIELD_NUMBER: builtins.int
    ENCRYPTION_CONFIG_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: builtins.int
    NODE_CONFIG_FIELD_NUMBER: builtins.int
    PRIVATE_ENVIRONMENT_CONFIG_FIELD_NUMBER: builtins.int
    SOFTWARE_CONFIG_FIELD_NUMBER: builtins.int
    WEB_SERVER_CONFIG_FIELD_NUMBER: builtins.int
    WEB_SERVER_NETWORK_ACCESS_CONTROL_FIELD_NUMBER: builtins.int
    WORKLOADS_CONFIG_FIELD_NUMBER: builtins.int
    airflow_uri: builtins.str
    dag_gcs_prefix: builtins.str
    environment_size: builtins.str
    gke_cluster: builtins.str
    node_count: builtins.float
    @property
    def database_config(self) -> global___ComposerEnvironmentXConfigXDatabaseConfig: ...
    @property
    def encryption_config(self) -> global___ComposerEnvironmentXConfigXEncryptionConfig: ...
    @property
    def maintenance_window(self) -> global___ComposerEnvironmentXConfigXMaintenanceWindow: ...
    @property
    def master_authorized_networks_config(self) -> global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfig: ...
    @property
    def node_config(self) -> global___ComposerEnvironmentXConfigXNodeConfig: ...
    @property
    def private_environment_config(self) -> global___ComposerEnvironmentXConfigXPrivateEnvironmentConfig: ...
    @property
    def software_config(self) -> global___ComposerEnvironmentXConfigXSoftwareConfig: ...
    @property
    def web_server_config(self) -> global___ComposerEnvironmentXConfigXWebServerConfig: ...
    @property
    def web_server_network_access_control(self) -> global___ComposerEnvironmentXConfigXWebServerNetworkAccessControl: ...
    @property
    def workloads_config(self) -> global___ComposerEnvironmentXConfigXWorkloadsConfig: ...
    def __init__(
        self,
        *,
        airflow_uri: builtins.str = ...,
        dag_gcs_prefix: builtins.str = ...,
        environment_size: builtins.str = ...,
        gke_cluster: builtins.str = ...,
        node_count: builtins.float = ...,
        database_config: global___ComposerEnvironmentXConfigXDatabaseConfig | None = ...,
        encryption_config: global___ComposerEnvironmentXConfigXEncryptionConfig | None = ...,
        maintenance_window: global___ComposerEnvironmentXConfigXMaintenanceWindow | None = ...,
        master_authorized_networks_config: global___ComposerEnvironmentXConfigXMasterAuthorizedNetworksConfig | None = ...,
        node_config: global___ComposerEnvironmentXConfigXNodeConfig | None = ...,
        private_environment_config: global___ComposerEnvironmentXConfigXPrivateEnvironmentConfig | None = ...,
        software_config: global___ComposerEnvironmentXConfigXSoftwareConfig | None = ...,
        web_server_config: global___ComposerEnvironmentXConfigXWebServerConfig | None = ...,
        web_server_network_access_control: global___ComposerEnvironmentXConfigXWebServerNetworkAccessControl | None = ...,
        workloads_config: global___ComposerEnvironmentXConfigXWorkloadsConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["database_config", b"database_config", "encryption_config", b"encryption_config", "maintenance_window", b"maintenance_window", "master_authorized_networks_config", b"master_authorized_networks_config", "node_config", b"node_config", "private_environment_config", b"private_environment_config", "software_config", b"software_config", "web_server_config", b"web_server_config", "web_server_network_access_control", b"web_server_network_access_control", "workloads_config", b"workloads_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["airflow_uri", b"airflow_uri", "dag_gcs_prefix", b"dag_gcs_prefix", "database_config", b"database_config", "encryption_config", b"encryption_config", "environment_size", b"environment_size", "gke_cluster", b"gke_cluster", "maintenance_window", b"maintenance_window", "master_authorized_networks_config", b"master_authorized_networks_config", "node_config", b"node_config", "node_count", b"node_count", "private_environment_config", b"private_environment_config", "software_config", b"software_config", "web_server_config", b"web_server_config", "web_server_network_access_control", b"web_server_network_access_control", "workloads_config", b"workloads_config"]) -> None: ...

global___ComposerEnvironmentXConfig = ComposerEnvironmentXConfig

@typing_extensions.final
class ComposerEnvironmentXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    create: builtins.str
    delete: builtins.str
    update: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
        delete: builtins.str = ...,
        update: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create", "delete", b"delete", "update", b"update"]) -> None: ...

global___ComposerEnvironmentXTimeouts = ComposerEnvironmentXTimeouts

@typing_extensions.final
class ComposerEnvironment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    project: builtins.str
    region: builtins.str
    @property
    def config(self) -> global___ComposerEnvironmentXConfig: ...
    @property
    def timeouts(self) -> global___ComposerEnvironmentXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        region: builtins.str = ...,
        config: global___ComposerEnvironmentXConfig | None = ...,
        timeouts: global___ComposerEnvironmentXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "id", b"id", "labels", b"labels", "name", b"name", "project", b"project", "region", b"region", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___ComposerEnvironment = ComposerEnvironment
