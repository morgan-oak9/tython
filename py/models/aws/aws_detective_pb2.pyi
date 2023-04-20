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
class Graph(google.protobuf.message.Message):
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

global___Graph = Graph

@typing_extensions.final
class Detective(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRAPH_FIELD_NUMBER: builtins.int
    MEMBER_INVITATION_FIELD_NUMBER: builtins.int
    @property
    def graph(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Graph]: ...
    @property
    def member_invitation(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MemberInvitation]: ...
    def __init__(
        self,
        *,
        graph: collections.abc.Iterable[global___Graph] | None = ...,
        member_invitation: collections.abc.Iterable[global___MemberInvitation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["graph", b"graph", "member_invitation", b"member_invitation"]) -> None: ...

global___Detective = Detective

@typing_extensions.final
class MemberInvitation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    GRAPH_ARN_FIELD_NUMBER: builtins.int
    MEMBER_ID_FIELD_NUMBER: builtins.int
    MEMBER_EMAIL_ADDRESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    graph_arn: builtins.str
    member_id: builtins.str
    member_email_address: builtins.str
    message: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        graph_arn: builtins.str = ...,
        member_id: builtins.str = ...,
        member_email_address: builtins.str = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["graph_arn", b"graph_arn", "member_email_address", b"member_email_address", "member_id", b"member_id", "message", b"message", "resource_info", b"resource_info"]) -> None: ...

global___MemberInvitation = MemberInvitation
