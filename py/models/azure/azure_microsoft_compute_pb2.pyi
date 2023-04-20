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
class Microsoft_Compute(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AVAILABILITY_SETS_FIELD_NUMBER: builtins.int
    CAPACITY_RESERVATION_GROUPS_FIELD_NUMBER: builtins.int
    HOST_GROUPS_FIELD_NUMBER: builtins.int
    IMAGES_FIELD_NUMBER: builtins.int
    PROXIMITY_PLACEMENT_GROUPS_FIELD_NUMBER: builtins.int
    RESTORE_POINT_COLLECTIONS_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEYS_FIELD_NUMBER: builtins.int
    @property
    def availability_sets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AvailabilitySets]: ...
    @property
    def capacity_reservation_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CapacityReservationGroups]: ...
    @property
    def host_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HostGroups]: ...
    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Images]: ...
    @property
    def proximity_placement_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProximityPlacementGroups]: ...
    @property
    def restore_point_collections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RestorePointCollections]: ...
    @property
    def ssh_public_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SshPublicKeys]: ...
    def __init__(
        self,
        *,
        availability_sets: collections.abc.Iterable[global___AvailabilitySets] | None = ...,
        capacity_reservation_groups: collections.abc.Iterable[global___CapacityReservationGroups] | None = ...,
        host_groups: collections.abc.Iterable[global___HostGroups] | None = ...,
        images: collections.abc.Iterable[global___Images] | None = ...,
        proximity_placement_groups: collections.abc.Iterable[global___ProximityPlacementGroups] | None = ...,
        restore_point_collections: collections.abc.Iterable[global___RestorePointCollections] | None = ...,
        ssh_public_keys: collections.abc.Iterable[global___SshPublicKeys] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["availability_sets", b"availability_sets", "capacity_reservation_groups", b"capacity_reservation_groups", "host_groups", b"host_groups", "images", b"images", "proximity_placement_groups", b"proximity_placement_groups", "restore_point_collections", b"restore_point_collections", "ssh_public_keys", b"ssh_public_keys"]) -> None: ...

global___Microsoft_Compute = Microsoft_Compute

@typing_extensions.final
class SshPublicKeys(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    public_key: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        public_key: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "name", b"name", "public_key", b"public_key", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___SshPublicKeys = SshPublicKeys

@typing_extensions.final
class RestorePointCollectionsRestorePoints(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    EXCLUDE_DISKS_FIELD_NUMBER: builtins.int
    SOURCE_RESTORE_POINT_FIELD_NUMBER: builtins.int
    TIME_CREATED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    name: builtins.str
    @property
    def exclude_disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiEntityReference]: ...
    @property
    def source_restore_point(self) -> global___ApiEntityReference: ...
    time_created: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        name: builtins.str = ...,
        exclude_disks: collections.abc.Iterable[global___ApiEntityReference] | None = ...,
        source_restore_point: global___ApiEntityReference | None = ...,
        time_created: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "source_restore_point", b"source_restore_point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exclude_disks", b"exclude_disks", "name", b"name", "resource_info", b"resource_info", "source_restore_point", b"source_restore_point", "time_created", b"time_created"]) -> None: ...

global___RestorePointCollectionsRestorePoints = RestorePointCollectionsRestorePoints

@typing_extensions.final
class ApiEntityReference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___ApiEntityReference = ApiEntityReference

@typing_extensions.final
class RestorePointCollections(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    RESTORE_POINT_COLLECTIONS_RESTORE_POINTS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    @property
    def source(self) -> global___RestorePointCollectionSourceProperties: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def restore_point_collections_restore_points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RestorePointCollectionsRestorePoints]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        source: global___RestorePointCollectionSourceProperties | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        restore_point_collections_restore_points: collections.abc.Iterable[global___RestorePointCollectionsRestorePoints] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "name", b"name", "resource_info", b"resource_info", "restore_point_collections_restore_points", b"restore_point_collections_restore_points", "source", b"source", "tags", b"tags"]) -> None: ...

global___RestorePointCollections = RestorePointCollections

@typing_extensions.final
class RestorePointCollectionSourceProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___RestorePointCollectionSourceProperties = RestorePointCollectionSourceProperties

