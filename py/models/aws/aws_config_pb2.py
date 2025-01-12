# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61ws/aws_config.proto\x12\x16oak9.tython.aws.config\x1a\x13shared/shared.proto\"\x88\x02\n\x18\x41ggregationAuthorization\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x61uthorized_account_id\x18\x02 \x01(\t\x12\x1d\n\x15\x61uthorized_aws_region\x18\x03 \x01(\t\x12H\n\x04tags\x18\x04 \x03(\x0b\x32:.oak9.tython.aws.config.AggregationAuthorization.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcc\x06\n\x06\x43onfig\x12S\n\x19\x61ggregation_authorization\x18\x01 \x03(\x0b\x32\x30.oak9.tython.aws.config.AggregationAuthorization\x12\x37\n\x0b\x63onfig_rule\x18\x02 \x03(\x0b\x32\".oak9.tython.aws.config.ConfigRule\x12Q\n\x18\x63onfiguration_aggregator\x18\x03 \x03(\x0b\x32/.oak9.tython.aws.config.ConfigurationAggregator\x12M\n\x16\x63onfiguration_recorder\x18\x04 \x03(\x0b\x32-.oak9.tython.aws.config.ConfigurationRecorder\x12\x41\n\x10\x63onformance_pack\x18\x05 \x03(\x0b\x32\'.oak9.tython.aws.config.ConformancePack\x12\x41\n\x10\x64\x65livery_channel\x18\x06 \x03(\x0b\x32\'.oak9.tython.aws.config.DeliveryChannel\x12P\n\x18organization_config_rule\x18\x07 \x03(\x0b\x32..oak9.tython.aws.config.OrganizationConfigRule\x12Z\n\x1dorganization_conformance_pack\x18\x08 \x03(\x0b\x32\x33.oak9.tython.aws.config.OrganizationConformancePack\x12S\n\x19remediation_configuration\x18\t \x03(\x0b\x32\x30.oak9.tython.aws.config.RemediationConfiguration\x12\x88\x01\n5remediation_configuration_remediation_parameter_value\x18\n \x03(\x0b\x32I.oak9.tython.aws.config.RemediationConfigurationRemediationParameterValue\"\xb1\x01\n\x0f\x43onfigRuleScope\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16\x63ompliance_resource_id\x18\x02 \x01(\t\x12!\n\x19\x63ompliance_resource_types\x18\x03 \x03(\t\x12\x0f\n\x07tag_key\x18\x04 \x01(\t\x12\x11\n\ttag_value\x18\x05 \x01(\t\"\xa2\x01\n\x16\x43onfigRuleSourceDetail\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x65vent_source\x18\x02 \x01(\t\x12#\n\x1bmaximum_execution_frequency\x18\x03 \x01(\t\x12\x14\n\x0cmessage_type\x18\x04 \x01(\t\"\xbd\x01\n\x10\x43onfigRuleSource\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x46\n\x0esource_details\x18\x03 \x03(\x0b\x32..oak9.tython.aws.config.ConfigRuleSourceDetail\x12\x19\n\x11source_identifier\x18\x04 \x01(\t\"\x96\x03\n\nConfigRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x63onfig_rule_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12Q\n\x10input_parameters\x18\x04 \x03(\x0b\x32\x37.oak9.tython.aws.config.ConfigRule.InputParametersEntry\x12#\n\x1bmaximum_execution_frequency\x18\x05 \x01(\t\x12\x36\n\x05scope\x18\x06 \x01(\x0b\x32\'.oak9.tython.aws.config.ConfigRuleScope\x12\x38\n\x06source\x18\x07 \x01(\x0b\x32(.oak9.tython.aws.config.ConfigRuleSource\x1a\x36\n\x14InputParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xad\x01\n/ConfigurationAggregatorAccountAggregationSource\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x61ll_aws_regions\x18\x02 \x01(\x08\x12\x13\n\x0b\x61ws_regions\x18\x03 \x03(\t\x12\x13\n\x0b\x61\x63\x63ount_ids\x18\x04 \x03(\t\"\xaf\x01\n4ConfigurationAggregatorOrganizationAggregationSource\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x61ll_aws_regions\x18\x02 \x01(\x08\x12\x13\n\x0b\x61ws_regions\x18\x03 \x03(\t\x12\x10\n\x08role_arn\x18\x04 \x01(\t\"\xd4\x03\n\x17\x43onfigurationAggregator\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12l\n\x1b\x61\x63\x63ount_aggregation_sources\x18\x02 \x03(\x0b\x32G.oak9.tython.aws.config.ConfigurationAggregatorAccountAggregationSource\x12%\n\x1d\x63onfiguration_aggregator_name\x18\x03 \x01(\t\x12u\n\x1forganization_aggregation_source\x18\x04 \x01(\x0b\x32L.oak9.tython.aws.config.ConfigurationAggregatorOrganizationAggregationSource\x12G\n\x04tags\x18\x05 \x03(\x0b\x32\x39.oak9.tython.aws.config.ConfigurationAggregator.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb4\x01\n#ConfigurationRecorderRecordingGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rall_supported\x18\x02 \x01(\x08\x12%\n\x1dinclude_global_resource_types\x18\x03 \x01(\x08\x12\x16\n\x0eresource_types\x18\x04 \x03(\t\"\xc6\x01\n\x15\x43onfigurationRecorder\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12T\n\x0frecording_group\x18\x03 \x01(\x0b\x32;.oak9.tython.aws.config.ConfigurationRecorderRecordingGroup\x12\x10\n\x08role_arn\x18\x04 \x01(\t\"\x98\x01\n,ConformancePackConformancePackInputParameter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0eparameter_name\x18\x02 \x01(\t\x12\x17\n\x0fparameter_value\x18\x03 \x01(\t\"\xc6\x02\n\x0f\x43onformancePack\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x63onformance_pack_name\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65livery_s3_bucket\x18\x03 \x01(\t\x12\x1e\n\x16\x64\x65livery_s3_key_prefix\x18\x04 \x01(\t\x12\x15\n\rtemplate_body\x18\x05 \x01(\t\x12\x17\n\x0ftemplate_s3_uri\x18\x06 \x01(\t\x12o\n!conformance_pack_input_parameters\x18\x07 \x03(\x0b\x32\x44.oak9.tython.aws.config.ConformancePackConformancePackInputParameter\"\x86\x01\n/DeliveryChannelConfigSnapshotDeliveryProperties\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12\x64\x65livery_frequency\x18\x02 \x01(\t\"\x94\x02\n\x0f\x44\x65liveryChannel\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12t\n#config_snapshot_delivery_properties\x18\x02 \x01(\x0b\x32G.oak9.tython.aws.config.DeliveryChannelConfigSnapshotDeliveryProperties\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0es3_bucket_name\x18\x04 \x01(\t\x12\x15\n\rs3_key_prefix\x18\x05 \x01(\t\x12\x15\n\rsns_topic_arn\x18\x06 \x01(\t\"\xc6\x02\n5OrganizationConfigRuleOrganizationManagedRuleMetadata\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rtag_key_scope\x18\x02 \x01(\t\x12\x17\n\x0ftag_value_scope\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x19\n\x11resource_id_scope\x18\x05 \x01(\t\x12\x17\n\x0frule_identifier\x18\x06 \x01(\t\x12\x1c\n\x14resource_types_scope\x18\x07 \x03(\t\x12#\n\x1bmaximum_execution_frequency\x18\x08 \x01(\t\x12\x18\n\x10input_parameters\x18\t \x01(\t\"\xf9\x02\n4OrganizationConfigRuleOrganizationCustomRuleMetadata\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rtag_key_scope\x18\x02 \x01(\t\x12\x17\n\x0ftag_value_scope\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x19\n\x11resource_id_scope\x18\x05 \x01(\t\x12\x1b\n\x13lambda_function_arn\x18\x06 \x01(\t\x12.\n&organization_config_rule_trigger_types\x18\x07 \x03(\t\x12\x1c\n\x14resource_types_scope\x18\x08 \x03(\t\x12#\n\x1bmaximum_execution_frequency\x18\t \x01(\t\x12\x18\n\x10input_parameters\x18\n \x01(\t\"\x87\x03\n\x16OrganizationConfigRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12y\n\"organization_managed_rule_metadata\x18\x02 \x01(\x0b\x32M.oak9.tython.aws.config.OrganizationConfigRuleOrganizationManagedRuleMetadata\x12%\n\x1dorganization_config_rule_name\x18\x03 \x01(\t\x12w\n!organization_custom_rule_metadata\x18\x04 \x01(\x0b\x32L.oak9.tython.aws.config.OrganizationConfigRuleOrganizationCustomRuleMetadata\x12\x19\n\x11\x65xcluded_accounts\x18\x05 \x03(\t\"\xa4\x01\n8OrganizationConformancePackConformancePackInputParameter\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0eparameter_name\x18\x02 \x01(\t\x12\x17\n\x0fparameter_value\x18\x03 \x01(\t\"\x86\x03\n\x1bOrganizationConformancePack\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12*\n\"organization_conformance_pack_name\x18\x02 \x01(\t\x12\x17\n\x0ftemplate_s3_uri\x18\x03 \x01(\t\x12\x15\n\rtemplate_body\x18\x04 \x01(\t\x12\x1a\n\x12\x64\x65livery_s3_bucket\x18\x05 \x01(\t\x12\x1e\n\x16\x64\x65livery_s3_key_prefix\x18\x06 \x01(\t\x12{\n!conformance_pack_input_parameters\x18\x07 \x03(\x0b\x32P.oak9.tython.aws.config.OrganizationConformancePackConformancePackInputParameter\x12\x19\n\x11\x65xcluded_accounts\x18\x08 \x03(\t\"\xa6\x01\n#RemediationConfigurationSsmControls\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x65rror_percentage\x18\x02 \x01(\x05\x12,\n$concurrent_execution_rate_percentage\x18\x03 \x01(\x05\"\xb7\x01\n)RemediationConfigurationExecutionControls\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12Q\n\x0cssm_controls\x18\x02 \x01(\x0b\x32;.oak9.tython.aws.config.RemediationConfigurationSsmControls\"\x82\x04\n\x18RemediationConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0etarget_version\x18\x02 \x01(\t\x12]\n\x12\x65xecution_controls\x18\x03 \x01(\x0b\x32\x41.oak9.tython.aws.config.RemediationConfigurationExecutionControls\x12T\n\nparameters\x18\x04 \x03(\x0b\x32@.oak9.tython.aws.config.RemediationConfiguration.ParametersEntry\x12\x13\n\x0btarget_type\x18\x05 \x01(\t\x12\x18\n\x10\x63onfig_rule_name\x18\x06 \x01(\t\x12\x15\n\rresource_type\x18\x07 \x01(\t\x12\x1d\n\x15retry_attempt_seconds\x18\x08 \x01(\x05\x12\"\n\x1amaximum_automatic_attempts\x18\t \x01(\x05\x12\x11\n\ttarget_id\x18\n \x01(\t\x12\x11\n\tautomatic\x18\x0b \x01(\x08\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"o\n%RemediationConfigurationResourceValue\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\"n\n#RemediationConfigurationStaticValue\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06values\x18\x02 \x03(\t\"\x96\x02\n1RemediationConfigurationRemediationParameterValue\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12U\n\x0eresource_value\x18\x02 \x01(\x0b\x32=.oak9.tython.aws.config.RemediationConfigurationResourceValue\x12Q\n\x0cstatic_value\x18\x03 \x01(\x0b\x32;.oak9.tython.aws.config.RemediationConfigurationStaticValueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AGGREGATIONAUTHORIZATION_TAGSENTRY._options = None
  _AGGREGATIONAUTHORIZATION_TAGSENTRY._serialized_options = b'8\001'
  _CONFIGRULE_INPUTPARAMETERSENTRY._options = None
  _CONFIGRULE_INPUTPARAMETERSENTRY._serialized_options = b'8\001'
  _CONFIGURATIONAGGREGATOR_TAGSENTRY._options = None
  _CONFIGURATIONAGGREGATOR_TAGSENTRY._serialized_options = b'8\001'
  _REMEDIATIONCONFIGURATION_PARAMETERSENTRY._options = None
  _REMEDIATIONCONFIGURATION_PARAMETERSENTRY._serialized_options = b'8\001'
  _AGGREGATIONAUTHORIZATION._serialized_start=70
  _AGGREGATIONAUTHORIZATION._serialized_end=334
  _AGGREGATIONAUTHORIZATION_TAGSENTRY._serialized_start=291
  _AGGREGATIONAUTHORIZATION_TAGSENTRY._serialized_end=334
  _CONFIG._serialized_start=337
  _CONFIG._serialized_end=1181
  _CONFIGRULESCOPE._serialized_start=1184
  _CONFIGRULESCOPE._serialized_end=1361
  _CONFIGRULESOURCEDETAIL._serialized_start=1364
  _CONFIGRULESOURCEDETAIL._serialized_end=1526
  _CONFIGRULESOURCE._serialized_start=1529
  _CONFIGRULESOURCE._serialized_end=1718
  _CONFIGRULE._serialized_start=1721
  _CONFIGRULE._serialized_end=2127
  _CONFIGRULE_INPUTPARAMETERSENTRY._serialized_start=2073
  _CONFIGRULE_INPUTPARAMETERSENTRY._serialized_end=2127
  _CONFIGURATIONAGGREGATORACCOUNTAGGREGATIONSOURCE._serialized_start=2130
  _CONFIGURATIONAGGREGATORACCOUNTAGGREGATIONSOURCE._serialized_end=2303
  _CONFIGURATIONAGGREGATORORGANIZATIONAGGREGATIONSOURCE._serialized_start=2306
  _CONFIGURATIONAGGREGATORORGANIZATIONAGGREGATIONSOURCE._serialized_end=2481
  _CONFIGURATIONAGGREGATOR._serialized_start=2484
  _CONFIGURATIONAGGREGATOR._serialized_end=2952
  _CONFIGURATIONAGGREGATOR_TAGSENTRY._serialized_start=291
  _CONFIGURATIONAGGREGATOR_TAGSENTRY._serialized_end=334
  _CONFIGURATIONRECORDERRECORDINGGROUP._serialized_start=2955
  _CONFIGURATIONRECORDERRECORDINGGROUP._serialized_end=3135
  _CONFIGURATIONRECORDER._serialized_start=3138
  _CONFIGURATIONRECORDER._serialized_end=3336
  _CONFORMANCEPACKCONFORMANCEPACKINPUTPARAMETER._serialized_start=3339
  _CONFORMANCEPACKCONFORMANCEPACKINPUTPARAMETER._serialized_end=3491
  _CONFORMANCEPACK._serialized_start=3494
  _CONFORMANCEPACK._serialized_end=3820
  _DELIVERYCHANNELCONFIGSNAPSHOTDELIVERYPROPERTIES._serialized_start=3823
  _DELIVERYCHANNELCONFIGSNAPSHOTDELIVERYPROPERTIES._serialized_end=3957
  _DELIVERYCHANNEL._serialized_start=3960
  _DELIVERYCHANNEL._serialized_end=4236
  _ORGANIZATIONCONFIGRULEORGANIZATIONMANAGEDRULEMETADATA._serialized_start=4239
  _ORGANIZATIONCONFIGRULEORGANIZATIONMANAGEDRULEMETADATA._serialized_end=4565
  _ORGANIZATIONCONFIGRULEORGANIZATIONCUSTOMRULEMETADATA._serialized_start=4568
  _ORGANIZATIONCONFIGRULEORGANIZATIONCUSTOMRULEMETADATA._serialized_end=4945
  _ORGANIZATIONCONFIGRULE._serialized_start=4948
  _ORGANIZATIONCONFIGRULE._serialized_end=5339
  _ORGANIZATIONCONFORMANCEPACKCONFORMANCEPACKINPUTPARAMETER._serialized_start=5342
  _ORGANIZATIONCONFORMANCEPACKCONFORMANCEPACKINPUTPARAMETER._serialized_end=5506
  _ORGANIZATIONCONFORMANCEPACK._serialized_start=5509
  _ORGANIZATIONCONFORMANCEPACK._serialized_end=5899
  _REMEDIATIONCONFIGURATIONSSMCONTROLS._serialized_start=5902
  _REMEDIATIONCONFIGURATIONSSMCONTROLS._serialized_end=6068
  _REMEDIATIONCONFIGURATIONEXECUTIONCONTROLS._serialized_start=6071
  _REMEDIATIONCONFIGURATIONEXECUTIONCONTROLS._serialized_end=6254
  _REMEDIATIONCONFIGURATION._serialized_start=6257
  _REMEDIATIONCONFIGURATION._serialized_end=6771
  _REMEDIATIONCONFIGURATION_PARAMETERSENTRY._serialized_start=6722
  _REMEDIATIONCONFIGURATION_PARAMETERSENTRY._serialized_end=6771
  _REMEDIATIONCONFIGURATIONRESOURCEVALUE._serialized_start=6773
  _REMEDIATIONCONFIGURATIONRESOURCEVALUE._serialized_end=6884
  _REMEDIATIONCONFIGURATIONSTATICVALUE._serialized_start=6886
  _REMEDIATIONCONFIGURATIONSTATICVALUE._serialized_end=6996
  _REMEDIATIONCONFIGURATIONREMEDIATIONPARAMETERVALUE._serialized_start=6999
  _REMEDIATIONCONFIGURATIONREMEDIATIONPARAMETERVALUE._serialized_end=7277
# @@protoc_insertion_point(module_scope)
