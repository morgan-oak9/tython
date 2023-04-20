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
class DHCPOptions(google.protobuf.message.Message):
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
    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    DOMAIN_NAME_SERVERS_FIELD_NUMBER: builtins.int
    NETBIOS_NAME_SERVERS_FIELD_NUMBER: builtins.int
    NETBIOS_NODE_TYPE_FIELD_NUMBER: builtins.int
    NTP_SERVERS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    domain_name: builtins.str
    @property
    def domain_name_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def netbios_name_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    netbios_node_type: builtins.int
    @property
    def ntp_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        domain_name: builtins.str = ...,
        domain_name_servers: collections.abc.Iterable[builtins.str] | None = ...,
        netbios_name_servers: collections.abc.Iterable[builtins.str] | None = ...,
        netbios_node_type: builtins.int = ...,
        ntp_servers: collections.abc.Iterable[builtins.str] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_name", b"domain_name", "domain_name_servers", b"domain_name_servers", "netbios_name_servers", b"netbios_name_servers", "netbios_node_type", b"netbios_node_type", "ntp_servers", b"ntp_servers", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___DHCPOptions = DHCPOptions

@typing_extensions.final
class EC2_DHCPOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DHCP_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def dhcp_options(self) -> global___DHCPOptions: ...
    def __init__(
        self,
        *,
        dhcp_options: global___DHCPOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dhcp_options", b"dhcp_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dhcp_options", b"dhcp_options"]) -> None: ...

global___EC2_DHCPOptions = EC2_DHCPOptions
