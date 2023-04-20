# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_healthcareapis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*azure/azure_microsoft_healthcareapis.proto\x12*oak9.tython.azure.microsoft_healthcareapis\x1a\x13shared/shared.proto\"b\n\x18Microsoft_HealthcareApis\x12\x46\n\x08services\x18\x01 \x01(\x0b\x32\x34.oak9.tython.azure.microsoft_healthcareapis.Services\"\xab\x03\n$WorkspacesPrivateEndpointConnections\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12U\n\x10private_endpoint\x18\x03 \x01(\x0b\x32;.oak9.tython.azure.microsoft_healthcareapis.PrivateEndpoint\x12|\n%private_link_service_connection_state\x18\x04 \x01(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.PrivateLinkServiceConnectionState\x12\x1a\n\x12provisioning_state\x18\x05 \x01(\t\x12K\n\x0bsystem_data\x18\x06 \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\"\x9e\x03\n\'WorkspacesIotconnectorsFhirdestinations\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12V\n\x0c\x66hir_mapping\x18\x05 \x01(\x0b\x32@.oak9.tython.azure.microsoft_healthcareapis.IotMappingProperties\x12 \n\x18\x66hir_service_resource_id\x18\x06 \x01(\t\x12\x1a\n\x12provisioning_state\x18\x07 \x01(\t\x12)\n!resource_identity_resolution_type\x18\x08 \x01(\t\x12K\n\x0bsystem_data\x18\t \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\"\xa7\x06\n\x17WorkspacesIotconnectors\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\\\n\x08identity\x18\x02 \x01(\x0b\x32J.oak9.tython.azure.microsoft_healthcareapis.ServiceManagedIdentityIdentity\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12X\n\x0e\x64\x65vice_mapping\x18\x05 \x01(\x0b\x32@.oak9.tython.azure.microsoft_healthcareapis.IotMappingProperties\x12\x7f\n ingestion_endpoint_configuration\x18\x06 \x01(\x0b\x32U.oak9.tython.azure.microsoft_healthcareapis.IotEventHubIngestionEndpointConfiguration\x12\x1a\n\x12provisioning_state\x18\x07 \x01(\t\x12K\n\x0bsystem_data\x18\x08 \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\x12[\n\x04tags\x18\t \x03(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.WorkspacesIotconnectors.TagsEntry\x12\x86\x01\n)workspaces_iotconnectors_fhirdestinations\x18\n \x03(\x0b\x32S.oak9.tython.azure.microsoft_healthcareapis.WorkspacesIotconnectorsFhirdestinations\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x88\x01\n)IotEventHubIngestionEndpointConfiguration\x12\x16\n\x0e\x63onsumer_group\x18\x01 \x01(\t\x12\x16\n\x0e\x65vent_hub_name\x18\x02 \x01(\t\x12+\n#fully_qualified_event_hub_namespace\x18\x03 \x01(\t\"\xa6\x01\n\x14IotMappingProperties\x12^\n\x07\x63ontent\x18\x01 \x03(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.IotMappingProperties.ContentEntry\x1a.\n\x0c\x43ontentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x93\t\n\x16WorkspacesFhirservices\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\\\n\x08identity\x18\x02 \x01(\x0b\x32J.oak9.tython.azure.microsoft_healthcareapis.ServiceManagedIdentityIdentity\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x61\n\x0f\x61\x63\x63\x65ss_policies\x18\x06 \x03(\x0b\x32H.oak9.tython.azure.microsoft_healthcareapis.FhirServiceAccessPolicyEntry\x12\x62\n\x11\x61\x63r_configuration\x18\x07 \x01(\x0b\x32G.oak9.tython.azure.microsoft_healthcareapis.FhirServiceAcrConfiguration\x12x\n\x1c\x61uthentication_configuration\x18\x08 \x01(\x0b\x32R.oak9.tython.azure.microsoft_healthcareapis.FhirServiceAuthenticationConfiguration\x12\x64\n\x12\x63ors_configuration\x18\t \x01(\x0b\x32H.oak9.tython.azure.microsoft_healthcareapis.FhirServiceCorsConfiguration\x12\x13\n\x0b\x65vent_state\x18\n \x01(\t\x12h\n\x14\x65xport_configuration\x18\x0b \x01(\x0b\x32J.oak9.tython.azure.microsoft_healthcareapis.FhirServiceExportConfiguration\x12\x1a\n\x12provisioning_state\x18\x0c \x01(\t\x12\x1d\n\x15public_network_access\x18\r \x01(\t\x12}\n%resource_version_policy_configuration\x18\x0e \x01(\x0b\x32N.oak9.tython.azure.microsoft_healthcareapis.ResourceVersionPolicyConfiguration\x12K\n\x0bsystem_data\x18\x0f \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\x12Z\n\x04tags\x18\x10 \x03(\x0b\x32L.oak9.tython.azure.microsoft_healthcareapis.WorkspacesFhirservices.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x80\x02\n\"ResourceVersionPolicyConfiguration\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\t\x12\x8a\x01\n\x17resource_type_overrides\x18\x02 \x03(\x0b\x32i.oak9.tython.azure.microsoft_healthcareapis.ResourceVersionPolicyConfiguration.ResourceTypeOverridesEntry\x1a<\n\x1aResourceTypeOverridesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\">\n\x1e\x46hirServiceExportConfiguration\x12\x1c\n\x14storage_account_name\x18\x01 \x01(\t\"}\n\x1c\x46hirServiceCorsConfiguration\x12\x19\n\x11\x61llow_credentials\x18\x01 \x01(\x08\x12\x0f\n\x07headers\x18\x02 \x03(\t\x12\x0f\n\x07max_age\x18\x03 \x01(\x05\x12\x0f\n\x07methods\x18\x04 \x03(\t\x12\x0f\n\x07origins\x18\x05 \x03(\t\"j\n&FhirServiceAuthenticationConfiguration\x12\x10\n\x08\x61udience\x18\x01 \x01(\t\x12\x11\n\tauthority\x18\x02 \x01(\t\x12\x1b\n\x13smart_proxy_enabled\x18\x03 \x01(\x08\"\x90\x01\n\x1b\x46hirServiceAcrConfiguration\x12\x15\n\rlogin_servers\x18\x01 \x03(\t\x12Z\n\roci_artifacts\x18\x02 \x03(\x0b\x32\x43.oak9.tython.azure.microsoft_healthcareapis.ServiceOciArtifactEntry\"1\n\x1c\x46hirServiceAccessPolicyEntry\x12\x11\n\tobject_id\x18\x01 \x01(\t\"\xdd\x04\n\x17WorkspacesDicomservices\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\\\n\x08identity\x18\x02 \x01(\x0b\x32J.oak9.tython.azure.microsoft_healthcareapis.ServiceManagedIdentityIdentity\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12y\n\x1c\x61uthentication_configuration\x18\x05 \x01(\x0b\x32S.oak9.tython.azure.microsoft_healthcareapis.DicomServiceAuthenticationConfiguration\x12\x1a\n\x12provisioning_state\x18\x06 \x01(\t\x12\x1d\n\x15public_network_access\x18\x07 \x01(\t\x12K\n\x0bsystem_data\x18\x08 \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\x12[\n\x04tags\x18\t \x03(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.WorkspacesDicomservices.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n\'DicomServiceAuthenticationConfiguration\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf8\x01\n\x1eServiceManagedIdentityIdentity\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x88\x01\n\x18user_assigned_identities\x18\x02 \x03(\x0b\x32\x66.oak9.tython.azure.microsoft_healthcareapis.ServiceManagedIdentityIdentity.UserAssignedIdentitiesEntry\x1a=\n\x1bUserAssignedIdentitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa1\x06\n\nWorkspaces\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1a\n\x12provisioning_state\x18\x04 \x01(\t\x12\x1d\n\x15public_network_access\x18\x05 \x01(\t\x12K\n\x0bsystem_data\x18\x06 \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\x12N\n\x04tags\x18\x07 \x03(\x0b\x32@.oak9.tython.azure.microsoft_healthcareapis.Workspaces.TagsEntry\x12\x65\n\x18workspaces_dicomservices\x18\x08 \x03(\x0b\x32\x43.oak9.tython.azure.microsoft_healthcareapis.WorkspacesDicomservices\x12\x65\n\x18workspaces_iotconnectors\x18\t \x03(\x0b\x32\x43.oak9.tython.azure.microsoft_healthcareapis.WorkspacesIotconnectors\x12\x63\n\x17workspaces_fhirservices\x18\n \x03(\x0b\x32\x42.oak9.tython.azure.microsoft_healthcareapis.WorkspacesFhirservices\x12\x81\x01\n\'workspaces_private_endpoint_connections\x18\x0b \x03(\x0b\x32P.oak9.tython.azure.microsoft_healthcareapis.WorkspacesPrivateEndpointConnections\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdc\x02\n\"ServicesPrivateEndpointConnections\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12U\n\x10private_endpoint\x18\x03 \x01(\x0b\x32;.oak9.tython.azure.microsoft_healthcareapis.PrivateEndpoint\x12|\n%private_link_service_connection_state\x18\x04 \x01(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.PrivateLinkServiceConnectionState\x12\x1a\n\x12provisioning_state\x18\x05 \x01(\t\"\xc3\t\n\x08Services\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12V\n\x08identity\x18\x03 \x01(\x0b\x32\x44.oak9.tython.azure.microsoft_healthcareapis.ServicesResourceIdentity\x12\x0c\n\x04kind\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12]\n\x0f\x61\x63\x63\x65ss_policies\x18\x07 \x03(\x0b\x32\x44.oak9.tython.azure.microsoft_healthcareapis.ServiceAccessPolicyEntry\x12\x62\n\x11\x61\x63r_configuration\x18\x08 \x01(\x0b\x32G.oak9.tython.azure.microsoft_healthcareapis.ServiceAcrConfigurationInfo\x12x\n\x1c\x61uthentication_configuration\x18\t \x01(\x0b\x32R.oak9.tython.azure.microsoft_healthcareapis.ServiceAuthenticationConfigurationInfo\x12\x64\n\x12\x63ors_configuration\x18\n \x01(\x0b\x32H.oak9.tython.azure.microsoft_healthcareapis.ServiceCorsConfigurationInfo\x12m\n\x17\x63osmos_db_configuration\x18\x0b \x01(\x0b\x32L.oak9.tython.azure.microsoft_healthcareapis.ServiceCosmosDbConfigurationInfo\x12h\n\x14\x65xport_configuration\x18\x0c \x01(\x0b\x32J.oak9.tython.azure.microsoft_healthcareapis.ServiceExportConfigurationInfo\x12k\n\x1cprivate_endpoint_connections\x18\r \x03(\x0b\x32\x45.oak9.tython.azure.microsoft_healthcareapis.PrivateEndpointConnection\x12\x1a\n\x12provisioning_state\x18\x0e \x01(\t\x12\x1d\n\x15public_network_access\x18\x0f \x01(\t\x12K\n\x0bsystem_data\x18\x10 \x01(\x0b\x32\x36.oak9.tython.azure.microsoft_healthcareapis.SystemData\x12L\n\x04tags\x18\x11 \x03(\x0b\x32>.oak9.tython.azure.microsoft_healthcareapis.Services.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa0\x01\n\nSystemData\x12\x12\n\ncreated_at\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12\x17\n\x0f\x63reated_by_type\x18\x03 \x01(\t\x12\x18\n\x10last_modified_at\x18\x04 \x01(\t\x12\x18\n\x10last_modified_by\x18\x05 \x01(\t\x12\x1d\n\x15last_modified_by_type\x18\x06 \x01(\t\"\x8c\x02\n\x19PrivateEndpointConnection\x12U\n\x10private_endpoint\x18\x01 \x01(\x0b\x32;.oak9.tython.azure.microsoft_healthcareapis.PrivateEndpoint\x12|\n%private_link_service_connection_state\x18\x02 \x01(\x0b\x32M.oak9.tython.azure.microsoft_healthcareapis.PrivateLinkServiceConnectionState\x12\x1a\n\x12provisioning_state\x18\x03 \x01(\t\"b\n!PrivateLinkServiceConnectionState\x12\x18\n\x10\x61\x63tions_required\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x1f\n\x0fPrivateEndpoint\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x1eServiceExportConfigurationInfo\x12\x1c\n\x14storage_account_name\x18\x01 \x01(\t\"W\n ServiceCosmosDbConfigurationInfo\x12\x19\n\x11key_vault_key_uri\x18\x01 \x01(\t\x12\x18\n\x10offer_throughput\x18\x02 \x01(\x05\"}\n\x1cServiceCorsConfigurationInfo\x12\x19\n\x11\x61llow_credentials\x18\x01 \x01(\x08\x12\x0f\n\x07headers\x18\x02 \x03(\t\x12\x0f\n\x07max_age\x18\x03 \x01(\x05\x12\x0f\n\x07methods\x18\x04 \x03(\t\x12\x0f\n\x07origins\x18\x05 \x03(\t\"j\n&ServiceAuthenticationConfigurationInfo\x12\x10\n\x08\x61udience\x18\x01 \x01(\t\x12\x11\n\tauthority\x18\x02 \x01(\t\x12\x1b\n\x13smart_proxy_enabled\x18\x03 \x01(\x08\"\x90\x01\n\x1bServiceAcrConfigurationInfo\x12\x15\n\rlogin_servers\x18\x01 \x03(\t\x12Z\n\roci_artifacts\x18\x02 \x03(\x0b\x32\x43.oak9.tython.azure.microsoft_healthcareapis.ServiceOciArtifactEntry\"S\n\x17ServiceOciArtifactEntry\x12\x0e\n\x06\x64igest\x18\x01 \x01(\t\x12\x12\n\nimage_name\x18\x02 \x01(\t\x12\x14\n\x0clogin_server\x18\x03 \x01(\t\"-\n\x18ServiceAccessPolicyEntry\x12\x11\n\tobject_id\x18\x01 \x01(\t\"(\n\x18ServicesResourceIdentity\x12\x0c\n\x04type\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_healthcareapis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKSPACESIOTCONNECTORS_TAGSENTRY._options = None
  _WORKSPACESIOTCONNECTORS_TAGSENTRY._serialized_options = b'8\001'
  _IOTMAPPINGPROPERTIES_CONTENTENTRY._options = None
  _IOTMAPPINGPROPERTIES_CONTENTENTRY._serialized_options = b'8\001'
  _WORKSPACESFHIRSERVICES_TAGSENTRY._options = None
  _WORKSPACESFHIRSERVICES_TAGSENTRY._serialized_options = b'8\001'
  _RESOURCEVERSIONPOLICYCONFIGURATION_RESOURCETYPEOVERRIDESENTRY._options = None
  _RESOURCEVERSIONPOLICYCONFIGURATION_RESOURCETYPEOVERRIDESENTRY._serialized_options = b'8\001'
  _WORKSPACESDICOMSERVICES_TAGSENTRY._options = None
  _WORKSPACESDICOMSERVICES_TAGSENTRY._serialized_options = b'8\001'
  _SERVICEMANAGEDIDENTITYIDENTITY_USERASSIGNEDIDENTITIESENTRY._options = None
  _SERVICEMANAGEDIDENTITYIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_options = b'8\001'
  _WORKSPACES_TAGSENTRY._options = None
  _WORKSPACES_TAGSENTRY._serialized_options = b'8\001'
  _SERVICES_TAGSENTRY._options = None
  _SERVICES_TAGSENTRY._serialized_options = b'8\001'
  _MICROSOFT_HEALTHCAREAPIS._serialized_start=111
  _MICROSOFT_HEALTHCAREAPIS._serialized_end=209
  _WORKSPACESPRIVATEENDPOINTCONNECTIONS._serialized_start=212
  _WORKSPACESPRIVATEENDPOINTCONNECTIONS._serialized_end=639
  _WORKSPACESIOTCONNECTORSFHIRDESTINATIONS._serialized_start=642
  _WORKSPACESIOTCONNECTORSFHIRDESTINATIONS._serialized_end=1056
  _WORKSPACESIOTCONNECTORS._serialized_start=1059
  _WORKSPACESIOTCONNECTORS._serialized_end=1866
  _WORKSPACESIOTCONNECTORS_TAGSENTRY._serialized_start=1823
  _WORKSPACESIOTCONNECTORS_TAGSENTRY._serialized_end=1866
  _IOTEVENTHUBINGESTIONENDPOINTCONFIGURATION._serialized_start=1869
  _IOTEVENTHUBINGESTIONENDPOINTCONFIGURATION._serialized_end=2005
  _IOTMAPPINGPROPERTIES._serialized_start=2008
  _IOTMAPPINGPROPERTIES._serialized_end=2174
  _IOTMAPPINGPROPERTIES_CONTENTENTRY._serialized_start=2128
  _IOTMAPPINGPROPERTIES_CONTENTENTRY._serialized_end=2174
  _WORKSPACESFHIRSERVICES._serialized_start=2177
  _WORKSPACESFHIRSERVICES._serialized_end=3348
  _WORKSPACESFHIRSERVICES_TAGSENTRY._serialized_start=1823
  _WORKSPACESFHIRSERVICES_TAGSENTRY._serialized_end=1866
  _RESOURCEVERSIONPOLICYCONFIGURATION._serialized_start=3351
  _RESOURCEVERSIONPOLICYCONFIGURATION._serialized_end=3607
  _RESOURCEVERSIONPOLICYCONFIGURATION_RESOURCETYPEOVERRIDESENTRY._serialized_start=3547
  _RESOURCEVERSIONPOLICYCONFIGURATION_RESOURCETYPEOVERRIDESENTRY._serialized_end=3607
  _FHIRSERVICEEXPORTCONFIGURATION._serialized_start=3609
  _FHIRSERVICEEXPORTCONFIGURATION._serialized_end=3671
  _FHIRSERVICECORSCONFIGURATION._serialized_start=3673
  _FHIRSERVICECORSCONFIGURATION._serialized_end=3798
  _FHIRSERVICEAUTHENTICATIONCONFIGURATION._serialized_start=3800
  _FHIRSERVICEAUTHENTICATIONCONFIGURATION._serialized_end=3906
  _FHIRSERVICEACRCONFIGURATION._serialized_start=3909
  _FHIRSERVICEACRCONFIGURATION._serialized_end=4053
  _FHIRSERVICEACCESSPOLICYENTRY._serialized_start=4055
  _FHIRSERVICEACCESSPOLICYENTRY._serialized_end=4104
  _WORKSPACESDICOMSERVICES._serialized_start=4107
  _WORKSPACESDICOMSERVICES._serialized_end=4712
  _WORKSPACESDICOMSERVICES_TAGSENTRY._serialized_start=1823
  _WORKSPACESDICOMSERVICES_TAGSENTRY._serialized_end=1866
  _DICOMSERVICEAUTHENTICATIONCONFIGURATION._serialized_start=4714
  _DICOMSERVICEAUTHENTICATIONCONFIGURATION._serialized_end=4769
  _SERVICEMANAGEDIDENTITYIDENTITY._serialized_start=4772
  _SERVICEMANAGEDIDENTITYIDENTITY._serialized_end=5020
  _SERVICEMANAGEDIDENTITYIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_start=4959
  _SERVICEMANAGEDIDENTITYIDENTITY_USERASSIGNEDIDENTITIESENTRY._serialized_end=5020
  _WORKSPACES._serialized_start=5023
  _WORKSPACES._serialized_end=5824
  _WORKSPACES_TAGSENTRY._serialized_start=1823
  _WORKSPACES_TAGSENTRY._serialized_end=1866
  _SERVICESPRIVATEENDPOINTCONNECTIONS._serialized_start=5827
  _SERVICESPRIVATEENDPOINTCONNECTIONS._serialized_end=6175
  _SERVICES._serialized_start=6178
  _SERVICES._serialized_end=7397
  _SERVICES_TAGSENTRY._serialized_start=1823
  _SERVICES_TAGSENTRY._serialized_end=1866
  _SYSTEMDATA._serialized_start=7400
  _SYSTEMDATA._serialized_end=7560
  _PRIVATEENDPOINTCONNECTION._serialized_start=7563
  _PRIVATEENDPOINTCONNECTION._serialized_end=7831
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_start=7833
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_end=7931
  _PRIVATEENDPOINT._serialized_start=7933
  _PRIVATEENDPOINT._serialized_end=7964
  _SERVICEEXPORTCONFIGURATIONINFO._serialized_start=7966
  _SERVICEEXPORTCONFIGURATIONINFO._serialized_end=8028
  _SERVICECOSMOSDBCONFIGURATIONINFO._serialized_start=8030
  _SERVICECOSMOSDBCONFIGURATIONINFO._serialized_end=8117
  _SERVICECORSCONFIGURATIONINFO._serialized_start=8119
  _SERVICECORSCONFIGURATIONINFO._serialized_end=8244
  _SERVICEAUTHENTICATIONCONFIGURATIONINFO._serialized_start=8246
  _SERVICEAUTHENTICATIONCONFIGURATIONINFO._serialized_end=8352
  _SERVICEACRCONFIGURATIONINFO._serialized_start=8355
  _SERVICEACRCONFIGURATIONINFO._serialized_end=8499
  _SERVICEOCIARTIFACTENTRY._serialized_start=8501
  _SERVICEOCIARTIFACTENTRY._serialized_end=8584
  _SERVICEACCESSPOLICYENTRY._serialized_start=8586
  _SERVICEACCESSPOLICYENTRY._serialized_end=8631
  _SERVICESRESOURCEIDENTITY._serialized_start=8633
  _SERVICESRESOURCEIDENTITY._serialized_end=8673
# @@protoc_insertion_point(module_scope)
