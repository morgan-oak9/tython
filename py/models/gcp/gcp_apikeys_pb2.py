# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_apikeys.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gcp/gcp_apikeys.proto\x12\x17oak9.tython.gcp.apikeys\x1a\x13shared/shared.proto\"t\nBApikeysKeyXRestrictionsXAndroidKeyRestrictionsXAllowedApplications\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x18\n\x10sha1_fingerprint\x18\x02 \x01(\t\"\xab\x01\n.ApikeysKeyXRestrictionsXAndroidKeyRestrictions\x12y\n\x14\x61llowed_applications\x18\x01 \x03(\x0b\x32[.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXAndroidKeyRestrictionsXAllowedApplications\"F\n\"ApikeysKeyXRestrictionsXApiTargets\x12\x0f\n\x07methods\x18\x01 \x03(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"K\n.ApikeysKeyXRestrictionsXBrowserKeyRestrictions\x12\x19\n\x11\x61llowed_referrers\x18\x01 \x03(\t\"H\n*ApikeysKeyXRestrictionsXIosKeyRestrictions\x12\x1a\n\x12\x61llowed_bundle_ids\x18\x01 \x03(\t\"D\n-ApikeysKeyXRestrictionsXServerKeyRestrictions\x12\x13\n\x0b\x61llowed_ips\x18\x01 \x03(\t\"\x8d\x04\n\x17\x41pikeysKeyXRestrictions\x12i\n\x18\x61ndroid_key_restrictions\x18\x01 \x01(\x0b\x32G.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXAndroidKeyRestrictions\x12P\n\x0b\x61pi_targets\x18\x02 \x03(\x0b\x32;.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXApiTargets\x12i\n\x18\x62rowser_key_restrictions\x18\x03 \x01(\x0b\x32G.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXBrowserKeyRestrictions\x12\x61\n\x14ios_key_restrictions\x18\x04 \x01(\x0b\x32\x43.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXIosKeyRestrictions\x12g\n\x17server_key_restrictions\x18\x05 \x01(\x0b\x32\x46.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictionsXServerKeyRestrictions\"E\n\x13\x41pikeysKeyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xaf\x02\n\nApikeysKey\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\nkey_string\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0b\n\x03uid\x18\x06 \x01(\t\x12\x46\n\x0crestrictions\x18\x07 \x01(\x0b\x32\x30.oak9.tython.gcp.apikeys.ApikeysKeyXRestrictions\x12>\n\x08timeouts\x18\x08 \x01(\x0b\x32,.oak9.tython.gcp.apikeys.ApikeysKeyXTimeouts\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_apikeys_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APIKEYSKEYXRESTRICTIONSXANDROIDKEYRESTRICTIONSXALLOWEDAPPLICATIONS._serialized_start=71
  _APIKEYSKEYXRESTRICTIONSXANDROIDKEYRESTRICTIONSXALLOWEDAPPLICATIONS._serialized_end=187
  _APIKEYSKEYXRESTRICTIONSXANDROIDKEYRESTRICTIONS._serialized_start=190
  _APIKEYSKEYXRESTRICTIONSXANDROIDKEYRESTRICTIONS._serialized_end=361
  _APIKEYSKEYXRESTRICTIONSXAPITARGETS._serialized_start=363
  _APIKEYSKEYXRESTRICTIONSXAPITARGETS._serialized_end=433
  _APIKEYSKEYXRESTRICTIONSXBROWSERKEYRESTRICTIONS._serialized_start=435
  _APIKEYSKEYXRESTRICTIONSXBROWSERKEYRESTRICTIONS._serialized_end=510
  _APIKEYSKEYXRESTRICTIONSXIOSKEYRESTRICTIONS._serialized_start=512
  _APIKEYSKEYXRESTRICTIONSXIOSKEYRESTRICTIONS._serialized_end=584
  _APIKEYSKEYXRESTRICTIONSXSERVERKEYRESTRICTIONS._serialized_start=586
  _APIKEYSKEYXRESTRICTIONSXSERVERKEYRESTRICTIONS._serialized_end=654
  _APIKEYSKEYXRESTRICTIONS._serialized_start=657
  _APIKEYSKEYXRESTRICTIONS._serialized_end=1182
  _APIKEYSKEYXTIMEOUTS._serialized_start=1184
  _APIKEYSKEYXTIMEOUTS._serialized_end=1253
  _APIKEYSKEY._serialized_start=1256
  _APIKEYSKEY._serialized_end=1559
# @@protoc_insertion_point(module_scope)
