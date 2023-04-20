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
class NetworkAcl(google.protobuf.message.Message):
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
    TAGS_FIELD_NUMBER: builtins.int
    VPC_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    vpc_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        vpc_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "tags", b"tags", "vpc_id", b"vpc_id"]) -> None: ...

global___NetworkAcl = NetworkAcl

@typing_extensions.final
class EC2_NetworkACL(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ACL_FIELD_NUMBER: builtins.int
    NETWORK_ACL_ENTRY_FIELD_NUMBER: builtins.int
    @property
    def network_acl(self) -> global___NetworkAcl: ...
    @property
    def network_acl_entry(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkAclEntry]: ...
    def __init__(
        self,
        *,
        network_acl: global___NetworkAcl | None = ...,
        network_acl_entry: collections.abc.Iterable[global___NetworkAclEntry] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["network_acl", b"network_acl"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["network_acl", b"network_acl", "network_acl_entry", b"network_acl_entry"]) -> None: ...

global___EC2_NetworkACL = EC2_NetworkACL

@typing_extensions.final
class NetworkAclEntryIcmp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    code: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        code: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "resource_info", b"resource_info"]) -> None: ...

global___NetworkAclEntryIcmp = NetworkAclEntryIcmp

@typing_extensions.final
class NetworkAclEntryPortRange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FROM_FIELD_NUMBER: builtins.int
    TO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    to: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        to: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["from", b"from", "resource_info", b"resource_info", "to", b"to"]) -> None: ...

global___NetworkAclEntryPortRange = NetworkAclEntryPortRange

@typing_extensions.final
class NetworkAclEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    CIDR_BLOCK_FIELD_NUMBER: builtins.int
    EGRESS_FIELD_NUMBER: builtins.int
    ICMP_FIELD_NUMBER: builtins.int
    IPV6_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    NETWORK_ACL_ID_FIELD_NUMBER: builtins.int
    PORT_RANGE_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    RULE_ACTION_FIELD_NUMBER: builtins.int
    RULE_NUMBER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    cidr_block: builtins.str
    egress: builtins.bool
    @property
    def icmp(self) -> global___NetworkAclEntryIcmp: ...
    ipv6_cidr_block: builtins.str
    network_acl_id: builtins.str
    @property
    def port_range(self) -> global___NetworkAclEntryPortRange: ...
    protocol: builtins.int
    rule_action: builtins.str
    rule_number: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        cidr_block: builtins.str = ...,
        egress: builtins.bool = ...,
        icmp: global___NetworkAclEntryIcmp | None = ...,
        ipv6_cidr_block: builtins.str = ...,
        network_acl_id: builtins.str = ...,
        port_range: global___NetworkAclEntryPortRange | None = ...,
        protocol: builtins.int = ...,
        rule_action: builtins.str = ...,
        rule_number: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["icmp", b"icmp", "port_range", b"port_range", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cidr_block", b"cidr_block", "egress", b"egress", "icmp", b"icmp", "ipv6_cidr_block", b"ipv6_cidr_block", "network_acl_id", b"network_acl_id", "port_range", b"port_range", "protocol", b"protocol", "resource_info", b"resource_info", "rule_action", b"rule_action", "rule_number", b"rule_number"]) -> None: ...

global___NetworkAclEntry = NetworkAclEntry