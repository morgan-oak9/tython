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
class DetectorCFNS3LogsConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ENABLE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    enable: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        enable: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enable", b"enable", "resource_info", b"resource_info"]) -> None: ...

global___DetectorCFNS3LogsConfiguration = DetectorCFNS3LogsConfiguration

@typing_extensions.final
class DetectorCFNDataSourceConfigurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    S3_LOGS_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def s3_logs(self) -> global___DetectorCFNS3LogsConfiguration: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        s3_logs: global___DetectorCFNS3LogsConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "s3_logs", b"s3_logs"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info", "s3_logs", b"s3_logs"]) -> None: ...

global___DetectorCFNDataSourceConfigurations = DetectorCFNDataSourceConfigurations

@typing_extensions.final
class Detector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FINDING_PUBLISHING_FREQUENCY_FIELD_NUMBER: builtins.int
    DATA_SOURCES_FIELD_NUMBER: builtins.int
    ENABLE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    finding_publishing_frequency: builtins.str
    @property
    def data_sources(self) -> global___DetectorCFNDataSourceConfigurations: ...
    enable: builtins.bool
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        finding_publishing_frequency: builtins.str = ...,
        data_sources: global___DetectorCFNDataSourceConfigurations | None = ...,
        enable: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data_sources", b"data_sources", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_sources", b"data_sources", "enable", b"enable", "finding_publishing_frequency", b"finding_publishing_frequency", "resource_info", b"resource_info"]) -> None: ...

global___Detector = Detector

@typing_extensions.final
class GuardDuty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DETECTOR_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    IP_SET_FIELD_NUMBER: builtins.int
    MASTER_FIELD_NUMBER: builtins.int
    MEMBER_FIELD_NUMBER: builtins.int
    THREAT_INTEL_SET_FIELD_NUMBER: builtins.int
    @property
    def detector(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Detector]: ...
    @property
    def filter(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Filter]: ...
    @property
    def ip_set(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IPSet]: ...
    @property
    def master(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Master]: ...
    @property
    def member(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Member]: ...
    @property
    def threat_intel_set(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThreatIntelSet]: ...
    def __init__(
        self,
        *,
        detector: collections.abc.Iterable[global___Detector] | None = ...,
        filter: collections.abc.Iterable[global___Filter] | None = ...,
        ip_set: collections.abc.Iterable[global___IPSet] | None = ...,
        master: collections.abc.Iterable[global___Master] | None = ...,
        member: collections.abc.Iterable[global___Member] | None = ...,
        threat_intel_set: collections.abc.Iterable[global___ThreatIntelSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["detector", b"detector", "filter", b"filter", "ip_set", b"ip_set", "master", b"master", "member", b"member", "threat_intel_set", b"threat_intel_set"]) -> None: ...

global___GuardDuty = GuardDuty

@typing_extensions.final
class FilterCondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    LT_FIELD_NUMBER: builtins.int
    GTE_FIELD_NUMBER: builtins.int
    NEQ_FIELD_NUMBER: builtins.int
    EQ_FIELD_NUMBER: builtins.int
    LTE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    lt: builtins.int
    gte: builtins.int
    @property
    def neq(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def eq(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    lte: builtins.int
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        lt: builtins.int = ...,
        gte: builtins.int = ...,
        neq: collections.abc.Iterable[builtins.str] | None = ...,
        eq: collections.abc.Iterable[builtins.str] | None = ...,
        lte: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["eq", b"eq", "gte", b"gte", "lt", b"lt", "lte", b"lte", "neq", b"neq", "resource_info", b"resource_info"]) -> None: ...

global___FilterCondition = FilterCondition

@typing_extensions.final
class FilterFindingCriteria(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class CriterionEntry(google.protobuf.message.Message):
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
    CRITERION_FIELD_NUMBER: builtins.int
    ITEM_TYPE_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    @property
    def criterion(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def item_type(self) -> global___FilterCondition: ...
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        criterion: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        item_type: global___FilterCondition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["item_type", b"item_type", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["criterion", b"criterion", "item_type", b"item_type", "resource_info", b"resource_info"]) -> None: ...

global___FilterFindingCriteria = FilterFindingCriteria

@typing_extensions.final
class Filter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DETECTOR_ID_FIELD_NUMBER: builtins.int
    FINDING_CRITERIA_FIELD_NUMBER: builtins.int
    RANK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    action: builtins.str
    description: builtins.str
    detector_id: builtins.str
    @property
    def finding_criteria(self) -> global___FilterFindingCriteria: ...
    rank: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        action: builtins.str = ...,
        description: builtins.str = ...,
        detector_id: builtins.str = ...,
        finding_criteria: global___FilterFindingCriteria | None = ...,
        rank: builtins.int = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["finding_criteria", b"finding_criteria", "resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "description", b"description", "detector_id", b"detector_id", "finding_criteria", b"finding_criteria", "name", b"name", "rank", b"rank", "resource_info", b"resource_info"]) -> None: ...

global___Filter = Filter

@typing_extensions.final
class IPSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    ACTIVATE_FIELD_NUMBER: builtins.int
    DETECTOR_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    format: builtins.str
    activate: builtins.bool
    detector_id: builtins.str
    name: builtins.str
    location: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        format: builtins.str = ...,
        activate: builtins.bool = ...,
        detector_id: builtins.str = ...,
        name: builtins.str = ...,
        location: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activate", b"activate", "detector_id", b"detector_id", "format", b"format", "location", b"location", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___IPSet = IPSet

@typing_extensions.final
class Master(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    DETECTOR_ID_FIELD_NUMBER: builtins.int
    MASTER_ID_FIELD_NUMBER: builtins.int
    INVITATION_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    detector_id: builtins.str
    master_id: builtins.str
    invitation_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        detector_id: builtins.str = ...,
        master_id: builtins.str = ...,
        invitation_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["detector_id", b"detector_id", "invitation_id", b"invitation_id", "master_id", b"master_id", "resource_info", b"resource_info"]) -> None: ...

global___Master = Master

@typing_extensions.final
class Member(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MEMBER_ID_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    DISABLE_EMAIL_NOTIFICATION_FIELD_NUMBER: builtins.int
    DETECTOR_ID_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    status: builtins.str
    member_id: builtins.str
    email: builtins.str
    message: builtins.str
    disable_email_notification: builtins.bool
    detector_id: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        status: builtins.str = ...,
        member_id: builtins.str = ...,
        email: builtins.str = ...,
        message: builtins.str = ...,
        disable_email_notification: builtins.bool = ...,
        detector_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["detector_id", b"detector_id", "disable_email_notification", b"disable_email_notification", "email", b"email", "member_id", b"member_id", "message", b"message", "resource_info", b"resource_info", "status", b"status"]) -> None: ...

global___Member = Member

@typing_extensions.final
class ThreatIntelSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_INFO_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    ACTIVATE_FIELD_NUMBER: builtins.int
    DETECTOR_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    @property
    def resource_info(self) -> shared.shared_pb2.ResourceInfo: ...
    format: builtins.str
    activate: builtins.bool
    detector_id: builtins.str
    name: builtins.str
    location: builtins.str
    def __init__(
        self,
        *,
        resource_info: shared.shared_pb2.ResourceInfo | None = ...,
        format: builtins.str = ...,
        activate: builtins.bool = ...,
        detector_id: builtins.str = ...,
        name: builtins.str = ...,
        location: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_info", b"resource_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activate", b"activate", "detector_id", b"detector_id", "format", b"format", "location", b"location", "name", b"name", "resource_info", b"resource_info"]) -> None: ...

global___ThreatIntelSet = ThreatIntelSet
