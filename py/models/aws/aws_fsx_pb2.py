# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_fsx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_fsx.proto\x12\x13oak9.tython.aws.fsx\x1a\x13shared/shared.proto\"\xb1\x03\n\x1d\x46ileSystemLustreConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x64rive_cache_type\x18\x02 \x01(\t\x12\x13\n\x0bimport_path\x18\x03 \x01(\t\x12%\n\x1dweekly_maintenance_start_time\x18\x04 \x01(\t\x12\x1a\n\x12\x61uto_import_policy\x18\x05 \x01(\t\x12 \n\x18imported_file_chunk_size\x18\x06 \x01(\x05\x12\x17\n\x0f\x64\x65ployment_type\x18\x07 \x01(\t\x12)\n!daily_automatic_backup_start_time\x18\x08 \x01(\t\x12\x1c\n\x14\x63opy_tags_to_backups\x18\t \x01(\x08\x12\x13\n\x0b\x65xport_path\x18\n \x01(\t\x12#\n\x1bper_unit_storage_throughput\x18\x0b \x01(\x05\x12\'\n\x1f\x61utomatic_backup_retention_days\x18\x0c \x01(\x05\"\x91\x02\n1FileSystemSelfManagedActiveDirectoryConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12(\n file_system_administrators_group\x18\x02 \x01(\t\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x04 \x01(\t\x12.\n&organizational_unit_distinguished_name\x18\x05 \x01(\t\x12\x0f\n\x07\x64ns_ips\x18\x06 \x03(\t\x12\x10\n\x08password\x18\x07 \x01(\t\"\xdf\x03\n\x1e\x46ileSystemWindowsConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12{\n+self_managed_active_directory_configuration\x18\x02 \x01(\x0b\x32\x46.oak9.tython.aws.fsx.FileSystemSelfManagedActiveDirectoryConfiguration\x12%\n\x1dweekly_maintenance_start_time\x18\x03 \x01(\t\x12\x1b\n\x13\x61\x63tive_directory_id\x18\x04 \x01(\t\x12\x17\n\x0f\x64\x65ployment_type\x18\x05 \x01(\t\x12\x1b\n\x13throughput_capacity\x18\x06 \x01(\x05\x12\x1c\n\x14\x63opy_tags_to_backups\x18\x07 \x01(\x08\x12)\n!daily_automatic_backup_start_time\x18\x08 \x01(\t\x12\'\n\x1f\x61utomatic_backup_retention_days\x18\t \x01(\x05\x12\x1b\n\x13preferred_subnet_id\x18\n \x01(\t\"\xf2\x03\n\nFileSystem\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cstorage_type\x18\x02 \x01(\t\x12\x12\n\nkms_key_id\x18\x03 \x01(\t\x12\x18\n\x10storage_capacity\x18\x04 \x01(\x05\x12\x18\n\x10\x66ile_system_type\x18\x05 \x01(\t\x12P\n\x14lustre_configuration\x18\x06 \x01(\x0b\x32\x32.oak9.tython.aws.fsx.FileSystemLustreConfiguration\x12\x11\n\tbackup_id\x18\x07 \x01(\t\x12\x12\n\nsubnet_ids\x18\x08 \x03(\t\x12\x1a\n\x12security_group_ids\x18\t \x03(\t\x12\x37\n\x04tags\x18\n \x03(\x0b\x32).oak9.tython.aws.fsx.FileSystem.TagsEntry\x12R\n\x15windows_configuration\x18\x0b \x01(\x0b\x32\x33.oak9.tython.aws.fsx.FileSystemWindowsConfiguration\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x03\x46Sx\x12\x34\n\x0b\x66ile_system\x18\x01 \x03(\x0b\x32\x1f.oak9.tython.aws.fsx.FileSystemb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_fsx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILESYSTEM_TAGSENTRY._options = None
  _FILESYSTEM_TAGSENTRY._serialized_options = b'8\001'
  _FILESYSTEMLUSTRECONFIGURATION._serialized_start=64
  _FILESYSTEMLUSTRECONFIGURATION._serialized_end=497
  _FILESYSTEMSELFMANAGEDACTIVEDIRECTORYCONFIGURATION._serialized_start=500
  _FILESYSTEMSELFMANAGEDACTIVEDIRECTORYCONFIGURATION._serialized_end=773
  _FILESYSTEMWINDOWSCONFIGURATION._serialized_start=776
  _FILESYSTEMWINDOWSCONFIGURATION._serialized_end=1255
  _FILESYSTEM._serialized_start=1258
  _FILESYSTEM._serialized_end=1756
  _FILESYSTEM_TAGSENTRY._serialized_start=1713
  _FILESYSTEM_TAGSENTRY._serialized_end=1756
  _FSX._serialized_start=1758
  _FSX._serialized_end=1817
# @@protoc_insertion_point(module_scope)
