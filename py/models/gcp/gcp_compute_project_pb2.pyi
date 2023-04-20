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
class ComputeProjectDefaultNetworkTierXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    create: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create"]) -> None: ...

global___ComputeProjectDefaultNetworkTierXTimeouts = ComputeProjectDefaultNetworkTierXTimeouts

@typing_extensions.final
class ComputeProjectDefaultNetworkTier(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NETWORK_TIER_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    network_tier: builtins.str
    project: builtins.str
    @property
    def timeouts(self) -> global___ComputeProjectDefaultNetworkTierXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        network_tier: builtins.str = ...,
        project: builtins.str = ...,
        timeouts: global___ComputeProjectDefaultNetworkTierXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "network_tier", b"network_tier", "project", b"project", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___ComputeProjectDefaultNetworkTier = ComputeProjectDefaultNetworkTier

@typing_extensions.final
class ComputeProjectMetadataXTimeouts(google.protobuf.message.Message):
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

global___ComputeProjectMetadataXTimeouts = ComputeProjectMetadataXTimeouts

@typing_extensions.final
class ComputeProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MetadataEntry(google.protobuf.message.Message):
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
    METADATA_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    project: builtins.str
    @property
    def timeouts(self) -> global___ComputeProjectMetadataXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        project: builtins.str = ...,
        timeouts: global___ComputeProjectMetadataXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "metadata", b"metadata", "project", b"project", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___ComputeProjectMetadata = ComputeProjectMetadata

@typing_extensions.final
class ComputeProjectMetadataItemXTimeouts(google.protobuf.message.Message):
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

global___ComputeProjectMetadataItemXTimeouts = ComputeProjectMetadataItemXTimeouts

@typing_extensions.final
class ComputeProjectMetadataItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    key: builtins.str
    project: builtins.str
    value: builtins.str
    @property
    def timeouts(self) -> global___ComputeProjectMetadataItemXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        key: builtins.str = ...,
        project: builtins.str = ...,
        value: builtins.str = ...,
        timeouts: global___ComputeProjectMetadataItemXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "key", b"key", "project", b"project", "resource_info", b"resource_info", "timeouts", b"timeouts", "value", b"value"]) -> None: ...

global___ComputeProjectMetadataItem = ComputeProjectMetadataItem