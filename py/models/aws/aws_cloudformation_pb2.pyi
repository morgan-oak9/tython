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
class CustomResource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SERVICE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    service_token: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        service_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "service_token", b"service_token"]) -> None: ...

global___CustomResource = CustomResource

@typing_extensions.final
class CloudFormation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUSTOM_RESOURCE_FIELD_NUMBER: builtins.int
    MACRO_FIELD_NUMBER: builtins.int
    STACK_FIELD_NUMBER: builtins.int
    STACK_SET_FIELD_NUMBER: builtins.int
    WAIT_CONDITION_FIELD_NUMBER: builtins.int
    WAIT_CONDITION_HANDLE_FIELD_NUMBER: builtins.int
    @property
    def custom_resource(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CustomResource]: ...
    @property
    def macro(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Macro]: ...
    @property
    def stack(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Stack]: ...
    @property
    def stack_set(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StackSet]: ...
    @property
    def wait_condition(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WaitCondition]: ...
    @property
    def wait_condition_handle(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WaitConditionHandle]: ...
    def __init__(
        self,
        *,
        custom_resource: collections.abc.Iterable[global___CustomResource] | None = ...,
        macro: collections.abc.Iterable[global___Macro] | None = ...,
        stack: collections.abc.Iterable[global___Stack] | None = ...,
        stack_set: collections.abc.Iterable[global___StackSet] | None = ...,
        wait_condition: collections.abc.Iterable[global___WaitCondition] | None = ...,
        wait_condition_handle: collections.abc.Iterable[global___WaitConditionHandle] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["custom_resource", b"custom_resource", "macro", b"macro", "stack", b"stack", "stack_set", b"stack_set", "wait_condition", b"wait_condition", "wait_condition_handle", b"wait_condition_handle"]) -> None: ...

global___CloudFormation = CloudFormation

