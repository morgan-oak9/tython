# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_recaptcha.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17gcp/gcp_recaptcha.proto\x12\x19oak9.tython.gcp.recaptcha\x1a\x13shared/shared.proto\"h\n&RecaptchaEnterpriseKeyXAndroidSettings\x12\x1f\n\x17\x61llow_all_package_names\x18\x01 \x01(\x08\x12\x1d\n\x15\x61llowed_package_names\x18\x02 \x03(\t\"^\n\"RecaptchaEnterpriseKeyXIosSettings\x12\x1c\n\x14\x61llow_all_bundle_ids\x18\x01 \x01(\x08\x12\x1a\n\x12\x61llowed_bundle_ids\x18\x02 \x03(\t\"Y\n%RecaptchaEnterpriseKeyXTestingOptions\x12\x19\n\x11testing_challenge\x18\x01 \x01(\t\x12\x15\n\rtesting_score\x18\x02 \x01(\x01\"Q\n\x1fRecaptchaEnterpriseKeyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xb4\x01\n\"RecaptchaEnterpriseKeyXWebSettings\x12\x19\n\x11\x61llow_all_domains\x18\x01 \x01(\x08\x12\x19\n\x11\x61llow_amp_traffic\x18\x02 \x01(\x08\x12\x17\n\x0f\x61llowed_domains\x18\x03 \x03(\t\x12%\n\x1d\x63hallenge_security_preference\x18\x04 \x01(\t\x12\x18\n\x10integration_type\x18\x05 \x01(\t\"\xd5\x05\n\x16RecaptchaEnterpriseKey\x12\x13\n\x0b\x63reate_time\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12M\n\x06labels\x18\x04 \x03(\x0b\x32=.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKey.LabelsEntry\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12[\n\x10\x61ndroid_settings\x18\x07 \x01(\x0b\x32\x41.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKeyXAndroidSettings\x12S\n\x0cios_settings\x18\x08 \x01(\x0b\x32=.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKeyXIosSettings\x12Y\n\x0ftesting_options\x18\t \x01(\x0b\x32@.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKeyXTestingOptions\x12L\n\x08timeouts\x18\n \x01(\x0b\x32:.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKeyXTimeouts\x12S\n\x0cweb_settings\x18\x0b \x01(\x0b\x32=.oak9.tython.gcp.recaptcha.RecaptchaEnterpriseKeyXWebSettings\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_recaptcha_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECAPTCHAENTERPRISEKEY_LABELSENTRY._options = None
  _RECAPTCHAENTERPRISEKEY_LABELSENTRY._serialized_options = b'8\001'
  _RECAPTCHAENTERPRISEKEYXANDROIDSETTINGS._serialized_start=75
  _RECAPTCHAENTERPRISEKEYXANDROIDSETTINGS._serialized_end=179
  _RECAPTCHAENTERPRISEKEYXIOSSETTINGS._serialized_start=181
  _RECAPTCHAENTERPRISEKEYXIOSSETTINGS._serialized_end=275
  _RECAPTCHAENTERPRISEKEYXTESTINGOPTIONS._serialized_start=277
  _RECAPTCHAENTERPRISEKEYXTESTINGOPTIONS._serialized_end=366
  _RECAPTCHAENTERPRISEKEYXTIMEOUTS._serialized_start=368
  _RECAPTCHAENTERPRISEKEYXTIMEOUTS._serialized_end=449
  _RECAPTCHAENTERPRISEKEYXWEBSETTINGS._serialized_start=452
  _RECAPTCHAENTERPRISEKEYXWEBSETTINGS._serialized_end=632
  _RECAPTCHAENTERPRISEKEY._serialized_start=635
  _RECAPTCHAENTERPRISEKEY._serialized_end=1360
  _RECAPTCHAENTERPRISEKEY_LABELSENTRY._serialized_start=1315
  _RECAPTCHAENTERPRISEKEY_LABELSENTRY._serialized_end=1360
# @@protoc_insertion_point(module_scope)
