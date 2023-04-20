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
class GkeHubMembershipXAuthority(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISSUER_FIELD_NUMBER: builtins.int
    issuer: builtins.str
    def __init__(
        self,
        *,
        issuer: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["issuer", b"issuer"]) -> None: ...

global___GkeHubMembershipXAuthority = GkeHubMembershipXAuthority

@typing_extensions.final
class GkeHubMembershipXEndpointXGkeCluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_LINK_FIELD_NUMBER: builtins.int
    resource_link: builtins.str
    def __init__(
        self,
        *,
        resource_link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_link", b"resource_link"]) -> None: ...

global___GkeHubMembershipXEndpointXGkeCluster = GkeHubMembershipXEndpointXGkeCluster

@typing_extensions.final
class GkeHubMembershipXEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GKE_CLUSTER_FIELD_NUMBER: builtins.int
    @property
    def gke_cluster(self) -> global___GkeHubMembershipXEndpointXGkeCluster: ...
    def __init__(
        self,
        *,
        gke_cluster: global___GkeHubMembershipXEndpointXGkeCluster | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gke_cluster", b"gke_cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gke_cluster", b"gke_cluster"]) -> None: ...

global___GkeHubMembershipXEndpoint = GkeHubMembershipXEndpoint

@typing_extensions.final
class GkeHubMembershipXTimeouts(google.protobuf.message.Message):
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

global___GkeHubMembershipXTimeouts = GkeHubMembershipXTimeouts

@typing_extensions.final
class GkeHubMembership(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MEMBERSHIP_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    AUTHORITY_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    membership_id: builtins.str
    name: builtins.str
    project: builtins.str
    @property
    def authority(self) -> global___GkeHubMembershipXAuthority: ...
    @property
    def endpoint(self) -> global___GkeHubMembershipXEndpoint: ...
    @property
    def timeouts(self) -> global___GkeHubMembershipXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        membership_id: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        authority: global___GkeHubMembershipXAuthority | None = ...,
        endpoint: global___GkeHubMembershipXEndpoint | None = ...,
        timeouts: global___GkeHubMembershipXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["authority", b"authority", "endpoint", b"endpoint", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authority", b"authority", "endpoint", b"endpoint", "id", b"id", "labels", b"labels", "membership_id", b"membership_id", "name", b"name", "project", b"project", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> None: ...

global___GkeHubMembership = GkeHubMembership