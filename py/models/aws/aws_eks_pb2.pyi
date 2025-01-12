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
class ClusterProvider(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_ARN_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key_arn: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key_arn: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_arn", b"key_arn", "resource_info", b"resource_info"]) -> None: ...

global___ClusterProvider = ClusterProvider

@typing_extensions.final
class ClusterEncryptionConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    PROVIDER_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def provider(self) -> global___ClusterProvider: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        resources: collections.abc.Iterable[builtins.str] | None = ...,
        provider: global___ClusterProvider | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["provider", b"provider", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["provider", b"provider", "resource_info", b"resource_info", "resources", b"resources"]) -> None: ...

global___ClusterEncryptionConfig = ClusterEncryptionConfig

@typing_extensions.final
class ClusterResourcesVpcConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    PUBLIC_ACCESS_CIDRS_FIELD_NUMBER: builtins.int
    ENDPOINT_PRIVATE_ACCESS_FIELD_NUMBER: builtins.int
    ENDPOINT_PUBLIC_ACCESS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def public_access_cidrs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    endpoint_private_access: builtins.bool
    endpoint_public_access: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
        public_access_cidrs: collections.abc.Iterable[builtins.str] | None = ...,
        endpoint_private_access: builtins.bool = ...,
        endpoint_public_access: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_private_access", b"endpoint_private_access", "endpoint_public_access", b"endpoint_public_access", "public_access_cidrs", b"public_access_cidrs", "resource_info", b"resource_info", "security_group_ids", b"security_group_ids", "subnet_ids", b"subnet_ids"]) -> None: ...

global___ClusterResourcesVpcConfig = ClusterResourcesVpcConfig

@typing_extensions.final
class ClusterKubernetesNetworkConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SERVICE_IPV4_CIDR_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    service_ipv4_cidr: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        service_ipv4_cidr: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "service_ipv4_cidr", b"service_ipv4_cidr"]) -> None: ...

global___ClusterKubernetesNetworkConfig = ClusterKubernetesNetworkConfig

@typing_extensions.final
class Cluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ENCRYPTION_CONFIG_FIELD_NUMBER: builtins.int
    ROLE_ARN_FIELD_NUMBER: builtins.int
    RESOURCES_VPC_CONFIG_FIELD_NUMBER: builtins.int
    KUBERNETES_NETWORK_CONFIG_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    version: builtins.str
    @property
    def encryption_config(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClusterEncryptionConfig]: ...
    role_arn: builtins.str
    @property
    def resources_vpc_config(self) -> global___ClusterResourcesVpcConfig: ...
    @property
    def kubernetes_network_config(self) -> global___ClusterKubernetesNetworkConfig: ...
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        version: builtins.str = ...,
        encryption_config: collections.abc.Iterable[global___ClusterEncryptionConfig] | None = ...,
        role_arn: builtins.str = ...,
        resources_vpc_config: global___ClusterResourcesVpcConfig | None = ...,
        kubernetes_network_config: global___ClusterKubernetesNetworkConfig | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["kubernetes_network_config", b"kubernetes_network_config", "resource_info", b"resource_info", "resources_vpc_config", b"resources_vpc_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["encryption_config", b"encryption_config", "kubernetes_network_config", b"kubernetes_network_config", "name", b"name", "resource_info", b"resource_info", "resources_vpc_config", b"resources_vpc_config", "role_arn", b"role_arn", "version", b"version"]) -> None: ...

global___Cluster = Cluster

@typing_extensions.final
class EKS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_FIELD_NUMBER: builtins.int
    FARGATE_PROFILE_FIELD_NUMBER: builtins.int
    NODEGROUP_FIELD_NUMBER: builtins.int
    @property
    def cluster(self) -> global___Cluster: ...
    @property
    def fargate_profile(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FargateProfile]: ...
    @property
    def nodegroup(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Nodegroup]: ...
    def __init__(
        self,
        *,
        cluster: global___Cluster | None = ...,
        fargate_profile: collections.abc.Iterable[global___FargateProfile] | None = ...,
        nodegroup: collections.abc.Iterable[global___Nodegroup] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cluster", b"cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "fargate_profile", b"fargate_profile", "nodegroup", b"nodegroup"]) -> None: ...

global___EKS = EKS

@typing_extensions.final
class FargateProfileLabel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "resource_info", b"resource_info", "value", b"value"]) -> None: ...

global___FargateProfileLabel = FargateProfileLabel

@typing_extensions.final
class FargateProfileSelector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    namespace: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FargateProfileLabel]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        namespace: builtins.str = ...,
        labels: collections.abc.Iterable[global___FargateProfileLabel] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["labels", b"labels", "namespace", b"namespace", "resource_info", b"resource_info"]) -> None: ...

global___FargateProfileSelector = FargateProfileSelector

