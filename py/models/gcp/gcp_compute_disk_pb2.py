# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_disk.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1agcp/gcp_compute_disk.proto\x12\x1coak9.tython.gcp.compute_disk\x1a\x13shared/shared.proto\"|\n\x1d\x43omputeDiskXDiskEncryptionKey\x12\x19\n\x11kms_key_self_link\x18\x01 \x01(\t\x12\x1f\n\x17kms_key_service_account\x18\x02 \x01(\t\x12\x0f\n\x07raw_key\x18\x03 \x01(\t\x12\x0e\n\x06sha256\x18\x04 \x01(\t\"\x83\x01\n$ComputeDiskXSourceImageEncryptionKey\x12\x19\n\x11kms_key_self_link\x18\x01 \x01(\t\x12\x1f\n\x17kms_key_service_account\x18\x02 \x01(\t\x12\x0f\n\x07raw_key\x18\x03 \x01(\t\x12\x0e\n\x06sha256\x18\x04 \x01(\t\"\x86\x01\n\'ComputeDiskXSourceSnapshotEncryptionKey\x12\x19\n\x11kms_key_self_link\x18\x01 \x01(\t\x12\x1f\n\x17kms_key_service_account\x18\x02 \x01(\t\x12\x0f\n\x07raw_key\x18\x03 \x01(\t\x12\x0e\n\x06sha256\x18\x04 \x01(\t\"F\n\x14\x43omputeDiskXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xc8\x07\n\x0b\x43omputeDisk\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\x12\x19\n\x11label_fingerprint\x18\x05 \x01(\t\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32\x35.oak9.tython.gcp.compute_disk.ComputeDisk.LabelsEntry\x12\x1d\n\x15last_attach_timestamp\x18\x07 \x01(\t\x12\x1d\n\x15last_detach_timestamp\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12!\n\x19physical_block_size_bytes\x18\n \x01(\x01\x12\x0f\n\x07project\x18\x0b \x01(\t\x12\x18\n\x10provisioned_iops\x18\x0c \x01(\x01\x12\x11\n\tself_link\x18\r \x01(\t\x12\x0c\n\x04size\x18\x0e \x01(\x01\x12\x10\n\x08snapshot\x18\x0f \x01(\t\x12\x17\n\x0fsource_image_id\x18\x10 \x01(\t\x12\x1a\n\x12source_snapshot_id\x18\x11 \x01(\t\x12\x0c\n\x04type\x18\x12 \x01(\t\x12\r\n\x05users\x18\x13 \x03(\t\x12\x0c\n\x04zone\x18\x14 \x01(\t\x12X\n\x13\x64isk_encryption_key\x18\x15 \x01(\x0b\x32;.oak9.tython.gcp.compute_disk.ComputeDiskXDiskEncryptionKey\x12g\n\x1bsource_image_encryption_key\x18\x16 \x01(\x0b\x32\x42.oak9.tython.gcp.compute_disk.ComputeDiskXSourceImageEncryptionKey\x12m\n\x1esource_snapshot_encryption_key\x18\x17 \x01(\x0b\x32\x45.oak9.tython.gcp.compute_disk.ComputeDiskXSourceSnapshotEncryptionKey\x12\x44\n\x08timeouts\x18\x18 \x01(\x0b\x32\x32.oak9.tython.gcp.compute_disk.ComputeDiskXTimeouts\x12\x37\n\rresource_info\x18\x19 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Y\n\x1f\x43omputeDiskIamBindingXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x88\x02\n\x15\x43omputeDiskIamBinding\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07members\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12P\n\tcondition\x18\x08 \x01(\x0b\x32=.oak9.tython.gcp.compute_disk.ComputeDiskIamBindingXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"X\n\x1e\x43omputeDiskIamMemberXCondition\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x85\x02\n\x14\x43omputeDiskIamMember\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06member\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12O\n\tcondition\x18\x08 \x01(\x0b\x32<.oak9.tython.gcp.compute_disk.ComputeDiskIamMemberXCondition\x12\x37\n\rresource_info\x18\t \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"\xab\x01\n\x14\x43omputeDiskIamPolicy\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bpolicy_data\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0c\n\x04zone\x18\x06 \x01(\t\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"N\n,ComputeDiskResourcePolicyAttachmentXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\x83\x02\n#ComputeDiskResourcePolicyAttachment\x12\x0c\n\x04\x64isk\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x0c\n\x04zone\x18\x05 \x01(\t\x12\\\n\x08timeouts\x18\x06 \x01(\x0b\x32J.oak9.tython.gcp.compute_disk.ComputeDiskResourcePolicyAttachmentXTimeouts\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_disk_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEDISK_LABELSENTRY._options = None
  _COMPUTEDISK_LABELSENTRY._serialized_options = b'8\001'
  _COMPUTEDISKXDISKENCRYPTIONKEY._serialized_start=81
  _COMPUTEDISKXDISKENCRYPTIONKEY._serialized_end=205
  _COMPUTEDISKXSOURCEIMAGEENCRYPTIONKEY._serialized_start=208
  _COMPUTEDISKXSOURCEIMAGEENCRYPTIONKEY._serialized_end=339
  _COMPUTEDISKXSOURCESNAPSHOTENCRYPTIONKEY._serialized_start=342
  _COMPUTEDISKXSOURCESNAPSHOTENCRYPTIONKEY._serialized_end=476
  _COMPUTEDISKXTIMEOUTS._serialized_start=478
  _COMPUTEDISKXTIMEOUTS._serialized_end=548
  _COMPUTEDISK._serialized_start=551
  _COMPUTEDISK._serialized_end=1519
  _COMPUTEDISK_LABELSENTRY._serialized_start=1474
  _COMPUTEDISK_LABELSENTRY._serialized_end=1519
  _COMPUTEDISKIAMBINDINGXCONDITION._serialized_start=1521
  _COMPUTEDISKIAMBINDINGXCONDITION._serialized_end=1610
  _COMPUTEDISKIAMBINDING._serialized_start=1613
  _COMPUTEDISKIAMBINDING._serialized_end=1877
  _COMPUTEDISKIAMMEMBERXCONDITION._serialized_start=1879
  _COMPUTEDISKIAMMEMBERXCONDITION._serialized_end=1967
  _COMPUTEDISKIAMMEMBER._serialized_start=1970
  _COMPUTEDISKIAMMEMBER._serialized_end=2231
  _COMPUTEDISKIAMPOLICY._serialized_start=2234
  _COMPUTEDISKIAMPOLICY._serialized_end=2405
  _COMPUTEDISKRESOURCEPOLICYATTACHMENTXTIMEOUTS._serialized_start=2407
  _COMPUTEDISKRESOURCEPOLICYATTACHMENTXTIMEOUTS._serialized_end=2485
  _COMPUTEDISKRESOURCEPOLICYATTACHMENT._serialized_start=2488
  _COMPUTEDISKRESOURCEPOLICYATTACHMENT._serialized_end=2747
# @@protoc_insertion_point(module_scope)