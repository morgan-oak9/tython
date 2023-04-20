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
class Connection(google.protobuf.message.Message):
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
    CONNECTION_NAME_FIELD_NUMBER: builtins.int
    PROVIDER_TYPE_FIELD_NUMBER: builtins.int
    HOST_ARN_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    connection_name: builtins.str
    provider_type: builtins.str
    host_arn: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        connection_name: builtins.str = ...,
        provider_type: builtins.str = ...,
        host_arn: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection_name", b"connection_name", "host_arn", b"host_arn", "provider_type", b"provider_type", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___Connection = Connection

@typing_extensions.final
class CodeStarConnections(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_FIELD_NUMBER: builtins.int
    @property
    def connection(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Connection]: ...
    def __init__(
        self,
        *,
        connection: collections.abc.Iterable[global___Connection] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection", b"connection"]) -> None: ...

global___CodeStarConnections = CodeStarConnections
