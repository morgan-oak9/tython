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
class HttpNamespace(google.protobuf.message.Message):
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
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    description: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        description: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___HttpNamespace = HttpNamespace

@typing_extensions.final
class ServiceDiscovery(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HTTP_NAMESPACE_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    PRIVATE_DNS_NAMESPACE_FIELD_NUMBER: builtins.int
    PUBLIC_DNS_NAMESPACE_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    @property
    def http_namespace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HttpNamespace]: ...
    @property
    def instance(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Instance]: ...
    @property
    def private_dns_namespace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PrivateDnsNamespace]: ...
    @property
    def public_dns_namespace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PublicDnsNamespace]: ...
    @property
    def service(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]: ...
    def __init__(
        self,
        *,
        http_namespace: collections.abc.Iterable[global___HttpNamespace] | None = ...,
        instance: collections.abc.Iterable[global___Instance] | None = ...,
        private_dns_namespace: collections.abc.Iterable[global___PrivateDnsNamespace] | None = ...,
        public_dns_namespace: collections.abc.Iterable[global___PublicDnsNamespace] | None = ...,
        service: collections.abc.Iterable[global___Service] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["http_namespace", b"http_namespace", "instance", b"instance", "private_dns_namespace", b"private_dns_namespace", "public_dns_namespace", b"public_dns_namespace", "service", b"service"]) -> None: ...

global___ServiceDiscovery = ServiceDiscovery

@typing_extensions.final
class Instance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class InstanceAttributesEntry(google.protobuf.message.Message):
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
    INSTANCE_ATTRIBUTES_FIELD_NUMBER: builtins.int
    INSTANCE_ID_FIELD_NUMBER: builtins.int
    SERVICE_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def instance_attributes(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    instance_id: builtins.str
    service_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        instance_attributes: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        instance_id: builtins.str = ...,
        service_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["instance_attributes", b"instance_attributes", "instance_id", b"instance_id", "resource_info", b"resource_info", "service_id", b"service_id"]) -> None: ...

global___Instance = Instance

@typing_extensions.final
class PrivateDnsNamespace(google.protobuf.message.Message):
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
    DESCRIPTION_FIELD_NUMBER: builtins.int
    VPC_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    description: builtins.str
    vpc: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        description: builtins.str = ...,
        vpc: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "resource_info", b"resource_info", "tags", b"tags", "vpc", b"vpc"]) -> None: ...

global___PrivateDnsNamespace = PrivateDnsNamespace

@typing_extensions.final
class PublicDnsNamespace(google.protobuf.message.Message):
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
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    description: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        description: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___PublicDnsNamespace = PublicDnsNamespace

@typing_extensions.final
class ServiceHealthCheckCustomConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FAILURE_THRESHOLD_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    failure_threshold: builtins.float
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        failure_threshold: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure_threshold", b"failure_threshold", "resource_info", b"resource_info"]) -> None: ...

global___ServiceHealthCheckCustomConfig = ServiceHealthCheckCustomConfig

@typing_extensions.final
class ServiceDnsRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    ttl: builtins.float
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        ttl: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "ttl", b"ttl"]) -> None: ...

global___ServiceDnsRecord = ServiceDnsRecord

@typing_extensions.final
class ServiceDnsConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DNS_RECORDS_FIELD_NUMBER: builtins.int
    ROUTING_POLICY_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def dns_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceDnsRecord]: ...
    routing_policy: builtins.str
    namespace_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        dns_records: collections.abc.Iterable[global___ServiceDnsRecord] | None = ...,
        routing_policy: builtins.str = ...,
        namespace_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_records", b"dns_records", "namespace_id", b"namespace_id", "resource_info", b"resource_info", "routing_policy", b"routing_policy"]) -> None: ...

global___ServiceDnsConfig = ServiceDnsConfig

@typing_extensions.final
class ServiceHealthCheckConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    RESOURCE_PATH_FIELD_NUMBER: builtins.int
    FAILURE_THRESHOLD_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    resource_path: builtins.str
    failure_threshold: builtins.float
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        resource_path: builtins.str = ...,
        failure_threshold: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure_threshold", b"failure_threshold", "resource_info", b"resource_info", "resource_path", b"resource_path"]) -> None: ...

global___ServiceHealthCheckConfig = ServiceHealthCheckConfig

@typing_extensions.final
class Service(google.protobuf.message.Message):
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
    DESCRIPTION_FIELD_NUMBER: builtins.int
    HEALTH_CHECK_CUSTOM_CONFIG_FIELD_NUMBER: builtins.int
    DNS_CONFIG_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    HEALTH_CHECK_CONFIG_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    description: builtins.str
    @property
    def health_check_custom_config(self) -> global___ServiceHealthCheckCustomConfig: ...
    @property
    def dns_config(self) -> global___ServiceDnsConfig: ...
    namespace_id: builtins.str
    @property
    def health_check_config(self) -> global___ServiceHealthCheckConfig: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        description: builtins.str = ...,
        health_check_custom_config: global___ServiceHealthCheckCustomConfig | None = ...,
        dns_config: global___ServiceDnsConfig | None = ...,
        namespace_id: builtins.str = ...,
        health_check_config: global___ServiceHealthCheckConfig | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dns_config", b"dns_config", "health_check_config", b"health_check_config", "health_check_custom_config", b"health_check_custom_config", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "dns_config", b"dns_config", "health_check_config", b"health_check_config", "health_check_custom_config", b"health_check_custom_config", "name", b"name", "namespace_id", b"namespace_id", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___Service = Service