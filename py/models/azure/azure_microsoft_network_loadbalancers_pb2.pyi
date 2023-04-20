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
class Microsoft_Network_loadBalancers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOAD_BALANCERS_FIELD_NUMBER: builtins.int
    LOAD_BALANCERS_BACKEND_ADDRESS_POOLS_FIELD_NUMBER: builtins.int
    LOAD_BALANCERS_INBOUND_NAT_RULES_FIELD_NUMBER: builtins.int
    @property
    def load_balancers(self) -> global___LoadBalancers: ...
    @property
    def load_balancers_backend_address_pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LoadBalancersBackendAddressPools]: ...
    @property
    def load_balancers_inbound_nat_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LoadBalancersInboundNatRules]: ...
    def __init__(
        self,
        *,
        load_balancers: global___LoadBalancers | None = ...,
        load_balancers_backend_address_pools: collections.abc.Iterable[global___LoadBalancersBackendAddressPools] | None = ...,
        load_balancers_inbound_nat_rules: collections.abc.Iterable[global___LoadBalancersInboundNatRules] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["load_balancers", b"load_balancers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["load_balancers", b"load_balancers", "load_balancers_backend_address_pools", b"load_balancers_backend_address_pools", "load_balancers_inbound_nat_rules", b"load_balancers_inbound_nat_rules"]) -> None: ...

global___Microsoft_Network_loadBalancers = Microsoft_Network_loadBalancers

@typing_extensions.final
class LoadBalancersInboundNatRules(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    FRONTEND_IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    FRONTEND_PORT_FIELD_NUMBER: builtins.int
    BACKEND_PORT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    ENABLE_FLOATING_IP_FIELD_NUMBER: builtins.int
    ENABLE_TCP_RESET_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    frontend_ip_configuration: builtins.str
    protocol: builtins.str
    frontend_port: builtins.int
    backend_port: builtins.int
    idle_timeout_in_minutes: builtins.int
    enable_floating_ip: builtins.bool
    enable_tcp_reset: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        frontend_ip_configuration: builtins.str = ...,
        protocol: builtins.str = ...,
        frontend_port: builtins.int = ...,
        backend_port: builtins.int = ...,
        idle_timeout_in_minutes: builtins.int = ...,
        enable_floating_ip: builtins.bool = ...,
        enable_tcp_reset: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_port", b"backend_port", "enable_floating_ip", b"enable_floating_ip", "enable_tcp_reset", b"enable_tcp_reset", "frontend_ip_configuration", b"frontend_ip_configuration", "frontend_port", b"frontend_port", "idle_timeout_in_minutes", b"idle_timeout_in_minutes", "name", b"name", "protocol", b"protocol", "resource_info", b"resource_info"]) -> None: ...

global___LoadBalancersInboundNatRules = LoadBalancersInboundNatRules

@typing_extensions.final
class LoadBalancersBackendAddressPools(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    LOAD_BALANCER_BACKEND_ADDRESSES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    location: builtins.str
    @property
    def load_balancer_backend_addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LoadBalancerBackendAddress]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        location: builtins.str = ...,
        load_balancer_backend_addresses: collections.abc.Iterable[global___LoadBalancerBackendAddress] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["load_balancer_backend_addresses", b"load_balancer_backend_addresses", "location", b"location", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___LoadBalancersBackendAddressPools = LoadBalancersBackendAddressPools

@typing_extensions.final
class LoadBalancers(google.protobuf.message.Message):
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
    SKU_FIELD_NUMBER: builtins.int
    FRONTEND_IP_CONFIGURATIONS_FIELD_NUMBER: builtins.int
    BACKEND_ADDRESS_POOLS_FIELD_NUMBER: builtins.int
    LOAD_BALANCING_RULES_FIELD_NUMBER: builtins.int
    PROBES_FIELD_NUMBER: builtins.int
    INBOUND_NAT_RULES_FIELD_NUMBER: builtins.int
    INBOUND_NAT_POOLS_FIELD_NUMBER: builtins.int
    OUTBOUND_RULES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    location: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def extended_location(self) -> global___ExtendedLocation: ...
    @property
    def sku(self) -> global___LoadBalancerSku: ...
    @property
    def frontend_ip_configurations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FrontendIPConfiguration]: ...
    @property
    def backend_address_pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BackendAddressPool]: ...
    @property
    def load_balancing_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LoadBalancingRule]: ...
    @property
    def probes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Probe]: ...
    @property
    def inbound_nat_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InboundNatRule]: ...
    @property
    def inbound_nat_pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InboundNatPool]: ...
    @property
    def outbound_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OutboundRule]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        location: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        extended_location: global___ExtendedLocation | None = ...,
        sku: global___LoadBalancerSku | None = ...,
        frontend_ip_configurations: collections.abc.Iterable[global___FrontendIPConfiguration] | None = ...,
        backend_address_pools: collections.abc.Iterable[global___BackendAddressPool] | None = ...,
        load_balancing_rules: collections.abc.Iterable[global___LoadBalancingRule] | None = ...,
        probes: collections.abc.Iterable[global___Probe] | None = ...,
        inbound_nat_rules: collections.abc.Iterable[global___InboundNatRule] | None = ...,
        inbound_nat_pools: collections.abc.Iterable[global___InboundNatPool] | None = ...,
        outbound_rules: collections.abc.Iterable[global___OutboundRule] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extended_location", b"extended_location", "resource_info", b"resource_info", "sku", b"sku"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_address_pools", b"backend_address_pools", "extended_location", b"extended_location", "frontend_ip_configurations", b"frontend_ip_configurations", "inbound_nat_pools", b"inbound_nat_pools", "inbound_nat_rules", b"inbound_nat_rules", "load_balancing_rules", b"load_balancing_rules", "location", b"location", "name", b"name", "outbound_rules", b"outbound_rules", "probes", b"probes", "resource_info", b"resource_info", "sku", b"sku", "tags", b"tags"]) -> None: ...

