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
class ServerProtocol(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> None: ...

global___ServerProtocol = ServerProtocol

@typing_extensions.final
class ServerIdentityProviderDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    INVOCATION_ROLE_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    invocation_role: builtins.str
    url: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        invocation_role: builtins.str = ...,
        url: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["invocation_role", b"invocation_role", "resource_info", b"resource_info", "url", b"url"]) -> None: ...

global___ServerIdentityProviderDetails = ServerIdentityProviderDetails

@typing_extensions.final
class ServerEndpointDetails(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ADDRESS_ALLOCATION_IDS_FIELD_NUMBER: builtins.int
    VPC_ID_FIELD_NUMBER: builtins.int
    VPC_ENDPOINT_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def address_allocation_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    vpc_id: builtins.str
    vpc_endpoint_id: builtins.str
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        address_allocation_ids: collections.abc.Iterable[builtins.str] | None = ...,
        vpc_id: builtins.str = ...,
        vpc_endpoint_id: builtins.str = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_allocation_ids", b"address_allocation_ids", "resource_info", b"resource_info", "subnet_ids", b"subnet_ids", "vpc_endpoint_id", b"vpc_endpoint_id", "vpc_id", b"vpc_id"]) -> None: ...

global___ServerEndpointDetails = ServerEndpointDetails

@typing_extensions.final
class Server(google.protobuf.message.Message):
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
    LOGGING_ROLE_FIELD_NUMBER: builtins.int
    PROTOCOLS_FIELD_NUMBER: builtins.int
    IDENTITY_PROVIDER_DETAILS_FIELD_NUMBER: builtins.int
    ENDPOINT_TYPE_FIELD_NUMBER: builtins.int
    SECURITY_POLICY_NAME_FIELD_NUMBER: builtins.int
    ENDPOINT_DETAILS_FIELD_NUMBER: builtins.int
    IDENTITY_PROVIDER_TYPE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    CERTIFICATE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    logging_role: builtins.str
    @property
    def protocols(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerProtocol]: ...
    @property
    def identity_provider_details(self) -> global___ServerIdentityProviderDetails: ...
    endpoint_type: builtins.str
    security_policy_name: builtins.str
    @property
    def endpoint_details(self) -> global___ServerEndpointDetails: ...
    identity_provider_type: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    certificate: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        logging_role: builtins.str = ...,
        protocols: collections.abc.Iterable[global___ServerProtocol] | None = ...,
        identity_provider_details: global___ServerIdentityProviderDetails | None = ...,
        endpoint_type: builtins.str = ...,
        security_policy_name: builtins.str = ...,
        endpoint_details: global___ServerEndpointDetails | None = ...,
        identity_provider_type: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        certificate: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint_details", b"endpoint_details", "identity_provider_details", b"identity_provider_details", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate", b"certificate", "endpoint_details", b"endpoint_details", "endpoint_type", b"endpoint_type", "identity_provider_details", b"identity_provider_details", "identity_provider_type", b"identity_provider_type", "logging_role", b"logging_role", "protocols", b"protocols", "resource_info", b"resource_info", "security_policy_name", b"security_policy_name", "tags", b"tags"]) -> None: ...

global___Server = Server

@typing_extensions.final
class Transfer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    @property
    def server(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Server]: ...
    @property
    def user(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]: ...
    def __init__(
        self,
        *,
        server: collections.abc.Iterable[global___Server] | None = ...,
        user: collections.abc.Iterable[global___User] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["server", b"server", "user", b"user"]) -> None: ...

global___Transfer = Transfer

@typing_extensions.final
class UserHomeDirectoryMapEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENTRY_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    entry: builtins.str
    target: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        entry: builtins.str = ...,
        target: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entry", b"entry", "resource_info", b"resource_info", "target", b"target"]) -> None: ...

global___UserHomeDirectoryMapEntry = UserHomeDirectoryMapEntry

@typing_extensions.final
class UserSshPublicKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> None: ...

global___UserSshPublicKey = UserSshPublicKey

@typing_extensions.final
class User(google.protobuf.message.Message):
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
    POLICY_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_TYPE_FIELD_NUMBER: builtins.int
    SERVER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_MAPPINGS_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEYS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    policy: builtins.str
    role: builtins.str
    home_directory: builtins.str
    home_directory_type: builtins.str
    server_id: builtins.str
    user_name: builtins.str
    @property
    def home_directory_mappings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserHomeDirectoryMapEntry]: ...
    @property
    def ssh_public_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserSshPublicKey]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        policy: builtins.str = ...,
        role: builtins.str = ...,
        home_directory: builtins.str = ...,
        home_directory_type: builtins.str = ...,
        server_id: builtins.str = ...,
        user_name: builtins.str = ...,
        home_directory_mappings: collections.abc.Iterable[global___UserHomeDirectoryMapEntry] | None = ...,
        ssh_public_keys: collections.abc.Iterable[global___UserSshPublicKey] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["home_directory", b"home_directory", "home_directory_mappings", b"home_directory_mappings", "home_directory_type", b"home_directory_type", "policy", b"policy", "resource_info", b"resource_info", "role", b"role", "server_id", b"server_id", "ssh_public_keys", b"ssh_public_keys", "tags", b"tags", "user_name", b"user_name"]) -> None: ...

global___User = User