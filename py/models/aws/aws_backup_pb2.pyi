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
class BackupPlanLifecycleResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DELETE_AFTER_DAYS_FIELD_NUMBER: builtins.int
    MOVE_TO_COLD_STORAGE_AFTER_DAYS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    delete_after_days: builtins.float
    move_to_cold_storage_after_days: builtins.float
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        delete_after_days: builtins.float = ...,
        move_to_cold_storage_after_days: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_after_days", b"delete_after_days", "move_to_cold_storage_after_days", b"move_to_cold_storage_after_days", "resource_info", b"resource_info"]) -> None: ...

global___BackupPlanLifecycleResourceType = BackupPlanLifecycleResourceType

@typing_extensions.final
class BackupPlanCopyActionResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LIFECYCLE_FIELD_NUMBER: builtins.int
    DESTINATION_BACKUP_VAULT_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def lifecycle(self) -> global___BackupPlanLifecycleResourceType: ...
    destination_backup_vault_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        lifecycle: global___BackupPlanLifecycleResourceType | None = ...,
        destination_backup_vault_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lifecycle", b"lifecycle", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["destination_backup_vault_arn", b"destination_backup_vault_arn", "lifecycle", b"lifecycle", "resource_info", b"resource_info"]) -> None: ...

global___BackupPlanCopyActionResourceType = BackupPlanCopyActionResourceType

@typing_extensions.final
class BackupPlanBackupRuleResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class RecoveryPointTagsEntry(google.protobuf.message.Message):
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
    COMPLETION_WINDOW_MINUTES_FIELD_NUMBER: builtins.int
    SCHEDULE_EXPRESSION_FIELD_NUMBER: builtins.int
    RECOVERY_POINT_TAGS_FIELD_NUMBER: builtins.int
    COPY_ACTIONS_FIELD_NUMBER: builtins.int
    LIFECYCLE_FIELD_NUMBER: builtins.int
    TARGET_BACKUP_VAULT_FIELD_NUMBER: builtins.int
    START_WINDOW_MINUTES_FIELD_NUMBER: builtins.int
    RULE_NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    completion_window_minutes: builtins.float
    schedule_expression: builtins.str
    @property
    def recovery_point_tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def copy_actions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupPlanCopyActionResourceType]: ...
    @property
    def lifecycle(self) -> global___BackupPlanLifecycleResourceType: ...
    target_backup_vault: builtins.str
    start_window_minutes: builtins.float
    rule_name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        completion_window_minutes: builtins.float = ...,
        schedule_expression: builtins.str = ...,
        recovery_point_tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        copy_actions: collections.abc.Iterable[global___BackupPlanCopyActionResourceType] | None = ...,
        lifecycle: global___BackupPlanLifecycleResourceType | None = ...,
        target_backup_vault: builtins.str = ...,
        start_window_minutes: builtins.float = ...,
        rule_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["lifecycle", b"lifecycle", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["completion_window_minutes", b"completion_window_minutes", "copy_actions", b"copy_actions", "lifecycle", b"lifecycle", "recovery_point_tags", b"recovery_point_tags", "resource_info", b"resource_info", "rule_name", b"rule_name", "schedule_expression", b"schedule_expression", "start_window_minutes", b"start_window_minutes", "target_backup_vault", b"target_backup_vault"]) -> None: ...

global___BackupPlanBackupRuleResourceType = BackupPlanBackupRuleResourceType

@typing_extensions.final
class BackupPlanBackupPlanResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BACKUP_PLAN_NAME_FIELD_NUMBER: builtins.int
    BACKUP_PLAN_RULE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    backup_plan_name: builtins.str
    @property
    def backup_plan_rule(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupPlanBackupRuleResourceType]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        backup_plan_name: builtins.str = ...,
        backup_plan_rule: collections.abc.Iterable[global___BackupPlanBackupRuleResourceType] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_plan_name", b"backup_plan_name", "backup_plan_rule", b"backup_plan_rule", "resource_info", b"resource_info"]) -> None: ...

global___BackupPlanBackupPlanResourceType = BackupPlanBackupPlanResourceType

@typing_extensions.final
class BackupPlan(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class BackupPlanTagsEntry(google.protobuf.message.Message):
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
    BACKUP_PLAN_FIELD_NUMBER: builtins.int
    BACKUP_PLAN_TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def backup_plan(self) -> global___BackupPlanBackupPlanResourceType: ...
    @property
    def backup_plan_tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        backup_plan: global___BackupPlanBackupPlanResourceType | None = ...,
        backup_plan_tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_plan", b"backup_plan", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_plan", b"backup_plan", "backup_plan_tags", b"backup_plan_tags", "resource_info", b"resource_info"]) -> None: ...

global___BackupPlan = BackupPlan

