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
class FolderXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    create: builtins.str
    delete: builtins.str
    read: builtins.str
    update: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
        delete: builtins.str = ...,
        read: builtins.str = ...,
        update: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create", "delete", b"delete", "read", b"read", "update", b"update"]) -> None: ...

global___FolderXTimeouts = FolderXTimeouts

@typing_extensions.final
class Folder(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_TIME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LIFECYCLE_STATE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    create_time: builtins.str
    display_name: builtins.str
    folder_id: builtins.str
    id: builtins.str
    lifecycle_state: builtins.str
    name: builtins.str
    parent: builtins.str
    @property
    def timeouts(self) -> global___FolderXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        create_time: builtins.str = ...,
        display_name: builtins.str = ...,
        folder_id: builtins.str = ...,
        id: builtins.str = ...,
        lifecycle_state: builtins.str = ...,
        name: builtins.str = ...,
        parent: builtins.str = ...,
        timeouts: global___FolderXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time", b"create_time", "display_name", b"display_name", "folder_id", b"folder_id", "id", b"id", "lifecycle_state", b"lifecycle_state", "name", b"name", "parent", b"parent", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___Folder = Folder

@typing_extensions.final
class FolderAccessApprovalSettingsXEnrolledServices(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_PRODUCT_FIELD_NUMBER: builtins.int
    ENROLLMENT_LEVEL_FIELD_NUMBER: builtins.int
    cloud_product: builtins.str
    enrollment_level: builtins.str
    def __init__(
        self,
        *,
        cloud_product: builtins.str = ...,
        enrollment_level: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_product", b"cloud_product", "enrollment_level", b"enrollment_level"]) -> None: ...

global___FolderAccessApprovalSettingsXEnrolledServices = FolderAccessApprovalSettingsXEnrolledServices

@typing_extensions.final
class FolderAccessApprovalSettingsXTimeouts(google.protobuf.message.Message):
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

global___FolderAccessApprovalSettingsXTimeouts = FolderAccessApprovalSettingsXTimeouts

@typing_extensions.final
class FolderAccessApprovalSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVE_KEY_VERSION_FIELD_NUMBER: builtins.int
    ANCESTOR_HAS_ACTIVE_KEY_VERSION_FIELD_NUMBER: builtins.int
    ENROLLED_ANCESTOR_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INVALID_KEY_VERSION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NOTIFICATION_EMAILS_FIELD_NUMBER: builtins.int
    ENROLLED_SERVICES_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    active_key_version: builtins.str
    ancestor_has_active_key_version: builtins.bool
    enrolled_ancestor: builtins.bool
    folder_id: builtins.str
    id: builtins.str
    invalid_key_version: builtins.bool
    name: builtins.str
    @property
    def notification_emails(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def enrolled_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FolderAccessApprovalSettingsXEnrolledServices]: ...
    @property
    def timeouts(self) -> global___FolderAccessApprovalSettingsXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        active_key_version: builtins.str = ...,
        ancestor_has_active_key_version: builtins.bool = ...,
        enrolled_ancestor: builtins.bool = ...,
        folder_id: builtins.str = ...,
        id: builtins.str = ...,
        invalid_key_version: builtins.bool = ...,
        name: builtins.str = ...,
        notification_emails: collections.abc.Iterable[builtins.str] | None = ...,
        enrolled_services: collections.abc.Iterable[global___FolderAccessApprovalSettingsXEnrolledServices] | None = ...,
        timeouts: global___FolderAccessApprovalSettingsXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_key_version", b"active_key_version", "ancestor_has_active_key_version", b"ancestor_has_active_key_version", "enrolled_ancestor", b"enrolled_ancestor", "enrolled_services", b"enrolled_services", "folder_id", b"folder_id", "id", b"id", "invalid_key_version", b"invalid_key_version", "name", b"name", "notification_emails", b"notification_emails", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___FolderAccessApprovalSettings = FolderAccessApprovalSettings

@typing_extensions.final
class FolderIamAuditConfigXAuditLogConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXEMPTED_MEMBERS_FIELD_NUMBER: builtins.int
    LOG_TYPE_FIELD_NUMBER: builtins.int
    @property
    def exempted_members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    log_type: builtins.str
    def __init__(
        self,
        *,
        exempted_members: collections.abc.Iterable[builtins.str] | None = ...,
        log_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exempted_members", b"exempted_members", "log_type", b"log_type"]) -> None: ...

global___FolderIamAuditConfigXAuditLogConfig = FolderIamAuditConfigXAuditLogConfig

@typing_extensions.final
class FolderIamAuditConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    AUDIT_LOG_CONFIG_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    folder: builtins.str
    id: builtins.str
    service: builtins.str
    @property
    def audit_log_config(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FolderIamAuditConfigXAuditLogConfig]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        folder: builtins.str = ...,
        id: builtins.str = ...,
        service: builtins.str = ...,
        audit_log_config: collections.abc.Iterable[global___FolderIamAuditConfigXAuditLogConfig] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audit_log_config", b"audit_log_config", "etag", b"etag", "folder", b"folder", "id", b"id", "resource_info", b"resource_info", "service", b"service"]) -> None: ...

global___FolderIamAuditConfig = FolderIamAuditConfig

@typing_extensions.final
class FolderIamBindingXCondition(google.protobuf.message.Message):
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

global___FolderIamBindingXCondition = FolderIamBindingXCondition

@typing_extensions.final
class FolderIamBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    folder: builtins.str
    id: builtins.str
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    role: builtins.str
    @property
    def condition(self) -> global___FolderIamBindingXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        folder: builtins.str = ...,
        id: builtins.str = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
        role: builtins.str = ...,
        condition: global___FolderIamBindingXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "folder", b"folder", "id", b"id", "members", b"members", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___FolderIamBinding = FolderIamBinding

@typing_extensions.final
class FolderIamMemberXCondition(google.protobuf.message.Message):
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

global___FolderIamMemberXCondition = FolderIamMemberXCondition

@typing_extensions.final
class FolderIamMember(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    folder: builtins.str
    id: builtins.str
    member: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___FolderIamMemberXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        folder: builtins.str = ...,
        id: builtins.str = ...,
        member: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___FolderIamMemberXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition", b"condition", "etag", b"etag", "folder", b"folder", "id", b"id", "member", b"member", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___FolderIamMember = FolderIamMember

@typing_extensions.final
class FolderIamPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    POLICY_DATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    etag: builtins.str
    folder: builtins.str
    id: builtins.str
    policy_data: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        folder: builtins.str = ...,
        id: builtins.str = ...,
        policy_data: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["etag", b"etag", "folder", b"folder", "id", b"id", "policy_data", b"policy_data", "resource_info", b"resource_info"]) -> None: ...

global___FolderIamPolicy = FolderIamPolicy

@typing_extensions.final
class FolderOrganizationPolicyXBooleanPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENFORCED_FIELD_NUMBER: builtins.int
    enforced: builtins.bool
    def __init__(
        self,
        *,
        enforced: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enforced", b"enforced"]) -> None: ...

global___FolderOrganizationPolicyXBooleanPolicy = FolderOrganizationPolicyXBooleanPolicy

@typing_extensions.final
class FolderOrganizationPolicyXListPolicyXAllow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALL_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    all: builtins.bool
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        all: builtins.bool = ...,
        values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["all", b"all", "values", b"values"]) -> None: ...

global___FolderOrganizationPolicyXListPolicyXAllow = FolderOrganizationPolicyXListPolicyXAllow

@typing_extensions.final
class FolderOrganizationPolicyXListPolicyXDeny(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALL_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    all: builtins.bool
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        all: builtins.bool = ...,
        values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["all", b"all", "values", b"values"]) -> None: ...

global___FolderOrganizationPolicyXListPolicyXDeny = FolderOrganizationPolicyXListPolicyXDeny

@typing_extensions.final
class FolderOrganizationPolicyXListPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INHERIT_FROM_PARENT_FIELD_NUMBER: builtins.int
    SUGGESTED_VALUE_FIELD_NUMBER: builtins.int
    ALLOW_FIELD_NUMBER: builtins.int
    DENY_FIELD_NUMBER: builtins.int
    inherit_from_parent: builtins.bool
    suggested_value: builtins.str
    @property
    def allow(self) -> global___FolderOrganizationPolicyXListPolicyXAllow: ...
    @property
    def deny(self) -> global___FolderOrganizationPolicyXListPolicyXDeny: ...
    def __init__(
        self,
        *,
        inherit_from_parent: builtins.bool = ...,
        suggested_value: builtins.str = ...,
        allow: global___FolderOrganizationPolicyXListPolicyXAllow | None = ...,
        deny: global___FolderOrganizationPolicyXListPolicyXDeny | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allow", b"allow", "deny", b"deny"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow", b"allow", "deny", b"deny", "inherit_from_parent", b"inherit_from_parent", "suggested_value", b"suggested_value"]) -> None: ...

global___FolderOrganizationPolicyXListPolicy = FolderOrganizationPolicyXListPolicy

@typing_extensions.final
class FolderOrganizationPolicyXRestorePolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_FIELD_NUMBER: builtins.int
    default: builtins.bool
    def __init__(
        self,
        *,
        default: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["default", b"default"]) -> None: ...

global___FolderOrganizationPolicyXRestorePolicy = FolderOrganizationPolicyXRestorePolicy

@typing_extensions.final
class FolderOrganizationPolicyXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    create: builtins.str
    delete: builtins.str
    read: builtins.str
    update: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
        delete: builtins.str = ...,
        read: builtins.str = ...,
        update: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create", "delete", b"delete", "read", b"read", "update", b"update"]) -> None: ...

global___FolderOrganizationPolicyXTimeouts = FolderOrganizationPolicyXTimeouts

@typing_extensions.final
class FolderOrganizationPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSTRAINT_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    BOOLEAN_POLICY_FIELD_NUMBER: builtins.int
    LIST_POLICY_FIELD_NUMBER: builtins.int
    RESTORE_POLICY_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    constraint: builtins.str
    etag: builtins.str
    folder: builtins.str
    id: builtins.str
    update_time: builtins.str
    version: builtins.float
    @property
    def boolean_policy(self) -> global___FolderOrganizationPolicyXBooleanPolicy: ...
    @property
    def list_policy(self) -> global___FolderOrganizationPolicyXListPolicy: ...
    @property
    def restore_policy(self) -> global___FolderOrganizationPolicyXRestorePolicy: ...
    @property
    def timeouts(self) -> global___FolderOrganizationPolicyXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        constraint: builtins.str = ...,
        etag: builtins.str = ...,
        folder: builtins.str = ...,
        id: builtins.str = ...,
        update_time: builtins.str = ...,
        version: builtins.float = ...,
        boolean_policy: global___FolderOrganizationPolicyXBooleanPolicy | None = ...,
        list_policy: global___FolderOrganizationPolicyXListPolicy | None = ...,
        restore_policy: global___FolderOrganizationPolicyXRestorePolicy | None = ...,
        timeouts: global___FolderOrganizationPolicyXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["boolean_policy", b"boolean_policy", "list_policy", b"list_policy", "resource_info", b"resource_info", "restore_policy", b"restore_policy", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["boolean_policy", b"boolean_policy", "constraint", b"constraint", "etag", b"etag", "folder", b"folder", "id", b"id", "list_policy", b"list_policy", "resource_info", b"resource_info", "restore_policy", b"restore_policy", "timeouts", b"timeouts", "update_time", b"update_time", "version", b"version"]) -> None: ...

global___FolderOrganizationPolicy = FolderOrganizationPolicy
