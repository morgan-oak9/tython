# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_datapipeline.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61ws/aws_datapipeline.proto\x12\x1coak9.tython.aws.datapipeline\x1a\x13shared/shared.proto\"x\n\x1aPipelineParameterAttribute\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\"\xac\x01\n\x17PipelineParameterObject\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12L\n\nattributes\x18\x02 \x03(\x0b\x32\x38.oak9.tython.aws.datapipeline.PipelineParameterAttribute\x12\n\n\x02id\x18\x03 \x01(\t\"s\n\x16PipelineParameterValue\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\"~\n\rPipelineField\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x11\n\tref_value\x18\x03 \x01(\t\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\"\xa8\x01\n\x16PipelinePipelineObject\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12;\n\x06\x66ields\x18\x02 \x03(\x0b\x32+.oak9.tython.aws.datapipeline.PipelineField\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"j\n\x13PipelinePipelineTag\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xb4\x03\n\x08Pipeline\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x61\x63tivate\x18\x02 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12P\n\x11parameter_objects\x18\x05 \x03(\x0b\x32\x35.oak9.tython.aws.datapipeline.PipelineParameterObject\x12N\n\x10parameter_values\x18\x06 \x03(\x0b\x32\x34.oak9.tython.aws.datapipeline.PipelineParameterValue\x12N\n\x10pipeline_objects\x18\x07 \x03(\x0b\x32\x34.oak9.tython.aws.datapipeline.PipelinePipelineObject\x12H\n\rpipeline_tags\x18\x08 \x03(\x0b\x32\x31.oak9.tython.aws.datapipeline.PipelinePipelineTag\"H\n\x0c\x44\x61taPipeline\x12\x38\n\x08pipeline\x18\x01 \x03(\x0b\x32&.oak9.tython.aws.datapipeline.Pipelineb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_datapipeline_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PIPELINEPARAMETERATTRIBUTE._serialized_start=81
  _PIPELINEPARAMETERATTRIBUTE._serialized_end=201
  _PIPELINEPARAMETEROBJECT._serialized_start=204
  _PIPELINEPARAMETEROBJECT._serialized_end=376
  _PIPELINEPARAMETERVALUE._serialized_start=378
  _PIPELINEPARAMETERVALUE._serialized_end=493
  _PIPELINEFIELD._serialized_start=495
  _PIPELINEFIELD._serialized_end=621
  _PIPELINEPIPELINEOBJECT._serialized_start=624
  _PIPELINEPIPELINEOBJECT._serialized_end=792
  _PIPELINEPIPELINETAG._serialized_start=794
  _PIPELINEPIPELINETAG._serialized_end=900
  _PIPELINE._serialized_start=903
  _PIPELINE._serialized_end=1339
  _DATAPIPELINE._serialized_start=1341
  _DATAPIPELINE._serialized_end=1413
# @@protoc_insertion_point(module_scope)