@typing_extensions.final
class Macro(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    LOG_GROUP_NAME_FIELD_NUMBER: builtins.int
    LOG_ROLE_ARN_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    description: builtins.str
    function_name: builtins.str
    log_group_name: builtins.str
    log_role_arn: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        description: builtins.str = ...,
        function_name: builtins.str = ...,
        log_group_name: builtins.str = ...,
        log_role_arn: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "function_name", b"function_name", "log_group_name", b"log_group_name", "log_role_arn", b"log_role_arn", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___Macro = Macro

@typing_extensions.final
class Stack(google.protobuf.message.Message):
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
    NOTIFICATION_ARNS_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    TEMPLATE_U_R_L_FIELD_NUMBER: builtins.int
    TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def notification_arns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def parameters(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    template_u_r_l: builtins.str
    timeout_in_minutes: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        notification_arns: collections.abc.Iterable[builtins.str] | None = ...,
        parameters: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        template_u_r_l: builtins.str = ...,
        timeout_in_minutes: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["notification_arns", b"notification_arns", "parameters", b"parameters", "resource_info", b"resource_info", "tags", b"tags", "template_u_r_l", b"template_u_r_l", "timeout_in_minutes", b"timeout_in_minutes"]) -> None: ...

global___Stack = Stack

@typing_extensions.final
class StackSetAutoDeployment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    RETAIN_STACKS_ON_ACCOUNT_REMOVAL_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enabled: builtins.bool
    retain_stacks_on_account_removal: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enabled: builtins.bool = ...,
        retain_stacks_on_account_removal: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled", b"enabled", "resource_info", b"resource_info", "retain_stacks_on_account_removal", b"retain_stacks_on_account_removal"]) -> None: ...

global___StackSetAutoDeployment = StackSetAutoDeployment

@typing_extensions.final
class StackSetOperationPreferences(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FAILURE_TOLERANCE_COUNT_FIELD_NUMBER: builtins.int
    FAILURE_TOLERANCE_PERCENTAGE_FIELD_NUMBER: builtins.int
    MAX_CONCURRENT_COUNT_FIELD_NUMBER: builtins.int
    MAX_CONCURRENT_PERCENTAGE_FIELD_NUMBER: builtins.int
    REGION_ORDER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    failure_tolerance_count: builtins.int
    failure_tolerance_percentage: builtins.int
    max_concurrent_count: builtins.int
    max_concurrent_percentage: builtins.int
    @property
    def region_order(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        failure_tolerance_count: builtins.int = ...,
        failure_tolerance_percentage: builtins.int = ...,
        max_concurrent_count: builtins.int = ...,
        max_concurrent_percentage: builtins.int = ...,
        region_order: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure_tolerance_count", b"failure_tolerance_count", "failure_tolerance_percentage", b"failure_tolerance_percentage", "max_concurrent_count", b"max_concurrent_count", "max_concurrent_percentage", b"max_concurrent_percentage", "region_order", b"region_order", "resource_info", b"resource_info"]) -> None: ...

global___StackSetOperationPreferences = StackSetOperationPreferences

@typing_extensions.final
class StackSetDeploymentTargets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ACCOUNTS_FIELD_NUMBER: builtins.int
    ORGANIZATIONAL_UNIT_IDS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def organizational_unit_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        accounts: collections.abc.Iterable[builtins.str] | None = ...,
        organizational_unit_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts", "organizational_unit_ids", b"organizational_unit_ids", "resource_info", b"resource_info"]) -> None: ...

global___StackSetDeploymentTargets = StackSetDeploymentTargets

@typing_extensions.final
class StackSetParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    PARAMETER_KEY_FIELD_NUMBER: builtins.int
    PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    parameter_key: builtins.str
    parameter_value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        parameter_key: builtins.str = ...,
        parameter_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parameter_key", b"parameter_key", "parameter_value", b"parameter_value", "resource_info", b"resource_info"]) -> None: ...

global___StackSetParameter = StackSetParameter

@typing_extensions.final
class StackSetStackInstances(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DEPLOYMENT_TARGETS_FIELD_NUMBER: builtins.int
    REGIONS_FIELD_NUMBER: builtins.int
    PARAMETER_OVERRIDES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def deployment_targets(self) -> global___StackSetDeploymentTargets: ...
    @property
    def regions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def parameter_overrides(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StackSetParameter]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        deployment_targets: global___StackSetDeploymentTargets | None = ...,
        regions: collections.abc.Iterable[builtins.str] | None = ...,
        parameter_overrides: collections.abc.Iterable[global___StackSetParameter] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deployment_targets", b"deployment_targets", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployment_targets", b"deployment_targets", "parameter_overrides", b"parameter_overrides", "regions", b"regions", "resource_info", b"resource_info"]) -> None: ...

global___StackSetStackInstances = StackSetStackInstances

@typing_extensions.final
class StackSet(google.protobuf.message.Message):
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
    STACK_SET_NAME_FIELD_NUMBER: builtins.int
    ADMINISTRATION_ROLE_ARN_FIELD_NUMBER: builtins.int
    AUTO_DEPLOYMENT_FIELD_NUMBER: builtins.int
    CAPABILITIES_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXECUTION_ROLE_NAME_FIELD_NUMBER: builtins.int
    OPERATION_PREFERENCES_FIELD_NUMBER: builtins.int
    STACK_INSTANCES_GROUP_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    PERMISSION_MODEL_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    TEMPLATE_BODY_FIELD_NUMBER: builtins.int
    TEMPLATE_U_R_L_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    stack_set_name: builtins.str
    administration_role_arn: builtins.str
    @property
    def auto_deployment(self) -> global___StackSetAutoDeployment: ...
    @property
    def capabilities(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    description: builtins.str
    execution_role_name: builtins.str
    @property
    def operation_preferences(self) -> global___StackSetOperationPreferences: ...
    @property
    def stack_instances_group(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StackSetStackInstances]: ...
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StackSetParameter]: ...
    permission_model: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    template_body: builtins.str
    template_u_r_l: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        stack_set_name: builtins.str = ...,
        administration_role_arn: builtins.str = ...,
        auto_deployment: global___StackSetAutoDeployment | None = ...,
        capabilities: collections.abc.Iterable[builtins.str] | None = ...,
        description: builtins.str = ...,
        execution_role_name: builtins.str = ...,
        operation_preferences: global___StackSetOperationPreferences | None = ...,
        stack_instances_group: collections.abc.Iterable[global___StackSetStackInstances] | None = ...,
        parameters: collections.abc.Iterable[global___StackSetParameter] | None = ...,
        permission_model: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        template_body: builtins.str = ...,
        template_u_r_l: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["auto_deployment", b"auto_deployment", "operation_preferences", b"operation_preferences", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["administration_role_arn", b"administration_role_arn", "auto_deployment", b"auto_deployment", "capabilities", b"capabilities", "description", b"description", "execution_role_name", b"execution_role_name", "operation_preferences", b"operation_preferences", "parameters", b"parameters", "permission_model", b"permission_model", "resource_info", b"resource_info", "stack_instances_group", b"stack_instances_group", "stack_set_name", b"stack_set_name", "tags", b"tags", "template_body", b"template_body", "template_u_r_l", b"template_u_r_l"]) -> None: ...

global___StackSet = StackSet

@typing_extensions.final
class WaitCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    HANDLE_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    count: builtins.int
    handle: builtins.str
    timeout: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        count: builtins.int = ...,
        handle: builtins.str = ...,
        timeout: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "handle", b"handle", "resource_info", b"resource_info", "timeout", b"timeout"]) -> None: ...

global___WaitCondition = WaitCondition

@typing_extensions.final
class WaitConditionHandle(google.protobuf.message.Message):
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

global___WaitConditionHandle = WaitConditionHandle