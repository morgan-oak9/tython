"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import kubernetes.kubernetes_io.k8s.api.admissionregistration.v1_pb2
import kubernetes.kubernetes_io.k8s.api.certificates.v1_pb2
import kubernetes.kubernetes_io.k8s.api.core.v1_pb2
import kubernetes.kubernetes_io.k8s.api.networking.v1_pb2
import kubernetes.kubernetes_io.k8s.api.node.v1_pb2
import kubernetes.kubernetes_io.k8s.api.rbac.v1_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Kubernetes_NonNamespaced(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPONENT_STATUS_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    NODE_FIELD_NUMBER: builtins.int
    PERSISTENT_VOLUME_FIELD_NUMBER: builtins.int
    CERTIFICATE_SIGNING_REQUEST_FIELD_NUMBER: builtins.int
    MUTATING_WEBHOOK_CONFIGURATION_FIELD_NUMBER: builtins.int
    VALIDATING_WEBHOOK_CONFIGURATION_FIELD_NUMBER: builtins.int
    INGRESS_CLASS_FIELD_NUMBER: builtins.int
    RUNTIME_CLASS_FIELD_NUMBER: builtins.int
    CLUSTER_ROLE_BINDING_FIELD_NUMBER: builtins.int
    CLUSTER_ROLE_FIELD_NUMBER: builtins.int
    @property
    def component_status(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.ComponentStatus]: ...
    @property
    def namespace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.Namespace]: ...
    @property
    def node(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.Node]: ...
    @property
    def persistent_volume(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.PersistentVolume]: ...
    @property
    def certificate_signing_request(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.certificates.v1_pb2.CertificateSigningRequest]: ...
    @property
    def mutating_webhook_configuration(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.admissionregistration.v1_pb2.MutatingWebhookConfiguration]: ...
    @property
    def validating_webhook_configuration(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.admissionregistration.v1_pb2.ValidatingWebhookConfiguration]: ...
    @property
    def ingress_class(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.networking.v1_pb2.IngressClass]: ...
    @property
    def runtime_class(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.node.v1_pb2.RuntimeClass]: ...
    @property
    def cluster_role_binding(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.rbac.v1_pb2.ClusterRoleBinding]: ...
    @property
    def cluster_role(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[kubernetes.kubernetes_io.k8s.api.rbac.v1_pb2.ClusterRole]: ...
    def __init__(
        self,
        *,
        component_status: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.ComponentStatus] | None = ...,
        namespace: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.Namespace] | None = ...,
        node: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.Node] | None = ...,
        persistent_volume: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.core.v1_pb2.PersistentVolume] | None = ...,
        certificate_signing_request: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.certificates.v1_pb2.CertificateSigningRequest] | None = ...,
        mutating_webhook_configuration: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.admissionregistration.v1_pb2.MutatingWebhookConfiguration] | None = ...,
        validating_webhook_configuration: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.admissionregistration.v1_pb2.ValidatingWebhookConfiguration] | None = ...,
        ingress_class: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.networking.v1_pb2.IngressClass] | None = ...,
        runtime_class: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.node.v1_pb2.RuntimeClass] | None = ...,
        cluster_role_binding: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.rbac.v1_pb2.ClusterRoleBinding] | None = ...,
        cluster_role: collections.abc.Iterable[kubernetes.kubernetes_io.k8s.api.rbac.v1_pb2.ClusterRole] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["certificate_signing_request", b"certificate_signing_request", "cluster_role", b"cluster_role", "cluster_role_binding", b"cluster_role_binding", "component_status", b"component_status", "ingress_class", b"ingress_class", "mutating_webhook_configuration", b"mutating_webhook_configuration", "namespace", b"namespace", "node", b"node", "persistent_volume", b"persistent_volume", "runtime_class", b"runtime_class", "validating_webhook_configuration", b"validating_webhook_configuration"]) -> None: ...

global___Kubernetes_NonNamespaced = Kubernetes_NonNamespaced