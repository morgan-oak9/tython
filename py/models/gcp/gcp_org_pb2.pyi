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
class OrgPolicyPolicyXSpecXRulesXCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPRESSION_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    description: builtins.str
    expression: builtins.str
    location: builtins.str
    title: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        expression: builtins.str = ...,
        location: builtins.str = ...,
        title: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "expression", b"expression", "location", b"location", "title", b"title"]) -> None: ...

global___OrgPolicyPolicyXSpecXRulesXCondition = OrgPolicyPolicyXSpecXRulesXCondition

@typing_extensions.final
class OrgPolicyPolicyXSpecXRulesXValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOWED_VALUES_FIELD_NUMBER: builtins.int
    DENIED_VALUES_FIELD_NUMBER: builtins.int
    @property
    def allowed_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def denied_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        allowed_values: collections.abc.Iterable[builtins.str] | None = ...,
        denied_values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_values", b"allowed_values", "denied_values", b"denied_values"]) -> None: ...

global___OrgPolicyPolicyXSpecXRulesXValues = OrgPolicyPolicyXSpecXRulesXValues

@typing_extensions.final
class OrgPolicyPolicyXSpecXRules(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOW_ALL_FIELD_NUMBER: builtins.int
    DENY_ALL_FIELD_NUMBER: builtins.int
    ENFORCE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    allow_all: builtins.str
    deny_all: builtins.str
    enforce: builtins.str
    @property
    def condition(self) -> global___OrgPolicyPolicyXSpecXRulesXCondition: ...
    @property
    def values(self) -> global___OrgPolicyPolicyXSpecXRulesXValues: ...
    def __init__(
        self,
        *,
        allow_all: builtins.str = ...,
        deny_all: builtins.str = ...,
        enforce: builtins.str = ...,
        condition: global___OrgPolicyPolicyXSpecXRulesXCondition | None = ...,
        values: global___OrgPolicyPolicyXSpecXRulesXValues | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "values", b"values"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_all", b"allow_all", "condition", b"condition", "deny_all", b"deny_all", "enforce", b"enforce", "values", b"values"]) -> None: ...

global___OrgPolicyPolicyXSpecXRules = OrgPolicyPolicyXSpecXRules

@typing_extensions.final
class OrgPolicyPolicyXSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    INHERIT_FROM_PARENT_FIELD_NUMBER: builtins.int
    RESET_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    etag: builtins.str
    inherit_from_parent: builtins.bool
    reset: builtins.bool
    update_time: builtins.str
    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrgPolicyPolicyXSpecXRules]: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        inherit_from_parent: builtins.bool = ...,
        reset: builtins.bool = ...,
        update_time: builtins.str = ...,
        rules: collections.abc.Iterable[global___OrgPolicyPolicyXSpecXRules] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["etag", b"etag", "inherit_from_parent", b"inherit_from_parent", "reset", b"reset", "rules", b"rules", "update_time", b"update_time"]) -> None: ...

global___OrgPolicyPolicyXSpec = OrgPolicyPolicyXSpec

@typing_extensions.final
class OrgPolicyPolicyXTimeouts(google.protobuf.message.Message):
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

global___OrgPolicyPolicyXTimeouts = OrgPolicyPolicyXTimeouts

@typing_extensions.final
class OrgPolicyPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    parent: builtins.str
    @property
    def spec(self) -> global___OrgPolicyPolicyXSpec: ...
    @property
    def timeouts(self) -> global___OrgPolicyPolicyXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        parent: builtins.str = ...,
        spec: global___OrgPolicyPolicyXSpec | None = ...,
        timeouts: global___OrgPolicyPolicyXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "spec", b"spec", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "parent", b"parent", "resource_info", b"resource_info", "spec", b"spec", "timeouts", b"timeouts"]) -> None: ...

global___OrgPolicyPolicy = OrgPolicyPolicy