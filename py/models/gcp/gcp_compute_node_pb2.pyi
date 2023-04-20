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
class ComputeNodeGroupXAutoscalingPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_NODES_FIELD_NUMBER: builtins.int
    MIN_NODES_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    max_nodes: builtins.float
    min_nodes: builtins.float
    mode: builtins.str
    def __init__(
        self,
        *,
        max_nodes: builtins.float = ...,
        min_nodes: builtins.float = ...,
        mode: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_nodes", b"max_nodes", "min_nodes", b"min_nodes", "mode", b"mode"]) -> None: ...

global___ComputeNodeGroupXAutoscalingPolicy = ComputeNodeGroupXAutoscalingPolicy

@typing_extensions.final
class ComputeNodeGroupXMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    start_time: builtins.str
    def __init__(
        self,
        *,
        start_time: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["start_time", b"start_time"]) -> None: ...

global___ComputeNodeGroupXMaintenanceWindow = ComputeNodeGroupXMaintenanceWindow

@typing_extensions.final
class ComputeNodeGroupXTimeouts(google.protobuf.message.Message):
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

global___ComputeNodeGroupXTimeouts = ComputeNodeGroupXTimeouts

@typing_extensions.final
class ComputeNodeGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INITIAL_SIZE_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NODE_TEMPLATE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    SELF_LINK_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    ZONE_FIELD_NUMBER: builtins.int
    AUTOSCALING_POLICY_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    creation_timestamp: builtins.str
    description: builtins.str
    id: builtins.str
    initial_size: builtins.float
    maintenance_policy: builtins.str
    name: builtins.str
    node_template: builtins.str
    project: builtins.str
    self_link: builtins.str
    size: builtins.float
    zone: builtins.str
    @property
    def autoscaling_policy(self) -> global___ComputeNodeGroupXAutoscalingPolicy: ...
    @property
    def maintenance_window(self) -> global___ComputeNodeGroupXMaintenanceWindow: ...
    @property
    def timeouts(self) -> global___ComputeNodeGroupXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        creation_timestamp: builtins.str = ...,
        description: builtins.str = ...,
        id: builtins.str = ...,
        initial_size: builtins.float = ...,
        maintenance_policy: builtins.str = ...,
        name: builtins.str = ...,
        node_template: builtins.str = ...,
        project: builtins.str = ...,
        self_link: builtins.str = ...,
        size: builtins.float = ...,
        zone: builtins.str = ...,
        autoscaling_policy: global___ComputeNodeGroupXAutoscalingPolicy | None = ...,
        maintenance_window: global___ComputeNodeGroupXMaintenanceWindow | None = ...,
        timeouts: global___ComputeNodeGroupXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["autoscaling_policy", b"autoscaling_policy", "maintenance_window", b"maintenance_window", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["autoscaling_policy", b"autoscaling_policy", "creation_timestamp", b"creation_timestamp", "description", b"description", "id", b"id", "initial_size", b"initial_size", "maintenance_policy", b"maintenance_policy", "maintenance_window", b"maintenance_window", "name", b"name", "node_template", b"node_template", "project", b"project", "resource_info", b"resource_info", "self_link", b"self_link", "size", b"size", "timeouts", b"timeouts", "zone", b"zone"]) -> None: ...

global___ComputeNodeGroup = ComputeNodeGroup

@typing_extensions.final
class ComputeNodeTemplateXNodeTypeFlexibility(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CPUS_FIELD_NUMBER: builtins.int
    LOCAL_SSD_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    cpus: builtins.str
    local_ssd: builtins.str
    memory: builtins.str
    def __init__(
        self,
        *,
        cpus: builtins.str = ...,
        local_ssd: builtins.str = ...,
        memory: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpus", b"cpus", "local_ssd", b"local_ssd", "memory", b"memory"]) -> None: ...

global___ComputeNodeTemplateXNodeTypeFlexibility = ComputeNodeTemplateXNodeTypeFlexibility

@typing_extensions.final
class ComputeNodeTemplateXServerBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    type: builtins.str
    def __init__(
        self,
        *,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["type", b"type"]) -> None: ...

global___ComputeNodeTemplateXServerBinding = ComputeNodeTemplateXServerBinding

@typing_extensions.final
class ComputeNodeTemplateXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    create: builtins.str
    delete: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
        delete: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create", "delete", b"delete"]) -> None: ...

global___ComputeNodeTemplateXTimeouts = ComputeNodeTemplateXTimeouts

@typing_extensions.final
class ComputeNodeTemplate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class NodeAffinityLabelsEntry(google.protobuf.message.Message):
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

    CPU_OVERCOMMIT_TYPE_FIELD_NUMBER: builtins.int
    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NODE_AFFINITY_LABELS_FIELD_NUMBER: builtins.int
    NODE_TYPE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    SELF_LINK_FIELD_NUMBER: builtins.int
    NODE_TYPE_FLEXIBILITY_FIELD_NUMBER: builtins.int
    SERVER_BINDING_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    cpu_overcommit_type: builtins.str
    creation_timestamp: builtins.str
    description: builtins.str
    id: builtins.str
    name: builtins.str
    @property
    def node_affinity_labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    node_type: builtins.str
    project: builtins.str
    region: builtins.str
    self_link: builtins.str
    @property
    def node_type_flexibility(self) -> global___ComputeNodeTemplateXNodeTypeFlexibility: ...
    @property
    def server_binding(self) -> global___ComputeNodeTemplateXServerBinding: ...
    @property
    def timeouts(self) -> global___ComputeNodeTemplateXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        cpu_overcommit_type: builtins.str = ...,
        creation_timestamp: builtins.str = ...,
        description: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        node_affinity_labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        node_type: builtins.str = ...,
        project: builtins.str = ...,
        region: builtins.str = ...,
        self_link: builtins.str = ...,
        node_type_flexibility: global___ComputeNodeTemplateXNodeTypeFlexibility | None = ...,
        server_binding: global___ComputeNodeTemplateXServerBinding | None = ...,
        timeouts: global___ComputeNodeTemplateXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node_type_flexibility", b"node_type_flexibility", "resource_info", b"resource_info", "server_binding", b"server_binding", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpu_overcommit_type", b"cpu_overcommit_type", "creation_timestamp", b"creation_timestamp", "description", b"description", "id", b"id", "name", b"name", "node_affinity_labels", b"node_affinity_labels", "node_type", b"node_type", "node_type_flexibility", b"node_type_flexibility", "project", b"project", "region", b"region", "resource_info", b"resource_info", "self_link", b"self_link", "server_binding", b"server_binding", "timeouts", b"timeouts"]) -> None: ...

global___ComputeNodeTemplate = ComputeNodeTemplate