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
class ComputeEnvironmentLaunchTemplateSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LAUNCH_TEMPLATE_NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    LAUNCH_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    launch_template_name: builtins.str
    version: builtins.str
    launch_template_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        launch_template_name: builtins.str = ...,
        version: builtins.str = ...,
        launch_template_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["launch_template_id", b"launch_template_id", "launch_template_name", b"launch_template_name", "resource_info", b"resource_info", "version", b"version"]) -> None: ...

global___ComputeEnvironmentLaunchTemplateSpecification = ComputeEnvironmentLaunchTemplateSpecification

@typing_extensions.final
class ComputeEnvironmentComputeResources(google.protobuf.message.Message):
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
    SPOT_IAM_FLEET_ROLE_FIELD_NUMBER: builtins.int
    MAXV_CPUS_FIELD_NUMBER: builtins.int
    BID_PERCENTAGE_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    SUBNETS_FIELD_NUMBER: builtins.int
    ALLOCATION_STRATEGY_FIELD_NUMBER: builtins.int
    MINV_CPUS_FIELD_NUMBER: builtins.int
    LAUNCH_TEMPLATE_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    INSTANCE_ROLE_FIELD_NUMBER: builtins.int
    INSTANCE_TYPES_FIELD_NUMBER: builtins.int
    EC2_KEY_PAIR_FIELD_NUMBER: builtins.int
    PLACEMENT_GROUP_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    DESIREDV_CPUS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    spot_iam_fleet_role: builtins.str
    maxv_cpus: builtins.int
    bid_percentage: builtins.int
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    allocation_strategy: builtins.str
    minv_cpus: builtins.int
    @property
    def launch_template(self) -> global___ComputeEnvironmentLaunchTemplateSpecification: ...
    image_id: builtins.str
    instance_role: builtins.str
    @property
    def instance_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    ec2_key_pair: builtins.str
    placement_group: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    desiredv_cpus: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        spot_iam_fleet_role: builtins.str = ...,
        maxv_cpus: builtins.int = ...,
        bid_percentage: builtins.int = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        subnets: collections.abc.Iterable[builtins.str] | None = ...,
        allocation_strategy: builtins.str = ...,
        minv_cpus: builtins.int = ...,
        launch_template: global___ComputeEnvironmentLaunchTemplateSpecification | None = ...,
        image_id: builtins.str = ...,
        instance_role: builtins.str = ...,
        instance_types: collections.abc.Iterable[builtins.str] | None = ...,
        ec2_key_pair: builtins.str = ...,
        placement_group: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        desiredv_cpus: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["launch_template", b"launch_template", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allocation_strategy", b"allocation_strategy", "bid_percentage", b"bid_percentage", "desiredv_cpus", b"desiredv_cpus", "ec2_key_pair", b"ec2_key_pair", "image_id", b"image_id", "instance_role", b"instance_role", "instance_types", b"instance_types", "launch_template", b"launch_template", "maxv_cpus", b"maxv_cpus", "minv_cpus", b"minv_cpus", "placement_group", b"placement_group", "resource_info", b"resource_info", "security_group_ids", b"security_group_ids", "spot_iam_fleet_role", b"spot_iam_fleet_role", "subnets", b"subnets", "tags", b"tags"]) -> None: ...

global___ComputeEnvironmentComputeResources = ComputeEnvironmentComputeResources

@typing_extensions.final
class ComputeEnvironment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SERVICE_ROLE_FIELD_NUMBER: builtins.int
    COMPUTE_ENVIRONMENT_NAME_FIELD_NUMBER: builtins.int
    COMPUTE_RESOURCES_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    type: builtins.str
    service_role: builtins.str
    compute_environment_name: builtins.str
    @property
    def compute_resources(self) -> global___ComputeEnvironmentComputeResources: ...
    state: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        type: builtins.str = ...,
        service_role: builtins.str = ...,
        compute_environment_name: builtins.str = ...,
        compute_resources: global___ComputeEnvironmentComputeResources | None = ...,
        state: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compute_resources", b"compute_resources", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_environment_name", b"compute_environment_name", "compute_resources", b"compute_resources", "resource_info", b"resource_info", "service_role", b"service_role", "state", b"state", "type", b"type"]) -> None: ...

global___ComputeEnvironment = ComputeEnvironment

