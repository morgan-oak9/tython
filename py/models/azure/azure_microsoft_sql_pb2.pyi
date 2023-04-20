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
class Microsoft_Sql(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCE_POOLS_FIELD_NUMBER: builtins.int
    LOCATIONS_INSTANCE_FAILOVER_GROUPS_FIELD_NUMBER: builtins.int
    LOCATIONS_SERVER_TRUST_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def instance_pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InstancePools]: ...
    @property
    def locations_instance_failover_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocationsInstanceFailoverGroups]: ...
    @property
    def locations_server_trust_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocationsServerTrustGroups]: ...
    def __init__(
        self,
        *,
        instance_pools: collections.abc.Iterable[global___InstancePools] | None = ...,
        locations_instance_failover_groups: collections.abc.Iterable[global___LocationsInstanceFailoverGroups] | None = ...,
        locations_server_trust_groups: collections.abc.Iterable[global___LocationsServerTrustGroups] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["instance_pools", b"instance_pools", "locations_instance_failover_groups", b"locations_instance_failover_groups", "locations_server_trust_groups", b"locations_server_trust_groups"]) -> None: ...

global___Microsoft_Sql = Microsoft_Sql

@typing_extensions.final
class LocationsServerTrustGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    GROUP_MEMBERS_FIELD_NUMBER: builtins.int
    TRUST_SCOPES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    @property
    def group_members(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerInfo]: ...
    @property
    def trust_scopes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        group_members: collections.abc.Iterable[global___ServerInfo] | None = ...,
        trust_scopes: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_members", b"group_members", "name", b"name", "resource_info", b"resource_info", "trust_scopes", b"trust_scopes"]) -> None: ...

global___LocationsServerTrustGroups = LocationsServerTrustGroups

@typing_extensions.final
class ServerInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["server_id", b"server_id"]) -> None: ...

global___ServerInfo = ServerInfo

@typing_extensions.final
class LocationsInstanceFailoverGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MANAGED_INSTANCE_PAIRS_FIELD_NUMBER: builtins.int
    PARTNER_REGIONS_FIELD_NUMBER: builtins.int
    READ_ONLY_ENDPOINT_FIELD_NUMBER: builtins.int
    READ_WRITE_ENDPOINT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    @property
    def managed_instance_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ManagedInstancePairInfo]: ...
    @property
    def partner_regions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PartnerRegionInfo]: ...
    @property
    def read_only_endpoint(self) -> global___InstanceFailoverGroupReadOnlyEndpoint: ...
    @property
    def read_write_endpoint(self) -> global___InstanceFailoverGroupReadWriteEndpoint: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        managed_instance_pairs: collections.abc.Iterable[global___ManagedInstancePairInfo] | None = ...,
        partner_regions: collections.abc.Iterable[global___PartnerRegionInfo] | None = ...,
        read_only_endpoint: global___InstanceFailoverGroupReadOnlyEndpoint | None = ...,
        read_write_endpoint: global___InstanceFailoverGroupReadWriteEndpoint | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_only_endpoint", b"read_only_endpoint", "read_write_endpoint", b"read_write_endpoint", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["managed_instance_pairs", b"managed_instance_pairs", "name", b"name", "partner_regions", b"partner_regions", "read_only_endpoint", b"read_only_endpoint", "read_write_endpoint", b"read_write_endpoint", "resource_info", b"resource_info"]) -> None: ...

global___LocationsInstanceFailoverGroups = LocationsInstanceFailoverGroups

@typing_extensions.final
class InstanceFailoverGroupReadWriteEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILOVER_POLICY_FIELD_NUMBER: builtins.int
    FAILOVER_WITH_DATA_LOSS_GRACE_PERIOD_MINUTES_FIELD_NUMBER: builtins.int
    failover_policy: builtins.str
    failover_with_data_loss_grace_period_minutes: builtins.int
    def __init__(
        self,
        *,
        failover_policy: builtins.str = ...,
        failover_with_data_loss_grace_period_minutes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failover_policy", b"failover_policy", "failover_with_data_loss_grace_period_minutes", b"failover_with_data_loss_grace_period_minutes"]) -> None: ...

global___InstanceFailoverGroupReadWriteEndpoint = InstanceFailoverGroupReadWriteEndpoint

@typing_extensions.final
class InstanceFailoverGroupReadOnlyEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILOVER_POLICY_FIELD_NUMBER: builtins.int
    failover_policy: builtins.str
    def __init__(
        self,
        *,
        failover_policy: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failover_policy", b"failover_policy"]) -> None: ...

global___InstanceFailoverGroupReadOnlyEndpoint = InstanceFailoverGroupReadOnlyEndpoint

@typing_extensions.final
class PartnerRegionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_FIELD_NUMBER: builtins.int
    location: builtins.str
    def __init__(
        self,
        *,
        location: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location"]) -> None: ...

global___PartnerRegionInfo = PartnerRegionInfo

@typing_extensions.final
class ManagedInstancePairInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARTNER_MANAGED_INSTANCE_ID_FIELD_NUMBER: builtins.int
    PRIMARY_MANAGED_INSTANCE_ID_FIELD_NUMBER: builtins.int
    partner_managed_instance_id: builtins.str
    primary_managed_instance_id: builtins.str
    def __init__(
        self,
        *,
        partner_managed_instance_id: builtins.str = ...,
        primary_managed_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["partner_managed_instance_id", b"partner_managed_instance_id", "primary_managed_instance_id", b"primary_managed_instance_id"]) -> None: ...

global___ManagedInstancePairInfo = ManagedInstancePairInfo

@typing_extensions.final
class InstancePools(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LICENSE_TYPE_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    V_CORES_FIELD_NUMBER: builtins.int
    SKU_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    license_type: builtins.str
    subnet_id: builtins.str
    v_cores: builtins.int
    @property
    def sku(self) -> global___Sku: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        license_type: builtins.str = ...,
        subnet_id: builtins.str = ...,
        v_cores: builtins.int = ...,
        sku: global___Sku | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sku", b"sku"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["license_type", b"license_type", "location", b"location", "name", b"name", "resource_info", b"resource_info", "sku", b"sku", "subnet_id", b"subnet_id", "tags", b"tags", "v_cores", b"v_cores"]) -> None: ...

global___InstancePools = InstancePools

@typing_extensions.final
class Sku(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAPACITY_FIELD_NUMBER: builtins.int
    FAMILY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    capacity: builtins.int
    family: builtins.str
    name: builtins.str
    size: builtins.str
    tier: builtins.str
    def __init__(
        self,
        *,
        capacity: builtins.int = ...,
        family: builtins.str = ...,
        name: builtins.str = ...,
        size: builtins.str = ...,
        tier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["capacity", b"capacity", "family", b"family", "name", b"name", "size", b"size", "tier", b"tier"]) -> None: ...

global___Sku = Sku