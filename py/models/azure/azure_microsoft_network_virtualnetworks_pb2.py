# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_network_virtualnetworks.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3azure/azure_microsoft_network_virtualnetworks.proto\x12\x33oak9.tython.azure.microsoft_network_virtualnetworks\x1a\x13shared/shared.proto\"\x82\x03\n!Microsoft_Network_virtualNetworks\x12^\n\x10virtual_networks\x18\x01 \x01(\x0b\x32\x44.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworks\x12m\n\x18virtual_networks_subnets\x18\x02 \x03(\x0b\x32K.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworksSubnets\x12\x8d\x01\n)virtual_networks_virtual_network_peerings\x18\x03 \x03(\x0b\x32Z.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworksVirtualNetworkPeerings\"\"\n\x14NetworkSecurityGroup\x12\n\n\x02id\x18\x01 \x01(\t\"\x18\n\nRouteTable\x12\n\n\x02id\x18\x01 \x01(\t\"\x19\n\x0bNatGateways\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x12\x44\x64osProtectionPlan\x12\n\n\x02id\x18\x01 \x01(\t\"\xfc\x03\n%VirtualNetworksVirtualNetworkPeerings\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x1c\x61llow_virtual_network_access\x18\x03 \x01(\x08\x12\x1f\n\x17\x61llow_forwarded_traffic\x18\x04 \x01(\x08\x12\x1d\n\x15\x61llow_gateway_transit\x18\x05 \x01(\x08\x12\x1b\n\x13use_remote_gateways\x18\x06 \x01(\x08\x12\x1e\n\x16remote_virtual_network\x18\x07 \x01(\t\x12_\n\x14remote_address_space\x18\x08 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_network_virtualnetworks.AddressSpace\x12q\n\x16remote_bgp_communities\x18\t \x01(\x0b\x32Q.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworkBgpCommunities\x12\x15\n\rpeering_state\x18\n \x01(\t\"\xc3\x05\n\x16VirtualNetworksSubnets\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x61\x64\x64ress_prefix\x18\x03 \x01(\t\x12\x18\n\x10\x61\x64\x64ress_prefixes\x18\x04 \x03(\t\x12i\n\x16network_security_group\x18\x05 \x01(\x0b\x32I.oak9.tython.azure.microsoft_network_virtualnetworks.NetworkSecurityGroup\x12T\n\x0broute_table\x18\x06 \x01(\x0b\x32?.oak9.tython.azure.microsoft_network_virtualnetworks.RouteTable\x12\x13\n\x0bnat_gateway\x18\x07 \x01(\t\x12o\n\x11service_endpoints\x18\x08 \x03(\x0b\x32T.oak9.tython.azure.microsoft_network_virtualnetworks.ServiceEndpointPropertiesFormat\x12!\n\x19service_endpoint_policies\x18\t \x03(\t\x12\x16\n\x0eip_allocations\x18\n \x03(\t\x12T\n\x0b\x64\x65legations\x18\x0b \x03(\x0b\x32?.oak9.tython.azure.microsoft_network_virtualnetworks.Delegation\x12)\n!private_endpoint_network_policies\x18\x0c \x01(\t\x12-\n%private_link_service_network_policies\x18\r \x01(\t\"\xee\x07\n\x0fVirtualNetworks\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\\\n\x04tags\x18\x04 \x03(\x0b\x32N.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworks.TagsEntry\x12`\n\x11\x65xtended_location\x18\x05 \x01(\x0b\x32\x45.oak9.tython.azure.microsoft_network_virtualnetworks.ExtendedLocation\x12X\n\raddress_space\x18\x06 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_network_virtualnetworks.AddressSpace\x12V\n\x0c\x64hcp_options\x18\x07 \x01(\x0b\x32@.oak9.tython.azure.microsoft_network_virtualnetworks.DhcpOptions\x12L\n\x07subnets\x18\x08 \x03(\x0b\x32;.oak9.tython.azure.microsoft_network_virtualnetworks.Subnet\x12l\n\x18virtual_network_peerings\x18\t \x03(\x0b\x32J.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworkPeering\x12\x1e\n\x16\x65nable_ddos_protection\x18\n \x01(\x08\x12\x1c\n\x14\x65nable_vm_protection\x18\x0b \x01(\x08\x12\x65\n\x14\x64\x64os_protection_plan\x18\x0c \x01(\x0b\x32G.oak9.tython.azure.microsoft_network_virtualnetworks.DdosProtectionPlan\x12j\n\x0f\x62gp_communities\x18\r \x01(\x0b\x32Q.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworkBgpCommunities\x12\x16\n\x0eip_allocations\x18\x0e \x03(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x03\n\x15VirtualNetworkPeering\x12$\n\x1c\x61llow_virtual_network_access\x18\x01 \x01(\x08\x12\x1f\n\x17\x61llow_forwarded_traffic\x18\x02 \x01(\x08\x12\x1d\n\x15\x61llow_gateway_transit\x18\x03 \x01(\x08\x12\x1b\n\x13use_remote_gateways\x18\x04 \x01(\x08\x12\x1e\n\x16remote_virtual_network\x18\x05 \x01(\t\x12_\n\x14remote_address_space\x18\x06 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_network_virtualnetworks.AddressSpace\x12q\n\x16remote_bgp_communities\x18\x07 \x01(\x0b\x32Q.oak9.tython.azure.microsoft_network_virtualnetworks.VirtualNetworkBgpCommunities\x12\x15\n\rpeering_state\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\"A\n\x1cVirtualNetworkBgpCommunities\x12!\n\x19virtual_network_community\x18\x01 \x01(\t\"\xfa\x04\n\x06Subnet\x12\x16\n\x0e\x61\x64\x64ress_prefix\x18\x01 \x01(\t\x12\x18\n\x10\x61\x64\x64ress_prefixes\x18\x02 \x03(\t\x12i\n\x16network_security_group\x18\x03 \x01(\x0b\x32I.oak9.tython.azure.microsoft_network_virtualnetworks.NetworkSecurityGroup\x12T\n\x0broute_table\x18\x04 \x01(\x0b\x32?.oak9.tython.azure.microsoft_network_virtualnetworks.RouteTable\x12\x13\n\x0bnat_gateway\x18\x05 \x01(\t\x12o\n\x11service_endpoints\x18\x06 \x03(\x0b\x32T.oak9.tython.azure.microsoft_network_virtualnetworks.ServiceEndpointPropertiesFormat\x12!\n\x19service_endpoint_policies\x18\x07 \x03(\t\x12\x16\n\x0eip_allocations\x18\x08 \x03(\t\x12T\n\x0b\x64\x65legations\x18\t \x03(\x0b\x32?.oak9.tython.azure.microsoft_network_virtualnetworks.Delegation\x12)\n!private_endpoint_network_policies\x18\n \x01(\t\x12-\n%private_link_service_network_policies\x18\x0b \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\"0\n\nDelegation\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"E\n\x1fServiceEndpointPropertiesFormat\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tlocations\x18\x02 \x03(\t\"\"\n\x0b\x44hcpOptions\x12\x13\n\x0b\x64ns_servers\x18\x01 \x03(\t\"(\n\x0c\x41\x64\x64ressSpace\x12\x18\n\x10\x61\x64\x64ress_prefixes\x18\x01 \x03(\t\".\n\x10\x45xtendedLocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_network_virtualnetworks_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VIRTUALNETWORKS_TAGSENTRY._options = None
  _VIRTUALNETWORKS_TAGSENTRY._serialized_options = b'8\001'
  _MICROSOFT_NETWORK_VIRTUALNETWORKS._serialized_start=130
  _MICROSOFT_NETWORK_VIRTUALNETWORKS._serialized_end=516
  _NETWORKSECURITYGROUP._serialized_start=518
  _NETWORKSECURITYGROUP._serialized_end=552
  _ROUTETABLE._serialized_start=554
  _ROUTETABLE._serialized_end=578
  _NATGATEWAYS._serialized_start=580
  _NATGATEWAYS._serialized_end=605
  _DDOSPROTECTIONPLAN._serialized_start=607
  _DDOSPROTECTIONPLAN._serialized_end=639
  _VIRTUALNETWORKSVIRTUALNETWORKPEERINGS._serialized_start=642
  _VIRTUALNETWORKSVIRTUALNETWORKPEERINGS._serialized_end=1150
  _VIRTUALNETWORKSSUBNETS._serialized_start=1153
  _VIRTUALNETWORKSSUBNETS._serialized_end=1860
  _VIRTUALNETWORKS._serialized_start=1863
  _VIRTUALNETWORKS._serialized_end=2869
  _VIRTUALNETWORKS_TAGSENTRY._serialized_start=2826
  _VIRTUALNETWORKS_TAGSENTRY._serialized_end=2869
  _VIRTUALNETWORKPEERING._serialized_start=2872
  _VIRTUALNETWORKPEERING._serialized_end=3307
  _VIRTUALNETWORKBGPCOMMUNITIES._serialized_start=3309
  _VIRTUALNETWORKBGPCOMMUNITIES._serialized_end=3374
  _SUBNET._serialized_start=3377
  _SUBNET._serialized_end=4011
  _DELEGATION._serialized_start=4013
  _DELEGATION._serialized_end=4061
  _SERVICEENDPOINTPROPERTIESFORMAT._serialized_start=4063
  _SERVICEENDPOINTPROPERTIESFORMAT._serialized_end=4132
  _DHCPOPTIONS._serialized_start=4134
  _DHCPOPTIONS._serialized_end=4168
  _ADDRESSSPACE._serialized_start=4170
  _ADDRESSSPACE._serialized_end=4210
  _EXTENDEDLOCATION._serialized_start=4212
  _EXTENDEDLOCATION._serialized_end=4258
# @@protoc_insertion_point(module_scope)