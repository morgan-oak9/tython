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
class ComputeFirewallXAllow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PORTS_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    @property
    def ports(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    protocol: builtins.str
    def __init__(
        self,
        *,
        ports: collections.abc.Iterable[builtins.str] | None = ...,
        protocol: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ports", b"ports", "protocol", b"protocol"]) -> None: ...

global___ComputeFirewallXAllow = ComputeFirewallXAllow

@typing_extensions.final
class ComputeFirewallXDeny(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PORTS_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    @property
    def ports(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    protocol: builtins.str
    def __init__(
        self,
        *,
        ports: collections.abc.Iterable[builtins.str] | None = ...,
        protocol: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ports", b"ports", "protocol", b"protocol"]) -> None: ...

global___ComputeFirewallXDeny = ComputeFirewallXDeny

@typing_extensions.final
class ComputeFirewallXLogConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    metadata: builtins.str
    def __init__(
        self,
        *,
        metadata: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> None: ...

global___ComputeFirewallXLogConfig = ComputeFirewallXLogConfig

@typing_extensions.final
class ComputeFirewallXTimeouts(google.protobuf.message.Message):
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

global___ComputeFirewallXTimeouts = ComputeFirewallXTimeouts

@typing_extensions.final
class ComputeFirewall(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DESTINATION_RANGES_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    ENABLE_LOGGING_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    SELF_LINK_FIELD_NUMBER: builtins.int
    SOURCE_RANGES_FIELD_NUMBER: builtins.int
    SOURCE_SERVICE_ACCOUNTS_FIELD_NUMBER: builtins.int
    SOURCE_TAGS_FIELD_NUMBER: builtins.int
    TARGET_SERVICE_ACCOUNTS_FIELD_NUMBER: builtins.int
    TARGET_TAGS_FIELD_NUMBER: builtins.int
    ALLOW_FIELD_NUMBER: builtins.int
    DENY_FIELD_NUMBER: builtins.int
    LOG_CONFIG_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    creation_timestamp: builtins.str
    description: builtins.str
    @property
    def destination_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    direction: builtins.str
    disabled: builtins.bool
    enable_logging: builtins.bool
    id: builtins.str
    name: builtins.str
    network: builtins.str
    priority: builtins.float
    project: builtins.str
    self_link: builtins.str
    @property
    def source_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def source_service_accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def source_tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def target_service_accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def target_tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def allow(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeFirewallXAllow]: ...
    @property
    def deny(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeFirewallXDeny]: ...
    @property
    def log_config(self) -> global___ComputeFirewallXLogConfig: ...
    @property
    def timeouts(self) -> global___ComputeFirewallXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        creation_timestamp: builtins.str = ...,
        description: builtins.str = ...,
        destination_ranges: collections.abc.Iterable[builtins.str] | None = ...,
        direction: builtins.str = ...,
        disabled: builtins.bool = ...,
        enable_logging: builtins.bool = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        network: builtins.str = ...,
        priority: builtins.float = ...,
        project: builtins.str = ...,
        self_link: builtins.str = ...,
        source_ranges: collections.abc.Iterable[builtins.str] | None = ...,
        source_service_accounts: collections.abc.Iterable[builtins.str] | None = ...,
        source_tags: collections.abc.Iterable[builtins.str] | None = ...,
        target_service_accounts: collections.abc.Iterable[builtins.str] | None = ...,
        target_tags: collections.abc.Iterable[builtins.str] | None = ...,
        allow: collections.abc.Iterable[global___ComputeFirewallXAllow] | None = ...,
        deny: collections.abc.Iterable[global___ComputeFirewallXDeny] | None = ...,
        log_config: global___ComputeFirewallXLogConfig | None = ...,
        timeouts: global___ComputeFirewallXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["log_config", b"log_config", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow", b"allow", "creation_timestamp", b"creation_timestamp", "deny", b"deny", "description", b"description", "destination_ranges", b"destination_ranges", "direction", b"direction", "disabled", b"disabled", "enable_logging", b"enable_logging", "id", b"id", "log_config", b"log_config", "name", b"name", "network", b"network", "priority", b"priority", "project", b"project", "resource_info", b"resource_info", "self_link", b"self_link", "source_ranges", b"source_ranges", "source_service_accounts", b"source_service_accounts", "source_tags", b"source_tags", "target_service_accounts", b"target_service_accounts", "target_tags", b"target_tags", "timeouts", b"timeouts"]) -> None: ...

global___ComputeFirewall = ComputeFirewall

@typing_extensions.final
class ComputeFirewallPolicyXTimeouts(google.protobuf.message.Message):
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

global___ComputeFirewallPolicyXTimeouts = ComputeFirewallPolicyXTimeouts

@typing_extensions.final
class ComputeFirewallPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    FIREWALL_POLICY_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    RULE_TUPLE_COUNT_FIELD_NUMBER: builtins.int
    SELF_LINK_FIELD_NUMBER: builtins.int
    SELF_LINK_WITH_ID_FIELD_NUMBER: builtins.int
    SHORT_NAME_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    creation_timestamp: builtins.str
    description: builtins.str
    fingerprint: builtins.str
    firewall_policy_id: builtins.str
    id: builtins.str
    name: builtins.str
    parent: builtins.str
    rule_tuple_count: builtins.float
    self_link: builtins.str
    self_link_with_id: builtins.str
    short_name: builtins.str
    @property
    def timeouts(self) -> global___ComputeFirewallPolicyXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        creation_timestamp: builtins.str = ...,
        description: builtins.str = ...,
        fingerprint: builtins.str = ...,
        firewall_policy_id: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        parent: builtins.str = ...,
        rule_tuple_count: builtins.float = ...,
        self_link: builtins.str = ...,
        self_link_with_id: builtins.str = ...,
        short_name: builtins.str = ...,
        timeouts: global___ComputeFirewallPolicyXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creation_timestamp", b"creation_timestamp", "description", b"description", "fingerprint", b"fingerprint", "firewall_policy_id", b"firewall_policy_id", "id", b"id", "name", b"name", "parent", b"parent", "resource_info", b"resource_info", "rule_tuple_count", b"rule_tuple_count", "self_link", b"self_link", "self_link_with_id", b"self_link_with_id", "short_name", b"short_name", "timeouts", b"timeouts"]) -> None: ...

global___ComputeFirewallPolicy = ComputeFirewallPolicy

@typing_extensions.final
class ComputeFirewallPolicyAssociationXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATE_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    create: builtins.str
    delete: builtins.str
    def __init__(
        self,
        *,
        create: builtins.str = ...,
        delete: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create", b"create", "delete", b"delete"]) -> None: ...

global___ComputeFirewallPolicyAssociationXTimeouts = ComputeFirewallPolicyAssociationXTimeouts

@typing_extensions.final
class ComputeFirewallPolicyAssociation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTACHMENT_TARGET_FIELD_NUMBER: builtins.int
    FIREWALL_POLICY_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SHORT_NAME_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    attachment_target: builtins.str
    firewall_policy: builtins.str
    id: builtins.str
    name: builtins.str
    short_name: builtins.str
    @property
    def timeouts(self) -> global___ComputeFirewallPolicyAssociationXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        attachment_target: builtins.str = ...,
        firewall_policy: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
        short_name: builtins.str = ...,
        timeouts: global___ComputeFirewallPolicyAssociationXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attachment_target", b"attachment_target", "firewall_policy", b"firewall_policy", "id", b"id", "name", b"name", "resource_info", b"resource_info", "short_name", b"short_name", "timeouts", b"timeouts"]) -> None: ...

global___ComputeFirewallPolicyAssociation = ComputeFirewallPolicyAssociation

@typing_extensions.final
class ComputeFirewallPolicyRuleXMatchXLayer4Configs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IP_PROTOCOL_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    ip_protocol: builtins.str
    @property
    def ports(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        ip_protocol: builtins.str = ...,
        ports: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ip_protocol", b"ip_protocol", "ports", b"ports"]) -> None: ...

global___ComputeFirewallPolicyRuleXMatchXLayer4Configs = ComputeFirewallPolicyRuleXMatchXLayer4Configs

@typing_extensions.final
class ComputeFirewallPolicyRuleXMatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEST_IP_RANGES_FIELD_NUMBER: builtins.int
    SRC_IP_RANGES_FIELD_NUMBER: builtins.int
    LAYER4_CONFIGS_FIELD_NUMBER: builtins.int
    @property
    def dest_ip_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def src_ip_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def layer4_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeFirewallPolicyRuleXMatchXLayer4Configs]: ...
    def __init__(
        self,
        *,
        dest_ip_ranges: collections.abc.Iterable[builtins.str] | None = ...,
        src_ip_ranges: collections.abc.Iterable[builtins.str] | None = ...,
        layer4_configs: collections.abc.Iterable[global___ComputeFirewallPolicyRuleXMatchXLayer4Configs] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dest_ip_ranges", b"dest_ip_ranges", "layer4_configs", b"layer4_configs", "src_ip_ranges", b"src_ip_ranges"]) -> None: ...

global___ComputeFirewallPolicyRuleXMatch = ComputeFirewallPolicyRuleXMatch

@typing_extensions.final
class ComputeFirewallPolicyRuleXTimeouts(google.protobuf.message.Message):
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

global___ComputeFirewallPolicyRuleXTimeouts = ComputeFirewallPolicyRuleXTimeouts

@typing_extensions.final
class ComputeFirewallPolicyRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTION_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    ENABLE_LOGGING_FIELD_NUMBER: builtins.int
    FIREWALL_POLICY_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    RULE_TUPLE_COUNT_FIELD_NUMBER: builtins.int
    TARGET_RESOURCES_FIELD_NUMBER: builtins.int
    TARGET_SERVICE_ACCOUNTS_FIELD_NUMBER: builtins.int
    MATCH_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    action: builtins.str
    description: builtins.str
    direction: builtins.str
    disabled: builtins.bool
    enable_logging: builtins.bool
    firewall_policy: builtins.str
    id: builtins.str
    kind: builtins.str
    priority: builtins.float
    rule_tuple_count: builtins.float
    @property
    def target_resources(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def target_service_accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def match(self) -> global___ComputeFirewallPolicyRuleXMatch: ...
    @property
    def timeouts(self) -> global___ComputeFirewallPolicyRuleXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        action: builtins.str = ...,
        description: builtins.str = ...,
        direction: builtins.str = ...,
        disabled: builtins.bool = ...,
        enable_logging: builtins.bool = ...,
        firewall_policy: builtins.str = ...,
        id: builtins.str = ...,
        kind: builtins.str = ...,
        priority: builtins.float = ...,
        rule_tuple_count: builtins.float = ...,
        target_resources: collections.abc.Iterable[builtins.str] | None = ...,
        target_service_accounts: collections.abc.Iterable[builtins.str] | None = ...,
        match: global___ComputeFirewallPolicyRuleXMatch | None = ...,
        timeouts: global___ComputeFirewallPolicyRuleXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["match", b"match", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "description", b"description", "direction", b"direction", "disabled", b"disabled", "enable_logging", b"enable_logging", "firewall_policy", b"firewall_policy", "id", b"id", "kind", b"kind", "match", b"match", "priority", b"priority", "resource_info", b"resource_info", "rule_tuple_count", b"rule_tuple_count", "target_resources", b"target_resources", "target_service_accounts", b"target_service_accounts", "timeouts", b"timeouts"]) -> None: ...

global___ComputeFirewallPolicyRule = ComputeFirewallPolicyRule
