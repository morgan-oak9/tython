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
class StreamStreamEncryption(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENCRYPTION_TYPE_FIELD_NUMBER: builtins.int
    KEY_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    encryption_type: builtins.str
    key_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        encryption_type: builtins.str = ...,
        key_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["encryption_type", b"encryption_type", "key_id", b"key_id", "resource_info", b"resource_info"]) -> None: ...

global___StreamStreamEncryption = StreamStreamEncryption

@typing_extensions.final
class Stream(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_HOURS_FIELD_NUMBER: builtins.int
    SHARD_COUNT_FIELD_NUMBER: builtins.int
    STREAM_ENCRYPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    retention_period_hours: builtins.int
    shard_count: builtins.int
    @property
    def stream_encryption(self) -> global___StreamStreamEncryption: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        retention_period_hours: builtins.int = ...,
        shard_count: builtins.int = ...,
        stream_encryption: global___StreamStreamEncryption | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "stream_encryption", b"stream_encryption"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info", "retention_period_hours", b"retention_period_hours", "shard_count", b"shard_count", "stream_encryption", b"stream_encryption", "tags", b"tags"]) -> None: ...

global___Stream = Stream

@typing_extensions.final
class Kinesis(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_FIELD_NUMBER: builtins.int
    @property
    def stream(self) -> global___Stream: ...
    def __init__(
        self,
        *,
        stream: global___Stream | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["stream", b"stream"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["stream", b"stream"]) -> None: ...

global___Kinesis = Kinesis

@typing_extensions.final
class StreamConsumer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CONSUMER_NAME_FIELD_NUMBER: builtins.int
    STREAM_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    consumer_name: builtins.str
    stream_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        consumer_name: builtins.str = ...,
        stream_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consumer_name", b"consumer_name", "resource_info", b"resource_info", "stream_arn", b"stream_arn"]) -> None: ...

global___StreamConsumer = StreamConsumer
