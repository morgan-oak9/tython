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
class Subnet(google.protobuf.message.Message):
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
    ASSIGN_IPV6_ADDRESS_ON_CREATION_FIELD_NUMBER: builtins.int
    AVAILABILITY_ZONE_FIELD_NUMBER: builtins.int
    CIDR_BLOCK_FIELD_NUMBER: builtins.int
    IPV6_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    MAP_PUBLIC_IP_ON_LAUNCH_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    VPC_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    assign_ipv6_address_on_creation: builtins.bool
    availability_zone: builtins.str
    cidr_block: builtins.str
    ipv6_cidr_block: builtins.str
    map_public_ip_on_launch: builtins.bool
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    vpc_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        assign_ipv6_address_on_creation: builtins.bool = ...,
        availability_zone: builtins.str = ...,
        cidr_block: builtins.str = ...,
        ipv6_cidr_block: builtins.str = ...,
        map_public_ip_on_launch: builtins.bool = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        vpc_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assign_ipv6_address_on_creation", b"assign_ipv6_address_on_creation", "availability_zone", b"availability_zone", "cidr_block", b"cidr_block", "ipv6_cidr_block", b"ipv6_cidr_block", "map_public_ip_on_launch", b"map_public_ip_on_launch", "resource_info", b"resource_info", "tags", b"tags", "vpc_id", b"vpc_id"]) -> None: ...

global___Subnet = Subnet

@typing_extensions.final
class EC2_Subnet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_FIELD_NUMBER: builtins.int
    SUBNET_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    SUBNET_NETWORK_ACL_ASSOCIATION_FIELD_NUMBER: builtins.int
    SUBNET_ROUTE_TABLE_ASSOCIATION_FIELD_NUMBER: builtins.int
    @property
    def subnet(self) -> global___Subnet: ...
    @property
    def subnet_cidr_block(self) -> global___SubnetCidrBlock: ...
    @property
    def subnet_network_acl_association(self) -> global___SubnetNetworkAclAssociation: ...
    @property
    def subnet_route_table_association(self) -> global___SubnetRouteTableAssociation: ...
    def __init__(
        self,
        *,
        subnet: global___Subnet | None = ...,
        subnet_cidr_block: global___SubnetCidrBlock | None = ...,
        subnet_network_acl_association: global___SubnetNetworkAclAssociation | None = ...,
        subnet_route_table_association: global___SubnetRouteTableAssociation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["subnet", b"subnet", "subnet_cidr_block", b"subnet_cidr_block", "subnet_network_acl_association", b"subnet_network_acl_association", "subnet_route_table_association", b"subnet_route_table_association"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["subnet", b"subnet", "subnet_cidr_block", b"subnet_cidr_block", "subnet_network_acl_association", b"subnet_network_acl_association", "subnet_route_table_association", b"subnet_route_table_association"]) -> None: ...

global___EC2_Subnet = EC2_Subnet

@typing_extensions.final
class SubnetCidrBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    IPV6_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    ipv6_cidr_block: builtins.str
    subnet_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        ipv6_cidr_block: builtins.str = ...,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ipv6_cidr_block", b"ipv6_cidr_block", "resource_info", b"resource_info", "subnet_id", b"subnet_id"]) -> None: ...

global___SubnetCidrBlock = SubnetCidrBlock

@typing_extensions.final
class SubnetNetworkAclAssociation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NETWORK_ACL_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    network_acl_id: builtins.str
    subnet_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        network_acl_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["network_acl_id", b"network_acl_id", "resource_info", b"resource_info", "subnet_id", b"subnet_id"]) -> None: ...

global___SubnetNetworkAclAssociation = SubnetNetworkAclAssociation

@typing_extensions.final
class SubnetRouteTableAssociation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    route_table_id: builtins.str
    subnet_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        route_table_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "route_table_id", b"route_table_id", "subnet_id", b"subnet_id"]) -> None: ...

global___SubnetRouteTableAssociation = SubnetRouteTableAssociation
