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
class ActivityTagsEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___ActivityTagsEntry = ActivityTagsEntry

@typing_extensions.final
class Activity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ARN_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    arn: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActivityTagsEntry]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        arn: builtins.str = ...,
        tags: collections.abc.Iterable[global___ActivityTagsEntry] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arn", b"arn", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___Activity = Activity

@typing_extensions.final
class StepFunctions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVITY_FIELD_NUMBER: builtins.int
    STATE_MACHINE_FIELD_NUMBER: builtins.int
    @property
    def activity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Activity]: ...
    @property
    def state_machine(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StateMachine]: ...
    def __init__(
        self,
        *,
        activity: collections.abc.Iterable[global___Activity] | None = ...,
        state_machine: collections.abc.Iterable[global___StateMachine] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity", b"activity", "state_machine", b"state_machine"]) -> None: ...

global___StepFunctions = StepFunctions

@typing_extensions.final
class StateMachineCloudWatchLogsLogGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LOG_GROUP_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    log_group_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        log_group_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["log_group_arn", b"log_group_arn", "resource_info", b"resource_info"]) -> None: ...

global___StateMachineCloudWatchLogsLogGroup = StateMachineCloudWatchLogsLogGroup

@typing_extensions.final
class StateMachineLogDestination(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CLOUD_WATCH_LOGS_LOG_GROUP_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def cloud_watch_logs_log_group(self) -> global___StateMachineCloudWatchLogsLogGroup: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        cloud_watch_logs_log_group: global___StateMachineCloudWatchLogsLogGroup | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cloud_watch_logs_log_group", b"cloud_watch_logs_log_group", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_watch_logs_log_group", b"cloud_watch_logs_log_group", "resource_info", b"resource_info"]) -> None: ...

global___StateMachineLogDestination = StateMachineLogDestination

@typing_extensions.final
class StateMachineLoggingConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    INCLUDE_EXECUTION_DATA_FIELD_NUMBER: builtins.int
    DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    level: builtins.str
    include_execution_data: builtins.bool
    @property
    def destinations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StateMachineLogDestination]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        level: builtins.str = ...,
        include_execution_data: builtins.bool = ...,
        destinations: collections.abc.Iterable[global___StateMachineLogDestination] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["destinations", b"destinations", "include_execution_data", b"include_execution_data", "level", b"level", "resource_info", b"resource_info"]) -> None: ...

global___StateMachineLoggingConfiguration = StateMachineLoggingConfiguration

@typing_extensions.final
class StateMachineTracingConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "resource_info", b"resource_info"]) -> None: ...

global___StateMachineTracingConfiguration = StateMachineTracingConfiguration

@typing_extensions.final
class StateMachineS3Location(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    bucket: builtins.str
    key: builtins.str
    version: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        bucket: builtins.str = ...,
        key: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket", "key", b"key", "resource_info", b"resource_info", "version", b"version"]) -> None: ...

global___StateMachineS3Location = StateMachineS3Location

@typing_extensions.final
class StateMachineDefinitionSubstitutions(google.protobuf.message.Message):
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

global___StateMachineDefinitionSubstitutions = StateMachineDefinitionSubstitutions

@typing_extensions.final
class StateMachineTagsEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___StateMachineTagsEntry = StateMachineTagsEntry

@typing_extensions.final
class StateMachine(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DEFINITION_STRING_FIELD_NUMBER: builtins.int
    ROLE_ARN_FIELD_NUMBER: builtins.int
    STATE_MACHINE_NAME_FIELD_NUMBER: builtins.int
    STATE_MACHINE_TYPE_FIELD_NUMBER: builtins.int
    LOGGING_CONFIGURATION_FIELD_NUMBER: builtins.int
    TRACING_CONFIGURATION_FIELD_NUMBER: builtins.int
    DEFINITION_S3_LOCATION_FIELD_NUMBER: builtins.int
    DEFINITION_SUBSTITUTIONS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    definition_string: builtins.str
    role_arn: builtins.str
    state_machine_name: builtins.str
    state_machine_type: builtins.str
    @property
    def logging_configuration(self) -> global___StateMachineLoggingConfiguration: ...
    @property
    def tracing_configuration(self) -> global___StateMachineTracingConfiguration: ...
    @property
    def definition_s3_location(self) -> global___StateMachineS3Location: ...
    @property
    def definition_substitutions(self) -> global___StateMachineDefinitionSubstitutions: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StateMachineTagsEntry]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        definition_string: builtins.str = ...,
        role_arn: builtins.str = ...,
        state_machine_name: builtins.str = ...,
        state_machine_type: builtins.str = ...,
        logging_configuration: global___StateMachineLoggingConfiguration | None = ...,
        tracing_configuration: global___StateMachineTracingConfiguration | None = ...,
        definition_s3_location: global___StateMachineS3Location | None = ...,
        definition_substitutions: global___StateMachineDefinitionSubstitutions | None = ...,
        tags: collections.abc.Iterable[global___StateMachineTagsEntry] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["definition_s3_location", b"definition_s3_location", "definition_substitutions", b"definition_substitutions", "logging_configuration", b"logging_configuration", "resource_info", b"resource_info", "tracing_configuration", b"tracing_configuration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["definition_s3_location", b"definition_s3_location", "definition_string", b"definition_string", "definition_substitutions", b"definition_substitutions", "logging_configuration", b"logging_configuration", "resource_info", b"resource_info", "role_arn", b"role_arn", "state_machine_name", b"state_machine_name", "state_machine_type", b"state_machine_type", "tags", b"tags", "tracing_configuration", b"tracing_configuration"]) -> None: ...

global___StateMachine = StateMachine