# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_logging.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gcp/gcp_logging.proto\x12\x17oak9.tython.gcp.logging\x1a\x13shared/shared.proto\"\xfa\x01\n!LoggingBillingAccountBucketConfig\x12\x17\n\x0f\x62illing_account\x18\x01 \x01(\t\x12\x11\n\tbucket_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x17\n\x0flifecycle_state\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x16\n\x0eretention_days\x18\x08 \x01(\x01\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xc3\x01\n\x1eLoggingBillingAccountExclusion\x12\x17\n\x0f\x62illing_account\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"K\n)LoggingBillingAccountSinkXBigqueryOptions\x12\x1e\n\x16use_partitioned_tables\x18\x01 \x01(\x08\"k\n$LoggingBillingAccountSinkXExclusions\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\x9d\x03\n\x19LoggingBillingAccountSink\x12\x17\n\x0f\x62illing_account\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12\x10\n\x08\x64isabled\x18\x04 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x17\n\x0fwriter_identity\x18\x08 \x01(\t\x12\\\n\x10\x62igquery_options\x18\t \x01(\x0b\x32\x42.oak9.tython.gcp.logging.LoggingBillingAccountSinkXBigqueryOptions\x12Q\n\nexclusions\x18\n \x03(\x0b\x32=.oak9.tython.gcp.logging.LoggingBillingAccountSinkXExclusions\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xe9\x01\n\x19LoggingFolderBucketConfig\x12\x11\n\tbucket_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06\x66older\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x17\n\x0flifecycle_state\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x16\n\x0eretention_days\x18\x08 \x01(\x01\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb2\x01\n\x16LoggingFolderExclusion\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x0e\n\x06\x66older\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"C\n!LoggingFolderSinkXBigqueryOptions\x12\x1e\n\x16use_partitioned_tables\x18\x01 \x01(\x08\"c\n\x1cLoggingFolderSinkXExclusions\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\x96\x03\n\x11LoggingFolderSink\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x0e\n\x06\x66older\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x18\n\x10include_children\x18\x07 \x01(\x08\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x17\n\x0fwriter_identity\x18\t \x01(\t\x12T\n\x10\x62igquery_options\x18\n \x01(\x0b\x32:.oak9.tython.gcp.logging.LoggingFolderSinkXBigqueryOptions\x12I\n\nexclusions\x18\x0b \x03(\x0b\x32\x35.oak9.tython.gcp.logging.LoggingFolderSinkXExclusions\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"I\n\x17LoggingLogViewXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xa8\x02\n\x0eLoggingLogView\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0e\n\x06parent\x18\x08 \x01(\t\x12\x13\n\x0bupdate_time\x18\t \x01(\t\x12\x42\n\x08timeouts\x18\n \x01(\x0b\x32\x30.oak9.tython.gcp.logging.LoggingLogViewXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"=\n+LoggingMetricXBucketOptionsXExplicitBuckets\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x01\"r\n.LoggingMetricXBucketOptionsXExponentialBuckets\x12\x15\n\rgrowth_factor\x18\x01 \x01(\x01\x12\x1a\n\x12num_finite_buckets\x18\x02 \x01(\x01\x12\r\n\x05scale\x18\x03 \x01(\x01\"f\n)LoggingMetricXBucketOptionsXLinearBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x01\x12\x0e\n\x06offset\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\"\xbf\x02\n\x1bLoggingMetricXBucketOptions\x12^\n\x10\x65xplicit_buckets\x18\x01 \x01(\x0b\x32\x44.oak9.tython.gcp.logging.LoggingMetricXBucketOptionsXExplicitBuckets\x12\x64\n\x13\x65xponential_buckets\x18\x02 \x01(\x0b\x32G.oak9.tython.gcp.logging.LoggingMetricXBucketOptionsXExponentialBuckets\x12Z\n\x0elinear_buckets\x18\x03 \x01(\x0b\x32\x42.oak9.tython.gcp.logging.LoggingMetricXBucketOptionsXLinearBuckets\"]\n%LoggingMetricXMetricDescriptorXLabels\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nvalue_type\x18\x03 \x01(\t\"\xbd\x01\n\x1eLoggingMetricXMetricDescriptor\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x13\n\x0bmetric_kind\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x12\n\nvalue_type\x18\x04 \x01(\t\x12N\n\x06labels\x18\x05 \x03(\x0b\x32>.oak9.tython.gcp.logging.LoggingMetricXMetricDescriptorXLabels\"H\n\x16LoggingMetricXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xa5\x04\n\rLoggingMetric\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12U\n\x10label_extractors\x18\x04 \x03(\x0b\x32;.oak9.tython.gcp.logging.LoggingMetric.LabelExtractorsEntry\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x17\n\x0fvalue_extractor\x18\x07 \x01(\t\x12L\n\x0e\x62ucket_options\x18\x08 \x01(\x0b\x32\x34.oak9.tython.gcp.logging.LoggingMetricXBucketOptions\x12R\n\x11metric_descriptor\x18\t \x01(\x0b\x32\x37.oak9.tython.gcp.logging.LoggingMetricXMetricDescriptor\x12\x41\n\x08timeouts\x18\n \x01(\x0b\x32/.oak9.tython.gcp.logging.LoggingMetricXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a\x36\n\x14LabelExtractorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf5\x01\n\x1fLoggingOrganizationBucketConfig\x12\x11\n\tbucket_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x17\n\x0flifecycle_state\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x14\n\x0corganization\x18\x07 \x01(\t\x12\x16\n\x0eretention_days\x18\x08 \x01(\x01\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb8\x01\n\x1cLoggingOrganizationExclusion\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06org_id\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"I\n\'LoggingOrganizationSinkXBigqueryOptions\x12\x1e\n\x16use_partitioned_tables\x18\x01 \x01(\x08\"i\n\"LoggingOrganizationSinkXExclusions\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xa8\x03\n\x17LoggingOrganizationSink\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x18\n\x10include_children\x18\x06 \x01(\x08\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0e\n\x06org_id\x18\x08 \x01(\t\x12\x17\n\x0fwriter_identity\x18\t \x01(\t\x12Z\n\x10\x62igquery_options\x18\n \x01(\x0b\x32@.oak9.tython.gcp.logging.LoggingOrganizationSinkXBigqueryOptions\x12O\n\nexclusions\x18\x0b \x03(\x0b\x32;.oak9.tython.gcp.logging.LoggingOrganizationSinkXExclusions\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xeb\x01\n\x1aLoggingProjectBucketConfig\x12\x11\n\tbucket_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x17\n\x0flifecycle_state\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x16\n\x0eretention_days\x18\x08 \x01(\x01\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb4\x01\n\x17LoggingProjectExclusion\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"D\n\"LoggingProjectSinkXBigqueryOptions\x12\x1e\n\x16use_partitioned_tables\x18\x01 \x01(\x08\"d\n\x1dLoggingProjectSinkXExclusions\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xa0\x03\n\x12LoggingProjectSink\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x1e\n\x16unique_writer_identity\x18\x08 \x01(\x08\x12\x17\n\x0fwriter_identity\x18\t \x01(\t\x12U\n\x10\x62igquery_options\x18\n \x01(\x0b\x32;.oak9.tython.gcp.logging.LoggingProjectSinkXBigqueryOptions\x12J\n\nexclusions\x18\x0b \x03(\x0b\x32\x36.oak9.tython.gcp.logging.LoggingProjectSinkXExclusions\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_logging_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGGINGMETRIC_LABELEXTRACTORSENTRY._options = None
  _LOGGINGMETRIC_LABELEXTRACTORSENTRY._serialized_options = b'8\001'
  _LOGGINGBILLINGACCOUNTBUCKETCONFIG._serialized_start=72
  _LOGGINGBILLINGACCOUNTBUCKETCONFIG._serialized_end=322
  _LOGGINGBILLINGACCOUNTEXCLUSION._serialized_start=325
  _LOGGINGBILLINGACCOUNTEXCLUSION._serialized_end=520
  _LOGGINGBILLINGACCOUNTSINKXBIGQUERYOPTIONS._serialized_start=522
  _LOGGINGBILLINGACCOUNTSINKXBIGQUERYOPTIONS._serialized_end=597
  _LOGGINGBILLINGACCOUNTSINKXEXCLUSIONS._serialized_start=599
  _LOGGINGBILLINGACCOUNTSINKXEXCLUSIONS._serialized_end=706
  _LOGGINGBILLINGACCOUNTSINK._serialized_start=709
  _LOGGINGBILLINGACCOUNTSINK._serialized_end=1122
  _LOGGINGFOLDERBUCKETCONFIG._serialized_start=1125
  _LOGGINGFOLDERBUCKETCONFIG._serialized_end=1358
  _LOGGINGFOLDEREXCLUSION._serialized_start=1361
  _LOGGINGFOLDEREXCLUSION._serialized_end=1539
  _LOGGINGFOLDERSINKXBIGQUERYOPTIONS._serialized_start=1541
  _LOGGINGFOLDERSINKXBIGQUERYOPTIONS._serialized_end=1608
  _LOGGINGFOLDERSINKXEXCLUSIONS._serialized_start=1610
  _LOGGINGFOLDERSINKXEXCLUSIONS._serialized_end=1709
  _LOGGINGFOLDERSINK._serialized_start=1712
  _LOGGINGFOLDERSINK._serialized_end=2118
  _LOGGINGLOGVIEWXTIMEOUTS._serialized_start=2120
  _LOGGINGLOGVIEWXTIMEOUTS._serialized_end=2193
  _LOGGINGLOGVIEW._serialized_start=2196
  _LOGGINGLOGVIEW._serialized_end=2492
  _LOGGINGMETRICXBUCKETOPTIONSXEXPLICITBUCKETS._serialized_start=2494
  _LOGGINGMETRICXBUCKETOPTIONSXEXPLICITBUCKETS._serialized_end=2555
  _LOGGINGMETRICXBUCKETOPTIONSXEXPONENTIALBUCKETS._serialized_start=2557
  _LOGGINGMETRICXBUCKETOPTIONSXEXPONENTIALBUCKETS._serialized_end=2671
  _LOGGINGMETRICXBUCKETOPTIONSXLINEARBUCKETS._serialized_start=2673
  _LOGGINGMETRICXBUCKETOPTIONSXLINEARBUCKETS._serialized_end=2775
  _LOGGINGMETRICXBUCKETOPTIONS._serialized_start=2778
  _LOGGINGMETRICXBUCKETOPTIONS._serialized_end=3097
  _LOGGINGMETRICXMETRICDESCRIPTORXLABELS._serialized_start=3099
  _LOGGINGMETRICXMETRICDESCRIPTORXLABELS._serialized_end=3192
  _LOGGINGMETRICXMETRICDESCRIPTOR._serialized_start=3195
  _LOGGINGMETRICXMETRICDESCRIPTOR._serialized_end=3384
  _LOGGINGMETRICXTIMEOUTS._serialized_start=3386
  _LOGGINGMETRICXTIMEOUTS._serialized_end=3458
  _LOGGINGMETRIC._serialized_start=3461
  _LOGGINGMETRIC._serialized_end=4010
  _LOGGINGMETRIC_LABELEXTRACTORSENTRY._serialized_start=3956
  _LOGGINGMETRIC_LABELEXTRACTORSENTRY._serialized_end=4010
  _LOGGINGORGANIZATIONBUCKETCONFIG._serialized_start=4013
  _LOGGINGORGANIZATIONBUCKETCONFIG._serialized_end=4258
  _LOGGINGORGANIZATIONEXCLUSION._serialized_start=4261
  _LOGGINGORGANIZATIONEXCLUSION._serialized_end=4445
  _LOGGINGORGANIZATIONSINKXBIGQUERYOPTIONS._serialized_start=4447
  _LOGGINGORGANIZATIONSINKXBIGQUERYOPTIONS._serialized_end=4520
  _LOGGINGORGANIZATIONSINKXEXCLUSIONS._serialized_start=4522
  _LOGGINGORGANIZATIONSINKXEXCLUSIONS._serialized_end=4627
  _LOGGINGORGANIZATIONSINK._serialized_start=4630
  _LOGGINGORGANIZATIONSINK._serialized_end=5054
  _LOGGINGPROJECTBUCKETCONFIG._serialized_start=5057
  _LOGGINGPROJECTBUCKETCONFIG._serialized_end=5292
  _LOGGINGPROJECTEXCLUSION._serialized_start=5295
  _LOGGINGPROJECTEXCLUSION._serialized_end=5475
  _LOGGINGPROJECTSINKXBIGQUERYOPTIONS._serialized_start=5477
  _LOGGINGPROJECTSINKXBIGQUERYOPTIONS._serialized_end=5545
  _LOGGINGPROJECTSINKXEXCLUSIONS._serialized_start=5547
  _LOGGINGPROJECTSINKXEXCLUSIONS._serialized_end=5647
  _LOGGINGPROJECTSINK._serialized_start=5650
  _LOGGINGPROJECTSINK._serialized_end=6066
# @@protoc_insertion_point(module_scope)
