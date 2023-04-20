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
class ClouddeployDeliveryPipelineXSerialPipelineXStages(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROFILES_FIELD_NUMBER: builtins.int
    TARGET_ID_FIELD_NUMBER: builtins.int
    @property
    def profiles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    target_id: builtins.str
    def __init__(
        self,
        *,
        profiles: collections.abc.Iterable[builtins.str] | None = ...,
        target_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["profiles", b"profiles", "target_id", b"target_id"]) -> None: ...

global___ClouddeployDeliveryPipelineXSerialPipelineXStages = ClouddeployDeliveryPipelineXSerialPipelineXStages

@typing_extensions.final
class ClouddeployDeliveryPipelineXSerialPipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STAGES_FIELD_NUMBER: builtins.int
    @property
    def stages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClouddeployDeliveryPipelineXSerialPipelineXStages]: ...
    def __init__(
        self,
        *,
        stages: collections.abc.Iterable[global___ClouddeployDeliveryPipelineXSerialPipelineXStages] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stages", b"stages"]) -> None: ...

global___ClouddeployDeliveryPipelineXSerialPipeline = ClouddeployDeliveryPipelineXSerialPipeline

@typing_extensions.final
class ClouddeployDeliveryPipelineXTimeouts(google.protobuf.message.Message):
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

global___ClouddeployDeliveryPipelineXTimeouts = ClouddeployDeliveryPipelineXTimeouts

@typing_extensions.final
class ClouddeployDeliveryPipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AnnotationsEntry(google.protobuf.message.Message):
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
    class ConditionEntry(google.protobuf.message.Message):
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

    ANNOTATIONS_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    SUSPENDED_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    SERIAL_PIPELINE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def condition(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    create_time: builtins.str
    description: builtins.str
    etag: builtins.str
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    location: builtins.str
    name: builtins.str
    project: builtins.str
    suspended: builtins.bool
    uid: builtins.str
    update_time: builtins.str
    @property
    def serial_pipeline(self) -> global___ClouddeployDeliveryPipelineXSerialPipeline: ...
    @property
    def timeouts(self) -> global___ClouddeployDeliveryPipelineXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        annotations: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        condition: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        create_time: builtins.str = ...,
        description: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        suspended: builtins.bool = ...,
        uid: builtins.str = ...,
        update_time: builtins.str = ...,
        serial_pipeline: global___ClouddeployDeliveryPipelineXSerialPipeline | None = ...,
        timeouts: global___ClouddeployDeliveryPipelineXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "serial_pipeline", b"serial_pipeline", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations", b"annotations", "condition", b"condition", "create_time", b"create_time", "description", b"description", "etag", b"etag", "id", b"id", "labels", b"labels", "location", b"location", "name", b"name", "project", b"project", "resource_info", b"resource_info", "serial_pipeline", b"serial_pipeline", "suspended", b"suspended", "timeouts", b"timeouts", "uid", b"uid", "update_time", b"update_time"]) -> None: ...

global___ClouddeployDeliveryPipeline = ClouddeployDeliveryPipeline

@typing_extensions.final
class ClouddeployTargetXAnthosCluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MEMBERSHIP_FIELD_NUMBER: builtins.int
    membership: builtins.str
    def __init__(
        self,
        *,
        membership: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["membership", b"membership"]) -> None: ...

global___ClouddeployTargetXAnthosCluster = ClouddeployTargetXAnthosCluster

@typing_extensions.final
class ClouddeployTargetXExecutionConfigs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_STORAGE_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    USAGES_FIELD_NUMBER: builtins.int
    WORKER_POOL_FIELD_NUMBER: builtins.int
    artifact_storage: builtins.str
    service_account: builtins.str
    @property
    def usages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    worker_pool: builtins.str
    def __init__(
        self,
        *,
        artifact_storage: builtins.str = ...,
        service_account: builtins.str = ...,
        usages: collections.abc.Iterable[builtins.str] | None = ...,
        worker_pool: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["artifact_storage", b"artifact_storage", "service_account", b"service_account", "usages", b"usages", "worker_pool", b"worker_pool"]) -> None: ...

global___ClouddeployTargetXExecutionConfigs = ClouddeployTargetXExecutionConfigs

@typing_extensions.final
class ClouddeployTargetXGke(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_FIELD_NUMBER: builtins.int
    INTERNAL_IP_FIELD_NUMBER: builtins.int
    cluster: builtins.str
    internal_ip: builtins.bool
    def __init__(
        self,
        *,
        cluster: builtins.str = ...,
        internal_ip: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "internal_ip", b"internal_ip"]) -> None: ...

global___ClouddeployTargetXGke = ClouddeployTargetXGke

@typing_extensions.final
class ClouddeployTargetXTimeouts(google.protobuf.message.Message):
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

global___ClouddeployTargetXTimeouts = ClouddeployTargetXTimeouts

@typing_extensions.final
class ClouddeployTarget(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AnnotationsEntry(google.protobuf.message.Message):
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

    ANNOTATIONS_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REQUIRE_APPROVAL_FIELD_NUMBER: builtins.int
    TARGET_ID_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    ANTHOS_CLUSTER_FIELD_NUMBER: builtins.int
    EXECUTION_CONFIGS_FIELD_NUMBER: builtins.int
    GKE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    create_time: builtins.str
    description: builtins.str
    etag: builtins.str
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    location: builtins.str
    name: builtins.str
    project: builtins.str
    require_approval: builtins.bool
    target_id: builtins.str
    uid: builtins.str
    update_time: builtins.str
    @property
    def anthos_cluster(self) -> global___ClouddeployTargetXAnthosCluster: ...
    @property
    def execution_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClouddeployTargetXExecutionConfigs]: ...
    @property
    def gke(self) -> global___ClouddeployTargetXGke: ...
    @property
    def timeouts(self) -> global___ClouddeployTargetXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        annotations: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        create_time: builtins.str = ...,
        description: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        require_approval: builtins.bool = ...,
        target_id: builtins.str = ...,
        uid: builtins.str = ...,
        update_time: builtins.str = ...,
        anthos_cluster: global___ClouddeployTargetXAnthosCluster | None = ...,
        execution_configs: collections.abc.Iterable[global___ClouddeployTargetXExecutionConfigs] | None = ...,
        gke: global___ClouddeployTargetXGke | None = ...,
        timeouts: global___ClouddeployTargetXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["anthos_cluster", b"anthos_cluster", "gke", b"gke", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations", b"annotations", "anthos_cluster", b"anthos_cluster", "create_time", b"create_time", "description", b"description", "etag", b"etag", "execution_configs", b"execution_configs", "gke", b"gke", "id", b"id", "labels", b"labels", "location", b"location", "name", b"name", "project", b"project", "require_approval", b"require_approval", "resource_info", b"resource_info", "target_id", b"target_id", "timeouts", b"timeouts", "uid", b"uid", "update_time", b"update_time"]) -> None: ...

global___ClouddeployTarget = ClouddeployTarget