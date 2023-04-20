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
class DataflowJobXTimeouts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATE_FIELD_NUMBER: builtins.int
    update: builtins.str
    def __init__(
        self,
        *,
        update: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["update", b"update"]) -> None: ...

global___DataflowJobXTimeouts = DataflowJobXTimeouts

@typing_extensions.final
class DataflowJob(google.protobuf.message.Message):
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
    class ParametersEntry(google.protobuf.message.Message):
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
    class TransformNameMappingEntry(google.protobuf.message.Message):
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

    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: builtins.int
    ENABLE_STREAMING_ENGINE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    IP_CONFIGURATION_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    KMS_KEY_NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MACHINE_TYPE_FIELD_NUMBER: builtins.int
    MAX_WORKERS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    ON_DELETE_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: builtins.int
    SKIP_WAIT_ON_JOB_TERMINATION_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    SUBNETWORK_FIELD_NUMBER: builtins.int
    TEMP_GCS_LOCATION_FIELD_NUMBER: builtins.int
    TEMPLATE_GCS_PATH_FIELD_NUMBER: builtins.int
    TRANSFORM_NAME_MAPPING_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ZONE_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    @property
    def additional_experiments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    enable_streaming_engine: builtins.bool
    id: builtins.str
    ip_configuration: builtins.str
    job_id: builtins.str
    kms_key_name: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    machine_type: builtins.str
    max_workers: builtins.float
    name: builtins.str
    network: builtins.str
    on_delete: builtins.str
    @property
    def parameters(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    project: builtins.str
    region: builtins.str
    service_account_email: builtins.str
    skip_wait_on_job_termination: builtins.bool
    state: builtins.str
    subnetwork: builtins.str
    temp_gcs_location: builtins.str
    template_gcs_path: builtins.str
    @property
    def transform_name_mapping(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    type: builtins.str
    zone: builtins.str
    @property
    def timeouts(self) -> global___DataflowJobXTimeouts: ...
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    def __init__(
        self,
        *,
        additional_experiments: collections.abc.Iterable[builtins.str] | None = ...,
        enable_streaming_engine: builtins.bool = ...,
        id: builtins.str = ...,
        ip_configuration: builtins.str = ...,
        job_id: builtins.str = ...,
        kms_key_name: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        machine_type: builtins.str = ...,
        max_workers: builtins.float = ...,
        name: builtins.str = ...,
        network: builtins.str = ...,
        on_delete: builtins.str = ...,
        parameters: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        project: builtins.str = ...,
        region: builtins.str = ...,
        service_account_email: builtins.str = ...,
        skip_wait_on_job_termination: builtins.bool = ...,
        state: builtins.str = ...,
        subnetwork: builtins.str = ...,
        temp_gcs_location: builtins.str = ...,
        template_gcs_path: builtins.str = ...,
        transform_name_mapping: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        type: builtins.str = ...,
        zone: builtins.str = ...,
        timeouts: global___DataflowJobXTimeouts | None = ...,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "timeouts", b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["additional_experiments", b"additional_experiments", "enable_streaming_engine", b"enable_streaming_engine", "id", b"id", "ip_configuration", b"ip_configuration", "job_id", b"job_id", "kms_key_name", b"kms_key_name", "labels", b"labels", "machine_type", b"machine_type", "max_workers", b"max_workers", "name", b"name", "network", b"network", "on_delete", b"on_delete", "parameters", b"parameters", "project", b"project", "region", b"region", "resource_info", b"resource_info", "service_account_email", b"service_account_email", "skip_wait_on_job_termination", b"skip_wait_on_job_termination", "state", b"state", "subnetwork", b"subnetwork", "temp_gcs_location", b"temp_gcs_location", "template_gcs_path", b"template_gcs_path", "timeouts", b"timeouts", "transform_name_mapping", b"transform_name_mapping", "type", b"type", "zone", b"zone"]) -> None: ...

global___DataflowJob = DataflowJob
