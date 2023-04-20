"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import kubernetes.kubernetes_io.k8s.api.core.v1_pb2
import kubernetes.kubernetes_io.k8s.apimachinery.pkg.api.resource_pb2
import kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CSIDriver(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def spec(self) -> global___CSIDriverSpec: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___CSIDriverSpec | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec"]) -> None: ...

global___CSIDriver = CSIDriver

@typing_extensions.final
class CSIDriverList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CSIDriver]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___CSIDriver] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___CSIDriverList = CSIDriverList

@typing_extensions.final
class CSIDriverSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTACH_REQUIRED_FIELD_NUMBER: builtins.int
    FS_GROUP_POLICY_FIELD_NUMBER: builtins.int
    POD_INFO_ON_MOUNT_FIELD_NUMBER: builtins.int
    REQUIRES_REPUBLISH_FIELD_NUMBER: builtins.int
    SE_LINUX_MOUNT_FIELD_NUMBER: builtins.int
    STORAGE_CAPACITY_FIELD_NUMBER: builtins.int
    TOKEN_REQUESTS_FIELD_NUMBER: builtins.int
    VOLUME_LIFECYCLE_MODES_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    attach_required: builtins.bool
    fs_group_policy: builtins.str
    pod_info_on_mount: builtins.bool
    requires_republish: builtins.bool
    se_linux_mount: builtins.bool
    storage_capacity: builtins.bool
    @property
    def token_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TokenRequest]: ...
    @property
    def volume_lifecycle_modes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        attach_required: builtins.bool = ...,
        fs_group_policy: builtins.str = ...,
        pod_info_on_mount: builtins.bool = ...,
        requires_republish: builtins.bool = ...,
        se_linux_mount: builtins.bool = ...,
        storage_capacity: builtins.bool = ...,
        token_requests: collections.abc.Iterable[global___TokenRequest] | None = ...,
        volume_lifecycle_modes: collections.abc.Iterable[builtins.str] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attach_required", b"attach_required", "fs_group_policy", b"fs_group_policy", "pod_info_on_mount", b"pod_info_on_mount", "requires_republish", b"requires_republish", "resource_info", b"resource_info", "se_linux_mount", b"se_linux_mount", "storage_capacity", b"storage_capacity", "token_requests", b"token_requests", "volume_lifecycle_modes", b"volume_lifecycle_modes"]) -> None: ...

global___CSIDriverSpec = CSIDriverSpec

@typing_extensions.final
class CSINode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def spec(self) -> global___CSINodeSpec: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___CSINodeSpec | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec"]) -> None: ...

global___CSINode = CSINode

@typing_extensions.final
class CSINodeDriver(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOCATABLE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NODE_ID_FIELD_NUMBER: builtins.int
    TOPOLOGY_KEYS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def allocatable(self) -> global___VolumeNodeResources: ...
    name: builtins.str
    node_id: builtins.str
    @property
    def topology_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        allocatable: global___VolumeNodeResources | None = ...,
        name: builtins.str = ...,
        node_id: builtins.str = ...,
        topology_keys: collections.abc.Iterable[builtins.str] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allocatable", b"allocatable", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allocatable", b"allocatable", "name", b"name", "node_id", b"node_id", "resource_info", b"resource_info", "topology_keys", b"topology_keys"]) -> None: ...

global___CSINodeDriver = CSINodeDriver

@typing_extensions.final
class CSINodeList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CSINode]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___CSINode] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___CSINodeList = CSINodeList

@typing_extensions.final
class CSINodeSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRIVERS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def drivers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CSINodeDriver]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        drivers: collections.abc.Iterable[global___CSINodeDriver] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["drivers", b"drivers", "resource_info", b"resource_info"]) -> None: ...

global___CSINodeSpec = CSINodeSpec

@typing_extensions.final
class CSIStorageCapacity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    CAPACITY_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    MAXIMUM_VOLUME_SIZE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    NODE_TOPOLOGY_FIELD_NUMBER: builtins.int
    STORAGE_CLASS_NAME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def capacity(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.api.resource_pb2.Quantity: ...
    kind: builtins.str
    @property
    def maximum_volume_size(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.api.resource_pb2.Quantity: ...
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def node_topology(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.LabelSelector: ...
    storage_class_name: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        capacity: kubernetes.kubernetes_io.k8s.apimachinery.pkg.api.resource_pb2.Quantity | None = ...,
        kind: builtins.str = ...,
        maximum_volume_size: kubernetes.kubernetes_io.k8s.apimachinery.pkg.api.resource_pb2.Quantity | None = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        node_topology: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.LabelSelector | None = ...,
        storage_class_name: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["capacity", b"capacity", "maximum_volume_size", b"maximum_volume_size", "metadata", b"metadata", "node_topology", b"node_topology", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "capacity", b"capacity", "kind", b"kind", "maximum_volume_size", b"maximum_volume_size", "metadata", b"metadata", "node_topology", b"node_topology", "resource_info", b"resource_info", "storage_class_name", b"storage_class_name"]) -> None: ...

global___CSIStorageCapacity = CSIStorageCapacity

@typing_extensions.final
class CSIStorageCapacityList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CSIStorageCapacity]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___CSIStorageCapacity] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___CSIStorageCapacityList = CSIStorageCapacityList

