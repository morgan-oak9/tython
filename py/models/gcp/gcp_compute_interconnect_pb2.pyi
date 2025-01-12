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
class ComputeInterconnectAttachmentXTimeouts(google.protobuf.message.Message):
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

global___ComputeInterconnectAttachmentXTimeouts = ComputeInterconnectAttachmentXTimeouts

@typing_extensions.final
class ComputeInterconnectAttachment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PrivateInterconnectInfoEntry(google.protobuf.message.Message):
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

    ADMIN_ENABLED_FIELD_NUMBER: builtins.int
    BANDWIDTH_FIELD_NUMBER: builtins.int
    CANDIDATE_SUBNETS_FIELD_NUMBER: builtins.int
    CLOUD_ROUTER_IP_ADDRESS_FIELD_NUMBER: builtins.int
    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    CUSTOMER_ROUTER_IP_ADDRESS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EDGE_AVAILABILITY_DOMAIN_FIELD_NUMBER: builtins.int
    ENCRYPTION_FIELD_NUMBER: builtins.int
    GOOGLE_REFERENCE_ID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    INTERCONNECT_FIELD_NUMBER: builtins.int
    IPSEC_INTERNAL_ADDRESSES_FIELD_NUMBER: builtins.int
    MTU_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PAIRING_KEY_FIELD_NUMBER: builtins.int
    PARTNER_ASN_FIELD_NUMBER: builtins.int
    PRIVATE_INTERCONNECT_INFO_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    ROUTER_FIELD_NUMBER: builtins.int
    SELF_LINK_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    VLAN_TAG8021Q_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    admin_enabled: builtins.bool
    bandwidth: builtins.str
    @property
    def candidate_subnets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    cloud_router_ip_address: builtins.str
    creation_timestamp: builtins.str
    customer_router_ip_address: builtins.str
    description: builtins.str
    edge_availability_domain: builtins.str
    encryption: builtins.str
    google_reference_id: builtins.str
    id: builtins.str
    interconnect: builtins.str
    @property
    def ipsec_internal_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    mtu: builtins.str
    name: builtins.str
    pairing_key: builtins.str
    partner_asn: builtins.str
    @property
    def private_interconnect_info(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    project: builtins.str
    region: builtins.str
    router: builtins.str
    self_link: builtins.str
    state: builtins.str
    type: builtins.str
    vlan_tag8021q: builtins.float
    @property
    def timeouts(self) -> global___ComputeInterconnectAttachmentXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        admin_enabled: builtins.bool = ...,
        bandwidth: builtins.str = ...,
        candidate_subnets: collections.abc.Iterable[builtins.str] | None = ...,
        cloud_router_ip_address: builtins.str = ...,
        creation_timestamp: builtins.str = ...,
        customer_router_ip_address: builtins.str = ...,
        description: builtins.str = ...,
        edge_availability_domain: builtins.str = ...,
        encryption: builtins.str = ...,
        google_reference_id: builtins.str = ...,
        id: builtins.str = ...,
        interconnect: builtins.str = ...,
        ipsec_internal_addresses: collections.abc.Iterable[builtins.str] | None = ...,
        mtu: builtins.str = ...,
        name: builtins.str = ...,
        pairing_key: builtins.str = ...,
        partner_asn: builtins.str = ...,
        private_interconnect_info: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        project: builtins.str = ...,
        region: builtins.str = ...,
        router: builtins.str = ...,
        self_link: builtins.str = ...,
        state: builtins.str = ...,
        type: builtins.str = ...,
        vlan_tag8021q: builtins.float = ...,
        timeouts: global___ComputeInterconnectAttachmentXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["admin_enabled", b"admin_enabled", "bandwidth", b"bandwidth", "candidate_subnets", b"candidate_subnets", "cloud_router_ip_address", b"cloud_router_ip_address", "creation_timestamp", b"creation_timestamp", "customer_router_ip_address", b"customer_router_ip_address", "description", b"description", "edge_availability_domain", b"edge_availability_domain", "encryption", b"encryption", "google_reference_id", b"google_reference_id", "id", b"id", "interconnect", b"interconnect", "ipsec_internal_addresses", b"ipsec_internal_addresses", "mtu", b"mtu", "name", b"name", "pairing_key", b"pairing_key", "partner_asn", b"partner_asn", "private_interconnect_info", b"private_interconnect_info", "project", b"project", "region", b"region", "resource_info", b"resource_info", "router", b"router", "self_link", b"self_link", "state", b"state", "timeouts", b"timeouts", "type", b"type", "vlan_tag8021q", b"vlan_tag8021q"]) -> None: ...

global___ComputeInterconnectAttachment = ComputeInterconnectAttachment
