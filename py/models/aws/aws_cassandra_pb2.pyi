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
class Keyspace(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEYSPACE_NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    keyspace_name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        keyspace_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["keyspace_name", b"keyspace_name", "resource_info", b"resource_info"]) -> None: ...

global___Keyspace = Keyspace

@typing_extensions.final
class Cassandra(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYSPACE_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    @property
    def keyspace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Keyspace]: ...
    @property
    def table(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Table]: ...
    def __init__(
        self,
        *,
        keyspace: collections.abc.Iterable[global___Keyspace] | None = ...,
        table: collections.abc.Iterable[global___Table] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keyspace", b"keyspace", "table", b"table"]) -> None: ...

global___Cassandra = Cassandra

@typing_extensions.final
class TableColumn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    COLUMN_NAME_FIELD_NUMBER: builtins.int
    COLUMN_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    column_name: builtins.str
    column_type: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        column_name: builtins.str = ...,
        column_type: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column_name", b"column_name", "column_type", b"column_type", "resource_info", b"resource_info"]) -> None: ...

global___TableColumn = TableColumn

@typing_extensions.final
class TableClusteringKeyColumn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    COLUMN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def column(self) -> global___TableColumn: ...
    order_by: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        column: global___TableColumn | None = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["column", b"column", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column", b"column", "order_by", b"order_by", "resource_info", b"resource_info"]) -> None: ...

global___TableClusteringKeyColumn = TableClusteringKeyColumn

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
class TableBillingMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    PROVISIONED_THROUGHPUT_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    mode: builtins.str
    @property
    def provisioned_throughput(self) -> global___TableProvisionedThroughput: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        mode: builtins.str = ...,
        provisioned_throughput: global___TableProvisionedThroughput | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["provisioned_throughput", b"provisioned_throughput", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode", "provisioned_throughput", b"provisioned_throughput", "resource_info", b"resource_info"]) -> None: ...

global___TableBillingMode = TableBillingMode

@typing_extensions.final
class Table(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEYSPACE_NAME_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    REGULAR_COLUMNS_FIELD_NUMBER: builtins.int
    PARTITION_KEY_COLUMNS_FIELD_NUMBER: builtins.int
    CLUSTERING_KEY_COLUMNS_FIELD_NUMBER: builtins.int
    BILLING_MODE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    keyspace_name: builtins.str
    table_name: builtins.str
    @property
    def regular_columns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableColumn]: ...
    @property
    def partition_key_columns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableColumn]: ...
    @property
    def clustering_key_columns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableClusteringKeyColumn]: ...
    @property
    def billing_mode(self) -> global___TableBillingMode: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        keyspace_name: builtins.str = ...,
        table_name: builtins.str = ...,
        regular_columns: collections.abc.Iterable[global___TableColumn] | None = ...,
        partition_key_columns: collections.abc.Iterable[global___TableColumn] | None = ...,
        clustering_key_columns: collections.abc.Iterable[global___TableClusteringKeyColumn] | None = ...,
        billing_mode: global___TableBillingMode | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["billing_mode", b"billing_mode", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_mode", b"billing_mode", "clustering_key_columns", b"clustering_key_columns", "keyspace_name", b"keyspace_name", "partition_key_columns", b"partition_key_columns", "regular_columns", b"regular_columns", "resource_info", b"resource_info", "table_name", b"table_name"]) -> None: ...

global___Table = Table