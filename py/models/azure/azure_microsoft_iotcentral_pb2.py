# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_iotcentral.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&azure/azure_microsoft_iotcentral.proto\x12&oak9.tython.azure.microsoft_iotcentral\x1a\x13shared/shared.proto\"Y\n\x14Microsoft_IotCentral\x12\x41\n\x08iot_apps\x18\x01 \x03(\x0b\x32/.oak9.tython.azure.microsoft_iotcentral.IotApps\"\xbc\x03\n\x07IotApps\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12W\n\x08identity\x18\x02 \x01(\x0b\x32\x45.oak9.tython.azure.microsoft_iotcentral.SystemAssignedServiceIdentity\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x11\n\tsubdomain\x18\x07 \x01(\t\x12\x10\n\x08template\x18\x08 \x01(\t\x12?\n\x03sku\x18\t \x01(\x0b\x32\x32.oak9.tython.azure.microsoft_iotcentral.AppSkuInfo\x12G\n\x04tags\x18\n \x03(\x0b\x32\x39.oak9.tython.azure.microsoft_iotcentral.IotApps.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1a\n\nAppSkuInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"-\n\x1dSystemAssignedServiceIdentity\x12\x0c\n\x04type\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_iotcentral_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IOTAPPS_TAGSENTRY._options = None
  _IOTAPPS_TAGSENTRY._serialized_options = b'8\001'
  _MICROSOFT_IOTCENTRAL._serialized_start=103
  _MICROSOFT_IOTCENTRAL._serialized_end=192
  _IOTAPPS._serialized_start=195
  _IOTAPPS._serialized_end=639
  _IOTAPPS_TAGSENTRY._serialized_start=596
  _IOTAPPS_TAGSENTRY._serialized_end=639
  _APPSKUINFO._serialized_start=641
  _APPSKUINFO._serialized_end=667
  _SYSTEMASSIGNEDSERVICEIDENTITY._serialized_start=669
  _SYSTEMASSIGNEDSERVICEIDENTITY._serialized_end=714
# @@protoc_insertion_point(module_scope)
