"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import gcp.gcp_compute_firewall_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GoogleComputeFirewallPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_FIREWALL_POLICY_FIELD_NUMBER: builtins.int
    COMPUTE_FIREWALL_POLICY_ASSOCIATION_FIELD_NUMBER: builtins.int
    COMPUTE_FIREWALL_POLICY_RULE_FIELD_NUMBER: builtins.int
    @property
    def compute_firewall_policy(self) -> gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicy: ...
    @property
    def compute_firewall_policy_association(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicyAssociation]: ...
    @property
    def compute_firewall_policy_rule(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicyRule]: ...
    def __init__(
        self,
        *,
        compute_firewall_policy: gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicy | None = ...,
        compute_firewall_policy_association: collections.abc.Iterable[gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicyAssociation] | None = ...,
        compute_firewall_policy_rule: collections.abc.Iterable[gcp.gcp_compute_firewall_pb2.ComputeFirewallPolicyRule] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compute_firewall_policy", b"compute_firewall_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_firewall_policy", b"compute_firewall_policy", "compute_firewall_policy_association", b"compute_firewall_policy_association", "compute_firewall_policy_rule", b"compute_firewall_policy_rule"]) -> None: ...

global___GoogleComputeFirewallPolicy = GoogleComputeFirewallPolicy
