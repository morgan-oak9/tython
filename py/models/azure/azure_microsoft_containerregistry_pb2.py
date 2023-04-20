# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/azure_microsoft_containerregistry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-azure/azure_microsoft_containerregistry.proto\x12-oak9.tython.azure.microsoft_containerregistry\x1a\x13shared/shared.proto\"l\n\x1bMicrosoft_ContainerRegistry\x12M\n\nregistries\x18\x01 \x03(\x0b\x32\x39.oak9.tython.azure.microsoft_containerregistry.Registries\"\xde\x03\n\x12RegistriesWebhooks\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x63tions\x18\x04 \x03(\t\x12l\n\x0e\x63ustom_headers\x18\x05 \x03(\x0b\x32T.oak9.tython.azure.microsoft_containerregistry.RegistriesWebhooks.CustomHeadersEntry\x12\r\n\x05scope\x18\x06 \x01(\t\x12\x13\n\x0bservice_uri\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12Y\n\x04tags\x18\t \x03(\x0b\x32K.oak9.tython.azure.microsoft_containerregistry.RegistriesWebhooks.TagsEntry\x1a\x34\n\x12\x43ustomHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdf\x01\n\x10RegistriesTokens\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12^\n\x0b\x63redentials\x18\x03 \x01(\x0b\x32I.oak9.tython.azure.microsoft_containerregistry.TokenCredentialsProperties\x12\x14\n\x0cscope_map_id\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\"\xc4\x01\n\x1aTokenCredentialsProperties\x12U\n\x0c\x63\x65rtificates\x18\x01 \x03(\x0b\x32?.oak9.tython.azure.microsoft_containerregistry.TokenCertificate\x12O\n\tpasswords\x18\x02 \x03(\x0b\x32<.oak9.tython.azure.microsoft_containerregistry.TokenPassword\"D\n\rTokenPassword\x12\x15\n\rcreation_time\x18\x01 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"e\n\x10TokenCertificate\x12\x1f\n\x17\x65ncoded_pem_certificate\x18\x01 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nthumbprint\x18\x04 \x01(\t\"\x82\x01\n\x13RegistriesScopeMaps\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x63tions\x18\x03 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\xb7\x02\n\x16RegistriesReplications\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1f\n\x17region_endpoint_enabled\x18\x04 \x01(\x08\x12\x17\n\x0fzone_redundancy\x18\x05 \x01(\t\x12]\n\x04tags\x18\x06 \x03(\x0b\x32O.oak9.tython.azure.microsoft_containerregistry.RegistriesReplications.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc8\x02\n$RegistriesPrivateEndpointConnections\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12X\n\x10private_endpoint\x18\x03 \x01(\x0b\x32>.oak9.tython.azure.microsoft_containerregistry.PrivateEndpoint\x12\x7f\n%private_link_service_connection_state\x18\x04 \x01(\x0b\x32P.oak9.tython.azure.microsoft_containerregistry.PrivateLinkServiceConnectionState\"b\n!PrivateLinkServiceConnectionState\x12\x18\n\x10\x61\x63tions_required\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x1d\n\x0fPrivateEndpoint\x12\n\n\x02id\x18\x01 \x01(\t\"\xcd\x01\n\x16RegistriesPipelineRuns\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10\x66orce_update_tag\x18\x03 \x01(\t\x12R\n\x07request\x18\x04 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.PipelineRunRequest\"\x95\x02\n\x12PipelineRunRequest\x12\x11\n\tartifacts\x18\x01 \x03(\t\x12\x16\n\x0e\x63\x61talog_digest\x18\x02 \x01(\t\x12\x1c\n\x14pipeline_resource_id\x18\x03 \x01(\t\x12Z\n\x06source\x18\x04 \x01(\x0b\x32J.oak9.tython.azure.microsoft_containerregistry.PipelineRunSourceProperties\x12Z\n\x06target\x18\x05 \x01(\x0b\x32J.oak9.tython.azure.microsoft_containerregistry.PipelineRunTargetProperties\"9\n\x1bPipelineRunTargetProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"9\n\x1bPipelineRunSourceProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x94\x03\n\x19RegistriesImportPipelines\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12S\n\x08identity\x18\x02 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.IdentityProperties\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07options\x18\x05 \x03(\t\x12]\n\x06source\x18\x06 \x01(\x0b\x32M.oak9.tython.azure.microsoft_containerregistry.ImportPipelineSourceProperties\x12Y\n\x07trigger\x18\x07 \x01(\x0b\x32H.oak9.tython.azure.microsoft_containerregistry.PipelineTriggerProperties\"\x83\x01\n\x19PipelineTriggerProperties\x12\x66\n\x0esource_trigger\x18\x01 \x01(\x0b\x32N.oak9.tython.azure.microsoft_containerregistry.PipelineSourceTriggerProperties\"1\n\x1fPipelineSourceTriggerProperties\x12\x0e\n\x06status\x18\x01 \x01(\t\"R\n\x1eImportPipelineSourceProperties\x12\x15\n\rkey_vault_uri\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\"\xb9\x02\n\x19RegistriesExportPipelines\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12S\n\x08identity\x18\x02 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.IdentityProperties\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07options\x18\x05 \x03(\t\x12]\n\x06target\x18\x06 \x01(\x0b\x32M.oak9.tython.azure.microsoft_containerregistry.ExportPipelineTargetProperties\"R\n\x1e\x45xportPipelineTargetProperties\x12\x15\n\rkey_vault_uri\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\"\xaa\x03\n\x1dRegistriesConnectedRegistries\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10\x63lient_token_ids\x18\x03 \x03(\t\x12Q\n\x07logging\x18\x04 \x01(\x0b\x32@.oak9.tython.azure.microsoft_containerregistry.LoggingProperties\x12Z\n\x0clogin_server\x18\x05 \x01(\x0b\x32\x44.oak9.tython.azure.microsoft_containerregistry.LoginServerProperties\x12\x0c\n\x04mode\x18\x06 \x01(\t\x12\x1a\n\x12notifications_list\x18\x07 \x03(\t\x12O\n\x06parent\x18\x08 \x01(\x0b\x32?.oak9.tython.azure.microsoft_containerregistry.ParentProperties\"v\n\x10ParentProperties\x12\n\n\x02id\x18\x01 \x01(\t\x12V\n\x0fsync_properties\x18\x02 \x01(\x0b\x32=.oak9.tython.azure.microsoft_containerregistry.SyncProperties\"^\n\x0eSyncProperties\x12\x13\n\x0bmessage_ttl\x18\x01 \x01(\t\x12\x10\n\x08schedule\x18\x02 \x01(\t\x12\x13\n\x0bsync_window\x18\x03 \x01(\t\x12\x10\n\x08token_id\x18\x04 \x01(\t\"%\n\x15LoginServerProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x11LoggingProperties\x12\x18\n\x10\x61udit_log_status\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t\"\xfa\r\n\nRegistries\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12S\n\x08identity\x18\x02 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.IdentityProperties\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1a\n\x12\x61\x64min_user_enabled\x18\x05 \x01(\x08\x12\x1e\n\x16\x61nonymous_pull_enabled\x18\x06 \x01(\x08\x12\x1d\n\x15\x64\x61ta_endpoint_enabled\x18\x07 \x01(\x08\x12U\n\nencryption\x18\x08 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.EncryptionProperty\x12#\n\x1bnetwork_rule_bypass_options\x18\t \x01(\t\x12W\n\x10network_rule_set\x18\n \x01(\x0b\x32=.oak9.tython.azure.microsoft_containerregistry.NetworkRuleSet\x12I\n\x08policies\x18\x0b \x01(\x0b\x32\x37.oak9.tython.azure.microsoft_containerregistry.Policies\x12\x1d\n\x15public_network_access\x18\x0c \x01(\t\x12\x17\n\x0fzone_redundancy\x18\r \x01(\t\x12?\n\x03sku\x18\x0e \x01(\x0b\x32\x32.oak9.tython.azure.microsoft_containerregistry.Sku\x12Q\n\x04tags\x18\x0f \x03(\x0b\x32\x43.oak9.tython.azure.microsoft_containerregistry.Registries.TagsEntry\x12u\n\x1fregistries_connected_registries\x18\x10 \x03(\x0b\x32L.oak9.tython.azure.microsoft_containerregistry.RegistriesConnectedRegistries\x12m\n\x1bregistries_export_pipelines\x18\x11 \x03(\x0b\x32H.oak9.tython.azure.microsoft_containerregistry.RegistriesExportPipelines\x12m\n\x1bregistries_import_pipelines\x18\x12 \x03(\x0b\x32H.oak9.tython.azure.microsoft_containerregistry.RegistriesImportPipelines\x12g\n\x18registries_pipeline_runs\x18\x13 \x03(\x0b\x32\x45.oak9.tython.azure.microsoft_containerregistry.RegistriesPipelineRuns\x12\x84\x01\n\'registries_private_endpoint_connections\x18\x14 \x03(\x0b\x32S.oak9.tython.azure.microsoft_containerregistry.RegistriesPrivateEndpointConnections\x12\x66\n\x17registries_replications\x18\x15 \x03(\x0b\x32\x45.oak9.tython.azure.microsoft_containerregistry.RegistriesReplications\x12\x61\n\x15registries_scope_maps\x18\x16 \x03(\x0b\x32\x42.oak9.tython.azure.microsoft_containerregistry.RegistriesScopeMaps\x12Z\n\x11registries_tokens\x18\x17 \x03(\x0b\x32?.oak9.tython.azure.microsoft_containerregistry.RegistriesTokens\x12^\n\x13registries_webhooks\x18\x18 \x03(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.RegistriesWebhooks\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x13\n\x03Sku\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe6\x02\n\x08Policies\x12R\n\rexport_policy\x18\x01 \x01(\x0b\x32;.oak9.tython.azure.microsoft_containerregistry.ExportPolicy\x12Z\n\x11quarantine_policy\x18\x02 \x01(\x0b\x32?.oak9.tython.azure.microsoft_containerregistry.QuarantinePolicy\x12X\n\x10retention_policy\x18\x03 \x01(\x0b\x32>.oak9.tython.azure.microsoft_containerregistry.RetentionPolicy\x12P\n\x0ctrust_policy\x18\x04 \x01(\x0b\x32:.oak9.tython.azure.microsoft_containerregistry.TrustPolicy\"+\n\x0bTrustPolicy\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"/\n\x0fRetentionPolicy\x12\x0c\n\x04\x64\x61ys\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"\"\n\x10QuarantinePolicy\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x1e\n\x0c\x45xportPolicy\x12\x0e\n\x06status\x18\x01 \x01(\t\"\xd3\x01\n\x0eNetworkRuleSet\x12\x16\n\x0e\x64\x65\x66\x61ult_action\x18\x01 \x01(\t\x12G\n\x08ip_rules\x18\x02 \x03(\x0b\x32\x35.oak9.tython.azure.microsoft_containerregistry.IPRule\x12`\n\x15virtual_network_rules\x18\x03 \x03(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.VirtualNetworkRule\"0\n\x12VirtualNetworkRule\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\'\n\x06IPRule\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x85\x01\n\x12\x45ncryptionProperty\x12_\n\x14key_vault_properties\x18\x01 \x01(\x0b\x32\x41.oak9.tython.azure.microsoft_containerregistry.KeyVaultProperties\x12\x0e\n\x06status\x18\x02 \x01(\t\">\n\x12KeyVaultProperties\x12\x10\n\x08identity\x18\x01 \x01(\t\x12\x16\n\x0ekey_identifier\x18\x02 \x01(\t\"\x8b\x02\n\x12IdentityProperties\x12\x14\n\x0cprincipal_id\x18\x01 \x01(\t\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x7f\n\x18user_assigned_identities\x18\x04 \x03(\x0b\x32].oak9.tython.azure.microsoft_containerregistry.IdentityProperties.UserAssignedIdentitiesEntry\x1a=\n\x1bUserAssignedIdentitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'azure.azure_microsoft_containerregistry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTRIESWEBHOOKS_CUSTOMHEADERSENTRY._options = None
  _REGISTRIESWEBHOOKS_CUSTOMHEADERSENTRY._serialized_options = b'8\001'
  _REGISTRIESWEBHOOKS_TAGSENTRY._options = None
  _REGISTRIESWEBHOOKS_TAGSENTRY._serialized_options = b'8\001'
  _REGISTRIESREPLICATIONS_TAGSENTRY._options = None
  _REGISTRIESREPLICATIONS_TAGSENTRY._serialized_options = b'8\001'
  _REGISTRIES_TAGSENTRY._options = None
  _REGISTRIES_TAGSENTRY._serialized_options = b'8\001'
  _IDENTITYPROPERTIES_USERASSIGNEDIDENTITIESENTRY._options = None
  _IDENTITYPROPERTIES_USERASSIGNEDIDENTITIESENTRY._serialized_options = b'8\001'
  _MICROSOFT_CONTAINERREGISTRY._serialized_start=117
  _MICROSOFT_CONTAINERREGISTRY._serialized_end=225
  _REGISTRIESWEBHOOKS._serialized_start=228
  _REGISTRIESWEBHOOKS._serialized_end=706
  _REGISTRIESWEBHOOKS_CUSTOMHEADERSENTRY._serialized_start=609
  _REGISTRIESWEBHOOKS_CUSTOMHEADERSENTRY._serialized_end=661
  _REGISTRIESWEBHOOKS_TAGSENTRY._serialized_start=663
  _REGISTRIESWEBHOOKS_TAGSENTRY._serialized_end=706
  _REGISTRIESTOKENS._serialized_start=709
  _REGISTRIESTOKENS._serialized_end=932
  _TOKENCREDENTIALSPROPERTIES._serialized_start=935
  _TOKENCREDENTIALSPROPERTIES._serialized_end=1131
  _TOKENPASSWORD._serialized_start=1133
  _TOKENPASSWORD._serialized_end=1201
  _TOKENCERTIFICATE._serialized_start=1203
  _TOKENCERTIFICATE._serialized_end=1304
  _REGISTRIESSCOPEMAPS._serialized_start=1307
  _REGISTRIESSCOPEMAPS._serialized_end=1437
  _REGISTRIESREPLICATIONS._serialized_start=1440
  _REGISTRIESREPLICATIONS._serialized_end=1751
  _REGISTRIESREPLICATIONS_TAGSENTRY._serialized_start=663
  _REGISTRIESREPLICATIONS_TAGSENTRY._serialized_end=706
  _REGISTRIESPRIVATEENDPOINTCONNECTIONS._serialized_start=1754
  _REGISTRIESPRIVATEENDPOINTCONNECTIONS._serialized_end=2082
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_start=2084
  _PRIVATELINKSERVICECONNECTIONSTATE._serialized_end=2182
  _PRIVATEENDPOINT._serialized_start=2184
  _PRIVATEENDPOINT._serialized_end=2213
  _REGISTRIESPIPELINERUNS._serialized_start=2216
  _REGISTRIESPIPELINERUNS._serialized_end=2421
  _PIPELINERUNREQUEST._serialized_start=2424
  _PIPELINERUNREQUEST._serialized_end=2701
  _PIPELINERUNTARGETPROPERTIES._serialized_start=2703
  _PIPELINERUNTARGETPROPERTIES._serialized_end=2760
  _PIPELINERUNSOURCEPROPERTIES._serialized_start=2762
  _PIPELINERUNSOURCEPROPERTIES._serialized_end=2819
  _REGISTRIESIMPORTPIPELINES._serialized_start=2822
  _REGISTRIESIMPORTPIPELINES._serialized_end=3226
  _PIPELINETRIGGERPROPERTIES._serialized_start=3229
  _PIPELINETRIGGERPROPERTIES._serialized_end=3360
  _PIPELINESOURCETRIGGERPROPERTIES._serialized_start=3362
  _PIPELINESOURCETRIGGERPROPERTIES._serialized_end=3411
  _IMPORTPIPELINESOURCEPROPERTIES._serialized_start=3413
  _IMPORTPIPELINESOURCEPROPERTIES._serialized_end=3495
  _REGISTRIESEXPORTPIPELINES._serialized_start=3498
  _REGISTRIESEXPORTPIPELINES._serialized_end=3811
  _EXPORTPIPELINETARGETPROPERTIES._serialized_start=3813
  _EXPORTPIPELINETARGETPROPERTIES._serialized_end=3895
  _REGISTRIESCONNECTEDREGISTRIES._serialized_start=3898
  _REGISTRIESCONNECTEDREGISTRIES._serialized_end=4324
  _PARENTPROPERTIES._serialized_start=4326
  _PARENTPROPERTIES._serialized_end=4444
  _SYNCPROPERTIES._serialized_start=4446
  _SYNCPROPERTIES._serialized_end=4540
  _LOGINSERVERPROPERTIES._serialized_start=4542
  _LOGINSERVERPROPERTIES._serialized_end=4579
  _LOGGINGPROPERTIES._serialized_start=4581
  _LOGGINGPROPERTIES._serialized_end=4645
  _REGISTRIES._serialized_start=4648
  _REGISTRIES._serialized_end=6434
  _REGISTRIES_TAGSENTRY._serialized_start=663
  _REGISTRIES_TAGSENTRY._serialized_end=706
  _SKU._serialized_start=6436
  _SKU._serialized_end=6455
  _POLICIES._serialized_start=6458
  _POLICIES._serialized_end=6816
  _TRUSTPOLICY._serialized_start=6818
  _TRUSTPOLICY._serialized_end=6861
  _RETENTIONPOLICY._serialized_start=6863
  _RETENTIONPOLICY._serialized_end=6910
  _QUARANTINEPOLICY._serialized_start=6912
  _QUARANTINEPOLICY._serialized_end=6946
  _EXPORTPOLICY._serialized_start=6948
  _EXPORTPOLICY._serialized_end=6978
  _NETWORKRULESET._serialized_start=6981
  _NETWORKRULESET._serialized_end=7192
  _VIRTUALNETWORKRULE._serialized_start=7194
  _VIRTUALNETWORKRULE._serialized_end=7242
  _IPRULE._serialized_start=7244
  _IPRULE._serialized_end=7283
  _ENCRYPTIONPROPERTY._serialized_start=7286
  _ENCRYPTIONPROPERTY._serialized_end=7419
  _KEYVAULTPROPERTIES._serialized_start=7421
  _KEYVAULTPROPERTIES._serialized_end=7483
  _IDENTITYPROPERTIES._serialized_start=7486
  _IDENTITYPROPERTIES._serialized_end=7753
  _IDENTITYPROPERTIES_USERASSIGNEDIDENTITIESENTRY._serialized_start=7692
  _IDENTITYPROPERTIES_USERASSIGNEDIDENTITIESENTRY._serialized_end=7753
# @@protoc_insertion_point(module_scope)
