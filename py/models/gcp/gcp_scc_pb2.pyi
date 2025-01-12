"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SccNotificationConfigXStreamingConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILTER_FIELD_NUMBER: builtins.int
    filter: builtins.str
    def __init__(
        self,
        *,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> None: ...

global___SccNotificationConfigXStreamingConfig = SccNotificationConfigXStreamingConfig

@typing_extensions.final
class SccNotificationConfigXTimeouts(google.protobuf.message.Message):
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

global___SccNotificationConfigXTimeouts = SccNotificationConfigXTimeouts

@typing_extensions.final
class SccNotificationConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    PUBSUB_TOPIC_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    STREAMING_CONFIG_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    config_id: builtins.str
    description: builtins.str
    id: builtins.str
    name: builtins.str
    organization: builtins.str
    pubsub_topic: builtins.str
    service_account: builtins.str
    @property
    def streaming_config(self) -> global___SccNotificationConfigXStreamingConfig: ...
    @property
    def timeouts(self) -> global___SccNotificationConfigXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        config_id: builtins.str = ...,
        description: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        organization: builtins.str = ...,
        pubsub_topic: builtins.str = ...,
        service_account: builtins.str = ...,
        streaming_config: global___SccNotificationConfigXStreamingConfig | None = ...,
        timeouts: global___SccNotificationConfigXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "streaming_config", b"streaming_config", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config_id", b"config_id", "description", b"description", "id", b"id", "name", b"name", "organization", b"organization", "pubsub_topic", b"pubsub_topic", "resource_info", b"resource_info", "service_account", b"service_account", "streaming_config", b"streaming_config", "timeouts", b"timeouts"]) -> None: ...

global___SccNotificationConfig = SccNotificationConfig

@typing_extensions.final
class SccSourceXTimeouts(google.protobuf.message.Message):
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

global___SccSourceXTimeouts = SccSourceXTimeouts

@typing_extensions.final
class SccSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    description: builtins.str
    display_name: builtins.str
    id: builtins.str
    name: builtins.str
    organization: builtins.str
    @property
    def timeouts(self) -> global___SccSourceXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        display_name: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        organization: builtins.str = ...,
        timeouts: global___SccSourceXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "display_name", b"display_name", "id", b"id", "name", b"name", "organization", b"organization", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___SccSource = SccSource