@typing_extensions.final
class StorageClass(google.protobuf.message.Message):
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

    ALLOW_VOLUME_EXPANSION_FIELD_NUMBER: builtins.int
    ALLOWED_TOPOLOGIES_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    MOUNT_OPTIONS_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    PROVISIONER_FIELD_NUMBER: builtins.int
    RECLAIM_POLICY_FIELD_NUMBER: builtins.int
    VOLUME_BINDING_MODE_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    allow_volume_expansion: builtins.bool
    @property
    def allowed_topologies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.TopologySelectorTerm]: ...
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def mount_options(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def parameters(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    provisioner: builtins.str
    reclaim_policy: builtins.str
    volume_binding_mode: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        allow_volume_expansion: builtins.bool = ...,
        allowed_topologies: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.TopologySelectorTerm] | None = ...,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        mount_options: collections.abc.Iterable[builtins.str] | None = ...,
        parameters: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        provisioner: builtins.str = ...,
        reclaim_policy: builtins.str = ...,
        volume_binding_mode: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_volume_expansion", b"allow_volume_expansion", "allowed_topologies", b"allowed_topologies", "api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "mount_options", b"mount_options", "parameters", b"parameters", "provisioner", b"provisioner", "reclaim_policy", b"reclaim_policy", "resource_info", b"resource_info", "volume_binding_mode", b"volume_binding_mode"]) -> None: ...

global___StorageClass = StorageClass

@typing_extensions.final
class StorageClassList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StorageClass]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___StorageClass] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___StorageClassList = StorageClassList

@typing_extensions.final
class TokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIENCE_FIELD_NUMBER: builtins.int
    EXPIRATION_SECONDS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    audience: builtins.str
    expiration_seconds: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        audience: builtins.str = ...,
        expiration_seconds: builtins.int = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audience", b"audience", "expiration_seconds", b"expiration_seconds", "resource_info", b"resource_info"]) -> None: ...

global___TokenRequest = TokenRequest

@typing_extensions.final
class VolumeAttachment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def spec(self) -> global___VolumeAttachmentSpec: ...
    @property
    def status(self) -> global___VolumeAttachmentStatus: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___VolumeAttachmentSpec | None = ...,
        status: global___VolumeAttachmentStatus | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> None: ...

global___VolumeAttachment = VolumeAttachment

@typing_extensions.final
class VolumeAttachmentList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VolumeAttachment]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___VolumeAttachment] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___VolumeAttachmentList = VolumeAttachmentList

@typing_extensions.final
class VolumeAttachmentSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INLINE_VOLUME_SPEC_FIELD_NUMBER: builtins.int
    PERSISTENT_VOLUME_NAME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def inline_volume_spec(self) -> kubernetes.kubernetes_io.k8s.api.core.v1_pb2.PersistentVolumeSpec: ...
    persistent_volume_name: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        inline_volume_spec: kubernetes.kubernetes_io.k8s.api.core.v1_pb2.PersistentVolumeSpec | None = ...,
        persistent_volume_name: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inline_volume_spec", b"inline_volume_spec", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inline_volume_spec", b"inline_volume_spec", "persistent_volume_name", b"persistent_volume_name", "resource_info", b"resource_info"]) -> None: ...

global___VolumeAttachmentSource = VolumeAttachmentSource

@typing_extensions.final
class VolumeAttachmentSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTACHER_FIELD_NUMBER: builtins.int
    NODE_NAME_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    attacher: builtins.str
    node_name: builtins.str
    @property
    def source(self) -> global___VolumeAttachmentSource: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        attacher: builtins.str = ...,
        node_name: builtins.str = ...,
        source: global___VolumeAttachmentSource | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attacher", b"attacher", "node_name", b"node_name", "resource_info", b"resource_info", "source", b"source"]) -> None: ...

global___VolumeAttachmentSpec = VolumeAttachmentSpec

@typing_extensions.final
class VolumeAttachmentStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttachmentMetadataEntry(google.protobuf.message.Message):
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

    ATTACH_ERROR_FIELD_NUMBER: builtins.int
    ATTACHED_FIELD_NUMBER: builtins.int
    ATTACHMENT_METADATA_FIELD_NUMBER: builtins.int
    DETACH_ERROR_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def attach_error(self) -> global___VolumeError: ...
    attached: builtins.bool
    @property
    def attachment_metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def detach_error(self) -> global___VolumeError: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        attach_error: global___VolumeError | None = ...,
        attached: builtins.bool = ...,
        attachment_metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        detach_error: global___VolumeError | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attach_error", b"attach_error", "detach_error", b"detach_error", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attach_error", b"attach_error", "attached", b"attached", "attachment_metadata", b"attachment_metadata", "detach_error", b"detach_error", "resource_info", b"resource_info"]) -> None: ...

global___VolumeAttachmentStatus = VolumeAttachmentStatus

@typing_extensions.final
class VolumeError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    message: builtins.str
    @property
    def time(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        message: builtins.str = ...,
        time: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "time", b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "resource_info", b"resource_info", "time", b"time"]) -> None: ...

global___VolumeError = VolumeError

@typing_extensions.final
class VolumeNodeResources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNT_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    count: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        count: builtins.int = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "resource_info", b"resource_info"]) -> None: ...

global___VolumeNodeResources = VolumeNodeResources