@typing_extensions.final
class FargateProfile(google.protobuf.message.Message):
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
    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    FARGATE_PROFILE_NAME_FIELD_NUMBER: builtins.int
    POD_EXECUTION_ROLE_ARN_FIELD_NUMBER: builtins.int
    SUBNETS_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    cluster_name: builtins.str
    fargate_profile_name: builtins.str
    pod_execution_role_arn: builtins.str
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def selectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FargateProfileSelector]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        cluster_name: builtins.str = ...,
        fargate_profile_name: builtins.str = ...,
        pod_execution_role_arn: builtins.str = ...,
        subnets: collections.abc.Iterable[builtins.str] | None = ...,
        selectors: collections.abc.Iterable[global___FargateProfileSelector] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_name", b"cluster_name", "fargate_profile_name", b"fargate_profile_name", "pod_execution_role_arn", b"pod_execution_role_arn", "resource_info", b"resource_info", "selectors", b"selectors", "subnets", b"subnets", "tags", b"tags"]) -> None: ...

global___FargateProfile = FargateProfile

@typing_extensions.final
class NodegroupScalingConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    MIN_SIZE_FIELD_NUMBER: builtins.int
    DESIRED_SIZE_FIELD_NUMBER: builtins.int
    MAX_SIZE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    min_size: builtins.float
    desired_size: builtins.float
    max_size: builtins.float
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        min_size: builtins.float = ...,
        desired_size: builtins.float = ...,
        max_size: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["desired_size", b"desired_size", "max_size", b"max_size", "min_size", b"min_size", "resource_info", b"resource_info"]) -> None: ...

global___NodegroupScalingConfig = NodegroupScalingConfig

@typing_extensions.final
class NodegroupLaunchTemplateSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    version: builtins.str
    id: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        version: builtins.str = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "resource_info", b"resource_info", "version", b"version"]) -> None: ...

global___NodegroupLaunchTemplateSpecification = NodegroupLaunchTemplateSpecification

@typing_extensions.final
class NodegroupRemoteAccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    SOURCE_SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    EC2_SSH_KEY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def source_security_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    ec2_ssh_key: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        source_security_groups: collections.abc.Iterable[builtins.str] | None = ...,
        ec2_ssh_key: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ec2_ssh_key", b"ec2_ssh_key", "resource_info", b"resource_info", "source_security_groups", b"source_security_groups"]) -> None: ...

global___NodegroupRemoteAccess = NodegroupRemoteAccess

@typing_extensions.final
class Nodegroup(google.protobuf.message.Message):
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
    SCALING_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RELEASE_VERSION_FIELD_NUMBER: builtins.int
    NODEGROUP_NAME_FIELD_NUMBER: builtins.int
    SUBNETS_FIELD_NUMBER: builtins.int
    NODE_ROLE_FIELD_NUMBER: builtins.int
    AMI_TYPE_FIELD_NUMBER: builtins.int
    FORCE_UPDATE_ENABLED_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    LAUNCH_TEMPLATE_FIELD_NUMBER: builtins.int
    REMOTE_ACCESS_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    INSTANCE_TYPES_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def scaling_config(self) -> global___NodegroupScalingConfig: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    release_version: builtins.str
    nodegroup_name: builtins.str
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    node_role: builtins.str
    ami_type: builtins.str
    force_update_enabled: builtins.bool
    version: builtins.str
    @property
    def launch_template(self) -> global___NodegroupLaunchTemplateSpecification: ...
    @property
    def remote_access(self) -> global___NodegroupRemoteAccess: ...
    disk_size: builtins.float
    cluster_name: builtins.str
    @property
    def instance_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        scaling_config: global___NodegroupScalingConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        release_version: builtins.str = ...,
        nodegroup_name: builtins.str = ...,
        subnets: collections.abc.Iterable[builtins.str] | None = ...,
        node_role: builtins.str = ...,
        ami_type: builtins.str = ...,
        force_update_enabled: builtins.bool = ...,
        version: builtins.str = ...,
        launch_template: global___NodegroupLaunchTemplateSpecification | None = ...,
        remote_access: global___NodegroupRemoteAccess | None = ...,
        disk_size: builtins.float = ...,
        cluster_name: builtins.str = ...,
        instance_types: collections.abc.Iterable[builtins.str] | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["launch_template", b"launch_template", "remote_access", b"remote_access", "resource_info", b"resource_info", "scaling_config", b"scaling_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ami_type", b"ami_type", "cluster_name", b"cluster_name", "disk_size", b"disk_size", "force_update_enabled", b"force_update_enabled", "instance_types", b"instance_types", "labels", b"labels", "launch_template", b"launch_template", "node_role", b"node_role", "nodegroup_name", b"nodegroup_name", "release_version", b"release_version", "remote_access", b"remote_access", "resource_info", b"resource_info", "scaling_config", b"scaling_config", "subnets", b"subnets", "tags", b"tags", "version", b"version"]) -> None: ...

global___Nodegroup = Nodegroup
