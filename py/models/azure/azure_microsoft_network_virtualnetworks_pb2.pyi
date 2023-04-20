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
class Microsoft_Network_virtualNetworks(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_NETWORKS_FIELD_NUMBER: builtins.int
    VIRTUAL_NETWORKS_SUBNETS_FIELD_NUMBER: builtins.int
    VIRTUAL_NETWORKS_VIRTUAL_NETWORK_PEERINGS_FIELD_NUMBER: builtins.int
    @property
    def virtual_networks(self) -> global___VirtualNetworks: ...
    @property
    def virtual_networks_subnets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VirtualNetworksSubnets]: ...
    @property
    def virtual_networks_virtual_network_peerings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VirtualNetworksVirtualNetworkPeerings]: ...
    def __init__(
        self,
        *,
        virtual_networks: global___VirtualNetworks | None = ...,
        virtual_networks_subnets: collections.abc.Iterable[global___VirtualNetworksSubnets] | None = ...,
        virtual_networks_virtual_network_peerings: collections.abc.Iterable[global___VirtualNetworksVirtualNetworkPeerings] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["virtual_networks", b"virtual_networks"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["virtual_networks", b"virtual_networks", "virtual_networks_subnets", b"virtual_networks_subnets", "virtual_networks_virtual_network_peerings", b"virtual_networks_virtual_network_peerings"]) -> None: ...

global___Microsoft_Network_virtualNetworks = Microsoft_Network_virtualNetworks

@typing_extensions.final
class NetworkSecurityGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___NetworkSecurityGroup = NetworkSecurityGroup

@typing_extensions.final
class RouteTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___RouteTable = RouteTable

@typing_extensions.final
class NatGateways(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___NatGateways = NatGateways

@typing_extensions.final
class DdosProtectionPlan(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___DdosProtectionPlan = DdosProtectionPlan

@typing_extensions.final
class VirtualNetworksVirtualNetworkPeerings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ALLOW_VIRTUAL_NETWORK_ACCESS_FIELD_NUMBER: builtins.int
    ALLOW_FORWARDED_TRAFFIC_FIELD_NUMBER: builtins.int
    ALLOW_GATEWAY_TRANSIT_FIELD_NUMBER: builtins.int
    USE_REMOTE_GATEWAYS_FIELD_NUMBER: builtins.int
    REMOTE_VIRTUAL_NETWORK_FIELD_NUMBER: builtins.int
    REMOTE_ADDRESS_SPACE_FIELD_NUMBER: builtins.int
    REMOTE_BGP_COMMUNITIES_FIELD_NUMBER: builtins.int
    PEERING_STATE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    allow_virtual_network_access: builtins.bool
    allow_forwarded_traffic: builtins.bool
    allow_gateway_transit: builtins.bool
    use_remote_gateways: builtins.bool
    remote_virtual_network: builtins.str
    @property
    def remote_address_space(self) -> global___AddressSpace: ...
    @property
    def remote_bgp_communities(self) -> global___VirtualNetworkBgpCommunities: ...
    peering_state: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        allow_virtual_network_access: builtins.bool = ...,
        allow_forwarded_traffic: builtins.bool = ...,
        allow_gateway_transit: builtins.bool = ...,
        use_remote_gateways: builtins.bool = ...,
        remote_virtual_network: builtins.str = ...,
        remote_address_space: global___AddressSpace | None = ...,
        remote_bgp_communities: global___VirtualNetworkBgpCommunities | None = ...,
        peering_state: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["remote_address_space", b"remote_address_space", "remote_bgp_communities", b"remote_bgp_communities", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_forwarded_traffic", b"allow_forwarded_traffic", "allow_gateway_transit", b"allow_gateway_transit", "allow_virtual_network_access", b"allow_virtual_network_access", "name", b"name", "peering_state", b"peering_state", "remote_address_space", b"remote_address_space", "remote_bgp_communities", b"remote_bgp_communities", "remote_virtual_network", b"remote_virtual_network", "resource_info", b"resource_info", "use_remote_gateways", b"use_remote_gateways"]) -> None: ...

global___VirtualNetworksVirtualNetworkPeerings = VirtualNetworksVirtualNetworkPeerings

@typing_extensions.final
class VirtualNetworksSubnets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ADDRESS_PREFIX_FIELD_NUMBER: builtins.int
    ADDRESS_PREFIXES_FIELD_NUMBER: builtins.int
    NETWORK_SECURITY_GROUP_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_FIELD_NUMBER: builtins.int
    NAT_GATEWAY_FIELD_NUMBER: builtins.int
    SERVICE_ENDPOINTS_FIELD_NUMBER: builtins.int
    SERVICE_ENDPOINT_POLICIES_FIELD_NUMBER: builtins.int
    IP_ALLOCATIONS_FIELD_NUMBER: builtins.int
    DELEGATIONS_FIELD_NUMBER: builtins.int
    PRIVATE_ENDPOINT_NETWORK_POLICIES_FIELD_NUMBER: builtins.int
    PRIVATE_LINK_SERVICE_NETWORK_POLICIES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    address_prefix: builtins.str
    @property
    def address_prefixes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def network_security_group(self) -> global___NetworkSecurityGroup: ...
    @property
    def route_table(self) -> global___RouteTable: ...
    nat_gateway: builtins.str
    @property
    def service_endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceEndpointPropertiesFormat]: ...
    @property
    def service_endpoint_policies(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def ip_allocations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def delegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Delegation]: ...
    private_endpoint_network_policies: builtins.str
    private_link_service_network_policies: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        address_prefix: builtins.str = ...,
        address_prefixes: collections.abc.Iterable[builtins.str] | None = ...,
        network_security_group: global___NetworkSecurityGroup | None = ...,
        route_table: global___RouteTable | None = ...,
        nat_gateway: builtins.str = ...,
        service_endpoints: collections.abc.Iterable[global___ServiceEndpointPropertiesFormat] | None = ...,
        service_endpoint_policies: collections.abc.Iterable[builtins.str] | None = ...,
        ip_allocations: collections.abc.Iterable[builtins.str] | None = ...,
        delegations: collections.abc.Iterable[global___Delegation] | None = ...,
        private_endpoint_network_policies: builtins.str = ...,
        private_link_service_network_policies: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["network_security_group", b"network_security_group", "resource_info", b"resource_info", "route_table", b"route_table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_prefix", b"address_prefix", "address_prefixes", b"address_prefixes", "delegations", b"delegations", "ip_allocations", b"ip_allocations", "name", b"name", "nat_gateway", b"nat_gateway", "network_security_group", b"network_security_group", "private_endpoint_network_policies", b"private_endpoint_network_policies", "private_link_service_network_policies", b"private_link_service_network_policies", "resource_info", b"resource_info", "route_table", b"route_table", "service_endpoint_policies", b"service_endpoint_policies", "service_endpoints", b"service_endpoints"]) -> None: ...

global___VirtualNetworksSubnets = VirtualNetworksSubnets

@typing_extensions.final
class VirtualNetworks(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    EXTENDED_LOCATION_FIELD_NUMBER: builtins.int
    ADDRESS_SPACE_FIELD_NUMBER: builtins.int
    DHCP_OPTIONS_FIELD_NUMBER: builtins.int
    SUBNETS_FIELD_NUMBER: builtins.int
    VIRTUAL_NETWORK_PEERINGS_FIELD_NUMBER: builtins.int
    ENABLE_DDOS_PROTECTION_FIELD_NUMBER: builtins.int
    ENABLE_VM_PROTECTION_FIELD_NUMBER: builtins.int
    DDOS_PROTECTION_PLAN_FIELD_NUMBER: builtins.int
    BGP_COMMUNITIES_FIELD_NUMBER: builtins.int
    IP_ALLOCATIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    location: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def extended_location(self) -> global___ExtendedLocation: ...
    @property
    def address_space(self) -> global___AddressSpace: ...
    @property
    def dhcp_options(self) -> global___DhcpOptions: ...
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Subnet]: ...
    @property
    def virtual_network_peerings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VirtualNetworkPeering]: ...
    enable_ddos_protection: builtins.bool
    enable_vm_protection: builtins.bool
    @property
    def ddos_protection_plan(self) -> global___DdosProtectionPlan: ...
    @property
    def bgp_communities(self) -> global___VirtualNetworkBgpCommunities: ...
    @property
    def ip_allocations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        location: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        extended_location: global___ExtendedLocation | None = ...,
        address_space: global___AddressSpace | None = ...,
        dhcp_options: global___DhcpOptions | None = ...,
        subnets: collections.abc.Iterable[global___Subnet] | None = ...,
        virtual_network_peerings: collections.abc.Iterable[global___VirtualNetworkPeering] | None = ...,
        enable_ddos_protection: builtins.bool = ...,
        enable_vm_protection: builtins.bool = ...,
        ddos_protection_plan: global___DdosProtectionPlan | None = ...,
        bgp_communities: global___VirtualNetworkBgpCommunities | None = ...,
        ip_allocations: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address_space", b"address_space", "bgp_communities", b"bgp_communities", "ddos_protection_plan", b"ddos_protection_plan", "dhcp_options", b"dhcp_options", "extended_location", b"extended_location", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_space", b"address_space", "bgp_communities", b"bgp_communities", "ddos_protection_plan", b"ddos_protection_plan", "dhcp_options", b"dhcp_options", "enable_ddos_protection", b"enable_ddos_protection", "enable_vm_protection", b"enable_vm_protection", "extended_location", b"extended_location", "ip_allocations", b"ip_allocations", "location", b"location", "name", b"name", "resource_info", b"resource_info", "subnets", b"subnets", "tags", b"tags", "virtual_network_peerings", b"virtual_network_peerings"]) -> None: ...