@typing_extensions.final
class Backup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_PLAN_FIELD_NUMBER: builtins.int
    BACKUP_SELECTION_FIELD_NUMBER: builtins.int
    BACKUP_VAULT_FIELD_NUMBER: builtins.int
    @property
    def backup_plan(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupPlan]: ...
    @property
    def backup_selection(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupSelection]: ...
    @property
    def backup_vault(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupVault]: ...
    def __init__(
        self,
        *,
        backup_plan: collections.abc.Iterable[global___BackupPlan] | None = ...,
        backup_selection: collections.abc.Iterable[global___BackupSelection] | None = ...,
        backup_vault: collections.abc.Iterable[global___BackupVault] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_plan", b"backup_plan", "backup_selection", b"backup_selection", "backup_vault", b"backup_vault"]) -> None: ...

global___Backup = Backup

@typing_extensions.final
class BackupSelectionConditionResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CONDITION_VALUE_FIELD_NUMBER: builtins.int
    CONDITION_KEY_FIELD_NUMBER: builtins.int
    CONDITION_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    condition_value: builtins.str
    condition_key: builtins.str
    condition_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        condition_value: builtins.str = ...,
        condition_key: builtins.str = ...,
        condition_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition_key", b"condition_key", "condition_type", b"condition_type", "condition_value", b"condition_value", "resource_info", b"resource_info"]) -> None: ...

global___BackupSelectionConditionResourceType = BackupSelectionConditionResourceType

@typing_extensions.final
class BackupSelectionBackupSelectionResourceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LIST_OF_TAGS_FIELD_NUMBER: builtins.int
    SELECTION_NAME_FIELD_NUMBER: builtins.int
    IAM_ROLE_ARN_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def list_of_tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackupSelectionConditionResourceType]: ...
    selection_name: builtins.str
    iam_role_arn: builtins.str
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        list_of_tags: collections.abc.Iterable[global___BackupSelectionConditionResourceType] | None = ...,
        selection_name: builtins.str = ...,
        iam_role_arn: builtins.str = ...,
        resources: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["iam_role_arn", b"iam_role_arn", "list_of_tags", b"list_of_tags", "resource_info", b"resource_info", "resources", b"resources", "selection_name", b"selection_name"]) -> None: ...

global___BackupSelectionBackupSelectionResourceType = BackupSelectionBackupSelectionResourceType

@typing_extensions.final
class BackupSelection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    BACKUP_SELECTION_FIELD_NUMBER: builtins.int
    BACKUP_PLAN_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def backup_selection(self) -> global___BackupSelectionBackupSelectionResourceType: ...
    backup_plan_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        backup_selection: global___BackupSelectionBackupSelectionResourceType | None = ...,
        backup_plan_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backup_selection", b"backup_selection", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_plan_id", b"backup_plan_id", "backup_selection", b"backup_selection", "resource_info", b"resource_info"]) -> None: ...

global___BackupSelection = BackupSelection

@typing_extensions.final
class BackupVaultNotificationObjectType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SNS_TOPIC_ARN_FIELD_NUMBER: builtins.int
    BACKUP_VAULT_EVENTS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    sns_topic_arn: builtins.str
    @property
    def backup_vault_events(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        sns_topic_arn: builtins.str = ...,
        backup_vault_events: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backup_vault_events", b"backup_vault_events", "resource_info", b"resource_info", "sns_topic_arn", b"sns_topic_arn"]) -> None: ...

global___BackupVaultNotificationObjectType = BackupVaultNotificationObjectType

@typing_extensions.final
class BackupVault(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class BackupVaultTagsEntry(google.protobuf.message.Message):
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
    class AccessPolicyEntry(google.protobuf.message.Message):
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
    BACKUP_VAULT_TAGS_FIELD_NUMBER: builtins.int
    BACKUP_VAULT_NAME_FIELD_NUMBER: builtins.int
    ENCRYPTION_KEY_ARN_FIELD_NUMBER: builtins.int
    NOTIFICATIONS_FIELD_NUMBER: builtins.int
    ACCESS_POLICY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def backup_vault_tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    backup_vault_name: builtins.str
    encryption_key_arn: builtins.str
    @property
    def notifications(self) -> global___BackupVaultNotificationObjectType: ...
    @property
    def access_policy(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        backup_vault_tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        backup_vault_name: builtins.str = ...,
        encryption_key_arn: builtins.str = ...,
        notifications: global___BackupVaultNotificationObjectType | None = ...,
        access_policy: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["notifications", b"notifications", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_policy", b"access_policy", "backup_vault_name", b"backup_vault_name", "backup_vault_tags", b"backup_vault_tags", "encryption_key_arn", b"encryption_key_arn", "notifications", b"notifications", "resource_info", b"resource_info"]) -> None: ...

global___BackupVault = BackupVault
