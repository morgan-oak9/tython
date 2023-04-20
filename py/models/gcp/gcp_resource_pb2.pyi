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
class ResourceManagerLienXTimeouts(google.protobuf.message.Message):
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

global___ResourceManagerLienXTimeouts = ResourceManagerLienXTimeouts

@typing_extensions.final
class ResourceManagerLien(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_TIME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    RESTRICTIONS_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    create_time: builtins.str
    id: builtins.str
    name: builtins.str
    origin: builtins.str
    parent: builtins.str
    reason: builtins.str
    @property
    def restrictions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def timeouts(self) -> global___ResourceManagerLienXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        create_time: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        origin: builtins.str = ...,
        parent: builtins.str = ...,
        reason: builtins.str = ...,
        restrictions: collections.abc.Iterable[builtins.str] | None = ...,
        timeouts: global___ResourceManagerLienXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time", b"create_time", "id", b"id", "name", b"name", "origin", b"origin", "parent", b"parent", "reason", b"reason", "resource_info", b"resource_info", "restrictions", b"restrictions", "timeouts", b"timeouts"]) -> None: ...

global___ResourceManagerLien = ResourceManagerLien