@typing_extensions.final
class ProximityPlacementGroups(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    COLOCATION_STATUS_FIELD_NUMBER: builtins.int
    PROXIMITY_PLACEMENT_GROUP_TYPE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    @property
    def colocation_status(self) -> global___InstanceViewStatus: ...
    proximity_placement_group_type: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        colocation_status: global___InstanceViewStatus | None = ...,
        proximity_placement_group_type: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["colocation_status", b"colocation_status", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["colocation_status", b"colocation_status", "location", b"location", "name", b"name", "proximity_placement_group_type", b"proximity_placement_group_type", "resource_info", b"resource_info", "tags", b"tags"]) -> None: ...

global___ProximityPlacementGroups = ProximityPlacementGroups

@typing_extensions.final
class InstanceViewStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    DISPLAY_STATUS_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    code: builtins.str
    display_status: builtins.str
    level: builtins.str
    message: builtins.str
    time: builtins.str
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        display_status: builtins.str = ...,
        level: builtins.str = ...,
        message: builtins.str = ...,
        time: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "display_status", b"display_status", "level", b"level", "message", b"message", "time", b"time"]) -> None: ...

global___InstanceViewStatus = InstanceViewStatus

@typing_extensions.final
class Images(google.protobuf.message.Message):
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
    EXTENDED_LOCATION_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    HYPER_V_GENERATION_FIELD_NUMBER: builtins.int
    SOURCE_VIRTUAL_MACHINE_FIELD_NUMBER: builtins.int
    STORAGE_PROFILE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def extended_location(self) -> global___ExtendedLocation: ...
    location: builtins.str
    name: builtins.str
    hyper_v_generation: builtins.str
    source_virtual_machine: builtins.str
    @property
    def storage_profile(self) -> global___ImageStorageProfile: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        extended_location: global___ExtendedLocation | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        hyper_v_generation: builtins.str = ...,
        source_virtual_machine: builtins.str = ...,
        storage_profile: global___ImageStorageProfile | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extended_location", b"extended_location", "resource_info", b"resource_info", "storage_profile", b"storage_profile"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["extended_location", b"extended_location", "hyper_v_generation", b"hyper_v_generation", "location", b"location", "name", b"name", "resource_info", b"resource_info", "source_virtual_machine", b"source_virtual_machine", "storage_profile", b"storage_profile", "tags", b"tags"]) -> None: ...

global___Images = Images

