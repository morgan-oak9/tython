# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_packet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgcp/gcp_compute_packet.proto\x12\x1eoak9.tython.gcp.compute_packet\x1a\x13shared/shared.proto\"2\n#ComputePacketMirroringXCollectorIlb\x12\x0b\n\x03url\x18\x01 \x01(\t\"]\n\x1d\x43omputePacketMirroringXFilter\x12\x13\n\x0b\x63idr_ranges\x18\x01 \x03(\t\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x14\n\x0cip_protocols\x18\x03 \x03(\t\"A\n2ComputePacketMirroringXMirroredResourcesXInstances\x12\x0b\n\x03url\x18\x01 \x01(\t\"C\n4ComputePacketMirroringXMirroredResourcesXSubnetworks\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x8a\x02\n(ComputePacketMirroringXMirroredResources\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x65\n\tinstances\x18\x02 \x03(\x0b\x32R.oak9.tython.gcp.compute_packet.ComputePacketMirroringXMirroredResourcesXInstances\x12i\n\x0bsubnetworks\x18\x03 \x03(\x0b\x32T.oak9.tython.gcp.compute_packet.ComputePacketMirroringXMirroredResourcesXSubnetworks\"-\n\x1e\x43omputePacketMirroringXNetwork\x12\x0b\n\x03url\x18\x01 \x01(\t\"Q\n\x1f\x43omputePacketMirroringXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xe8\x04\n\x16\x43omputePacketMirroring\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08priority\x18\x04 \x01(\x01\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12Z\n\rcollector_ilb\x18\x07 \x01(\x0b\x32\x43.oak9.tython.gcp.compute_packet.ComputePacketMirroringXCollectorIlb\x12M\n\x06\x66ilter\x18\x08 \x01(\x0b\x32=.oak9.tython.gcp.compute_packet.ComputePacketMirroringXFilter\x12\x64\n\x12mirrored_resources\x18\t \x01(\x0b\x32H.oak9.tython.gcp.compute_packet.ComputePacketMirroringXMirroredResources\x12O\n\x07network\x18\n \x01(\x0b\x32>.oak9.tython.gcp.compute_packet.ComputePacketMirroringXNetwork\x12Q\n\x08timeouts\x18\x0b \x01(\x0b\x32?.oak9.tython.gcp.compute_packet.ComputePacketMirroringXTimeouts\x12\x37\n\rresource_info\x18\x0c \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_packet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEPACKETMIRRORINGXCOLLECTORILB._serialized_start=85
  _COMPUTEPACKETMIRRORINGXCOLLECTORILB._serialized_end=135
  _COMPUTEPACKETMIRRORINGXFILTER._serialized_start=137
  _COMPUTEPACKETMIRRORINGXFILTER._serialized_end=230
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCESXINSTANCES._serialized_start=232
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCESXINSTANCES._serialized_end=297
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCESXSUBNETWORKS._serialized_start=299
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCESXSUBNETWORKS._serialized_end=366
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCES._serialized_start=369
  _COMPUTEPACKETMIRRORINGXMIRROREDRESOURCES._serialized_end=635
  _COMPUTEPACKETMIRRORINGXNETWORK._serialized_start=637
  _COMPUTEPACKETMIRRORINGXNETWORK._serialized_end=682
  _COMPUTEPACKETMIRRORINGXTIMEOUTS._serialized_start=684
  _COMPUTEPACKETMIRRORINGXTIMEOUTS._serialized_end=765
  _COMPUTEPACKETMIRRORING._serialized_start=768
  _COMPUTEPACKETMIRRORING._serialized_end=1384
# @@protoc_insertion_point(module_scope)
