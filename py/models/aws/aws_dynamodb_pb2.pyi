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
class TableAttributeDefinition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ATTRIBUTE_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    attribute_name: builtins.str
    attribute_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attribute_name: builtins.str = ...,
        attribute_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attribute_name", b"attribute_name", "attribute_type", b"attribute_type", "resource_info", b"resource_info"]) -> None: ...

global___TableAttributeDefinition = TableAttributeDefinition

@typing_extensions.final
class DynamoDB(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_ATTRIBUTE_DEFINITION_FIELD_NUMBER: builtins.int
    TABLE_GLOBAL_SECONDARY_INDEX_FIELD_NUMBER: builtins.int
    TABLE_LOCAL_SECONDARY_INDEX_FIELD_NUMBER: builtins.int
    TABLE_POINT_IN_TIME_RECOVERY_SPECIFICATION_FIELD_NUMBER: builtins.int
    TABLE_SSE_SPECIFICATION_FIELD_NUMBER: builtins.int
    TABLE_STREAM_SPECIFICATION_FIELD_NUMBER: builtins.int
    TABLE_TIME_TO_LIVE_SPECIFICATION_FIELD_NUMBER: builtins.int
    @property
    def table_attribute_definition(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableAttributeDefinition]: ...
    @property
    def table_global_secondary_index(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableGlobalSecondaryIndex]: ...
    @property
    def table_local_secondary_index(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableLocalSecondaryIndex]: ...
    @property
    def table_point_in_time_recovery_specification(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TablePointInTimeRecoverySpecification]: ...
    @property
    def table_sse_specification(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableSSESpecification]: ...
    @property
    def table_stream_specification(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableStreamSpecification]: ...
    @property
    def table_time_to_live_specification(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableTimeToLiveSpecification]: ...
    def __init__(
        self,
        *,
        table_attribute_definition: collections.abc.Iterable[global___TableAttributeDefinition] | None = ...,
        table_global_secondary_index: collections.abc.Iterable[global___TableGlobalSecondaryIndex] | None = ...,
        table_local_secondary_index: collections.abc.Iterable[global___TableLocalSecondaryIndex] | None = ...,
        table_point_in_time_recovery_specification: collections.abc.Iterable[global___TablePointInTimeRecoverySpecification] | None = ...,
        table_sse_specification: collections.abc.Iterable[global___TableSSESpecification] | None = ...,
        table_stream_specification: collections.abc.Iterable[global___TableStreamSpecification] | None = ...,
        table_time_to_live_specification: collections.abc.Iterable[global___TableTimeToLiveSpecification] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["table_attribute_definition", b"table_attribute_definition", "table_global_secondary_index", b"table_global_secondary_index", "table_local_secondary_index", b"table_local_secondary_index", "table_point_in_time_recovery_specification", b"table_point_in_time_recovery_specification", "table_sse_specification", b"table_sse_specification", "table_stream_specification", b"table_stream_specification", "table_time_to_live_specification", b"table_time_to_live_specification"]) -> None: ...

global___DynamoDB = DynamoDB

@typing_extensions.final
class TableKeySchema(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    KEY_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    attribute_name: builtins.str
    key_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attribute_name: builtins.str = ...,
        key_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attribute_name", b"attribute_name", "key_type", b"key_type", "resource_info", b"resource_info"]) -> None: ...

global___TableKeySchema = TableKeySchema

@typing_extensions.final
class TableProjection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    NON_KEY_ATTRIBUTES_FIELD_NUMBER: builtins.int
    PROJECTION_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def non_key_attributes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    projection_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        non_key_attributes: collections.abc.Iterable[builtins.str] | None = ...,
        projection_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["non_key_attributes", b"non_key_attributes", "projection_type", b"projection_type", "resource_info", b"resource_info"]) -> None: ...

global___TableProjection = TableProjection

@typing_extensions.final
class TableProvisionedThroughput(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    READ_CAPACITY_UNITS_FIELD_NUMBER: builtins.int
    WRITE_CAPACITY_UNITS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    read_capacity_units: builtins.int
    write_capacity_units: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        read_capacity_units: builtins.int = ...,
        write_capacity_units: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["read_capacity_units", b"read_capacity_units", "resource_info", b"resource_info", "write_capacity_units", b"write_capacity_units"]) -> None: ...

global___TableProvisionedThroughput = TableProvisionedThroughput

@typing_extensions.final
class TableGlobalSecondaryIndex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    INDEX_NAME_FIELD_NUMBER: builtins.int
    KEY_SCHEMA_FIELD_NUMBER: builtins.int
    PROJECTION_FIELD_NUMBER: builtins.int
    PROVISIONED_THROUGHPUT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    index_name: builtins.str
    @property
    def key_schema(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableKeySchema]: ...
    @property
    def projection(self) -> global___TableProjection: ...
    @property
    def provisioned_throughput(self) -> global___TableProvisionedThroughput: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        index_name: builtins.str = ...,
        key_schema: collections.abc.Iterable[global___TableKeySchema] | None = ...,
        projection: global___TableProjection | None = ...,
        provisioned_throughput: global___TableProvisionedThroughput | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["projection", b"projection", "provisioned_throughput", b"provisioned_throughput", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name", b"index_name", "key_schema", b"key_schema", "projection", b"projection", "provisioned_throughput", b"provisioned_throughput", "resource_info", b"resource_info"]) -> None: ...

global___TableGlobalSecondaryIndex = TableGlobalSecondaryIndex

@typing_extensions.final
class TableLocalSecondaryIndex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    INDEX_NAME_FIELD_NUMBER: builtins.int
    KEY_SCHEMA_FIELD_NUMBER: builtins.int
    PROJECTION_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    index_name: builtins.str
    @property
    def key_schema(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableKeySchema]: ...
    @property
    def projection(self) -> global___TableProjection: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        index_name: builtins.str = ...,
        key_schema: collections.abc.Iterable[global___TableKeySchema] | None = ...,
        projection: global___TableProjection | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["projection", b"projection", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_name", b"index_name", "key_schema", b"key_schema", "projection", b"projection", "resource_info", b"resource_info"]) -> None: ...

global___TableLocalSecondaryIndex = TableLocalSecondaryIndex

@typing_extensions.final
class TablePointInTimeRecoverySpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    POINT_IN_TIME_RECOVERY_ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    point_in_time_recovery_enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        point_in_time_recovery_enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["point_in_time_recovery_enabled", b"point_in_time_recovery_enabled", "resource_info", b"resource_info"]) -> None: ...

global___TablePointInTimeRecoverySpecification = TablePointInTimeRecoverySpecification

@typing_extensions.final
class TableSSESpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KMS_MASTER_KEY_ID_FIELD_NUMBER: builtins.int
    SSE_ENABLED_FIELD_NUMBER: builtins.int
    SSE_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    kms_master_key_id: builtins.str
    sse_enabled: builtins.bool
    sse_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        kms_master_key_id: builtins.str = ...,
        sse_enabled: builtins.bool = ...,
        sse_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["kms_master_key_id", b"kms_master_key_id", "resource_info", b"resource_info", "sse_enabled", b"sse_enabled", "sse_type", b"sse_type"]) -> None: ...

global___TableSSESpecification = TableSSESpecification

@typing_extensions.final
class TableStreamSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    STREAM_VIEW_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    stream_view_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        stream_view_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "stream_view_type", b"stream_view_type"]) -> None: ...

global___TableStreamSpecification = TableStreamSpecification

@typing_extensions.final
class TableTimeToLiveSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTRIBUTE_NAME_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    attribute_name: builtins.str
    enabled: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attribute_name: builtins.str = ...,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attribute_name", b"attribute_name", "enabled", b"enabled", "resource_info", b"resource_info"]) -> None: ...

global___TableTimeToLiveSpecification = TableTimeToLiveSpecification
