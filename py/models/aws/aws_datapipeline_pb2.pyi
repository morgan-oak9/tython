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
class PipelineParameterAttribute(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    string_value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        string_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "resource_info", b"resource_info", "string_value", b"string_value"]) -> None: ...

global___PipelineParameterAttribute = PipelineParameterAttribute

@typing_extensions.final
class PipelineParameterObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def attributes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineParameterAttribute]: ...
    id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        attributes: collections.abc.Iterable[global___PipelineParameterAttribute] | None = ...,
        id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes", b"attributes", "id", b"id", "resource_info", b"resource_info"]) -> None: ...

global___PipelineParameterObject = PipelineParameterObject

@typing_extensions.final
class PipelineParameterValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    id: builtins.str
    string_value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        id: builtins.str = ...,
        string_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "resource_info", b"resource_info", "string_value", b"string_value"]) -> None: ...

global___PipelineParameterValue = PipelineParameterValue

@typing_extensions.final
class PipelineField(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    REF_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    key: builtins.str
    ref_value: builtins.str
    string_value: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        key: builtins.str = ...,
        ref_value: builtins.str = ...,
        string_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "ref_value", b"ref_value", "resource_info", b"resource_info", "string_value", b"string_value"]) -> None: ...

global___PipelineField = PipelineField

@typing_extensions.final
class PipelinePipelineObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineField]: ...
    id: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        fields: collections.abc.Iterable[global___PipelineField] | None = ...,
        id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "id", b"id", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___PipelinePipelineObject = PipelinePipelineObject

@typing_extensions.final
class PipelinePipelineTag(google.protobuf.message.Message):
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

global___PipelinePipelineTag = PipelinePipelineTag

@typing_extensions.final
class Pipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ACTIVATE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PARAMETER_OBJECTS_FIELD_NUMBER: builtins.int
    PARAMETER_VALUES_FIELD_NUMBER: builtins.int
    PIPELINE_OBJECTS_FIELD_NUMBER: builtins.int
    PIPELINE_TAGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    activate: builtins.bool
    description: builtins.str
    name: builtins.str
    @property
    def parameter_objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineParameterObject]: ...
    @property
    def parameter_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineParameterValue]: ...
    @property
    def pipeline_objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelinePipelineObject]: ...
    @property
    def pipeline_tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelinePipelineTag]: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        activate: builtins.bool = ...,
        description: builtins.str = ...,
        name: builtins.str = ...,
        parameter_objects: collections.abc.Iterable[global___PipelineParameterObject] | None = ...,
        parameter_values: collections.abc.Iterable[global___PipelineParameterValue] | None = ...,
        pipeline_objects: collections.abc.Iterable[global___PipelinePipelineObject] | None = ...,
        pipeline_tags: collections.abc.Iterable[global___PipelinePipelineTag] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activate", b"activate", "description", b"description", "name", b"name", "parameter_objects", b"parameter_objects", "parameter_values", b"parameter_values", "pipeline_objects", b"pipeline_objects", "pipeline_tags", b"pipeline_tags", "resource_info", b"resource_info"]) -> None: ...

global___Pipeline = Pipeline

@typing_extensions.final
class DataPipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIPELINE_FIELD_NUMBER: builtins.int
    @property
    def pipeline(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pipeline]: ...
    def __init__(
        self,
        *,
        pipeline: collections.abc.Iterable[global___Pipeline] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pipeline", b"pipeline"]) -> None: ...

global___DataPipeline = DataPipeline