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
class RepositoryAssociation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    CONNECTION_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    type: builtins.str
    owner: builtins.str
    connection_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        type: builtins.str = ...,
        owner: builtins.str = ...,
        connection_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connection_arn", b"connection_arn", "name", b"name", "owner", b"owner", "resource_info", b"resource_info", "type", b"type"]) -> None: ...

global___RepositoryAssociation = RepositoryAssociation

@typing_extensions.final
class CodeGuruReviewer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REPOSITORY_ASSOCIATION_FIELD_NUMBER: builtins.int
    @property
    def repository_association(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RepositoryAssociation]: ...
    def __init__(
        self,
        *,
        repository_association: collections.abc.Iterable[global___RepositoryAssociation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["repository_association", b"repository_association"]) -> None: ...

global___CodeGuruReviewer = CodeGuruReviewer