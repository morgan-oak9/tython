# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_ml.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10gcp/gcp_ml.proto\x12\x12oak9.tython.gcp.ml\x1a\x13shared/shared.proto\",\n\x1cMlEngineModelXDefaultVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\x16MlEngineModelXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\xde\x03\n\rMlEngineModel\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12=\n\x06labels\x18\x03 \x03(\x0b\x32-.oak9.tython.gcp.ml.MlEngineModel.LabelsEntry\x12\x0c\n\x04name\x18\x04 \x01(\t\x12)\n!online_prediction_console_logging\x18\x05 \x01(\x08\x12!\n\x19online_prediction_logging\x18\x06 \x01(\x08\x12\x0f\n\x07project\x18\x07 \x01(\t\x12\x0f\n\x07regions\x18\x08 \x03(\t\x12I\n\x0f\x64\x65\x66\x61ult_version\x18\t \x01(\x0b\x32\x30.oak9.tython.gcp.ml.MlEngineModelXDefaultVersion\x12<\n\x08timeouts\x18\n \x01(\x0b\x32*.oak9.tython.gcp.ml.MlEngineModelXTimeouts\x12\x37\n\rresource_info\x18\x0b \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_ml_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MLENGINEMODEL_LABELSENTRY._options = None
  _MLENGINEMODEL_LABELSENTRY._serialized_options = b'8\001'
  _MLENGINEMODELXDEFAULTVERSION._serialized_start=61
  _MLENGINEMODELXDEFAULTVERSION._serialized_end=105
  _MLENGINEMODELXTIMEOUTS._serialized_start=107
  _MLENGINEMODELXTIMEOUTS._serialized_end=163
  _MLENGINEMODEL._serialized_start=166
  _MLENGINEMODEL._serialized_end=644
  _MLENGINEMODEL_LABELSENTRY._serialized_start=599
  _MLENGINEMODEL_LABELSENTRY._serialized_end=644
# @@protoc_insertion_point(module_scope)
