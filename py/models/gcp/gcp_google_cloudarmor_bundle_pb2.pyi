"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import gcp.gcp_compute_security_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GoogleCloudarmor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_SECURITY_POLICY_FIELD_NUMBER: builtins.int
    @property
    def compute_security_policy(self) -> gcp.gcp_compute_security_pb2.ComputeSecurityPolicy: ...
    def __init__(
        self,
        *,
        compute_security_policy: gcp.gcp_compute_security_pb2.ComputeSecurityPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compute_security_policy", b"compute_security_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_security_policy", b"compute_security_policy"]) -> None: ...

global___GoogleCloudarmor = GoogleCloudarmor
