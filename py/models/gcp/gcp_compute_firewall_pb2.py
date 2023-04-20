# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcp/gcp_compute_firewall.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egcp/gcp_compute_firewall.proto\x12 oak9.tython.gcp.compute_firewall\x1a\x13shared/shared.proto\"8\n\x15\x43omputeFirewallXAllow\x12\r\n\x05ports\x18\x01 \x03(\t\x12\x10\n\x08protocol\x18\x02 \x01(\t\"7\n\x14\x43omputeFirewallXDeny\x12\r\n\x05ports\x18\x01 \x03(\t\x12\x10\n\x08protocol\x18\x02 \x01(\t\"-\n\x19\x43omputeFirewallXLogConfig\x12\x10\n\x08metadata\x18\x01 \x01(\t\"J\n\x18\x43omputeFirewallXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xe5\x05\n\x0f\x43omputeFirewall\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65stination_ranges\x18\x03 \x03(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x10\n\x08\x64isabled\x18\x05 \x01(\x08\x12\x16\n\x0e\x65nable_logging\x18\x06 \x01(\x08\x12\n\n\x02id\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0f\n\x07network\x18\t \x01(\t\x12\x10\n\x08priority\x18\n \x01(\x01\x12\x0f\n\x07project\x18\x0b \x01(\t\x12\x11\n\tself_link\x18\x0c \x01(\t\x12\x15\n\rsource_ranges\x18\r \x03(\t\x12\x1f\n\x17source_service_accounts\x18\x0e \x03(\t\x12\x13\n\x0bsource_tags\x18\x0f \x03(\t\x12\x1f\n\x17target_service_accounts\x18\x10 \x03(\t\x12\x13\n\x0btarget_tags\x18\x11 \x03(\t\x12\x46\n\x05\x61llow\x18\x12 \x03(\x0b\x32\x37.oak9.tython.gcp.compute_firewall.ComputeFirewallXAllow\x12\x44\n\x04\x64\x65ny\x18\x13 \x03(\x0b\x32\x36.oak9.tython.gcp.compute_firewall.ComputeFirewallXDeny\x12O\n\nlog_config\x18\x14 \x01(\x0b\x32;.oak9.tython.gcp.compute_firewall.ComputeFirewallXLogConfig\x12L\n\x08timeouts\x18\x15 \x01(\x0b\x32:.oak9.tython.gcp.compute_firewall.ComputeFirewallXTimeouts\x12\x37\n\rresource_info\x18\x16 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"P\n\x1e\x43omputeFirewallPolicyXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\x8c\x03\n\x15\x43omputeFirewallPolicy\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x03 \x01(\t\x12\x1a\n\x12\x66irewall_policy_id\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0e\n\x06parent\x18\x07 \x01(\t\x12\x18\n\x10rule_tuple_count\x18\x08 \x01(\x01\x12\x11\n\tself_link\x18\t \x01(\t\x12\x19\n\x11self_link_with_id\x18\n \x01(\t\x12\x12\n\nshort_name\x18\x0b \x01(\t\x12R\n\x08timeouts\x18\x0c \x01(\x0b\x32@.oak9.tython.gcp.compute_firewall.ComputeFirewallPolicyXTimeouts\x12\x37\n\rresource_info\x18\r \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"K\n)ComputeFirewallPolicyAssociationXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\"\x9c\x02\n ComputeFirewallPolicyAssociation\x12\x19\n\x11\x61ttachment_target\x18\x01 \x01(\t\x12\x17\n\x0f\x66irewall_policy\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nshort_name\x18\x05 \x01(\t\x12]\n\x08timeouts\x18\x06 \x01(\x0b\x32K.oak9.tython.gcp.compute_firewall.ComputeFirewallPolicyAssociationXTimeouts\x12\x37\n\rresource_info\x18\x07 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\"S\n-ComputeFirewallPolicyRuleXMatchXLayer4Configs\x12\x13\n\x0bip_protocol\x18\x01 \x01(\t\x12\r\n\x05ports\x18\x02 \x03(\t\"\xb9\x01\n\x1f\x43omputeFirewallPolicyRuleXMatch\x12\x16\n\x0e\x64\x65st_ip_ranges\x18\x01 \x03(\t\x12\x15\n\rsrc_ip_ranges\x18\x02 \x03(\t\x12g\n\x0elayer4_configs\x18\x03 \x03(\x0b\x32O.oak9.tython.gcp.compute_firewall.ComputeFirewallPolicyRuleXMatchXLayer4Configs\"T\n\"ComputeFirewallPolicyRuleXTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\t\"\xfa\x03\n\x19\x43omputeFirewallPolicyRule\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x10\n\x08\x64isabled\x18\x04 \x01(\x08\x12\x16\n\x0e\x65nable_logging\x18\x05 \x01(\x08\x12\x17\n\x0f\x66irewall_policy\x18\x06 \x01(\t\x12\n\n\x02id\x18\x07 \x01(\t\x12\x0c\n\x04kind\x18\x08 \x01(\t\x12\x10\n\x08priority\x18\t \x01(\x01\x12\x18\n\x10rule_tuple_count\x18\n \x01(\x01\x12\x18\n\x10target_resources\x18\x0b \x03(\t\x12\x1f\n\x17target_service_accounts\x18\x0c \x03(\t\x12P\n\x05match\x18\r \x01(\x0b\x32\x41.oak9.tython.gcp.compute_firewall.ComputeFirewallPolicyRuleXMatch\x12V\n\x08timeouts\x18\x0e \x01(\x0b\x32\x44.oak9.tython.gcp.compute_firewall.ComputeFirewallPolicyRuleXTimeouts\x12\x37\n\rresource_info\x18\x0f \x01(\x0b\x32 .oak9.tython.shared.ResourceInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcp.gcp_compute_firewall_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPUTEFIREWALLXALLOW._serialized_start=89
  _COMPUTEFIREWALLXALLOW._serialized_end=145
  _COMPUTEFIREWALLXDENY._serialized_start=147
  _COMPUTEFIREWALLXDENY._serialized_end=202
  _COMPUTEFIREWALLXLOGCONFIG._serialized_start=204
  _COMPUTEFIREWALLXLOGCONFIG._serialized_end=249
  _COMPUTEFIREWALLXTIMEOUTS._serialized_start=251
  _COMPUTEFIREWALLXTIMEOUTS._serialized_end=325
  _COMPUTEFIREWALL._serialized_start=328
  _COMPUTEFIREWALL._serialized_end=1069
  _COMPUTEFIREWALLPOLICYXTIMEOUTS._serialized_start=1071
  _COMPUTEFIREWALLPOLICYXTIMEOUTS._serialized_end=1151
  _COMPUTEFIREWALLPOLICY._serialized_start=1154
  _COMPUTEFIREWALLPOLICY._serialized_end=1550
  _COMPUTEFIREWALLPOLICYASSOCIATIONXTIMEOUTS._serialized_start=1552
  _COMPUTEFIREWALLPOLICYASSOCIATIONXTIMEOUTS._serialized_end=1627
  _COMPUTEFIREWALLPOLICYASSOCIATION._serialized_start=1630
  _COMPUTEFIREWALLPOLICYASSOCIATION._serialized_end=1914
  _COMPUTEFIREWALLPOLICYRULEXMATCHXLAYER4CONFIGS._serialized_start=1916
  _COMPUTEFIREWALLPOLICYRULEXMATCHXLAYER4CONFIGS._serialized_end=1999
  _COMPUTEFIREWALLPOLICYRULEXMATCH._serialized_start=2002
  _COMPUTEFIREWALLPOLICYRULEXMATCH._serialized_end=2187
  _COMPUTEFIREWALLPOLICYRULEXTIMEOUTS._serialized_start=2189
  _COMPUTEFIREWALLPOLICYRULEXTIMEOUTS._serialized_end=2273
  _COMPUTEFIREWALLPOLICYRULE._serialized_start=2276
  _COMPUTEFIREWALLPOLICYRULE._serialized_end=2782
# @@protoc_insertion_point(module_scope)
