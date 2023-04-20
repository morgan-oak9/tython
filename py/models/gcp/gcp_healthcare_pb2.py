# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_healthcare.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18gcp/gcp_healthcare.proto\x12\x1aoak9.tython.gcp.healthcare\x1a\x13shared/shared.proto\"Q\n\x1fHealthcareConsentStoreXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x90\x03\n\x16HealthcareConsentStore\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\x1b\n\x13\x64\x65\x66\x61ult_consent_ttl\x18\x02 \x01(\t\x12\'\n\x1f\x65nable_consent_create_on_update\x18\x03 \x01(\x08\x12\n\n\x02id\x18\x04 \x01(\t\x12N\n\x06labels\x18\x05 \x03(\x0b\x32>.oak9.tython.gcp.healthcare.HealthcareConsentStore.LabelsEntry\x12\x0c\n\x04name\x18\x06 \x01(\t\x12M\n\x08timeouts\x18\x07 \x01(\x0b\x32;.oak9.tython.gcp.healthcare.HealthcareConsentStoreXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"d\n*HealthcareConsentStoreIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x9a\x02\n HealthcareConsentStoreIamBinding\x12\x18\n\x10\x63onsent_store_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0f\n\x07members\x18\x05 \x03(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12Y\n\tcondition\x18\x07 \x01(\x0b\x32\x46.oak9.tython.gcp.healthcare.HealthcareConsentStoreIamBindingXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"c\n)HealthcareConsentStoreIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x97\x02\n\x1fHealthcareConsentStoreIamMember\x12\x18\n\x10\x63onsent_store_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0e\n\x06member\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12X\n\tcondition\x18\x07 \x01(\x0b\x32\x45.oak9.tython.gcp.healthcare.HealthcareConsentStoreIamMemberXCondition\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xb4\x01\n\x1fHealthcareConsentStoreIamPolicy\x12\x18\n\x10\x63onsent_store_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x05 \x01(\t\x12\x37\n\rresource_info\x18\x06 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"L\n\x1aHealthcareDatasetXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xf9\x01\n\x11HealthcareDataset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\x12\x11\n\ttime_zone\x18\x06 \x01(\t\x12H\n\x08timeouts\x18\x07 \x01(\x0b\x32\x36.oak9.tython.gcp.healthcare.HealthcareDatasetXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"_\n%HealthcareDatasetIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xf9\x01\n\x1bHealthcareDatasetIamBinding\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12T\n\tcondition\x18\x06 \x01(\x0b\x32\x41.oak9.tython.gcp.healthcare.HealthcareDatasetIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"^\n$HealthcareDatasetIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xf6\x01\n\x1aHealthcareDatasetIamMember\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12S\n\tcondition\x18\x06 \x01(\x0b\x32@.oak9.tython.gcp.healthcare.HealthcareDatasetIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x98\x01\n\x1aHealthcareDatasetIamPolicy\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"?\n\'HealthcareDicomStoreXNotificationConfig\x12\x14\n\x0cpubsub_topic\x18\x01 \x01(\t\"O\n\x1dHealthcareDicomStoreXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xb9\x03\n\x14HealthcareDicomStore\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12L\n\x06labels\x18\x03 \x03(\x0b\x32<.oak9.tython.gcp.healthcare.HealthcareDicomStore.LabelsEntry\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\x12`\n\x13notification_config\x18\x06 \x01(\x0b\x32\x43.oak9.tython.gcp.healthcare.HealthcareDicomStoreXNotificationConfig\x12K\n\x08timeouts\x18\x07 \x01(\x0b\x32\x39.oak9.tython.gcp.healthcare.HealthcareDicomStoreXTimeouts\x12\x37\n\rresource_info\x18\x08 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n(HealthcareDicomStoreIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x83\x02\n\x1eHealthcareDicomStoreIamBinding\x12\x16\n\x0e\x64icom_store_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12W\n\tcondition\x18\x06 \x01(\x0b\x32\x44.oak9.tython.gcp.healthcare.HealthcareDicomStoreIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"a\n\'HealthcareDicomStoreIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x80\x02\n\x1dHealthcareDicomStoreIamMember\x12\x16\n\x0e\x64icom_store_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12V\n\tcondition\x18\x06 \x01(\x0b\x32\x43.oak9.tython.gcp.healthcare.HealthcareDicomStoreIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x9f\x01\n\x1dHealthcareDicomStoreIamPolicy\x12\x16\n\x0e\x64icom_store_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\">\n&HealthcareFhirStoreXNotificationConfig\x12\x14\n\x0cpubsub_topic\x18\x01 \x01(\t\"|\nBHealthcareFhirStoreXStreamConfigsXBigqueryDestinationXSchemaConfig\x12!\n\x19recursive_structure_depth\x18\x01 \x01(\x01\x12\x13\n\x0bschema_type\x18\x02 \x01(\t\"\xc3\x01\n5HealthcareFhirStoreXStreamConfigsXBigqueryDestination\x12\x13\n\x0b\x64\x61taset_uri\x18\x01 \x01(\t\x12u\n\rschema_config\x18\x02 \x01(\x0b\x32^.oak9.tython.gcp.healthcare.HealthcareFhirStoreXStreamConfigsXBigqueryDestinationXSchemaConfig\"\xac\x01\n!HealthcareFhirStoreXStreamConfigs\x12\x16\n\x0eresource_types\x18\x01 \x03(\t\x12o\n\x14\x62igquery_destination\x18\x02 \x01(\x0b\x32Q.oak9.tython.gcp.healthcare.HealthcareFhirStoreXStreamConfigsXBigqueryDestination\"N\n\x1cHealthcareFhirStoreXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xa6\x05\n\x13HealthcareFhirStore\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12%\n\x1d\x64isable_referential_integrity\x18\x02 \x01(\x08\x12#\n\x1b\x64isable_resource_versioning\x18\x03 \x01(\x08\x12\x1d\n\x15\x65nable_history_import\x18\x04 \x01(\x08\x12\x1c\n\x14\x65nable_update_create\x18\x05 \x01(\x08\x12\n\n\x02id\x18\x06 \x01(\t\x12K\n\x06labels\x18\x07 \x03(\x0b\x32;.oak9.tython.gcp.healthcare.HealthcareFhirStore.LabelsEntry\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x11\n\tself_link\x18\t \x01(\t\x12\x0f\n\x07version\x18\n \x01(\t\x12_\n\x13notification_config\x18\x0b \x01(\x0b\x32\x42.oak9.tython.gcp.healthcare.HealthcareFhirStoreXNotificationConfig\x12U\n\x0estream_configs\x18\x0c \x03(\x0b\x32=.oak9.tython.gcp.healthcare.HealthcareFhirStoreXStreamConfigs\x12J\n\x08timeouts\x18\r \x01(\x0b\x32\x38.oak9.tython.gcp.healthcare.HealthcareFhirStoreXTimeouts\x12\x37\n\rresource_info\x18\x0e \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"a\n\'HealthcareFhirStoreIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x80\x02\n\x1dHealthcareFhirStoreIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x15\n\rfhir_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12V\n\tcondition\x18\x06 \x01(\x0b\x32\x43.oak9.tython.gcp.healthcare.HealthcareFhirStoreIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"`\n&HealthcareFhirStoreIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xfd\x01\n\x1cHealthcareFhirStoreIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x15\n\rfhir_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12U\n\tcondition\x18\x06 \x01(\x0b\x32\x42.oak9.tython.gcp.healthcare.HealthcareFhirStoreIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\x9d\x01\n\x1cHealthcareFhirStoreIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x15\n\rfhir_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"?\n\'HealthcareHl7V2StoreXNotificationConfig\x12\x14\n\x0cpubsub_topic\x18\x01 \x01(\t\"P\n(HealthcareHl7V2StoreXNotificationConfigs\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x14\n\x0cpubsub_topic\x18\x02 \x01(\t\"{\n!HealthcareHl7V2StoreXParserConfig\x12\x19\n\x11\x61llow_null_header\x18\x01 \x01(\x08\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x1a\n\x12segment_terminator\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"O\n\x1dHealthcareHl7V2StoreXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xf3\x04\n\x14HealthcareHl7V2Store\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12L\n\x06labels\x18\x03 \x03(\x0b\x32<.oak9.tython.gcp.healthcare.HealthcareHl7V2Store.LabelsEntry\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\x12`\n\x13notification_config\x18\x06 \x01(\x0b\x32\x43.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreXNotificationConfig\x12\x62\n\x14notification_configs\x18\x07 \x03(\x0b\x32\x44.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreXNotificationConfigs\x12T\n\rparser_config\x18\x08 \x01(\x0b\x32=.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreXParserConfig\x12K\n\x08timeouts\x18\t \x01(\x0b\x32\x39.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreXTimeouts\x12\x37\n\rresource_info\x18\n \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n(HealthcareHl7V2StoreIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x84\x02\n\x1eHealthcareHl7V2StoreIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x17\n\x0fhl7_v2_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12W\n\tcondition\x18\x06 \x01(\x0b\x32\x44.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreIamBindingXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"a\n\'HealthcareHl7V2StoreIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x81\x02\n\x1dHealthcareHl7V2StoreIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x17\n\x0fhl7_v2_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06member\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12V\n\tcondition\x18\x06 \x01(\x0b\x32\x43.oak9.tython.gcp.healthcare.HealthcareHl7V2StoreIamMemberXCondition\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xa0\x01\n\x1dHealthcareHl7V2StoreIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x17\n\x0fhl7_v2_store_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x37\n\rresource_info\x18\x05 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_healthcare_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEALTHCARECONSENTSTORE_LABELSENTRY._options = None
  _HEALTHCARECONSENTSTORE_LABELSENTRY._serialized_options = b'8\001'
  _HEALTHCAREDICOMSTORE_LABELSENTRY._options = None
  _HEALTHCAREDICOMSTORE_LABELSENTRY._serialized_options = b'8\001'
  _HEALTHCAREFHIRSTORE_LABELSENTRY._options = None
  _HEALTHCAREFHIRSTORE_LABELSENTRY._serialized_options = b'8\001'
  _HEALTHCAREHL7V2STORE_LABELSENTRY._options = None
  _HEALTHCAREHL7V2STORE_LABELSENTRY._serialized_options = b'8\001'
  _HEALTHCARECONSENTSTOREXTIMEOUTS._serialized_start=77
  _HEALTHCARECONSENTSTOREXTIMEOUTS._serialized_end=158
  _HEALTHCARECONSENTSTORE._serialized_start=161
  _HEALTHCARECONSENTSTORE._serialized_end=561
  _HEALTHCARECONSENTSTORE_LABELSENTRY._serialized_start=516
  _HEALTHCARECONSENTSTORE_LABELSENTRY._serialized_end=561
  _HEALTHCARECONSENTSTOREIAMBINDINGXCONDITION._serialized_start=563
  _HEALTHCARECONSENTSTOREIAMBINDINGXCONDITION._serialized_end=663
  _HEALTHCARECONSENTSTOREIAMBINDING._serialized_start=666
  _HEALTHCARECONSENTSTOREIAMBINDING._serialized_end=948
  _HEALTHCARECONSENTSTOREIAMMEMBERXCONDITION._serialized_start=950
  _HEALTHCARECONSENTSTOREIAMMEMBERXCONDITION._serialized_end=1049
  _HEALTHCARECONSENTSTOREIAMMEMBER._serialized_start=1052
  _HEALTHCARECONSENTSTOREIAMMEMBER._serialized_end=1331
  _HEALTHCARECONSENTSTOREIAMPOLICY._serialized_start=1334
  _HEALTHCARECONSENTSTOREIAMPOLICY._serialized_end=1514
  _HEALTHCAREDATASETXTIMEOUTS._serialized_start=1516
  _HEALTHCAREDATASETXTIMEOUTS._serialized_end=1592
  _HEALTHCAREDATASET._serialized_start=1595
  _HEALTHCAREDATASET._serialized_end=1844
  _HEALTHCAREDATASETIAMBINDINGXCONDITION._serialized_start=1846
  _HEALTHCAREDATASETIAMBINDINGXCONDITION._serialized_end=1941
  _HEALTHCAREDATASETIAMBINDING._serialized_start=1944
  _HEALTHCAREDATASETIAMBINDING._serialized_end=2193
  _HEALTHCAREDATASETIAMMEMBERXCONDITION._serialized_start=2195
  _HEALTHCAREDATASETIAMMEMBERXCONDITION._serialized_end=2289
  _HEALTHCAREDATASETIAMMEMBER._serialized_start=2292
  _HEALTHCAREDATASETIAMMEMBER._serialized_end=2538
  _HEALTHCAREDATASETIAMPOLICY._serialized_start=2541
  _HEALTHCAREDATASETIAMPOLICY._serialized_end=2693
  _HEALTHCAREDICOMSTOREXNOTIFICATIONCONFIG._serialized_start=2695
  _HEALTHCAREDICOMSTOREXNOTIFICATIONCONFIG._serialized_end=2758
  _HEALTHCAREDICOMSTOREXTIMEOUTS._serialized_start=2760
  _HEALTHCAREDICOMSTOREXTIMEOUTS._serialized_end=2839
  _HEALTHCAREDICOMSTORE._serialized_start=2842
  _HEALTHCAREDICOMSTORE._serialized_end=3283
  _HEALTHCAREDICOMSTORE_LABELSENTRY._serialized_start=516
  _HEALTHCAREDICOMSTORE_LABELSENTRY._serialized_end=561
  _HEALTHCAREDICOMSTOREIAMBINDINGXCONDITION._serialized_start=3285
  _HEALTHCAREDICOMSTOREIAMBINDINGXCONDITION._serialized_end=3383
  _HEALTHCAREDICOMSTOREIAMBINDING._serialized_start=3386
  _HEALTHCAREDICOMSTOREIAMBINDING._serialized_end=3645
  _HEALTHCAREDICOMSTOREIAMMEMBERXCONDITION._serialized_start=3647
  _HEALTHCAREDICOMSTOREIAMMEMBERXCONDITION._serialized_end=3744
  _HEALTHCAREDICOMSTOREIAMMEMBER._serialized_start=3747
  _HEALTHCAREDICOMSTOREIAMMEMBER._serialized_end=4003
  _HEALTHCAREDICOMSTOREIAMPOLICY._serialized_start=4006
  _HEALTHCAREDICOMSTOREIAMPOLICY._serialized_end=4165
  _HEALTHCAREFHIRSTOREXNOTIFICATIONCONFIG._serialized_start=4167
  _HEALTHCAREFHIRSTOREXNOTIFICATIONCONFIG._serialized_end=4229
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGSXBIGQUERYDESTINATIONXSCHEMACONFIG._serialized_start=4231
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGSXBIGQUERYDESTINATIONXSCHEMACONFIG._serialized_end=4355
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGSXBIGQUERYDESTINATION._serialized_start=4358
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGSXBIGQUERYDESTINATION._serialized_end=4553
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGS._serialized_start=4556
  _HEALTHCAREFHIRSTOREXSTREAMCONFIGS._serialized_end=4728
  _HEALTHCAREFHIRSTOREXTIMEOUTS._serialized_start=4730
  _HEALTHCAREFHIRSTOREXTIMEOUTS._serialized_end=4808
  _HEALTHCAREFHIRSTORE._serialized_start=4811
  _HEALTHCAREFHIRSTORE._serialized_end=5489
  _HEALTHCAREFHIRSTORE_LABELSENTRY._serialized_start=516
  _HEALTHCAREFHIRSTORE_LABELSENTRY._serialized_end=561
  _HEALTHCAREFHIRSTOREIAMBINDINGXCONDITION._serialized_start=5491
  _HEALTHCAREFHIRSTOREIAMBINDINGXCONDITION._serialized_end=5588
  _HEALTHCAREFHIRSTOREIAMBINDING._serialized_start=5591
  _HEALTHCAREFHIRSTOREIAMBINDING._serialized_end=5847
  _HEALTHCAREFHIRSTOREIAMMEMBERXCONDITION._serialized_start=5849
  _HEALTHCAREFHIRSTOREIAMMEMBERXCONDITION._serialized_end=5945
  _HEALTHCAREFHIRSTOREIAMMEMBER._serialized_start=5948
  _HEALTHCAREFHIRSTOREIAMMEMBER._serialized_end=6201
  _HEALTHCAREFHIRSTOREIAMPOLICY._serialized_start=6204
  _HEALTHCAREFHIRSTOREIAMPOLICY._serialized_end=6361
  _HEALTHCAREHL7V2STOREXNOTIFICATIONCONFIG._serialized_start=6363
  _HEALTHCAREHL7V2STOREXNOTIFICATIONCONFIG._serialized_end=6426
  _HEALTHCAREHL7V2STOREXNOTIFICATIONCONFIGS._serialized_start=6428
  _HEALTHCAREHL7V2STOREXNOTIFICATIONCONFIGS._serialized_end=6508
  _HEALTHCAREHL7V2STOREXPARSERCONFIG._serialized_start=6510
  _HEALTHCAREHL7V2STOREXPARSERCONFIG._serialized_end=6633
  _HEALTHCAREHL7V2STOREXTIMEOUTS._serialized_start=6635
  _HEALTHCAREHL7V2STOREXTIMEOUTS._serialized_end=6714
  _HEALTHCAREHL7V2STORE._serialized_start=6717
  _HEALTHCAREHL7V2STORE._serialized_end=7344
  _HEALTHCAREHL7V2STORE_LABELSENTRY._serialized_start=516
  _HEALTHCAREHL7V2STORE_LABELSENTRY._serialized_end=561
  _HEALTHCAREHL7V2STOREIAMBINDINGXCONDITION._serialized_start=7346
  _HEALTHCAREHL7V2STOREIAMBINDINGXCONDITION._serialized_end=7444
  _HEALTHCAREHL7V2STOREIAMBINDING._serialized_start=7447
  _HEALTHCAREHL7V2STOREIAMBINDING._serialized_end=7707
  _HEALTHCAREHL7V2STOREIAMMEMBERXCONDITION._serialized_start=7709
  _HEALTHCAREHL7V2STOREIAMMEMBERXCONDITION._serialized_end=7806
  _HEALTHCAREHL7V2STOREIAMMEMBER._serialized_start=7809
  _HEALTHCAREHL7V2STOREIAMMEMBER._serialized_end=8066
  _HEALTHCAREHL7V2STOREIAMPOLICY._serialized_start=8069
  _HEALTHCAREHL7V2STOREIAMPOLICY._serialized_end=8229
# @@protoc_insertion_point(module_scope)