@typing_extensions.final
class Batch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_ENVIRONMENT_FIELD_NUMBER: builtins.int
    JOB_DEFINITION_FIELD_NUMBER: builtins.int
    JOB_QUEUE_FIELD_NUMBER: builtins.int
    @property
    def compute_environment(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeEnvironment]: ...
    @property
    def job_definition(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinition]: ...
    @property
    def job_queue(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobQueue]: ...
    def __init__(
        self,
        *,
        compute_environment: collections.abc.Iterable[global___ComputeEnvironment] | None = ...,
        job_definition: collections.abc.Iterable[global___JobDefinition] | None = ...,
        job_queue: collections.abc.Iterable[global___JobQueue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_environment", b"compute_environment", "job_definition", b"job_definition", "job_queue", b"job_queue"]) -> None: ...

global___Batch = Batch

@typing_extensions.final
class JobDefinitionSecret(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VALUE_FROM_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    value_from: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        value_from: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info", "value_from", b"value_from"]) -> None: ...

global___JobDefinitionSecret = JobDefinitionSecret

@typing_extensions.final
class JobDefinitionTmpfs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    CONTAINER_PATH_FIELD_NUMBER: builtins.int
    MOUNT_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    size: builtins.int
    container_path: builtins.str
    @property
    def mount_options(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        size: builtins.int = ...,
        container_path: builtins.str = ...,
        mount_options: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_path", b"container_path", "mount_options", b"mount_options", "resource_info", b"resource_info", "size", b"size"]) -> None: ...

global___JobDefinitionTmpfs = JobDefinitionTmpfs

@typing_extensions.final
class JobDefinitionDevice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    HOST_PATH_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    CONTAINER_PATH_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    host_path: builtins.str
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    container_path: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        host_path: builtins.str = ...,
        permissions: collections.abc.Iterable[builtins.str] | None = ...,
        container_path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_path", b"container_path", "host_path", b"host_path", "permissions", b"permissions", "resource_info", b"resource_info"]) -> None: ...

global___JobDefinitionDevice = JobDefinitionDevice

@typing_extensions.final
class JobDefinitionLinuxParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SWAPPINESS_FIELD_NUMBER: builtins.int
    TMPFS_FIELD_NUMBER: builtins.int
    SHARED_MEMORY_SIZE_FIELD_NUMBER: builtins.int
    DEVICES_FIELD_NUMBER: builtins.int
    INIT_PROCESS_ENABLED_FIELD_NUMBER: builtins.int
    MAX_SWAP_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    swappiness: builtins.int
    @property
    def tmpfs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionTmpfs]: ...
    shared_memory_size: builtins.int
    @property
    def devices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionDevice]: ...
    init_process_enabled: builtins.bool
    max_swap: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        swappiness: builtins.int = ...,
        tmpfs: collections.abc.Iterable[global___JobDefinitionTmpfs] | None = ...,
        shared_memory_size: builtins.int = ...,
        devices: collections.abc.Iterable[global___JobDefinitionDevice] | None = ...,
        init_process_enabled: builtins.bool = ...,
        max_swap: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["devices", b"devices", "init_process_enabled", b"init_process_enabled", "max_swap", b"max_swap", "resource_info", b"resource_info", "shared_memory_size", b"shared_memory_size", "swappiness", b"swappiness", "tmpfs", b"tmpfs"]) -> None: ...

global___JobDefinitionLinuxParameters = JobDefinitionLinuxParameters

@typing_extensions.final
class JobDefinitionResourceRequirement(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___JobDefinitionResourceRequirement = JobDefinitionResourceRequirement

@typing_extensions.final
class JobDefinitionLogConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
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
    SECRET_OPTIONS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    LOG_DRIVER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def secret_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionSecret]: ...
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    log_driver: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        secret_options: collections.abc.Iterable[global___JobDefinitionSecret] | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        log_driver: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_driver", b"log_driver", "options", b"options", "resource_info", b"resource_info", "secret_options", b"secret_options"]) -> None: ...

global___JobDefinitionLogConfiguration = JobDefinitionLogConfiguration

@typing_extensions.final
class JobDefinitionMountPoints(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    READ_ONLY_FIELD_NUMBER: builtins.int
    SOURCE_VOLUME_FIELD_NUMBER: builtins.int
    CONTAINER_PATH_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    read_only: builtins.bool
    source_volume: builtins.str
    container_path: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        read_only: builtins.bool = ...,
        source_volume: builtins.str = ...,
        container_path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_path", b"container_path", "read_only", b"read_only", "resource_info", b"resource_info", "source_volume", b"source_volume"]) -> None: ...

global___JobDefinitionMountPoints = JobDefinitionMountPoints

@typing_extensions.final
class JobDefinitionVolumesHost(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SOURCE_PATH_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    source_path: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        source_path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "source_path", b"source_path"]) -> None: ...

global___JobDefinitionVolumesHost = JobDefinitionVolumesHost

@typing_extensions.final
class JobDefinitionVolumes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def host(self) -> global___JobDefinitionVolumesHost: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        host: global___JobDefinitionVolumesHost | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host", b"host", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["host", b"host", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___JobDefinitionVolumes = JobDefinitionVolumes

@typing_extensions.final
class JobDefinitionEnvironment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    value: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        value: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___JobDefinitionEnvironment = JobDefinitionEnvironment

@typing_extensions.final
class JobDefinitionUlimit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SOFT_LIMIT_FIELD_NUMBER: builtins.int
    HARD_LIMIT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    soft_limit: builtins.int
    hard_limit: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        soft_limit: builtins.int = ...,
        hard_limit: builtins.int = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hard_limit", b"hard_limit", "name", b"name", "resource_info", b"resource_info", "soft_limit", b"soft_limit"]) -> None: ...

global___JobDefinitionUlimit = JobDefinitionUlimit

@typing_extensions.final
class JobDefinitionContainerProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    SECRETS_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    PRIVILEGED_FIELD_NUMBER: builtins.int
    LINUX_PARAMETERS_FIELD_NUMBER: builtins.int
    JOB_ROLE_ARN_FIELD_NUMBER: builtins.int
    READONLY_ROOT_FILESYSTEM_FIELD_NUMBER: builtins.int
    VCPUS_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    RESOURCE_REQUIREMENTS_FIELD_NUMBER: builtins.int
    LOG_CONFIGURATION_FIELD_NUMBER: builtins.int
    MOUNT_POINTS_FIELD_NUMBER: builtins.int
    EXECUTION_ROLE_ARN_FIELD_NUMBER: builtins.int
    VOLUMES_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    ULIMITS_FIELD_NUMBER: builtins.int
    INSTANCE_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    user: builtins.str
    @property
    def secrets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionSecret]: ...
    memory: builtins.int
    privileged: builtins.bool
    @property
    def linux_parameters(self) -> global___JobDefinitionLinuxParameters: ...
    job_role_arn: builtins.str
    readonly_root_filesystem: builtins.bool
    vcpus: builtins.int
    image: builtins.str
    @property
    def resource_requirements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionResourceRequirement]: ...
    @property
    def log_configuration(self) -> global___JobDefinitionLogConfiguration: ...
    @property
    def mount_points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionMountPoints]: ...
    execution_role_arn: builtins.str
    @property
    def volumes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionVolumes]: ...
    @property
    def command(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def environment(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionEnvironment]: ...
    @property
    def ulimits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionUlimit]: ...
    instance_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        user: builtins.str = ...,
        secrets: collections.abc.Iterable[global___JobDefinitionSecret] | None = ...,
        memory: builtins.int = ...,
        privileged: builtins.bool = ...,
        linux_parameters: global___JobDefinitionLinuxParameters | None = ...,
        job_role_arn: builtins.str = ...,
        readonly_root_filesystem: builtins.bool = ...,
        vcpus: builtins.int = ...,
        image: builtins.str = ...,
        resource_requirements: collections.abc.Iterable[global___JobDefinitionResourceRequirement] | None = ...,
        log_configuration: global___JobDefinitionLogConfiguration | None = ...,
        mount_points: collections.abc.Iterable[global___JobDefinitionMountPoints] | None = ...,
        execution_role_arn: builtins.str = ...,
        volumes: collections.abc.Iterable[global___JobDefinitionVolumes] | None = ...,
        command: collections.abc.Iterable[builtins.str] | None = ...,
        environment: collections.abc.Iterable[global___JobDefinitionEnvironment] | None = ...,
        ulimits: collections.abc.Iterable[global___JobDefinitionUlimit] | None = ...,
        instance_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["linux_parameters", b"linux_parameters", "log_configuration", b"log_configuration", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["command", b"command", "environment", b"environment", "execution_role_arn", b"execution_role_arn", "image", b"image", "instance_type", b"instance_type", "job_role_arn", b"job_role_arn", "linux_parameters", b"linux_parameters", "log_configuration", b"log_configuration", "memory", b"memory", "mount_points", b"mount_points", "privileged", b"privileged", "readonly_root_filesystem", b"readonly_root_filesystem", "resource_info", b"resource_info", "resource_requirements", b"resource_requirements", "secrets", b"secrets", "ulimits", b"ulimits", "user", b"user", "vcpus", b"vcpus", "volumes", b"volumes"]) -> None: ...

