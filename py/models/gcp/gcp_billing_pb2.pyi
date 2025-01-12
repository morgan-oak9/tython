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
class BillingAccountIamBindingXCondition(google.protobuf.message.Message):
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

global___BillingAccountIamBindingXCondition = BillingAccountIamBindingXCondition

@typing_extensions.final
class BillingAccountIamBinding(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    billing_account_id: builtins.str
    etag: builtins.str
    id: builtins.str
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    role: builtins.str
    @property
    def condition(self) -> global___BillingAccountIamBindingXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        billing_account_id: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        members: collections.abc.Iterable[builtins.str] | None = ...,
        role: builtins.str = ...,
        condition: global___BillingAccountIamBindingXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_account_id", b"billing_account_id", "condition", b"condition", "etag", b"etag", "id", b"id", "members", b"members", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___BillingAccountIamBinding = BillingAccountIamBinding

@typing_extensions.final
class BillingAccountIamMemberXCondition(google.protobuf.message.Message):
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

global___BillingAccountIamMemberXCondition = BillingAccountIamMemberXCondition

@typing_extensions.final
class BillingAccountIamMember(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    billing_account_id: builtins.str
    etag: builtins.str
    id: builtins.str
    member: builtins.str
    role: builtins.str
    @property
    def condition(self) -> global___BillingAccountIamMemberXCondition: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        billing_account_id: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        member: builtins.str = ...,
        role: builtins.str = ...,
        condition: global___BillingAccountIamMemberXCondition | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["condition", b"condition", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_account_id", b"billing_account_id", "condition", b"condition", "etag", b"etag", "id", b"id", "member", b"member", "resource_info", b"resource_info", "role", b"role"]) -> None: ...

global___BillingAccountIamMember = BillingAccountIamMember

@typing_extensions.final
class BillingAccountIamPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    POLICY_DATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    billing_account_id: builtins.str
    etag: builtins.str
    id: builtins.str
    policy_data: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        billing_account_id: builtins.str = ...,
        etag: builtins.str = ...,
        id: builtins.str = ...,
        policy_data: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_account_id", b"billing_account_id", "etag", b"etag", "id", b"id", "policy_data", b"policy_data", "resource_info", b"resource_info"]) -> None: ...

global___BillingAccountIamPolicy = BillingAccountIamPolicy

@typing_extensions.final
class BillingBudgetXAllUpdatesRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISABLE_DEFAULT_IAM_RECIPIENTS_FIELD_NUMBER: builtins.int
    MONITORING_NOTIFICATION_CHANNELS_FIELD_NUMBER: builtins.int
    PUBSUB_TOPIC_FIELD_NUMBER: builtins.int
    SCHEMA_VERSION_FIELD_NUMBER: builtins.int
    disable_default_iam_recipients: builtins.bool
    @property
    def monitoring_notification_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    pubsub_topic: builtins.str
    schema_version: builtins.str
    def __init__(
        self,
        *,
        disable_default_iam_recipients: builtins.bool = ...,
        monitoring_notification_channels: collections.abc.Iterable[builtins.str] | None = ...,
        pubsub_topic: builtins.str = ...,
        schema_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disable_default_iam_recipients", b"disable_default_iam_recipients", "monitoring_notification_channels", b"monitoring_notification_channels", "pubsub_topic", b"pubsub_topic", "schema_version", b"schema_version"]) -> None: ...

global___BillingBudgetXAllUpdatesRule = BillingBudgetXAllUpdatesRule

@typing_extensions.final
class BillingBudgetXAmountXSpecifiedAmount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    NANOS_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    currency_code: builtins.str
    nanos: builtins.float
    units: builtins.str
    def __init__(
        self,
        *,
        currency_code: builtins.str = ...,
        nanos: builtins.float = ...,
        units: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["currency_code", b"currency_code", "nanos", b"nanos", "units", b"units"]) -> None: ...

global___BillingBudgetXAmountXSpecifiedAmount = BillingBudgetXAmountXSpecifiedAmount

@typing_extensions.final
class BillingBudgetXAmount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_PERIOD_AMOUNT_FIELD_NUMBER: builtins.int
    SPECIFIED_AMOUNT_FIELD_NUMBER: builtins.int
    last_period_amount: builtins.bool
    @property
    def specified_amount(self) -> global___BillingBudgetXAmountXSpecifiedAmount: ...
    def __init__(
        self,
        *,
        last_period_amount: builtins.bool = ...,
        specified_amount: global___BillingBudgetXAmountXSpecifiedAmount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["specified_amount", b"specified_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_period_amount", b"last_period_amount", "specified_amount", b"specified_amount"]) -> None: ...

global___BillingBudgetXAmount = BillingBudgetXAmount

@typing_extensions.final
class BillingBudgetXBudgetFilterXCustomPeriodXEndDate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAY_FIELD_NUMBER: builtins.int
    MONTH_FIELD_NUMBER: builtins.int
    YEAR_FIELD_NUMBER: builtins.int
    day: builtins.float
    month: builtins.float
    year: builtins.float
    def __init__(
        self,
        *,
        day: builtins.float = ...,
        month: builtins.float = ...,
        year: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day", b"day", "month", b"month", "year", b"year"]) -> None: ...

global___BillingBudgetXBudgetFilterXCustomPeriodXEndDate = BillingBudgetXBudgetFilterXCustomPeriodXEndDate

@typing_extensions.final
class BillingBudgetXBudgetFilterXCustomPeriodXStartDate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAY_FIELD_NUMBER: builtins.int
    MONTH_FIELD_NUMBER: builtins.int
    YEAR_FIELD_NUMBER: builtins.int
    day: builtins.float
    month: builtins.float
    year: builtins.float
    def __init__(
        self,
        *,
        day: builtins.float = ...,
        month: builtins.float = ...,
        year: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day", b"day", "month", b"month", "year", b"year"]) -> None: ...

global___BillingBudgetXBudgetFilterXCustomPeriodXStartDate = BillingBudgetXBudgetFilterXCustomPeriodXStartDate

@typing_extensions.final
class BillingBudgetXBudgetFilterXCustomPeriod(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    END_DATE_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    @property
    def end_date(self) -> global___BillingBudgetXBudgetFilterXCustomPeriodXEndDate: ...
    @property
    def start_date(self) -> global___BillingBudgetXBudgetFilterXCustomPeriodXStartDate: ...
    def __init__(
        self,
        *,
        end_date: global___BillingBudgetXBudgetFilterXCustomPeriodXEndDate | None = ...,
        start_date: global___BillingBudgetXBudgetFilterXCustomPeriodXStartDate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_date", b"end_date", "start_date", b"start_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_date", b"end_date", "start_date", b"start_date"]) -> None: ...

global___BillingBudgetXBudgetFilterXCustomPeriod = BillingBudgetXBudgetFilterXCustomPeriod

@typing_extensions.final
class BillingBudgetXBudgetFilter(google.protobuf.message.Message):
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

    CALENDAR_PERIOD_FIELD_NUMBER: builtins.int
    CREDIT_TYPES_FIELD_NUMBER: builtins.int
    CREDIT_TYPES_TREATMENT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    PROJECTS_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBACCOUNTS_FIELD_NUMBER: builtins.int
    CUSTOM_PERIOD_FIELD_NUMBER: builtins.int
    calendar_period: builtins.str
    @property
    def credit_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    credit_types_treatment: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def projects(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def subaccounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def custom_period(self) -> global___BillingBudgetXBudgetFilterXCustomPeriod: ...
    def __init__(
        self,
        *,
        calendar_period: builtins.str = ...,
        credit_types: collections.abc.Iterable[builtins.str] | None = ...,
        credit_types_treatment: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        projects: collections.abc.Iterable[builtins.str] | None = ...,
        services: collections.abc.Iterable[builtins.str] | None = ...,
        subaccounts: collections.abc.Iterable[builtins.str] | None = ...,
        custom_period: global___BillingBudgetXBudgetFilterXCustomPeriod | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["custom_period", b"custom_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["calendar_period", b"calendar_period", "credit_types", b"credit_types", "credit_types_treatment", b"credit_types_treatment", "custom_period", b"custom_period", "labels", b"labels", "projects", b"projects", "services", b"services", "subaccounts", b"subaccounts"]) -> None: ...

global___BillingBudgetXBudgetFilter = BillingBudgetXBudgetFilter

@typing_extensions.final
class BillingBudgetXThresholdRules(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEND_BASIS_FIELD_NUMBER: builtins.int
    THRESHOLD_PERCENT_FIELD_NUMBER: builtins.int
    spend_basis: builtins.str
    threshold_percent: builtins.float
    def __init__(
        self,
        *,
        spend_basis: builtins.str = ...,
        threshold_percent: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["spend_basis", b"spend_basis", "threshold_percent", b"threshold_percent"]) -> None: ...

global___BillingBudgetXThresholdRules = BillingBudgetXThresholdRules

@typing_extensions.final
class BillingBudgetXTimeouts(google.protobuf.message.Message):
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

global___BillingBudgetXTimeouts = BillingBudgetXTimeouts

@typing_extensions.final
class BillingBudget(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BILLING_ACCOUNT_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ALL_UPDATES_RULE_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    BUDGET_FILTER_FIELD_NUMBER: builtins.int
    THRESHOLD_RULES_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    billing_account: builtins.str
    display_name: builtins.str
    id: builtins.str
    name: builtins.str
    @property
    def all_updates_rule(self) -> global___BillingBudgetXAllUpdatesRule: ...
    @property
    def amount(self) -> global___BillingBudgetXAmount: ...
    @property
    def budget_filter(self) -> global___BillingBudgetXBudgetFilter: ...
    @property
    def threshold_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BillingBudgetXThresholdRules]: ...
    @property
    def timeouts(self) -> global___BillingBudgetXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        billing_account: builtins.str = ...,
        display_name: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        all_updates_rule: global___BillingBudgetXAllUpdatesRule | None = ...,
        amount: global___BillingBudgetXAmount | None = ...,
        budget_filter: global___BillingBudgetXBudgetFilter | None = ...,
        threshold_rules: collections.abc.Iterable[global___BillingBudgetXThresholdRules] | None = ...,
        timeouts: global___BillingBudgetXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["all_updates_rule", b"all_updates_rule", "amount", b"amount", "budget_filter", b"budget_filter", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["all_updates_rule", b"all_updates_rule", "amount", b"amount", "billing_account", b"billing_account", "budget_filter", b"budget_filter", "display_name", b"display_name", "id", b"id", "name", b"name", "resource_info", b"resource_info", "threshold_rules", b"threshold_rules", "timeouts", b"timeouts"]) -> None: ...

global___BillingBudget = BillingBudget

@typing_extensions.final
class BillingSubaccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    DELETION_POLICY_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MASTER_BILLING_ACCOUNT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    billing_account_id: builtins.str
    deletion_policy: builtins.str
    display_name: builtins.str
    id: builtins.str
    master_billing_account: builtins.str
    name: builtins.str
    open: builtins.bool
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        billing_account_id: builtins.str = ...,
        deletion_policy: builtins.str = ...,
        display_name: builtins.str = ...,
        id: builtins.str = ...,
        master_billing_account: builtins.str = ...,
        name: builtins.str = ...,
        open: builtins.bool = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_account_id", b"billing_account_id", "deletion_policy", b"deletion_policy", "display_name", b"display_name", "id", b"id", "master_billing_account", b"master_billing_account", "name", b"name", "open", b"open", "resource_info", b"resource_info"]) -> None: ...

global___BillingSubaccount = BillingSubaccount