global___VirtualNetworks = VirtualNetworks

@typing_extensions.final
class VirtualNetworkPeering(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOW_VIRTUAL_NETWORK_ACCESS_FIELD_NUMBER: builtins.int
    ALLOW_FORWARDED_TRAFFIC_FIELD_NUMBER: builtins.int
    ALLOW_GATEWAY_TRANSIT_FIELD_NUMBER: builtins.int
    USE_REMOTE_GATEWAYS_FIELD_NUMBER: builtins.int
    REMOTE_VIRTUAL_NETWORK_FIELD_NUMBER: builtins.int
    REMOTE_ADDRESS_SPACE_FIELD_NUMBER: builtins.int
    REMOTE_BGP_COMMUNITIES_FIELD_NUMBER: builtins.int
    PEERING_STATE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    allow_virtual_network_access: builtins.bool
    allow_forwarded_traffic: builtins.bool
    allow_gateway_transit: builtins.bool
    use_remote_gateways: builtins.bool
    remote_virtual_network: builtins.str
    @property
    def remote_address_space(self) -> global___AddressSpace: ...
    @property
    def remote_bgp_communities(self) -> global___VirtualNetworkBgpCommunities: ...
    peering_state: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        allow_virtual_network_access: builtins.bool = ...,
        allow_forwarded_traffic: builtins.bool = ...,
        allow_gateway_transit: builtins.bool = ...,
        use_remote_gateways: builtins.bool = ...,
        remote_virtual_network: builtins.str = ...,
        remote_address_space: global___AddressSpace | None = ...,
        remote_bgp_communities: global___VirtualNetworkBgpCommunities | None = ...,
        peering_state: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["remote_address_space", b"remote_address_space", "remote_bgp_communities", b"remote_bgp_communities"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_forwarded_traffic", b"allow_forwarded_traffic", "allow_gateway_transit", b"allow_gateway_transit", "allow_virtual_network_access", b"allow_virtual_network_access", "name", b"name", "peering_state", b"peering_state", "remote_address_space", b"remote_address_space", "remote_bgp_communities", b"remote_bgp_communities", "remote_virtual_network", b"remote_virtual_network", "use_remote_gateways", b"use_remote_gateways"]) -> None: ...

global___VirtualNetworkPeering = VirtualNetworkPeering

@typing_extensions.final
class VirtualNetworkBgpCommunities(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_NETWORK_COMMUNITY_FIELD_NUMBER: builtins.int
    virtual_network_community: builtins.str
    def __init__(
        self,
        *,
        virtual_network_community: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["virtual_network_community", b"virtual_network_community"]) -> None: ...

global___VirtualNetworkBgpCommunities = VirtualNetworkBgpCommunities

@typing_extensions.final
class Subnet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_PREFIX_FIELD_NUMBER: builtins.int
    ADDRESS_PREFIXES_FIELD_NUMBER: builtins.int
    NETWORK_SECURITY_GROUP_FIELD_NUMBER: builtins.int
    ROUTE_TABLE_FIELD_NUMBER: builtins.int
    NAT_GATEWAY_FIELD_NUMBER: builtins.int
    SERVICE_ENDPOINTS_FIELD_NUMBER: builtins.int
    SERVICE_ENDPOINT_POLICIES_FIELD_NUMBER: builtins.int
    IP_ALLOCATIONS_FIELD_NUMBER: builtins.int
    DELEGATIONS_FIELD_NUMBER: builtins.int
    PRIVATE_ENDPOINT_NETWORK_POLICIES_FIELD_NUMBER: builtins.int
    PRIVATE_LINK_SERVICE_NETWORK_POLICIES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    address_prefix: builtins.str
    @property
    def address_prefixes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def network_security_group(self) -> global___NetworkSecurityGroup: ...
    @property
    def route_table(self) -> global___RouteTable: ...
    nat_gateway: builtins.str
    @property
    def service_endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceEndpointPropertiesFormat]: ...
    @property
    def service_endpoint_policies(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def ip_allocations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def delegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Delegation]: ...
    private_endpoint_network_policies: builtins.str
    private_link_service_network_policies: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        address_prefix: builtins.str = ...,
        address_prefixes: collections.abc.Iterable[builtins.str] | None = ...,
        network_security_group: global___NetworkSecurityGroup | None = ...,
        route_table: global___RouteTable | None = ...,
        nat_gateway: builtins.str = ...,
        service_endpoints: collections.abc.Iterable[global___ServiceEndpointPropertiesFormat] | None = ...,
        service_endpoint_policies: collections.abc.Iterable[builtins.str] | None = ...,
        ip_allocations: collections.abc.Iterable[builtins.str] | None = ...,
        delegations: collections.abc.Iterable[global___Delegation] | None = ...,
        private_endpoint_network_policies: builtins.str = ...,
        private_link_service_network_policies: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["network_security_group", b"network_security_group", "route_table", b"route_table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_prefix", b"address_prefix", "address_prefixes", b"address_prefixes", "delegations", b"delegations", "ip_allocations", b"ip_allocations", "name", b"name", "nat_gateway", b"nat_gateway", "network_security_group", b"network_security_group", "private_endpoint_network_policies", b"private_endpoint_network_policies", "private_link_service_network_policies", b"private_link_service_network_policies", "route_table", b"route_table", "service_endpoint_policies", b"service_endpoint_policies", "service_endpoints", b"service_endpoints"]) -> None: ...

global___Subnet = Subnet

@typing_extensions.final
class Delegation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_NAME_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    service_name: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        service_name: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "service_name", b"service_name"]) -> None: ...

global___Delegation = Delegation

@typing_extensions.final
class ServiceEndpointPropertiesFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_FIELD_NUMBER: builtins.int
    LOCATIONS_FIELD_NUMBER: builtins.int
    service: builtins.str
    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        service: builtins.str = ...,
        locations: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locations", b"locations", "service", b"service"]) -> None: ...

global___ServiceEndpointPropertiesFormat = ServiceEndpointPropertiesFormat

@typing_extensions.final
class DhcpOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DNS_SERVERS_FIELD_NUMBER: builtins.int
    @property
    def dns_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        dns_servers: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_servers", b"dns_servers"]) -> None: ...

global___DhcpOptions = DhcpOptions

@typing_extensions.final
class AddressSpace(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_PREFIXES_FIELD_NUMBER: builtins.int
    @property
    def address_prefixes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        address_prefixes: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_prefixes", b"address_prefixes"]) -> None: ...

global___AddressSpace = AddressSpace

@typing_extensions.final
class ExtendedLocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    type: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "type", b"type"]) -> None: ...

global___ExtendedLocation = ExtendedLocation