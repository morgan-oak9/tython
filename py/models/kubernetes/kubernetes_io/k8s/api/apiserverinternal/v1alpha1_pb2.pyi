"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ServerStorageVersion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_SERVER_ID_FIELD_NUMBER: builtins.int
    DECODABLE_VERSIONS_FIELD_NUMBER: builtins.int
    ENCODING_VERSION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_server_id: builtins.str
    @property
    def decodable_versions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    encoding_version: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_server_id: builtins.str = ...,
        decodable_versions: collections.abc.Iterable[builtins.str] | None = ...,
        encoding_version: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_server_id", b"api_server_id", "decodable_versions", b"decodable_versions", "encoding_version", b"encoding_version", "resource_info", b"resource_info"]) -> None: ...

global___ServerStorageVersion = ServerStorageVersion

@typing_extensions.final
class StorageVersion(google.protobuf.message.Message):
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
    def spec(self) -> global___StorageVersionSpec: ...
    @property
    def status(self) -> global___StorageVersionStatus: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___StorageVersionSpec | None = ...,
        status: global___StorageVersionStatus | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> None: ...

global___StorageVersion = StorageVersion

@typing_extensions.final
class StorageVersionCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_TRANSITION_TIME_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    OBSERVED_GENERATION_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def last_transition_time(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time: ...
    message: builtins.str
    observed_generation: builtins.int
    reason: builtins.str
    status: builtins.str
    type: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        last_transition_time: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time | None = ...,
        message: builtins.str = ...,
        observed_generation: builtins.int = ...,
        reason: builtins.str = ...,
        status: builtins.str = ...,
        type: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_transition_time", b"last_transition_time", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_transition_time", b"last_transition_time", "message", b"message", "observed_generation", b"observed_generation", "reason", b"reason", "resource_info", b"resource_info", "status", b"status", "type", b"type"]) -> None: ...

global___StorageVersionCondition = StorageVersionCondition

@typing_extensions.final
class StorageVersionList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StorageVersion]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___StorageVersion] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___StorageVersionList = StorageVersionList

@typing_extensions.final
class StorageVersionSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> None: ...

global___StorageVersionSpec = StorageVersionSpec

@typing_extensions.final
class StorageVersionStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_ENCODING_VERSION_FIELD_NUMBER: builtins.int
    CONDITIONS_FIELD_NUMBER: builtins.int
    STORAGE_VERSIONS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    common_encoding_version: builtins.str
    @property
    def conditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StorageVersionCondition]: ...
    @property
    def storage_versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerStorageVersion]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        common_encoding_version: builtins.str = ...,
        conditions: collections.abc.Iterable[global___StorageVersionCondition] | None = ...,
        storage_versions: collections.abc.Iterable[global___ServerStorageVersion] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["common_encoding_version", b"common_encoding_version", "conditions", b"conditions", "resource_info", b"resource_info", "storage_versions", b"storage_versions"]) -> None: ...

global___StorageVersionStatus = StorageVersionStatus
