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
class Queue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class RedrivePolicyEntry(google.protobuf.message.Message):
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
    CONTENT_BASED_DEDUPLICATION_FIELD_NUMBER: builtins.int
    DELAY_SECONDS_FIELD_NUMBER: builtins.int
    FIFO_QUEUE_FIELD_NUMBER: builtins.int
    KMS_DATA_KEY_REUSE_PERIOD_SECONDS_FIELD_NUMBER: builtins.int
    KMS_MASTER_KEY_ID_FIELD_NUMBER: builtins.int
    MAXIMUM_MESSAGE_SIZE_FIELD_NUMBER: builtins.int
    MESSAGE_RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    QUEUE_NAME_FIELD_NUMBER: builtins.int
    RECEIVE_MESSAGE_WAIT_TIME_SECONDS_FIELD_NUMBER: builtins.int
    REDRIVE_POLICY_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    VISIBILITY_TIMEOUT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    content_based_deduplication: builtins.bool
    delay_seconds: builtins.int
    fifo_queue: builtins.bool
    kms_data_key_reuse_period_seconds: builtins.int
    kms_master_key_id: builtins.str
    maximum_message_size: builtins.int
    message_retention_period: builtins.int
    queue_name: builtins.str
    receive_message_wait_time_seconds: builtins.int
    @property
    def redrive_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    visibility_timeout: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        content_based_deduplication: builtins.bool = ...,
        delay_seconds: builtins.int = ...,
        fifo_queue: builtins.bool = ...,
        kms_data_key_reuse_period_seconds: builtins.int = ...,
        kms_master_key_id: builtins.str = ...,
        maximum_message_size: builtins.int = ...,
        message_retention_period: builtins.int = ...,
        queue_name: builtins.str = ...,
        receive_message_wait_time_seconds: builtins.int = ...,
        redrive_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        visibility_timeout: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content_based_deduplication", b"content_based_deduplication", "delay_seconds", b"delay_seconds", "fifo_queue", b"fifo_queue", "kms_data_key_reuse_period_seconds", b"kms_data_key_reuse_period_seconds", "kms_master_key_id", b"kms_master_key_id", "maximum_message_size", b"maximum_message_size", "message_retention_period", b"message_retention_period", "queue_name", b"queue_name", "receive_message_wait_time_seconds", b"receive_message_wait_time_seconds", "redrive_policy", b"redrive_policy", "resource_info", b"resource_info", "tags", b"tags", "visibility_timeout", b"visibility_timeout"]) -> None: ...

global___Queue = Queue

@typing_extensions.final
class SQS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUEUE_FIELD_NUMBER: builtins.int
    QUEUE_POLICY_FIELD_NUMBER: builtins.int
    @property
    def queue(self) -> global___Queue: ...
    @property
    def queue_policy(self) -> global___QueuePolicy: ...
    def __init__(
        self,
        *,
        queue: global___Queue | None = ...,
        queue_policy: global___QueuePolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["queue", b"queue", "queue_policy", b"queue_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["queue", b"queue", "queue_policy", b"queue_policy"]) -> None: ...

global___SQS = SQS

@typing_extensions.final
class QueuePolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    QUEUES_FIELD_NUMBER: builtins.int
    POLICY_DOCUMENT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def queues(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    policy_document: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        queues: collections.abc.Iterable[builtins.str] | None = ...,
        policy_document: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["policy_document", b"policy_document", "queues", b"queues", "resource_info", b"resource_info"]) -> None: ...

global___QueuePolicy = QueuePolicy
