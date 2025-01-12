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
class DataplexLakeXMetastore(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_FIELD_NUMBER: builtins.int
    service: builtins.str
    def __init__(
        self,
        *,
        service: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["service", b"service"]) -> None: ...

global___DataplexLakeXMetastore = DataplexLakeXMetastore

@typing_extensions.final
class DataplexLakeXTimeouts(google.protobuf.message.Message):
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

global___DataplexLakeXTimeouts = DataplexLakeXTimeouts

@typing_extensions.final
class DataplexLake(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AssetStatusEntry(google.protobuf.message.Message):
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
    class MetastoreStatusEntry(google.protobuf.message.Message):
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

    ASSET_STATUS_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    METASTORE_STATUS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    METASTORE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def asset_status(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    create_time: builtins.str
    description: builtins.str
    display_name: builtins.str
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    location: builtins.str
    @property
    def metastore_status(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    name: builtins.str
    project: builtins.str
    service_account: builtins.str
    state: builtins.str
    uid: builtins.str
    update_time: builtins.str
    @property
    def metastore(self) -> global___DataplexLakeXMetastore: ...
    @property
    def timeouts(self) -> global___DataplexLakeXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        asset_status: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        create_time: builtins.str = ...,
        description: builtins.str = ...,
        display_name: builtins.str = ...,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        location: builtins.str = ...,
        metastore_status: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        service_account: builtins.str = ...,
        state: builtins.str = ...,
        uid: builtins.str = ...,
        update_time: builtins.str = ...,
        metastore: global___DataplexLakeXMetastore | None = ...,
        timeouts: global___DataplexLakeXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metastore", b"metastore", "resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_status", b"asset_status", "create_time", b"create_time", "description", b"description", "display_name", b"display_name", "id", b"id", "labels", b"labels", "location", b"location", "metastore", b"metastore", "metastore_status", b"metastore_status", "name", b"name", "project", b"project", "resource_info", b"resource_info", "service_account", b"service_account", "state", b"state", "timeouts", b"timeouts", "uid", b"uid", "update_time", b"update_time"]) -> None: ...

global___DataplexLake = DataplexLake

@typing_extensions.final
class DataplexZoneXDiscoverySpecXCsvOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELIMITER_FIELD_NUMBER: builtins.int
    DISABLE_TYPE_INFERENCE_FIELD_NUMBER: builtins.int
    ENCODING_FIELD_NUMBER: builtins.int
    HEADER_ROWS_FIELD_NUMBER: builtins.int
    delimiter: builtins.str
    disable_type_inference: builtins.bool
    encoding: builtins.str
    header_rows: builtins.float
    def __init__(
        self,
        *,
        delimiter: builtins.str = ...,
        disable_type_inference: builtins.bool = ...,
        encoding: builtins.str = ...,
        header_rows: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delimiter", b"delimiter", "disable_type_inference", b"disable_type_inference", "encoding", b"encoding", "header_rows", b"header_rows"]) -> None: ...

global___DataplexZoneXDiscoverySpecXCsvOptions = DataplexZoneXDiscoverySpecXCsvOptions

@typing_extensions.final
class DataplexZoneXDiscoverySpecXJsonOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISABLE_TYPE_INFERENCE_FIELD_NUMBER: builtins.int
    ENCODING_FIELD_NUMBER: builtins.int
    disable_type_inference: builtins.bool
    encoding: builtins.str
    def __init__(
        self,
        *,
        disable_type_inference: builtins.bool = ...,
        encoding: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disable_type_inference", b"disable_type_inference", "encoding", b"encoding"]) -> None: ...

global___DataplexZoneXDiscoverySpecXJsonOptions = DataplexZoneXDiscoverySpecXJsonOptions

@typing_extensions.final
class DataplexZoneXDiscoverySpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    EXCLUDE_PATTERNS_FIELD_NUMBER: builtins.int
    INCLUDE_PATTERNS_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    CSV_OPTIONS_FIELD_NUMBER: builtins.int
    JSON_OPTIONS_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    @property
    def exclude_patterns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def include_patterns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    schedule: builtins.str
    @property
    def csv_options(self) -> global___DataplexZoneXDiscoverySpecXCsvOptions: ...
    @property
    def json_options(self) -> global___DataplexZoneXDiscoverySpecXJsonOptions: ...
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        exclude_patterns: collections.abc.Iterable[builtins.str] | None = ...,
        include_patterns: collections.abc.Iterable[builtins.str] | None = ...,
        schedule: builtins.str = ...,
        csv_options: global___DataplexZoneXDiscoverySpecXCsvOptions | None = ...,
        json_options: global___DataplexZoneXDiscoverySpecXJsonOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["csv_options", b"csv_options", "json_options", b"json_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["csv_options", b"csv_options", "enabled", b"enabled", "exclude_patterns", b"exclude_patterns", "include_patterns", b"include_patterns", "json_options", b"json_options", "schedule", b"schedule"]) -> None: ...

global___DataplexZoneXDiscoverySpec = DataplexZoneXDiscoverySpec

@typing_extensions.final
class DataplexZoneXResourceSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_TYPE_FIELD_NUMBER: builtins.int
    location_type: builtins.str
    def __init__(
        self,
        *,
        location_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["location_type", b"location_type"]) -> None: ...

global___DataplexZoneXResourceSpec = DataplexZoneXResourceSpec

@typing_extensions.final
class DataplexZoneXTimeouts(google.protobuf.message.Message):
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

global___DataplexZoneXTimeouts = DataplexZoneXTimeouts

@typing_extensions.final
class DataplexZone(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AssetStatusEntry(google.protobuf.message.Message):
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

    ASSET_STATUS_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    LAKE_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    DISCOVERY_SPEC_FIELD_NUMBER: builtins.int
    RESOURCE_SPEC_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def asset_status(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    create_time: builtins.str
    description: builtins.str
    display_name: builtins.str
    id: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    lake: builtins.str
    location: builtins.str
    name: builtins.str
    project: builtins.str
    state: builtins.str
    type: builtins.str
    uid: builtins.str
    update_time: builtins.str
    @property
    def discovery_spec(self) -> global___DataplexZoneXDiscoverySpec: ...
    @property
    def resource_spec(self) -> global___DataplexZoneXResourceSpec: ...
    @property
    def timeouts(self) -> global___DataplexZoneXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        asset_status: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        create_time: builtins.str = ...,
        description: builtins.str = ...,
        display_name: builtins.str = ...,
        id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        lake: builtins.str = ...,
        location: builtins.str = ...,
        name: builtins.str = ...,
        project: builtins.str = ...,
        state: builtins.str = ...,
        type: builtins.str = ...,
        uid: builtins.str = ...,
        update_time: builtins.str = ...,
        discovery_spec: global___DataplexZoneXDiscoverySpec | None = ...,
        resource_spec: global___DataplexZoneXResourceSpec | None = ...,
        timeouts: global___DataplexZoneXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["discovery_spec", b"discovery_spec", "resource_info", b"resource_info", "resource_spec", b"resource_spec", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_status", b"asset_status", "create_time", b"create_time", "description", b"description", "discovery_spec", b"discovery_spec", "display_name", b"display_name", "id", b"id", "labels", b"labels", "lake", b"lake", "location", b"location", "name", b"name", "project", b"project", "resource_info", b"resource_info", "resource_spec", b"resource_spec", "state", b"state", "timeouts", b"timeouts", "type", b"type", "uid", b"uid", "update_time", b"update_time"]) -> None: ...

global___DataplexZone = DataplexZone
