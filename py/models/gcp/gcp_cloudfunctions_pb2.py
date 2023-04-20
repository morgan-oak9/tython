# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_cloudfunctions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgcp/gcp_cloudfunctions.proto\x12\x1eoak9.tython.gcp.cloudfunctions\x1a\x13shared/shared.proto\"B\n1CloudfunctionsFunctionXEventTriggerXFailurePolicy\x12\r\n\x05retry\x18\x01 \x01(\x08\"\xb6\x01\n#CloudfunctionsFunctionXEventTrigger\x12\x12\n\nevent_type\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x02 \x01(\t\x12i\n\x0e\x66\x61ilure_policy\x18\x03 \x01(\x0b\x32Q.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXEventTriggerXFailurePolicy\"u\n1CloudfunctionsFunctionXSecretEnvironmentVariables\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"N\n-CloudfunctionsFunctionXSecretVolumesXVersions\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xbf\x01\n$CloudfunctionsFunctionXSecretVolumes\x12\x12\n\nmount_path\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\x12_\n\x08versions\x18\x04 \x03(\x0b\x32M.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXSecretVolumesXVersions\"L\n\'CloudfunctionsFunctionXSourceRepository\x12\x14\n\x0c\x64\x65ployed_url\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"_\n\x1f\x43loudfunctionsFunctionXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0c\n\x04read\x18\x03 \x01(\t\x12\x0e\n\x06update\x18\x04 \x01(\t\"\xd2\x0c\n\x16\x43loudfunctionsFunction\x12\x1b\n\x13\x61vailable_memory_mb\x18\x01 \x01(\x01\x12z\n\x1b\x62uild_environment_variables\x18\x02 \x03(\x0b\x32U.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunction.BuildEnvironmentVariablesEntry\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x17\n\x0f\x64ocker_registry\x18\x04 \x01(\t\x12\x19\n\x11\x64ocker_repository\x18\x05 \x01(\t\x12\x13\n\x0b\x65ntry_point\x18\x06 \x01(\t\x12o\n\x15\x65nvironment_variables\x18\x07 \x03(\x0b\x32P.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunction.EnvironmentVariablesEntry\x12$\n\x1chttps_trigger_security_level\x18\x08 \x01(\t\x12\x19\n\x11https_trigger_url\x18\t \x01(\t\x12\n\n\x02id\x18\n \x01(\t\x12\x18\n\x10ingress_settings\x18\x0b \x01(\t\x12\x14\n\x0ckms_key_name\x18\x0c \x01(\t\x12R\n\x06labels\x18\r \x03(\x0b\x32\x42.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunction.LabelsEntry\x12\x15\n\rmax_instances\x18\x0e \x01(\x01\x12\x15\n\rmin_instances\x18\x0f \x01(\x01\x12\x0c\n\x04name\x18\x10 \x01(\t\x12\x0f\n\x07project\x18\x11 \x01(\t\x12\x0e\n\x06region\x18\x12 \x01(\t\x12\x0f\n\x07runtime\x18\x13 \x01(\t\x12\x1d\n\x15service_account_email\x18\x14 \x01(\t\x12\x1d\n\x15source_archive_bucket\x18\x15 \x01(\t\x12\x1d\n\x15source_archive_object\x18\x16 \x01(\t\x12\x0f\n\x07timeout\x18\x17 \x01(\x01\x12\x14\n\x0ctrigger_http\x18\x18 \x01(\x08\x12\x15\n\rvpc_connector\x18\x19 \x01(\t\x12%\n\x1dvpc_connector_egress_settings\x18\x1a \x01(\t\x12Z\n\revent_trigger\x18\x1b \x01(\x0b\x32\x43.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXEventTrigger\x12w\n\x1csecret_environment_variables\x18\x1c \x03(\x0b\x32Q.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXSecretEnvironmentVariables\x12\\\n\x0esecret_volumes\x18\x1d \x03(\x0b\x32\x44.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXSecretVolumes\x12\x62\n\x11source_repository\x18\x1e \x01(\x0b\x32G.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXSourceRepository\x12Q\n\x08timeouts\x18\x1f \x01(\x0b\x32?.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionXTimeouts\x12\x37\n\rresource_info\x18  \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a@\n\x1e\x42uildEnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19\x45nvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"d\n*CloudfunctionsFunctionIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xac\x02\n CloudfunctionsFunctionIamBinding\x12\x16\n\x0e\x63loud_function\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12]\n\tcondition\x18\x08 \x01(\x0b\x32J.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"c\n)CloudfunctionsFunctionIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xa9\x02\n\x1f\x43loudfunctionsFunctionIamMember\x12\x16\n\x0e\x63loud_function\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12\\\n\tcondition\x18\x08 \x01(\x0b\x32I.oak9.tython.gcp.cloudfunctions.CloudfunctionsFunctionIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xc2\x01\n\x1f\x43loudfunctionsFunctionIamPolicy\x12\x16\n\x0e\x63loud_function\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_cloudfunctions_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLOUDFUNCTIONSFUNCTION_BUILDENVIRONMENTVARIABLESENTRY._options = None
  _CLOUDFUNCTIONSFUNCTION_BUILDENVIRONMENTVARIABLESENTRY._serialized_options = b'8\001'
  _CLOUDFUNCTIONSFUNCTION_ENVIRONMENTVARIABLESENTRY._options = None
  _CLOUDFUNCTIONSFUNCTION_ENVIRONMENTVARIABLESENTRY._serialized_options = b'8\001'
  _CLOUDFUNCTIONSFUNCTION_LABELSENTRY._options = None
  _CLOUDFUNCTIONSFUNCTION_LABELSENTRY._serialized_options = b'8\001'
  _CLOUDFUNCTIONSFUNCTIONXEVENTTRIGGERXFAILUREPOLICY._serialized_start=85
  _CLOUDFUNCTIONSFUNCTIONXEVENTTRIGGERXFAILUREPOLICY._serialized_end=151
  _CLOUDFUNCTIONSFUNCTIONXEVENTTRIGGER._serialized_start=154
  _CLOUDFUNCTIONSFUNCTIONXEVENTTRIGGER._serialized_end=336
  _CLOUDFUNCTIONSFUNCTIONXSECRETENVIRONMENTVARIABLES._serialized_start=338
  _CLOUDFUNCTIONSFUNCTIONXSECRETENVIRONMENTVARIABLES._serialized_end=455
  _CLOUDFUNCTIONSFUNCTIONXSECRETVOLUMESXVERSIONS._serialized_start=457
  _CLOUDFUNCTIONSFUNCTIONXSECRETVOLUMESXVERSIONS._serialized_end=535
  _CLOUDFUNCTIONSFUNCTIONXSECRETVOLUMES._serialized_start=538
  _CLOUDFUNCTIONSFUNCTIONXSECRETVOLUMES._serialized_end=729
  _CLOUDFUNCTIONSFUNCTIONXSOURCEREPOSITORY._serialized_start=731
  _CLOUDFUNCTIONSFUNCTIONXSOURCEREPOSITORY._serialized_end=807
  _CLOUDFUNCTIONSFUNCTIONXTIMEOUTS._serialized_start=809
  _CLOUDFUNCTIONSFUNCTIONXTIMEOUTS._serialized_end=904
  _CLOUDFUNCTIONSFUNCTION._serialized_start=907
  _CLOUDFUNCTIONSFUNCTION._serialized_end=2525
  _CLOUDFUNCTIONSFUNCTION_BUILDENVIRONMENTVARIABLESENTRY._serialized_start=2353
  _CLOUDFUNCTIONSFUNCTION_BUILDENVIRONMENTVARIABLESENTRY._serialized_end=2417
  _CLOUDFUNCTIONSFUNCTION_ENVIRONMENTVARIABLESENTRY._serialized_start=2419
  _CLOUDFUNCTIONSFUNCTION_ENVIRONMENTVARIABLESENTRY._serialized_end=2478
  _CLOUDFUNCTIONSFUNCTION_LABELSENTRY._serialized_start=2480
  _CLOUDFUNCTIONSFUNCTION_LABELSENTRY._serialized_end=2525
  _CLOUDFUNCTIONSFUNCTIONIAMBINDINGXCONDITION._serialized_start=2527
  _CLOUDFUNCTIONSFUNCTIONIAMBINDINGXCONDITION._serialized_end=2627
  _CLOUDFUNCTIONSFUNCTIONIAMBINDING._serialized_start=2630
  _CLOUDFUNCTIONSFUNCTIONIAMBINDING._serialized_end=2930
  _CLOUDFUNCTIONSFUNCTIONIAMMEMBERXCONDITION._serialized_start=2932
  _CLOUDFUNCTIONSFUNCTIONIAMMEMBERXCONDITION._serialized_end=3031
  _CLOUDFUNCTIONSFUNCTIONIAMMEMBER._serialized_start=3034
  _CLOUDFUNCTIONSFUNCTIONIAMMEMBER._serialized_end=3331
  _CLOUDFUNCTIONSFUNCTIONIAMPOLICY._serialized_start=3334
  _CLOUDFUNCTIONSFUNCTIONIAMPOLICY._serialized_end=3528
# @@protoc_insertion_point(module_scope)