global___LoadBalancers = LoadBalancers

@typing_extensions.final
class OutboundRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOCATED_OUTBOUND_PORTS_FIELD_NUMBER: builtins.int
    FRONTEND_IP_CONFIGURATIONS_FIELD_NUMBER: builtins.int
    BACKEND_ADDRESS_POOL_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    ENABLE_TCP_RESET_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    allocated_outbound_ports: builtins.int
    @property
    def frontend_ip_configurations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    backend_address_pool: builtins.str
    protocol: builtins.str
    enable_tcp_reset: builtins.bool
    idle_timeout_in_minutes: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        allocated_outbound_ports: builtins.int = ...,
        frontend_ip_configurations: collections.abc.Iterable[builtins.str] | None = ...,
        backend_address_pool: builtins.str = ...,
        protocol: builtins.str = ...,
        enable_tcp_reset: builtins.bool = ...,
        idle_timeout_in_minutes: builtins.int = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allocated_outbound_ports", b"allocated_outbound_ports", "backend_address_pool", b"backend_address_pool", "enable_tcp_reset", b"enable_tcp_reset", "frontend_ip_configurations", b"frontend_ip_configurations", "idle_timeout_in_minutes", b"idle_timeout_in_minutes", "name", b"name", "protocol", b"protocol"]) -> None: ...

global___OutboundRule = OutboundRule

