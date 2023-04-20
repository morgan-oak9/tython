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
class Subscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class DeliveryPolicyEntry(google.protobuf.message.Message):
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
    class FilterPolicyEntry(google.protobuf.message.Message):
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

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DELIVERY_POLICY_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    FILTER_POLICY_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    RAW_MESSAGE_DELIVERY_FIELD_NUMBER: builtins.int
    REDRIVE_POLICY_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    TOPIC_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def delivery_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    endpoint: builtins.str
    @property
    def filter_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    protocol: builtins.str
    raw_message_delivery: builtins.bool
    @property
    def redrive_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    region: builtins.str
    topic_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        delivery_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        endpoint: builtins.str = ...,
        filter_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        protocol: builtins.str = ...,
        raw_message_delivery: builtins.bool = ...,
        redrive_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        region: builtins.str = ...,
        topic_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delivery_policy", b"delivery_policy", "endpoint", b"endpoint", "filter_policy", b"filter_policy", "protocol", b"protocol", "raw_message_delivery", b"raw_message_delivery", "redrive_policy", b"redrive_policy", "region", b"region", "resource_info", b"resource_info", "topic_arn", b"topic_arn"]) -> None: ...

global___Subscription = Subscription

@typing_extensions.final
class SNS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    TOPIC_POLICY_FIELD_NUMBER: builtins.int
    @property
    def subscription(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Subscription]: ...
    @property
    def topic(self) -> global___Topic: ...
    @property
    def topic_policy(self) -> global___TopicPolicy: ...
    def __init__(
        self,
        *,
        subscription: collections.abc.Iterable[global___Subscription] | None = ...,
        topic: global___Topic | None = ...,
        topic_policy: global___TopicPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["topic", b"topic", "topic_policy", b"topic_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["subscription", b"subscription", "topic", b"topic", "topic_policy", b"topic_policy"]) -> None: ...

global___SNS = SNS

@typing_extensions.final
class TopicSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    endpoint: builtins.str
    protocol: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        endpoint: builtins.str = ...,
        protocol: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint", b"endpoint", "protocol", b"protocol", "resource_info", b"resource_info"]) -> None: ...

global___TopicSubscription = TopicSubscription

@typing_extensions.final
class Topic(google.protobuf.message.Message):
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
    CONTENT_BASED_DEDUPLICATION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    KMS_MASTER_KEY_ID_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    TOPIC_NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    content_based_deduplication: builtins.bool
    display_name: builtins.str
    kms_master_key_id: builtins.str
    @property
    def subscription(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TopicSubscription]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    topic_name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        content_based_deduplication: builtins.bool = ...,
        display_name: builtins.str = ...,
        kms_master_key_id: builtins.str = ...,
        subscription: collections.abc.Iterable[global___TopicSubscription] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        topic_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content_based_deduplication", b"content_based_deduplication", "display_name", b"display_name", "kms_master_key_id", b"kms_master_key_id", "resource_info", b"resource_info", "subscription", b"subscription", "tags", b"tags", "topic_name", b"topic_name"]) -> None: ...

global___Topic = Topic

@typing_extensions.final
class TopicPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    POLICY_DOCUMENT_FIELD_NUMBER: builtins.int
    TOPICS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    policy_document: builtins.str
    @property
    def topics(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        policy_document: builtins.str = ...,
        topics: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["policy_document", b"policy_document", "resource_info", b"resource_info", "topics", b"topics"]) -> None: ...

global___TopicPolicy = TopicPolicy
