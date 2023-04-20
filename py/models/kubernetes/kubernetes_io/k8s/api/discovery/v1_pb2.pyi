"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import kubernetes.kubernetes_io.k8s.api.core.v1_pb2
import kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Endpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class DeprecatedTopologyEntry(google.protobuf.message.Message):
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

    ADDRESSES_FIELD_NUMBER: builtins.int
    CONDITIONS_FIELD_NUMBER: builtins.int
    DEPRECATED_TOPOLOGY_FIELD_NUMBER: builtins.int
    HINTS_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    NODE_NAME_FIELD_NUMBER: builtins.int
    TARGET_REF_FIELD_NUMBER: builtins.int
    ZONE_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def conditions(self) -> global___EndpointConditions: ...
    @property
    def deprecated_topology(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def hints(self) -> global___EndpointHints: ...
    hostname: builtins.str
    node_name: builtins.str
    @property
    def target_ref(self) -> kubernetes.kubernetes_io.k8s.api.core.v1_pb2.ObjectReference: ...
    zone: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        addresses: collections.abc.Iterable[builtins.str] | None = ...,
        conditions: global___EndpointConditions | None = ...,
        deprecated_topology: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        hints: global___EndpointHints | None = ...,
        hostname: builtins.str = ...,
        node_name: builtins.str = ...,
        target_ref: kubernetes.kubernetes_io.k8s.api.core.v1_pb2.ObjectReference | None = ...,
        zone: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["conditions", b"conditions", "hints", b"hints", "resource_info", b"resource_info", "target_ref", b"target_ref"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["addresses", b"addresses", "conditions", b"conditions", "deprecated_topology", b"deprecated_topology", "hints", b"hints", "hostname", b"hostname", "node_name", b"node_name", "resource_info", b"resource_info", "target_ref", b"target_ref", "zone", b"zone"]) -> None: ...

global___Endpoint = Endpoint

@typing_extensions.final
class EndpointConditions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    READY_FIELD_NUMBER: builtins.int
    SERVING_FIELD_NUMBER: builtins.int
    TERMINATING_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ready: builtins.bool
    serving: builtins.bool
    terminating: builtins.bool
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        ready: builtins.bool = ...,
        serving: builtins.bool = ...,
        terminating: builtins.bool = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ready", b"ready", "resource_info", b"resource_info", "serving", b"serving", "terminating", b"terminating"]) -> None: ...

global___EndpointConditions = EndpointConditions

@typing_extensions.final
class EndpointHints(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOR_ZONES_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def for_zones(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ForZone]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        for_zones: collections.abc.Iterable[global___ForZone] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["for_zones", b"for_zones", "resource_info", b"resource_info"]) -> None: ...

global___EndpointHints = EndpointHints

@typing_extensions.final
class EndpointPort(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APP_PROTOCOL_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    app_protocol: builtins.str
    name: builtins.str
    port: builtins.int
    protocol: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        app_protocol: builtins.str = ...,
        name: builtins.str = ...,
        port: builtins.int = ...,
        protocol: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_protocol", b"app_protocol", "name", b"name", "port", b"port", "protocol", b"protocol", "resource_info", b"resource_info"]) -> None: ...

global___EndpointPort = EndpointPort

@typing_extensions.final
class EndpointSlice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_TYPE_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    ENDPOINTS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    address_type: builtins.str
    api_version: builtins.str
    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Endpoint]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def ports(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointPort]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        address_type: builtins.str = ...,
        api_version: builtins.str = ...,
        endpoints: collections.abc.Iterable[global___Endpoint] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        ports: collections.abc.Iterable[global___EndpointPort] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_type", b"address_type", "api_version", b"api_version", "endpoints", b"endpoints", "kind", b"kind", "metadata", b"metadata", "ports", b"ports", "resource_info", b"resource_info"]) -> None: ...

global___EndpointSlice = EndpointSlice

@typing_extensions.final
class EndpointSliceList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointSlice]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___EndpointSlice] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___EndpointSliceList = EndpointSliceList

@typing_extensions.final
class ForZone(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___ForZone = ForZone