@typing_extensions.final
class InboundNatPool(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRONTEND_IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    FRONTEND_PORT_RANGE_START_FIELD_NUMBER: builtins.int
    FRONTEND_PORT_RANGE_END_FIELD_NUMBER: builtins.int
    BACKEND_PORT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    ENABLE_FLOATING_IP_FIELD_NUMBER: builtins.int
    ENABLE_TCP_RESET_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    frontend_ip_configuration: builtins.str
    protocol: builtins.str
    frontend_port_range_start: builtins.int
    frontend_port_range_end: builtins.int
    backend_port: builtins.int
    idle_timeout_in_minutes: builtins.int
    enable_floating_ip: builtins.bool
    enable_tcp_reset: builtins.bool
    name: builtins.str
    def __init__(
        self,
        *,
        frontend_ip_configuration: builtins.str = ...,
        protocol: builtins.str = ...,
        frontend_port_range_start: builtins.int = ...,
        frontend_port_range_end: builtins.int = ...,
        backend_port: builtins.int = ...,
        idle_timeout_in_minutes: builtins.int = ...,
        enable_floating_ip: builtins.bool = ...,
        enable_tcp_reset: builtins.bool = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_port", b"backend_port", "enable_floating_ip", b"enable_floating_ip", "enable_tcp_reset", b"enable_tcp_reset", "frontend_ip_configuration", b"frontend_ip_configuration", "frontend_port_range_end", b"frontend_port_range_end", "frontend_port_range_start", b"frontend_port_range_start", "idle_timeout_in_minutes", b"idle_timeout_in_minutes", "name", b"name", "protocol", b"protocol"]) -> None: ...

global___InboundNatPool = InboundNatPool

@typing_extensions.final
class InboundNatRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRONTEND_IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    FRONTEND_PORT_FIELD_NUMBER: builtins.int
    BACKEND_PORT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    ENABLE_FLOATING_IP_FIELD_NUMBER: builtins.int
    ENABLE_TCP_RESET_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    frontend_ip_configuration: builtins.str
    protocol: builtins.str
    frontend_port: builtins.int
    backend_port: builtins.int
    idle_timeout_in_minutes: builtins.int
    enable_floating_ip: builtins.bool
    enable_tcp_reset: builtins.bool
    name: builtins.str
    def __init__(
        self,
        *,
        frontend_ip_configuration: builtins.str = ...,
        protocol: builtins.str = ...,
        frontend_port: builtins.int = ...,
        backend_port: builtins.int = ...,
        idle_timeout_in_minutes: builtins.int = ...,
        enable_floating_ip: builtins.bool = ...,
        enable_tcp_reset: builtins.bool = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_port", b"backend_port", "enable_floating_ip", b"enable_floating_ip", "enable_tcp_reset", b"enable_tcp_reset", "frontend_ip_configuration", b"frontend_ip_configuration", "frontend_port", b"frontend_port", "idle_timeout_in_minutes", b"idle_timeout_in_minutes", "name", b"name", "protocol", b"protocol"]) -> None: ...

global___InboundNatRule = InboundNatRule

@typing_extensions.final
class Probe(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROTOCOL_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    INTERVAL_IN_SECONDS_FIELD_NUMBER: builtins.int
    NUMBER_OF_PROBES_FIELD_NUMBER: builtins.int
    REQUEST_PATH_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    protocol: builtins.str
    port: builtins.int
    interval_in_seconds: builtins.int
    number_of_probes: builtins.int
    request_path: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        protocol: builtins.str = ...,
        port: builtins.int = ...,
        interval_in_seconds: builtins.int = ...,
        number_of_probes: builtins.int = ...,
        request_path: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interval_in_seconds", b"interval_in_seconds", "name", b"name", "number_of_probes", b"number_of_probes", "port", b"port", "protocol", b"protocol", "request_path", b"request_path"]) -> None: ...

global___Probe = Probe

@typing_extensions.final
class LoadBalancingRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRONTEND_IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    BACKEND_ADDRESS_POOL_FIELD_NUMBER: builtins.int
    PROBE_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    LOAD_DISTRIBUTION_FIELD_NUMBER: builtins.int
    FRONTEND_PORT_FIELD_NUMBER: builtins.int
    BACKEND_PORT_FIELD_NUMBER: builtins.int
    IDLE_TIMEOUT_IN_MINUTES_FIELD_NUMBER: builtins.int
    ENABLE_FLOATING_IP_FIELD_NUMBER: builtins.int
    ENABLE_TCP_RESET_FIELD_NUMBER: builtins.int
    DISABLE_OUTBOUND_SNAT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    frontend_ip_configuration: builtins.str
    backend_address_pool: builtins.str
    probe: builtins.str
    protocol: builtins.str
    load_distribution: builtins.str
    frontend_port: builtins.int
    backend_port: builtins.int
    idle_timeout_in_minutes: builtins.int
    enable_floating_ip: builtins.bool
    enable_tcp_reset: builtins.bool
    disable_outbound_snat: builtins.bool
    name: builtins.str
    def __init__(
        self,
        *,
        frontend_ip_configuration: builtins.str = ...,
        backend_address_pool: builtins.str = ...,
        probe: builtins.str = ...,
        protocol: builtins.str = ...,
        load_distribution: builtins.str = ...,
        frontend_port: builtins.int = ...,
        backend_port: builtins.int = ...,
        idle_timeout_in_minutes: builtins.int = ...,
        enable_floating_ip: builtins.bool = ...,
        enable_tcp_reset: builtins.bool = ...,
        disable_outbound_snat: builtins.bool = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["backend_address_pool", b"backend_address_pool", "backend_port", b"backend_port", "disable_outbound_snat", b"disable_outbound_snat", "enable_floating_ip", b"enable_floating_ip", "enable_tcp_reset", b"enable_tcp_reset", "frontend_ip_configuration", b"frontend_ip_configuration", "frontend_port", b"frontend_port", "idle_timeout_in_minutes", b"idle_timeout_in_minutes", "load_distribution", b"load_distribution", "name", b"name", "probe", b"probe", "protocol", b"protocol"]) -> None: ...

global___LoadBalancingRule = LoadBalancingRule

@typing_extensions.final
class BackendAddressPool(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_FIELD_NUMBER: builtins.int
    LOAD_BALANCER_BACKEND_ADDRESSES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    location: builtins.str
    @property
    def load_balancer_backend_addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LoadBalancerBackendAddress]: ...
    name: builtins.str
    def __init__(
        self,
        *,
        location: builtins.str = ...,
        load_balancer_backend_addresses: collections.abc.Iterable[global___LoadBalancerBackendAddress] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["load_balancer_backend_addresses", b"load_balancer_backend_addresses", "location", b"location", "name", b"name"]) -> None: ...

global___BackendAddressPool = BackendAddressPool

@typing_extensions.final
class LoadBalancerBackendAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_NETWORK_FIELD_NUMBER: builtins.int
    IP_ADDRESS_FIELD_NUMBER: builtins.int
    LOAD_BALANCER_FRONTEND_IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    virtual_network: builtins.str
    ip_address: builtins.str
    load_balancer_frontend_ip_configuration: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        virtual_network: builtins.str = ...,
        ip_address: builtins.str = ...,
        load_balancer_frontend_ip_configuration: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ip_address", b"ip_address", "load_balancer_frontend_ip_configuration", b"load_balancer_frontend_ip_configuration", "name", b"name", "virtual_network", b"virtual_network"]) -> None: ...

global___LoadBalancerBackendAddress = LoadBalancerBackendAddress

@typing_extensions.final
class FrontendIPConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRIVATE_IP_ADDRESS_FIELD_NUMBER: builtins.int
    PRIVATE_IP_ALLOCATION_METHOD_FIELD_NUMBER: builtins.int
    PRIVATE_IP_ADDRESS_VERSION_FIELD_NUMBER: builtins.int
    SUBNET_FIELD_NUMBER: builtins.int
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: builtins.int
    PUBLIC_IP_PREFIX_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ZONES_FIELD_NUMBER: builtins.int
    private_ip_address: builtins.str
    private_ip_allocation_method: builtins.str
    private_ip_address_version: builtins.str
    subnet: builtins.str
    public_ip_address: builtins.str
    public_ip_prefix: builtins.str
    name: builtins.str
    @property
    def zones(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        private_ip_address: builtins.str = ...,
        private_ip_allocation_method: builtins.str = ...,
        private_ip_address_version: builtins.str = ...,
        subnet: builtins.str = ...,
        public_ip_address: builtins.str = ...,
        public_ip_prefix: builtins.str = ...,
        name: builtins.str = ...,
        zones: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "private_ip_address", b"private_ip_address", "private_ip_address_version", b"private_ip_address_version", "private_ip_allocation_method", b"private_ip_allocation_method", "public_ip_address", b"public_ip_address", "public_ip_prefix", b"public_ip_prefix", "subnet", b"subnet", "zones", b"zones"]) -> None: ...

global___FrontendIPConfiguration = FrontendIPConfiguration

@typing_extensions.final
class LoadBalancerSku(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    name: builtins.str
    tier: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        tier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "tier", b"tier"]) -> None: ...

global___LoadBalancerSku = LoadBalancerSku

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
