# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_cloudwatch.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61ws/aws_cloudwatch.proto\x12\x1aoak9.tython.aws.cloudwatch\x1a\x13shared/shared.proto\"f\n\x0e\x41larmDimension\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xae\x01\n\x0b\x41larmMetric\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12>\n\ndimensions\x18\x02 \x03(\x0b\x32*.oak9.tython.aws.cloudwatch.AlarmDimension\x12\x13\n\x0bmetric_name\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\"\xaf\x01\n\x0f\x41larmMetricStat\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x37\n\x06metric\x18\x02 \x01(\x0b\x32\'.oak9.tython.aws.cloudwatch.AlarmMetric\x12\x0e\n\x06period\x18\x03 \x01(\x05\x12\x0c\n\x04stat\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\"\xe5\x01\n\x14\x41larmMetricDataQuery\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12@\n\x0bmetric_stat\x18\x05 \x01(\x0b\x32+.oak9.tython.aws.cloudwatch.AlarmMetricStat\x12\x0e\n\x06period\x18\x06 \x01(\x05\x12\x13\n\x0breturn_data\x18\x07 \x01(\x08\"\x9e\x05\n\x05\x41larm\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x61\x63tions_enabled\x18\x02 \x01(\x08\x12\x15\n\ralarm_actions\x18\x03 \x03(\t\x12\x19\n\x11\x61larm_description\x18\x04 \x01(\t\x12\x12\n\nalarm_name\x18\x05 \x01(\t\x12\x1b\n\x13\x63omparison_operator\x18\x06 \x01(\t\x12\x1b\n\x13\x64\x61tapoints_to_alarm\x18\x07 \x01(\x05\x12>\n\ndimensions\x18\x08 \x03(\x0b\x32*.oak9.tython.aws.cloudwatch.AlarmDimension\x12,\n$evaluate_low_sample_count_percentile\x18\t \x01(\t\x12\x1a\n\x12\x65valuation_periods\x18\n \x01(\x05\x12\x1a\n\x12\x65xtended_statistic\x18\x0b \x01(\t\x12!\n\x19insufficient_data_actions\x18\x0c \x03(\t\x12\x13\n\x0bmetric_name\x18\r \x01(\t\x12\x41\n\x07metrics\x18\x0e \x03(\x0b\x32\x30.oak9.tython.aws.cloudwatch.AlarmMetricDataQuery\x12\x11\n\tnamespace\x18\x0f \x01(\t\x12\x12\n\nok_actions\x18\x10 \x03(\t\x12\x0e\n\x06period\x18\x11 \x01(\x05\x12\x11\n\tstatistic\x18\x12 \x01(\t\x12\x11\n\tthreshold\x18\x13 \x01(\x01\x12\x1b\n\x13threshold_metric_id\x18\x14 \x01(\t\x12\x1a\n\x12treat_missing_data\x18\x15 \x01(\t\x12\x0c\n\x04unit\x18\x16 \x01(\t\"\xc3\x02\n\nCloudWatch\x12\x30\n\x05\x61larm\x18\x01 \x03(\x0b\x32!.oak9.tython.aws.cloudwatch.Alarm\x12\x45\n\x10\x61nomaly_detector\x18\x02 \x03(\x0b\x32+.oak9.tython.aws.cloudwatch.AnomalyDetector\x12\x43\n\x0f\x63omposite_alarm\x18\x03 \x03(\x0b\x32*.oak9.tython.aws.cloudwatch.CompositeAlarm\x12\x38\n\tdashboard\x18\x04 \x03(\x0b\x32%.oak9.tython.aws.cloudwatch.Dashboard\x12=\n\x0cinsight_rule\x18\x05 \x03(\x0b\x32\'.oak9.tython.aws.cloudwatch.InsightRule\"u\n\x14\x41nomalyDetectorRange\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\"\xc1\x01\n\x1c\x41nomalyDetectorConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10metric_time_zone\x18\x02 \x01(\t\x12N\n\x14\x65xcluded_time_ranges\x18\x03 \x03(\x0b\x32\x30.oak9.tython.aws.cloudwatch.AnomalyDetectorRange\"p\n\x18\x41nomalyDetectorDimension\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x9b\x02\n\x0f\x41nomalyDetector\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\x12\x0c\n\x04stat\x18\x03 \x01(\t\x12O\n\rconfiguration\x18\x04 \x01(\x0b\x32\x38.oak9.tython.aws.cloudwatch.AnomalyDetectorConfiguration\x12H\n\ndimensions\x18\x05 \x03(\x0b\x32\x34.oak9.tython.aws.cloudwatch.AnomalyDetectorDimension\x12\x11\n\tnamespace\x18\x06 \x01(\t\"\xf3\x01\n\x0e\x43ompositeAlarm\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nalarm_name\x18\x02 \x01(\t\x12\x12\n\nalarm_rule\x18\x03 \x01(\t\x12\x19\n\x11\x61larm_description\x18\x04 \x01(\t\x12\x17\n\x0f\x61\x63tions_enabled\x18\x05 \x01(\x08\x12\x12\n\nok_actions\x18\x06 \x03(\t\x12\x15\n\ralarm_actions\x18\x07 \x03(\t\x12!\n\x19insufficient_data_actions\x18\x08 \x03(\t\"t\n\tDashboard\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x64\x61shboard_name\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x61shboard_body\x18\x03 \x01(\t\"J\n\x0fInsightRuleTags\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xbb\x01\n\x0bInsightRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nrule_state\x18\x02 \x01(\t\x12\x11\n\trule_body\x18\x03 \x01(\t\x12\x11\n\trule_name\x18\x04 \x01(\t\x12\x39\n\x04tags\x18\x05 \x01(\x0b\x32+.oak9.tython.aws.cloudwatch.InsightRuleTagsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_cloudwatch_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALARMDIMENSION._serialized_start=77
  _ALARMDIMENSION._serialized_end=179
  _ALARMMETRIC._serialized_start=182
  _ALARMMETRIC._serialized_end=356
  _ALARMMETRICSTAT._serialized_start=359
  _ALARMMETRICSTAT._serialized_end=534
  _ALARMMETRICDATAQUERY._serialized_start=537
  _ALARMMETRICDATAQUERY._serialized_end=766
  _ALARM._serialized_start=769
  _ALARM._serialized_end=1439
  _CLOUDWATCH._serialized_start=1442
  _CLOUDWATCH._serialized_end=1765
  _ANOMALYDETECTORRANGE._serialized_start=1767
  _ANOMALYDETECTORRANGE._serialized_end=1884
  _ANOMALYDETECTORCONFIGURATION._serialized_start=1887
  _ANOMALYDETECTORCONFIGURATION._serialized_end=2080
  _ANOMALYDETECTORDIMENSION._serialized_start=2082
  _ANOMALYDETECTORDIMENSION._serialized_end=2194
  _ANOMALYDETECTOR._serialized_start=2197
  _ANOMALYDETECTOR._serialized_end=2480
  _COMPOSITEALARM._serialized_start=2483
  _COMPOSITEALARM._serialized_end=2726
  _DASHBOARD._serialized_start=2728
  _DASHBOARD._serialized_end=2844
  _INSIGHTRULETAGS._serialized_start=2846
  _INSIGHTRULETAGS._serialized_end=2920
  _INSIGHTRULE._serialized_start=2923
  _INSIGHTRULE._serialized_end=3110
# @@protoc_insertion_point(module_scope)
