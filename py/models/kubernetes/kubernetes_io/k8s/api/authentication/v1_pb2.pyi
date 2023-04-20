"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2
import shared.shared_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BoundObjectReference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    name: builtins.str
    uid: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        name: builtins.str = ...,
        uid: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "name", b"name", "resource_info", b"resource_info", "uid", b"uid"]) -> None: ...

global___BoundObjectReference = BoundObjectReference

@typing_extensions.final
class TokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def spec(self) -> global___TokenRequestSpec: ...
    @property
    def status(self) -> global___TokenRequestStatus: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___TokenRequestSpec | None = ...,
        status: global___TokenRequestStatus | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> None: ...

global___TokenRequest = TokenRequest

@typing_extensions.final
class TokenRequestSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIENCES_FIELD_NUMBER: builtins.int
    BOUND_OBJECT_REF_FIELD_NUMBER: builtins.int
    EXPIRATION_SECONDS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def audiences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def bound_object_ref(self) -> global___BoundObjectReference: ...
    expiration_seconds: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        audiences: collections.abc.Iterable[builtins.str] | None = ...,
        bound_object_ref: global___BoundObjectReference | None = ...,
        expiration_seconds: builtins.int = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bound_object_ref", b"bound_object_ref", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audiences", b"audiences", "bound_object_ref", b"bound_object_ref", "expiration_seconds", b"expiration_seconds", "resource_info", b"resource_info"]) -> None: ...

global___TokenRequestSpec = TokenRequestSpec

@typing_extensions.final
class TokenRequestStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPIRATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def expiration_timestamp(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time: ...
    token: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        expiration_timestamp: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time | None = ...,
        token: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiration_timestamp", b"expiration_timestamp", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiration_timestamp", b"expiration_timestamp", "resource_info", b"resource_info", "token", b"token"]) -> None: ...

global___TokenRequestStatus = TokenRequestStatus

@typing_extensions.final
class TokenReview(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta: ...
    @property
    def spec(self) -> global___TokenReviewSpec: ...
    @property
    def status(self) -> global___TokenReviewStatus: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___TokenReviewSpec | None = ...,
        status: global___TokenReviewStatus | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> None: ...

global___TokenReview = TokenReview

@typing_extensions.final
class TokenReviewSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIENCES_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def audiences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    token: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        audiences: collections.abc.Iterable[builtins.str] | None = ...,
        token: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audiences", b"audiences", "resource_info", b"resource_info", "token", b"token"]) -> None: ...

global___TokenReviewSpec = TokenReviewSpec

@typing_extensions.final
class TokenReviewStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIENCES_FIELD_NUMBER: builtins.int
    AUTHENTICATED_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def audiences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    authenticated: builtins.bool
    error: builtins.str
    @property
    def user(self) -> global___UserInfo: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        audiences: collections.abc.Iterable[builtins.str] | None = ...,
        authenticated: builtins.bool = ...,
        error: builtins.str = ...,
        user: global___UserInfo | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["audiences", b"audiences", "authenticated", b"authenticated", "error", b"error", "resource_info", b"resource_info", "user", b"user"]) -> None: ...

global___TokenReviewStatus = TokenReviewStatus

@typing_extensions.final
class UserInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ExtraEntry(google.protobuf.message.Message):
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

    EXTRA_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def extra(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    uid: builtins.str
    username: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        extra: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        groups: collections.abc.Iterable[builtins.str] | None = ...,
        uid: builtins.str = ...,
        username: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["extra", b"extra", "groups", b"groups", "resource_info", b"resource_info", "uid", b"uid", "username", b"username"]) -> None: ...

global___UserInfo = UserInfo
