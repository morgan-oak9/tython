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
class SpannerDatabaseXEncryptionConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KMS_KEY_NAME_FIELD_NUMBER: builtins.int
    kms_key_name: builtins.str
    def __init__(
        self,
        *,
        kms_key_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["kms_key_name", b"kms_key_name"]) -> None: ...

global___SpannerDatabaseXEncryptionConfig = SpannerDatabaseXEncryptionConfig

@typing_extensions.final
class SpannerDatabaseXTimeouts(google.protobuf.message.Message):
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

global___SpannerDatabaseXTimeouts = SpannerDatabaseXTimeouts

@typing_extensions.final
class SpannerDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_DIALECT_FIELD_NUMBER: builtins.int
    DDL_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    VERSION_RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    ENCRYPTION_CONFIG_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    database_dialect: builtins.str
    @property
    def ddl(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    deletion_protection: builtins.bool
    id: builtins.str
    instance: builtins.str
    name: builtins.str
    project: builtins.str
    state: builtins.str
    version_retention_period: builtins.str
    @property
    def encryption_config(self) -> global___SpannerDatabaseXEncryptionConfig: ...
    @property
    def timeouts(self) -> global___SpannerDatabaseXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        database_dialect: builtins.str = ...,
        ddl: collections.abc.Iterable[builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        state: builtins.str = ...,
        version_retention_period: builtins.str = ...,
        encryption_config: global___SpannerDatabaseXEncryptionConfig | None = ...,
        timeouts: global___SpannerDatabaseXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["encryption_config", b"encryption_config", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["database_dialect", b"database_dialect", "ddl", b"ddl", "deletion_protection", b"deletion_protection", "encryption_config", b"encryption_config", "id", b"id", "instance", b"instance", "name", b"name", "project", b"project", "resource_info", b"resource_info", "state", b"state", "timeouts", b"timeouts", "version_retention_period", b"version_retention_period"]) -> None: ...

global___SpannerDatabase = SpannerDatabase

@typing_extensions.final
class SpannerDatabaseIamBindingXCondition(google.protobuf.message.Message):
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

global___SpannerDatabaseIamBindingXCondition = SpannerDatabaseIamBindingXCondition

@typing_extensions.final
class SpannerDatabaseIamBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    database: builtins.str
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    project: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SpannerDatabaseIamBindingXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        database: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
        project: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SpannerDatabaseIamBindingXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "database", b"database", "etag", b"etag", "id", b"id", "instance", b"instance", "members", b"members", "project", b"project", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SpannerDatabaseIamBinding = SpannerDatabaseIamBinding

@typing_extensions.final
class SpannerDatabaseIamMemberXCondition(google.protobuf.message.Message):
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

global___SpannerDatabaseIamMemberXCondition = SpannerDatabaseIamMemberXCondition

@typing_extensions.final
class SpannerDatabaseIamMember(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    database: builtins.str
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    member: builtins.str
    project: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SpannerDatabaseIamMemberXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        database: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        member: builtins.str = ...,
        project: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SpannerDatabaseIamMemberXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "database", b"database", "etag", b"etag", "id", b"id", "instance", b"instance", "member", b"member", "project", b"project", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SpannerDatabaseIamMember = SpannerDatabaseIamMember

@typing_extensions.final
class SpannerDatabaseIamPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    POLICY_DATA_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    database: builtins.str
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    policy_data: builtins.str
    project: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        database: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        policy_data: builtins.str = ...,
        project: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "etag", b"etag", "id", b"id", "instance", b"instance", "policy_data", b"policy_data", "project", b"project", "resource_info", b"resource_info"]) -> None: ...

global___SpannerDatabaseIamPolicy = SpannerDatabaseIamPolicy

@typing_extensions.final
class SpannerInstanceXTimeouts(google.protobuf.message.Message):
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

global___SpannerInstanceXTimeouts = SpannerInstanceXTimeouts

@typing_extensions.final
class SpannerInstance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
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

    CONFIG_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    FORCE_DESTROY_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NUM_NODES_FIELD_NUMBER: builtins.int
    PROCESSING_UNITS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    config: builtins.str
    display_name: builtins.str
    force_destroy: builtins.bool
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    num_nodes: builtins.float
    processing_units: builtins.float
    project: builtins.str
    state: builtins.str
    @property
    def timeouts(self) -> global___SpannerInstanceXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        config: builtins.str = ...,
        display_name: builtins.str = ...,
        force_destroy: builtins.bool = ...,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
        num_nodes: builtins.float = ...,
        processing_units: builtins.float = ...,
        project: builtins.str = ...,
        state: builtins.str = ...,
        timeouts: global___SpannerInstanceXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "display_name", b"display_name", "force_destroy", b"force_destroy", "id", b"id", "labels", b"labels", "name", b"name", "num_nodes", b"num_nodes", "processing_units", b"processing_units", "project", b"project", "resource_info", b"resource_info", "state", b"state", "timeouts", b"timeouts"]) -> None: ...

global___SpannerInstance = SpannerInstance

@typing_extensions.final
class SpannerInstanceIamBindingXCondition(google.protobuf.message.Message):
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

global___SpannerInstanceIamBindingXCondition = SpannerInstanceIamBindingXCondition

@typing_extensions.final
class SpannerInstanceIamBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    project: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SpannerInstanceIamBindingXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
        project: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SpannerInstanceIamBindingXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "id", b"id", "instance", b"instance", "members", b"members", "project", b"project", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SpannerInstanceIamBinding = SpannerInstanceIamBinding

@typing_extensions.final
class SpannerInstanceIamMemberXCondition(google.protobuf.message.Message):
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

global___SpannerInstanceIamMemberXCondition = SpannerInstanceIamMemberXCondition

@typing_extensions.final
class SpannerInstanceIamMember(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    member: builtins.str
    project: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___SpannerInstanceIamMemberXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        member: builtins.str = ...,
        project: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___SpannerInstanceIamMemberXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "id", b"id", "instance", b"instance", "member", b"member", "project", b"project", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___SpannerInstanceIamMember = SpannerInstanceIamMember

@typing_extensions.final
class SpannerInstanceIamPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    POLICY_DATA_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    id: builtins.str
    instance: builtins.str
    policy_data: builtins.str
    project: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        instance: builtins.str = ...,
        policy_data: builtins.str = ...,
        project: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["etag", b"etag", "id", b"id", "instance", b"instance", "policy_data", b"policy_data", "project", b"project", "resource_info", b"resource_info"]) -> None: ...

global___SpannerInstanceIamPolicy = SpannerInstanceIamPolicy
