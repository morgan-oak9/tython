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
class SourcerepoRepositoryXPubsubConfigs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FORMAT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    message_format: builtins.str
    service_account_email: builtins.str
    topic: builtins.str
    def __init__(
        self,
        *,
        message_format: builtins.str = ...,
        service_account_email: builtins.str = ...,
        topic: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message_format", b"message_format", "service_account_email", b"service_account_email", "topic", b"topic"]) -> None: ...

global___SourcerepoRepositoryXPubsubConfigs = SourcerepoRepositoryXPubsubConfigs

@typing_extensions.final
class SourcerepoRepositoryXTimeouts(google.protobuf.message.Message):
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

global___SourcerepoRepositoryXTimeouts = SourcerepoRepositoryXTimeouts

@typing_extensions.final
class SourcerepoRepository(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    PUBSUB_CONFIGS_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    project: builtins.str
    size: builtins.float
    url: builtins.str
    @property
    def pubsub_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SourcerepoRepositoryXPubsubConfigs]: ...
    @property
    def timeouts(self) -> global___SourcerepoRepositoryXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        size: builtins.float = ...,
        url: builtins.str = ...,
        pubsub_configs: collections.abc.Iterable[global___SourcerepoRepositoryXPubsubConfigs] | None = ...,
        timeouts: global___SourcerepoRepositoryXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "project", b"project", "pubsub_configs", b"pubsub_configs", "resource_info", b"resource_info", "size", b"size", "timeouts", b"timeouts", "url", b"url"]) -> None: ...

global___SourcerepoRepository = SourcerepoRepository

@typing_extensions.final
class SourcerepoRepositoryIamBindingXCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPRESSION_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    description: builtins.str
    expression: builtins.str
    title: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        expression: builtins.str = ...,
        title: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "expression", b"expression", "title", b"title"]) -> None: ...

global___SourcerepoRepositoryIamBindingXCondition = SourcerepoRepositoryIamBindingXCondition

@typing_extensions.final
class SourcerepoRepositoryIamBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    project: builtins.str
    repository: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SourcerepoRepositoryIamBindingXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
        project: builtins.str = ...,
        repository: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SourcerepoRepositoryIamBindingXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "id", b"id", "members", b"members", "project", b"project", "repository", b"repository", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SourcerepoRepositoryIamBinding = SourcerepoRepositoryIamBinding

@typing_extensions.final
class SourcerepoRepositoryIamMemberXCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPRESSION_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    description: builtins.str
    expression: builtins.str
    title: builtins.str
    def __init__(
        self,
        *,
        description: builtins.str = ...,
        expression: builtins.str = ...,
        title: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "expression", b"expression", "title", b"title"]) -> None: ...

global___SourcerepoRepositoryIamMemberXCondition = SourcerepoRepositoryIamMemberXCondition

@typing_extensions.final
class SourcerepoRepositoryIamMember(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    member: builtins.str
    project: builtins.str
    repository: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SourcerepoRepositoryIamMemberXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        member: builtins.str = ...,
        project: builtins.str = ...,
        repository: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SourcerepoRepositoryIamMemberXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "id", b"id", "member", b"member", "project", b"project", "repository", b"repository", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SourcerepoRepositoryIamMember = SourcerepoRepositoryIamMember

@typing_extensions.final
class SourcerepoRepositoryIamPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    POLICY_DATA_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REPOSITORY_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    policy_data: builtins.str
    project: builtins.str
    repository: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        policy_data: builtins.str = ...,
        project: builtins.str = ...,
        repository: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["etag", b"etag", "id", b"id", "policy_data", b"policy_data", "project", b"project", "repository", b"repository", "resource_info", b"resource_info"]) -> None: ...

global___SourcerepoRepositoryIamPolicy = SourcerepoRepositoryIamPolicy
