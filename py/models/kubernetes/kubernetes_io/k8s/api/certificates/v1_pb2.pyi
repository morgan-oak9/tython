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
class CertificateSigningRequest(google.protobuf.message.Message):
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
    def spec(self) -> global___CertificateSigningRequestSpec: ...
    @property
    def status(self) -> global___CertificateSigningRequestStatus: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ObjectMeta | None = ...,
        spec: global___CertificateSigningRequestSpec | None = ...,
        status: global___CertificateSigningRequestStatus | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info", "spec", b"spec", "status", b"status"]) -> None: ...

global___CertificateSigningRequest = CertificateSigningRequest

@typing_extensions.final
class CertificateSigningRequestCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_TRANSITION_TIME_FIELD_NUMBER: builtins.int
    LAST_UPDATE_TIME_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def last_transition_time(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time: ...
    @property
    def last_update_time(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time: ...
    message: builtins.str
    reason: builtins.str
    status: builtins.str
    type: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        last_transition_time: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time | None = ...,
        last_update_time: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.Time | None = ...,
        message: builtins.str = ...,
        reason: builtins.str = ...,
        status: builtins.str = ...,
        type: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_transition_time", b"last_transition_time", "last_update_time", b"last_update_time", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_transition_time", b"last_transition_time", "last_update_time", b"last_update_time", "message", b"message", "reason", b"reason", "resource_info", b"resource_info", "status", b"status", "type", b"type"]) -> None: ...

global___CertificateSigningRequestCondition = CertificateSigningRequestCondition

@typing_extensions.final
class CertificateSigningRequestList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    API_VERSION_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    api_version: builtins.str
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CertificateSigningRequest]: ...
    kind: builtins.str
    @property
    def metadata(self) -> kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        api_version: builtins.str = ...,
        items: collections.abc.Iterable[global___CertificateSigningRequest] | None = ...,
        kind: builtins.str = ...,
        metadata: kubernetes.kubernetes_io.k8s.apimachinery.pkg.apis.meta.v1_pb2.ListMeta | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "items", b"items", "kind", b"kind", "metadata", b"metadata", "resource_info", b"resource_info"]) -> None: ...

global___CertificateSigningRequestList = CertificateSigningRequestList

@typing_extensions.final
class CertificateSigningRequestSpec(google.protobuf.message.Message):
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

    EXPIRATION_SECONDS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    GROUPS_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    SIGNER_NAME_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    USAGES_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    expiration_seconds: builtins.int
    @property
    def extra(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    request: builtins.str
    signer_name: builtins.str
    uid: builtins.str
    @property
    def usages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    username: builtins.str
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        expiration_seconds: builtins.int = ...,
        extra: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        groups: collections.abc.Iterable[builtins.str] | None = ...,
        request: builtins.str = ...,
        signer_name: builtins.str = ...,
        uid: builtins.str = ...,
        usages: collections.abc.Iterable[builtins.str] | None = ...,
        username: builtins.str = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiration_seconds", b"expiration_seconds", "extra", b"extra", "groups", b"groups", "request", b"request", "resource_info", b"resource_info", "signer_name", b"signer_name", "uid", b"uid", "usages", b"usages", "username", b"username"]) -> None: ...

global___CertificateSigningRequestSpec = CertificateSigningRequestSpec

@typing_extensions.final
class CertificateSigningRequestStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_FIELD_NUMBER: builtins.int
    CONDITIONS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    certificate: builtins.str
    @property
    def conditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CertificateSigningRequestCondition]: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        certificate: builtins.str = ...,
        conditions: collections.abc.Iterable[global___CertificateSigningRequestCondition] | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate", b"certificate", "conditions", b"conditions", "resource_info", b"resource_info"]) -> None: ...

global___CertificateSigningRequestStatus = CertificateSigningRequestStatus