@typing_extensions.final
class ImageStorageProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_DISKS_FIELD_NUMBER: builtins.int
    OS_DISK_FIELD_NUMBER: builtins.int
    ZONE_RESILIENT_FIELD_NUMBER: builtins.int
    @property
    def data_disks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ImageDataDisk]: ...
    @property
    def os_disk(self) -> global___ImageOSDisk: ...
    zone_resilient: builtins.bool
    def __init__(
        self,
        *,
        data_disks: collections.abc.Iterable[global___ImageDataDisk] | None = ...,
        os_disk: global___ImageOSDisk | None = ...,
        zone_resilient: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["os_disk", b"os_disk"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_disks", b"data_disks", "os_disk", b"os_disk", "zone_resilient", b"zone_resilient"]) -> None: ...

global___ImageStorageProfile = ImageStorageProfile

@typing_extensions.final
class ImageOSDisk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOB_URI_FIELD_NUMBER: builtins.int
    CACHING_FIELD_NUMBER: builtins.int
    DISK_ENCRYPTION_SET_FIELD_NUMBER: builtins.int
    DISK_SIZE_GB_FIELD_NUMBER: builtins.int
    MANAGED_DISK_FIELD_NUMBER: builtins.int
    OS_STATE_FIELD_NUMBER: builtins.int
    OS_TYPE_FIELD_NUMBER: builtins.int
    SNAPSHOT_FIELD_NUMBER: builtins.int
    STORAGE_ACCOUNT_TYPE_FIELD_NUMBER: builtins.int
    blob_uri: builtins.str
    caching: builtins.str
    @property
    def disk_encryption_set(self) -> global___DiskEncryptionSetParameters: ...
    disk_size_gb: builtins.int
    managed_disk: builtins.str
    os_state: builtins.str
    os_type: builtins.str
    snapshot: builtins.str
    storage_account_type: builtins.str
    def __init__(
        self,
        *,
        blob_uri: builtins.str = ...,
        caching: builtins.str = ...,
        disk_encryption_set: global___DiskEncryptionSetParameters | None = ...,
        disk_size_gb: builtins.int = ...,
        managed_disk: builtins.str = ...,
        os_state: builtins.str = ...,
        os_type: builtins.str = ...,
        snapshot: builtins.str = ...,
        storage_account_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disk_encryption_set", b"disk_encryption_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blob_uri", b"blob_uri", "caching", b"caching", "disk_encryption_set", b"disk_encryption_set", "disk_size_gb", b"disk_size_gb", "managed_disk", b"managed_disk", "os_state", b"os_state", "os_type", b"os_type", "snapshot", b"snapshot", "storage_account_type", b"storage_account_type"]) -> None: ...

global___ImageOSDisk = ImageOSDisk

@typing_extensions.final
class ImageDataDisk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOB_URI_FIELD_NUMBER: builtins.int
    CACHING_FIELD_NUMBER: builtins.int
    DISK_ENCRYPTION_SET_FIELD_NUMBER: builtins.int
    DISK_SIZE_GB_FIELD_NUMBER: builtins.int
    LUN_FIELD_NUMBER: builtins.int
    MANAGED_DISK_FIELD_NUMBER: builtins.int
    SNAPSHOT_FIELD_NUMBER: builtins.int
    STORAGE_ACCOUNT_TYPE_FIELD_NUMBER: builtins.int
    blob_uri: builtins.str
    caching: builtins.str
    @property
    def disk_encryption_set(self) -> global___DiskEncryptionSetParameters: ...
    disk_size_gb: builtins.int
    lun: builtins.int
    managed_disk: builtins.str
    snapshot: builtins.str
    storage_account_type: builtins.str
    def __init__(
        self,
        *,
        blob_uri: builtins.str = ...,
        caching: builtins.str = ...,
        disk_encryption_set: global___DiskEncryptionSetParameters | None = ...,
        disk_size_gb: builtins.int = ...,
        lun: builtins.int = ...,
        managed_disk: builtins.str = ...,
        snapshot: builtins.str = ...,
        storage_account_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disk_encryption_set", b"disk_encryption_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blob_uri", b"blob_uri", "caching", b"caching", "disk_encryption_set", b"disk_encryption_set", "disk_size_gb", b"disk_size_gb", "lun", b"lun", "managed_disk", b"managed_disk", "snapshot", b"snapshot", "storage_account_type", b"storage_account_type"]) -> None: ...

global___ImageDataDisk = ImageDataDisk

@typing_extensions.final
class DiskEncryptionSetParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___DiskEncryptionSetParameters = DiskEncryptionSetParameters

@typing_extensions.final
class ExtendedLocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    type: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "type", b"type"]) -> None: ...

global___ExtendedLocation = ExtendedLocation

@typing_extensions.final
class HostGroupsHosts(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AUTO_REPLACE_ON_FAILURE_FIELD_NUMBER: builtins.int
    LICENSE_TYPE_FIELD_NUMBER: builtins.int
    PLATFORM_FAULT_DOMAIN_FIELD_NUMBER: builtins.int
    SKU_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    auto_replace_on_failure: builtins.bool
    license_type: builtins.str
    platform_fault_domain: builtins.int
    @property
    def sku(self) -> global___Sku: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        auto_replace_on_failure: builtins.bool = ...,
        license_type: builtins.str = ...,
        platform_fault_domain: builtins.int = ...,
        sku: global___Sku | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sku", b"sku"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_replace_on_failure", b"auto_replace_on_failure", "license_type", b"license_type", "location", b"location", "name", b"name", "platform_fault_domain", b"platform_fault_domain", "resource_info", b"resource_info", "sku", b"sku", "tags", b"tags"]) -> None: ...

global___HostGroupsHosts = HostGroupsHosts

@typing_extensions.final
class HostGroups(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PLATFORM_FAULT_DOMAIN_COUNT_FIELD_NUMBER: builtins.int
    SUPPORT_AUTOMATIC_PLACEMENT_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ZONES_FIELD_NUMBER: builtins.int
    HOST_GROUPS_HOSTS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    platform_fault_domain_count: builtins.int
    support_automatic_placement: builtins.bool
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def zones(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def host_groups_hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HostGroupsHosts]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        platform_fault_domain_count: builtins.int = ...,
        support_automatic_placement: builtins.bool = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zones: collections.abc.Iterable[builtins.str] | None = ...,
        host_groups_hosts: collections.abc.Iterable[global___HostGroupsHosts] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_groups_hosts", b"host_groups_hosts", "location", b"location", "name", b"name", "platform_fault_domain_count", b"platform_fault_domain_count", "resource_info", b"resource_info", "support_automatic_placement", b"support_automatic_placement", "tags", b"tags", "zones", b"zones"]) -> None: ...

global___HostGroups = HostGroups

@typing_extensions.final
class CapacityReservationGroupsCapacityReservations(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SKU_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ZONES_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    @property
    def sku(self) -> global___Sku: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def zones(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        sku: global___Sku | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zones: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sku", b"sku"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "name", b"name", "resource_info", b"resource_info", "sku", b"sku", "tags", b"tags", "zones", b"zones"]) -> None: ...

global___CapacityReservationGroupsCapacityReservations = CapacityReservationGroupsCapacityReservations

@typing_extensions.final
class CapacityReservationGroups(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ZONES_FIELD_NUMBER: builtins.int
    CAPACITY_RESERVATION_GROUPS_CAPACITY_RESERVATIONS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def zones(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def capacity_reservation_groups_capacity_reservations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CapacityReservationGroupsCapacityReservations]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zones: collections.abc.Iterable[builtins.str] | None = ...,
        capacity_reservation_groups_capacity_reservations: collections.abc.Iterable[global___CapacityReservationGroupsCapacityReservations] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["capacity_reservation_groups_capacity_reservations", b"capacity_reservation_groups_capacity_reservations", "location", b"location", "name", b"name", "resource_info", b"resource_info", "tags", b"tags", "zones", b"zones"]) -> None: ...

global___CapacityReservationGroups = CapacityReservationGroups

@typing_extensions.final
class AvailabilitySets(google.protobuf.message.Message):
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
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PLATFORM_FAULT_DOMAIN_COUNT_FIELD_NUMBER: builtins.int
    PLATFORM_UPDATE_DOMAIN_COUNT_FIELD_NUMBER: builtins.int
    PROXIMITY_PLACEMENT_GROUP_FIELD_NUMBER: builtins.int
    VIRTUAL_MACHINES_FIELD_NUMBER: builtins.int
    SKU_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    location: builtins.str
    name: builtins.str
    platform_fault_domain_count: builtins.int
    platform_update_domain_count: builtins.int
    proximity_placement_group: builtins.str
    @property
    def virtual_machines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def sku(self) -> global___Sku: ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        platform_fault_domain_count: builtins.int = ...,
        platform_update_domain_count: builtins.int = ...,
        proximity_placement_group: builtins.str = ...,
        virtual_machines: collections.abc.Iterable[builtins.str] | None = ...,
        sku: global___Sku | None = ...,
        tags: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "sku", b"sku"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "name", b"name", "platform_fault_domain_count", b"platform_fault_domain_count", "platform_update_domain_count", b"platform_update_domain_count", "proximity_placement_group", b"proximity_placement_group", "resource_info", b"resource_info", "sku", b"sku", "tags", b"tags", "virtual_machines", b"virtual_machines"]) -> None: ...

global___AvailabilitySets = AvailabilitySets

@typing_extensions.final
class Sku(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAPACITY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    capacity: builtins.int
    name: builtins.str
    tier: builtins.str
    def __init__(
        self,
        *,
        capacity: builtins.int = ...,
        name: builtins.str = ...,
        tier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["capacity", b"capacity", "name", b"name", "tier", b"tier"]) -> None: ...

global___Sku = Sku