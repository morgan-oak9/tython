"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import gcp.gcp_dns_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GoogleDns(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DNS_MANAGED_ZONE_FIELD_NUMBER: builtins.int
    DNS_POLICY_FIELD_NUMBER: builtins.int
    DNS_RECORD_SET_FIELD_NUMBER: builtins.int
    @property
    def dns_managed_zone(self) -> gcp.gcp_dns_pb2.DnsManagedZone: ...
    @property
    def dns_policy(self) -> gcp.gcp_dns_pb2.DnsPolicy: ...
    @property
    def dns_record_set(self) -> gcp.gcp_dns_pb2.DnsRecordSet: ...
    def __init__(
        self,
        *,
        dns_managed_zone: gcp.gcp_dns_pb2.DnsManagedZone | None = ...,
        dns_policy: gcp.gcp_dns_pb2.DnsPolicy | None = ...,
        dns_record_set: gcp.gcp_dns_pb2.DnsRecordSet | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dns_managed_zone", b"dns_managed_zone", "dns_policy", b"dns_policy", "dns_record_set", b"dns_record_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dns_managed_zone", b"dns_managed_zone", "dns_policy", b"dns_policy", "dns_record_set", b"dns_record_set"]) -> None: ...

global___GoogleDns = GoogleDns