global___JobDefinitionContainerProperties = JobDefinitionContainerProperties

@typing_extensions.final
class JobDefinitionNodeRangeProperty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CONTAINER_FIELD_NUMBER: builtins.int
    TARGET_NODES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def container(self) -> global___JobDefinitionContainerProperties: ...
    target_nodes: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        container: global___JobDefinitionContainerProperties | None = ...,
        target_nodes: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["container", b"container", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container", b"container", "resource_info", b"resource_info", "target_nodes", b"target_nodes"]) -> None: ...

global___JobDefinitionNodeRangeProperty = JobDefinitionNodeRangeProperty

@typing_extensions.final
class JobDefinitionNodeProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    MAIN_NODE_FIELD_NUMBER: builtins.int
    NODE_RANGE_PROPERTIES_FIELD_NUMBER: builtins.int
    NUM_NODES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    main_node: builtins.int
    @property
    def node_range_properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDefinitionNodeRangeProperty]: ...
    num_nodes: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        main_node: builtins.int = ...,
        node_range_properties: collections.abc.Iterable[global___JobDefinitionNodeRangeProperty] | None = ...,
        num_nodes: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["main_node", b"main_node", "node_range_properties", b"node_range_properties", "num_nodes", b"num_nodes", "resource_info", b"resource_info"]) -> None: ...

global___JobDefinitionNodeProperties = JobDefinitionNodeProperties

@typing_extensions.final
class JobDefinitionTimeout(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTEMPT_DURATION_SECONDS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    attempt_duration_seconds: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attempt_duration_seconds: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attempt_duration_seconds", b"attempt_duration_seconds", "resource_info", b"resource_info"]) -> None: ...

global___JobDefinitionTimeout = JobDefinitionTimeout

@typing_extensions.final
class JobDefinitionRetryStrategy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTEMPTS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    attempts: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attempts: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attempts", b"attempts", "resource_info", b"resource_info"]) -> None: ...

global___JobDefinitionRetryStrategy = JobDefinitionRetryStrategy

@typing_extensions.final
class JobDefinition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ParametersEntry(google.protobuf.message.Message):
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
    TYPE_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    NODE_PROPERTIES_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    CONTAINER_PROPERTIES_FIELD_NUMBER: builtins.int
    JOB_DEFINITION_NAME_FIELD_NUMBER: builtins.int
    RETRY_STRATEGY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    type: builtins.str
    @property
    def parameters(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def node_properties(self) -> global___JobDefinitionNodeProperties: ...
    @property
    def timeout(self) -> global___JobDefinitionTimeout: ...
    @property
    def container_properties(self) -> global___JobDefinitionContainerProperties: ...
    job_definition_name: builtins.str
    @property
    def retry_strategy(self) -> global___JobDefinitionRetryStrategy: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        type: builtins.str = ...,
        parameters: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        node_properties: global___JobDefinitionNodeProperties | None = ...,
        timeout: global___JobDefinitionTimeout | None = ...,
        container_properties: global___JobDefinitionContainerProperties | None = ...,
        job_definition_name: builtins.str = ...,
        retry_strategy: global___JobDefinitionRetryStrategy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["container_properties", b"container_properties", "node_properties", b"node_properties", "resource_info", b"resource_info", "retry_strategy", b"retry_strategy", "timeout", b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["container_properties", b"container_properties", "job_definition_name", b"job_definition_name", "node_properties", b"node_properties", "parameters", b"parameters", "resource_info", b"resource_info", "retry_strategy", b"retry_strategy", "timeout", b"timeout", "type", b"type"]) -> None: ...

global___JobDefinition = JobDefinition

@typing_extensions.final
class JobQueueComputeEnvironmentOrder(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    COMPUTE_ENVIRONMENT_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    compute_environment: builtins.str
    order: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        compute_environment: builtins.str = ...,
        order: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_environment", b"compute_environment", "order", b"order", "resource_info", b"resource_info"]) -> None: ...

global___JobQueueComputeEnvironmentOrder = JobQueueComputeEnvironmentOrder

@typing_extensions.final
class JobQueue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    COMPUTE_ENVIRONMENT_ORDER_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    JOB_QUEUE_NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def compute_environment_order(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobQueueComputeEnvironmentOrder]: ...
    priority: builtins.int
    state: builtins.str
    job_queue_name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        compute_environment_order: collections.abc.Iterable[global___JobQueueComputeEnvironmentOrder] | None = ...,
        priority: builtins.int = ...,
        state: builtins.str = ...,
        job_queue_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_environment_order", b"compute_environment_order", "job_queue_name", b"job_queue_name", "priority", b"priority", "resource_info", b"resource_info", "state", b"state"]) -> None: ...

global___JobQueue = JobQueue
