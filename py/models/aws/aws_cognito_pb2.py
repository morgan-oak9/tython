# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_cognito.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ws/aws_cognito.proto\x12\x17oak9.tython.aws.cognito\x1a\x13shared/shared.proto\"{\n\x14IdentityPoolPushSync\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10\x61pplication_arns\x18\x02 \x03(\t\x12\x10\n\x08role_arn\x18\x03 \x01(\t\"\xa9\x01\n#IdentityPoolCognitoIdentityProvider\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1f\n\x17server_side_token_check\x18\x02 \x01(\x08\x12\x15\n\rprovider_name\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\"\x96\x01\n\x1aIdentityPoolCognitoStreams\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10streaming_status\x18\x02 \x01(\t\x12\x13\n\x0bstream_name\x18\x03 \x01(\t\x12\x10\n\x08role_arn\x18\x04 \x01(\t\"\xae\x06\n\x0cIdentityPool\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12@\n\tpush_sync\x18\x02 \x01(\x0b\x32-.oak9.tython.aws.cognito.IdentityPoolPushSync\x12`\n\x1a\x63ognito_identity_providers\x18\x03 \x03(\x0b\x32<.oak9.tython.aws.cognito.IdentityPoolCognitoIdentityProvider\x12P\n\x0e\x63ognito_events\x18\x04 \x03(\x0b\x32\x38.oak9.tython.aws.cognito.IdentityPool.CognitoEventsEntry\x12\x1f\n\x17\x64\x65veloper_provider_name\x18\x05 \x01(\t\x12L\n\x0f\x63ognito_streams\x18\x06 \x01(\x0b\x32\x33.oak9.tython.aws.cognito.IdentityPoolCognitoStreams\x12\x1a\n\x12identity_pool_name\x18\x07 \x01(\t\x12(\n allow_unauthenticated_identities\x18\x08 \x01(\x08\x12\x65\n\x19supported_login_providers\x18\t \x03(\x0b\x32\x42.oak9.tython.aws.cognito.IdentityPool.SupportedLoginProvidersEntry\x12\x1a\n\x12saml_provider_arns\x18\n \x03(\t\x12%\n\x1dopen_id_connect_provider_arns\x18\x0b \x03(\t\x12\x1a\n\x12\x61llow_classic_flow\x18\x0c \x01(\x08\x1a\x34\n\x12\x43ognitoEventsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a>\n\x1cSupportedLoginProvidersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb2\t\n\x07\x43ognito\x12<\n\ridentity_pool\x18\x01 \x03(\x0b\x32%.oak9.tython.aws.cognito.IdentityPool\x12Z\n\x1didentity_pool_role_attachment\x18\x02 \x03(\x0b\x32\x33.oak9.tython.aws.cognito.IdentityPoolRoleAttachment\x12\x34\n\tuser_pool\x18\x03 \x03(\x0b\x32!.oak9.tython.aws.cognito.UserPool\x12\x41\n\x10user_pool_client\x18\x04 \x03(\x0b\x32\'.oak9.tython.aws.cognito.UserPoolClient\x12\x41\n\x10user_pool_domain\x18\x05 \x03(\x0b\x32\'.oak9.tython.aws.cognito.UserPoolDomain\x12?\n\x0fuser_pool_group\x18\x06 \x03(\x0b\x32&.oak9.tython.aws.cognito.UserPoolGroup\x12V\n\x1buser_pool_identity_provider\x18\x07 \x03(\x0b\x32\x31.oak9.tython.aws.cognito.UserPoolIdentityProvider\x12R\n\x19user_pool_resource_server\x18\x08 \x03(\x0b\x32/.oak9.tython.aws.cognito.UserPoolResourceServer\x12m\n\'user_pool_risk_configuration_attachment\x18\t \x03(\x0b\x32<.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachment\x12j\n&user_pool_u_i_customization_attachment\x18\n \x03(\x0b\x32:.oak9.tython.aws.cognito.UserPoolUICustomizationAttachment\x12=\n\x0euser_pool_user\x18\x0b \x03(\x0b\x32%.oak9.tython.aws.cognito.UserPoolUser\x12\x62\n\"user_pool_user_to_group_attachment\x18\x0c \x03(\x0b\x32\x36.oak9.tython.aws.cognito.UserPoolUserToGroupAttachment\x12r\n*identity_pool_role_attachment_mapping_rule\x18\r \x03(\x0b\x32>.oak9.tython.aws.cognito.IdentityPoolRoleAttachmentMappingRule\x12r\n*identity_pool_role_attachment_role_mapping\x18\x0e \x03(\x0b\x32>.oak9.tython.aws.cognito.IdentityPoolRoleAttachmentRoleMapping\"\xff\x02\n\x1aIdentityPoolRoleAttachment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\\\n\rrole_mappings\x18\x02 \x03(\x0b\x32\x45.oak9.tython.aws.cognito.IdentityPoolRoleAttachment.RoleMappingsEntry\x12\x18\n\x10identity_pool_id\x18\x03 \x01(\t\x12M\n\x05roles\x18\x04 \x03(\x0b\x32>.oak9.tython.aws.cognito.IdentityPoolRoleAttachment.RolesEntry\x1a\x33\n\x11RoleMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nRolesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfb\x01\n\x16UserPoolPasswordPolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0frequire_numbers\x18\x02 \x01(\x08\x12\x16\n\x0eminimum_length\x18\x03 \x01(\x05\x12(\n temporary_password_validity_days\x18\x04 \x01(\x05\x12\x19\n\x11require_uppercase\x18\x05 \x01(\x08\x12\x19\n\x11require_lowercase\x18\x06 \x01(\x08\x12\x17\n\x0frequire_symbols\x18\x07 \x01(\x08\"\x95\x01\n\x10UserPoolPolicies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12H\n\x0fpassword_policy\x18\x02 \x01(\x0b\x32/.oak9.tython.aws.cognito.UserPoolPasswordPolicy\"\xfd\x01\n#UserPoolVerificationMessageTemplate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x65mail_message_by_link\x18\x02 \x01(\t\x12\x15\n\remail_message\x18\x03 \x01(\t\x12\x13\n\x0bsms_message\x18\x04 \x01(\t\x12\x15\n\remail_subject\x18\x05 \x01(\t\x12\x1c\n\x14\x64\x65\x66\x61ult_email_option\x18\x06 \x01(\t\x12\x1d\n\x15\x65mail_subject_by_link\x18\x07 \x01(\t\"\x85\x01\n\"UserPoolStringAttributeConstraints\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nmin_length\x18\x02 \x01(\t\x12\x12\n\nmax_length\x18\x03 \x01(\t\"\x83\x01\n\"UserPoolNumberAttributeConstraints\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tmin_value\x18\x02 \x01(\t\x12\x11\n\tmax_value\x18\x03 \x01(\t\"\x88\x03\n\x17UserPoolSchemaAttribute\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12 \n\x18\x64\x65veloper_only_attribute\x18\x02 \x01(\x08\x12\x0f\n\x07mutable\x18\x03 \x01(\x08\x12\x1b\n\x13\x61ttribute_data_type\x18\x04 \x01(\t\x12\x61\n\x1cstring_attribute_constraints\x18\x05 \x01(\x0b\x32;.oak9.tython.aws.cognito.UserPoolStringAttributeConstraints\x12\x10\n\x08required\x18\x06 \x01(\x08\x12\x61\n\x1cnumber_attribute_constraints\x18\x07 \x01(\x0b\x32;.oak9.tython.aws.cognito.UserPoolNumberAttributeConstraints\x12\x0c\n\x04name\x18\x08 \x01(\t\"\x9b\x01\n\x1dUserPoolInviteMessageTemplate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\remail_message\x18\x02 \x01(\t\x12\x13\n\x0bsms_message\x18\x03 \x01(\t\x12\x15\n\remail_subject\x18\x04 \x01(\t\"\xfd\x01\n\x1dUserPoolAdminCreateUserConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12W\n\x17invite_message_template\x18\x02 \x01(\x0b\x32\x36.oak9.tython.aws.cognito.UserPoolInviteMessageTemplate\x12$\n\x1cunused_account_validity_days\x18\x03 \x01(\x05\x12$\n\x1c\x61llow_admin_create_user_only\x18\x04 \x01(\x08\"p\n\x1dUserPoolUsernameConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x16\n\x0e\x63\x61se_sensitive\x18\x02 \x01(\x08\"q\n\x16UserPoolUserPoolAddOns\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16\x61\x64vanced_security_mode\x18\x02 \x01(\t\"\xd1\x01\n\x1aUserPoolEmailConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16reply_to_email_address\x18\x02 \x01(\t\x12\x19\n\x11\x63onfiguration_set\x18\x03 \x01(\t\x12\x1d\n\x15\x65mail_sending_account\x18\x04 \x01(\t\x12\x12\n\nsource_arn\x18\x05 \x01(\t\x12\x0c\n\x04\x66rom\x18\x06 \x01(\t\"\x80\x01\n\x18UserPoolSmsConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x65xternal_id\x18\x02 \x01(\t\x12\x16\n\x0esns_caller_arn\x18\x03 \x01(\t\"\xec\x02\n\x14UserPoolLambdaConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x63reate_auth_challenge\x18\x02 \x01(\t\x12\x1a\n\x12pre_authentication\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x65\x66ine_auth_challenge\x18\x04 \x01(\t\x12\x13\n\x0bpre_sign_up\x18\x05 \x01(\t\x12\x1c\n\x14pre_token_generation\x18\x06 \x01(\t\x12\x16\n\x0euser_migration\x18\x07 \x01(\t\x12\x1b\n\x13post_authentication\x18\x08 \x01(\t\x12\x19\n\x11post_confirmation\x18\t \x01(\t\x12\x16\n\x0e\x63ustom_message\x18\n \x01(\t\x12&\n\x1everify_auth_challenge_response\x18\x0b \x01(\t\"\xaf\x01\n\x1bUserPoolDeviceConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12-\n%device_only_remembered_on_user_prompt\x18\x02 \x01(\x08\x12(\n challenge_required_on_new_device\x18\x03 \x01(\x08\"q\n\x16UserPoolRecoveryOption\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08priority\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xa7\x01\n\x1eUserPoolAccountRecoverySetting\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12L\n\x13recovery_mechanisms\x18\x02 \x03(\x0b\x32/.oak9.tython.aws.cognito.UserPoolRecoveryOption\"\xec\n\n\x08UserPool\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\x0euser_pool_tags\x18\x02 \x03(\x0b\x32\x33.oak9.tython.aws.cognito.UserPool.UserPoolTagsEntry\x12;\n\x08policies\x18\x03 \x01(\x0b\x32).oak9.tython.aws.cognito.UserPoolPolicies\x12\x63\n\x1dverification_message_template\x18\x04 \x01(\x0b\x32<.oak9.tython.aws.cognito.UserPoolVerificationMessageTemplate\x12\x19\n\x11mfa_configuration\x18\x05 \x01(\t\x12@\n\x06schema\x18\x06 \x03(\x0b\x32\x30.oak9.tython.aws.cognito.UserPoolSchemaAttribute\x12X\n\x18\x61\x64min_create_user_config\x18\x07 \x01(\x0b\x32\x36.oak9.tython.aws.cognito.UserPoolAdminCreateUserConfig\x12\"\n\x1asms_authentication_message\x18\x08 \x01(\t\x12V\n\x16username_configuration\x18\t \x01(\x0b\x32\x36.oak9.tython.aws.cognito.UserPoolUsernameConfiguration\x12\x16\n\x0euser_pool_name\x18\n \x01(\t\x12 \n\x18sms_verification_message\x18\x0b \x01(\t\x12J\n\x11user_pool_add_ons\x18\x0c \x01(\x0b\x32/.oak9.tython.aws.cognito.UserPoolUserPoolAddOns\x12P\n\x13\x65mail_configuration\x18\r \x01(\x0b\x32\x33.oak9.tython.aws.cognito.UserPoolEmailConfiguration\x12L\n\x11sms_configuration\x18\x0e \x01(\x0b\x32\x31.oak9.tython.aws.cognito.UserPoolSmsConfiguration\x12\x18\n\x10\x61lias_attributes\x18\x0f \x03(\t\x12\x14\n\x0c\x65nabled_mfas\x18\x10 \x03(\t\x12\"\n\x1a\x65mail_verification_subject\x18\x11 \x01(\t\x12\x44\n\rlambda_config\x18\x12 \x01(\x0b\x32-.oak9.tython.aws.cognito.UserPoolLambdaConfig\x12\x1b\n\x13username_attributes\x18\x13 \x03(\t\x12 \n\x18\x61uto_verified_attributes\x18\x14 \x03(\t\x12R\n\x14\x64\x65vice_configuration\x18\x15 \x01(\x0b\x32\x34.oak9.tython.aws.cognito.UserPoolDeviceConfiguration\x12\"\n\x1a\x65mail_verification_message\x18\x16 \x01(\t\x12Y\n\x18\x61\x63\x63ount_recovery_setting\x18\x17 \x01(\x0b\x32\x37.oak9.tython.aws.cognito.UserPoolAccountRecoverySetting\x1a\x33\n\x11UserPoolTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb8\x01\n$UserPoolClientAnalyticsConfiguration\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x18\n\x10user_data_shared\x18\x02 \x01(\x08\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x04 \x01(\t\x12\x10\n\x08role_arn\x18\x05 \x01(\t\"\x9a\x01\n UserPoolClientTokenValidityUnits\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08id_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\"\xf9\x05\n\x0eUserPoolClient\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12^\n\x17\x61nalytics_configuration\x18\x02 \x01(\x0b\x32=.oak9.tython.aws.cognito.UserPoolClientAnalyticsConfiguration\x12\x17\n\x0fgenerate_secret\x18\x03 \x01(\x08\x12\x17\n\x0f\x63\x61llback_u_r_ls\x18\x04 \x03(\t\x12\x19\n\x11id_token_validity\x18\x05 \x01(\x05\x12\x1d\n\x15\x61llowed_o_auth_scopes\x18\x06 \x03(\t\x12W\n\x14token_validity_units\x18\x07 \x01(\x0b\x32\x39.oak9.tython.aws.cognito.UserPoolClientTokenValidityUnits\x12\x17\n\x0fread_attributes\x18\x08 \x03(\t\x12-\n%allowed_o_auth_flows_user_pool_client\x18\t \x01(\x08\x12\x1e\n\x16\x64\x65\x66\x61ult_redirect_u_r_i\x18\n \x01(\t\x12$\n\x1csupported_identity_providers\x18\x0b \x03(\t\x12\x13\n\x0b\x63lient_name\x18\x0c \x01(\t\x12\x14\n\x0cuser_pool_id\x18\r \x01(\t\x12\x1c\n\x14\x61llowed_o_auth_flows\x18\x0e \x03(\t\x12\x1b\n\x13\x65xplicit_auth_flows\x18\x0f \x03(\t\x12\x15\n\rlogout_u_r_ls\x18\x10 \x03(\t\x12\x1d\n\x15\x61\x63\x63\x65ss_token_validity\x18\x11 \x01(\x05\x12\x1e\n\x16refresh_token_validity\x18\x12 \x01(\x05\x12\x18\n\x10write_attributes\x18\x13 \x03(\t\x12%\n\x1dprevent_user_existence_errors\x18\x14 \x01(\t\"x\n$UserPoolDomainCustomDomainConfigType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63\x65rtificate_arn\x18\x02 \x01(\t\"\xcc\x01\n\x0eUserPoolDomain\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cuser_pool_id\x18\x02 \x01(\t\x12[\n\x14\x63ustom_domain_config\x18\x03 \x01(\x0b\x32=.oak9.tython.aws.cognito.UserPoolDomainCustomDomainConfigType\x12\x0e\n\x06\x64omain\x18\x04 \x01(\t\"\xad\x01\n\rUserPoolGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cuser_pool_id\x18\x04 \x01(\t\x12\x12\n\nprecedence\x18\x05 \x01(\x01\x12\x10\n\x08role_arn\x18\x06 \x01(\t\"\xe7\x03\n\x18UserPoolIdentityProvider\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rprovider_name\x18\x02 \x01(\t\x12\x14\n\x0cuser_pool_id\x18\x03 \x01(\t\x12\x62\n\x11\x61ttribute_mapping\x18\x04 \x03(\x0b\x32G.oak9.tython.aws.cognito.UserPoolIdentityProvider.AttributeMappingEntry\x12`\n\x10provider_details\x18\x05 \x03(\x0b\x32\x46.oak9.tython.aws.cognito.UserPoolIdentityProvider.ProviderDetailsEntry\x12\x15\n\rprovider_type\x18\x06 \x01(\t\x12\x17\n\x0fidp_identifiers\x18\x07 \x03(\t\x1a\x37\n\x15\x41ttributeMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14ProviderDetailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x97\x01\n-UserPoolResourceServerResourceServerScopeType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nscope_name\x18\x02 \x01(\t\x12\x19\n\x11scope_description\x18\x03 \x01(\t\"\xe1\x01\n\x16UserPoolResourceServer\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cuser_pool_id\x18\x02 \x01(\t\x12\x12\n\nidentifier\x18\x03 \x01(\t\x12V\n\x06scopes\x18\x04 \x03(\x0b\x32\x46.oak9.tython.aws.cognito.UserPoolResourceServerResourceServerScopeType\x12\x0c\n\x04name\x18\x05 \x01(\t\"\x95\x01\nDUserPoolRiskConfigurationAttachmentCompromisedCredentialsActionsType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0c\x65vent_action\x18\x02 \x01(\t\"\x8f\x02\nNUserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12n\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32].oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentCompromisedCredentialsActionsType\x12\x14\n\x0c\x65vent_filter\x18\x03 \x03(\t\"\x9d\x01\n<UserPoolRiskConfigurationAttachmentAccountTakeoverActionType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06notify\x18\x02 \x01(\x08\x12\x14\n\x0c\x65vent_action\x18\x03 \x01(\t\"\xbd\x03\n=UserPoolRiskConfigurationAttachmentAccountTakeoverActionsType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12j\n\x0bhigh_action\x18\x02 \x01(\x0b\x32U.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentAccountTakeoverActionType\x12i\n\nlow_action\x18\x03 \x01(\x0b\x32U.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentAccountTakeoverActionType\x12l\n\rmedium_action\x18\x04 \x01(\x0b\x32U.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentAccountTakeoverActionType\"\xa4\x01\n2UserPoolRiskConfigurationAttachmentNotifyEmailType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\ttext_body\x18\x02 \x01(\t\x12\x11\n\thtml_body\x18\x03 \x01(\t\x12\x0f\n\x07subject\x18\x04 \x01(\t\"\xd1\x03\n:UserPoolRiskConfigurationAttachmentNotifyConfigurationType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12`\n\x0b\x62lock_email\x18\x02 \x01(\x0b\x32K.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentNotifyEmailType\x12\x10\n\x08reply_to\x18\x03 \x01(\t\x12\x12\n\nsource_arn\x18\x04 \x01(\t\x12\x64\n\x0fno_action_email\x18\x05 \x01(\x0b\x32K.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentNotifyEmailType\x12\x0c\n\x04\x66rom\x18\x06 \x01(\t\x12^\n\tmfa_email\x18\x07 \x01(\x0b\x32K.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentNotifyEmailType\"\xde\x02\nGUserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12g\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32V.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentAccountTakeoverActionsType\x12q\n\x14notify_configuration\x18\x03 \x01(\x0b\x32S.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentNotifyConfigurationType\"\xba\x01\nAUserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15\x62locked_ip_range_list\x18\x02 \x03(\t\x12\x1d\n\x15skipped_ip_range_list\x18\x03 \x03(\t\"\xb8\x04\n#UserPoolRiskConfigurationAttachment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x9b\x01\n*compromised_credentials_risk_configuration\x18\x02 \x01(\x0b\x32g.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType\x12\x14\n\x0cuser_pool_id\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\x8d\x01\n#account_takeover_risk_configuration\x18\x05 \x01(\x0b\x32`.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType\x12\x80\x01\n\x1crisk_exception_configuration\x18\x06 \x01(\x0b\x32Z.oak9.tython.aws.cognito.UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType\"\x93\x01\n!UserPoolUICustomizationAttachment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x63s_s\x18\x02 \x01(\t\x12\x14\n\x0cuser_pool_id\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\"q\n\x19UserPoolUserAttributeType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xec\x03\n\x0cUserPoolUser\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12K\n\x0fvalidation_data\x18\x02 \x03(\x0b\x32\x32.oak9.tython.aws.cognito.UserPoolUserAttributeType\x12\x14\n\x0cuser_pool_id\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x16\n\x0emessage_action\x18\x05 \x01(\t\x12R\n\x0f\x63lient_metadata\x18\x06 \x03(\x0b\x32\x39.oak9.tython.aws.cognito.UserPoolUser.ClientMetadataEntry\x12 \n\x18\x64\x65sired_delivery_mediums\x18\x07 \x03(\t\x12\x1c\n\x14\x66orce_alias_creation\x18\x08 \x01(\x08\x12K\n\x0fuser_attributes\x18\t \x03(\x0b\x32\x32.oak9.tython.aws.cognito.UserPoolUserAttributeType\x1a\x35\n\x13\x43lientMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x94\x01\n\x1dUserPoolUserToGroupAttachment\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x14\n\x0cuser_pool_id\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\"\xa4\x01\n%IdentityPoolRoleAttachmentMappingRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x12\n\nmatch_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\r\n\x05\x63laim\x18\x04 \x01(\t\x12\x10\n\x08role_arn\x18\x05 \x01(\t\"\xba\x01\n0IdentityPoolRoleAttachmentRulesConfigurationType\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12M\n\x05rules\x18\x02 \x03(\x0b\x32>.oak9.tython.aws.cognito.IdentityPoolRoleAttachmentMappingRule\"\x86\x02\n%IdentityPoolRoleAttachmentRoleMapping\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12!\n\x19\x61mbiguous_role_resolution\x18\x02 \x01(\t\x12\x66\n\x13rules_configuration\x18\x03 \x01(\x0b\x32I.oak9.tython.aws.cognito.IdentityPoolRoleAttachmentRulesConfigurationType\x12\x19\n\x11identity_provider\x18\x04 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_cognito_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IDENTITYPOOL_COGNITOEVENTSENTRY._options = None
  _IDENTITYPOOL_COGNITOEVENTSENTRY._serialized_options = b'8\001'
  _IDENTITYPOOL_SUPPORTEDLOGINPROVIDERSENTRY._options = None
  _IDENTITYPOOL_SUPPORTEDLOGINPROVIDERSENTRY._serialized_options = b'8\001'
  _IDENTITYPOOLROLEATTACHMENT_ROLEMAPPINGSENTRY._options = None
  _IDENTITYPOOLROLEATTACHMENT_ROLEMAPPINGSENTRY._serialized_options = b'8\001'
  _IDENTITYPOOLROLEATTACHMENT_ROLESENTRY._options = None
  _IDENTITYPOOLROLEATTACHMENT_ROLESENTRY._serialized_options = b'8\001'
  _USERPOOL_USERPOOLTAGSENTRY._options = None
  _USERPOOL_USERPOOLTAGSENTRY._serialized_options = b'8\001'
  _USERPOOLIDENTITYPROVIDER_ATTRIBUTEMAPPINGENTRY._options = None
  _USERPOOLIDENTITYPROVIDER_ATTRIBUTEMAPPINGENTRY._serialized_options = b'8\001'
  _USERPOOLIDENTITYPROVIDER_PROVIDERDETAILSENTRY._options = None
  _USERPOOLIDENTITYPROVIDER_PROVIDERDETAILSENTRY._serialized_options = b'8\001'
  _USERPOOLUSER_CLIENTMETADATAENTRY._options = None
  _USERPOOLUSER_CLIENTMETADATAENTRY._serialized_options = b'8\001'
  _IDENTITYPOOLPUSHSYNC._serialized_start=71
  _IDENTITYPOOLPUSHSYNC._serialized_end=194
  _IDENTITYPOOLCOGNITOIDENTITYPROVIDER._serialized_start=197
  _IDENTITYPOOLCOGNITOIDENTITYPROVIDER._serialized_end=366
  _IDENTITYPOOLCOGNITOSTREAMS._serialized_start=369
  _IDENTITYPOOLCOGNITOSTREAMS._serialized_end=519
  _IDENTITYPOOL._serialized_start=522
  _IDENTITYPOOL._serialized_end=1336
  _IDENTITYPOOL_COGNITOEVENTSENTRY._serialized_start=1220
  _IDENTITYPOOL_COGNITOEVENTSENTRY._serialized_end=1272
  _IDENTITYPOOL_SUPPORTEDLOGINPROVIDERSENTRY._serialized_start=1274
  _IDENTITYPOOL_SUPPORTEDLOGINPROVIDERSENTRY._serialized_end=1336
  _COGNITO._serialized_start=1339
  _COGNITO._serialized_end=2541
  _IDENTITYPOOLROLEATTACHMENT._serialized_start=2544
  _IDENTITYPOOLROLEATTACHMENT._serialized_end=2927
  _IDENTITYPOOLROLEATTACHMENT_ROLEMAPPINGSENTRY._serialized_start=2830
  _IDENTITYPOOLROLEATTACHMENT_ROLEMAPPINGSENTRY._serialized_end=2881
  _IDENTITYPOOLROLEATTACHMENT_ROLESENTRY._serialized_start=2883
  _IDENTITYPOOLROLEATTACHMENT_ROLESENTRY._serialized_end=2927
  _USERPOOLPASSWORDPOLICY._serialized_start=2930
  _USERPOOLPASSWORDPOLICY._serialized_end=3181
  _USERPOOLPOLICIES._serialized_start=3184
  _USERPOOLPOLICIES._serialized_end=3333
  _USERPOOLVERIFICATIONMESSAGETEMPLATE._serialized_start=3336
  _USERPOOLVERIFICATIONMESSAGETEMPLATE._serialized_end=3589
  _USERPOOLSTRINGATTRIBUTECONSTRAINTS._serialized_start=3592
  _USERPOOLSTRINGATTRIBUTECONSTRAINTS._serialized_end=3725
  _USERPOOLNUMBERATTRIBUTECONSTRAINTS._serialized_start=3728
  _USERPOOLNUMBERATTRIBUTECONSTRAINTS._serialized_end=3859
  _USERPOOLSCHEMAATTRIBUTE._serialized_start=3862
  _USERPOOLSCHEMAATTRIBUTE._serialized_end=4254
  _USERPOOLINVITEMESSAGETEMPLATE._serialized_start=4257
  _USERPOOLINVITEMESSAGETEMPLATE._serialized_end=4412
  _USERPOOLADMINCREATEUSERCONFIG._serialized_start=4415
  _USERPOOLADMINCREATEUSERCONFIG._serialized_end=4668
  _USERPOOLUSERNAMECONFIGURATION._serialized_start=4670
  _USERPOOLUSERNAMECONFIGURATION._serialized_end=4782
  _USERPOOLUSERPOOLADDONS._serialized_start=4784
  _USERPOOLUSERPOOLADDONS._serialized_end=4897
  _USERPOOLEMAILCONFIGURATION._serialized_start=4900
  _USERPOOLEMAILCONFIGURATION._serialized_end=5109
  _USERPOOLSMSCONFIGURATION._serialized_start=5112
  _USERPOOLSMSCONFIGURATION._serialized_end=5240
  _USERPOOLLAMBDACONFIG._serialized_start=5243
  _USERPOOLLAMBDACONFIG._serialized_end=5607
  _USERPOOLDEVICECONFIGURATION._serialized_start=5610
  _USERPOOLDEVICECONFIGURATION._serialized_end=5785
  _USERPOOLRECOVERYOPTION._serialized_start=5787
  _USERPOOLRECOVERYOPTION._serialized_end=5900
  _USERPOOLACCOUNTRECOVERYSETTING._serialized_start=5903
  _USERPOOLACCOUNTRECOVERYSETTING._serialized_end=6070
  _USERPOOL._serialized_start=6073
  _USERPOOL._serialized_end=7461
  _USERPOOL_USERPOOLTAGSENTRY._serialized_start=7410
  _USERPOOL_USERPOOLTAGSENTRY._serialized_end=7461
  _USERPOOLCLIENTANALYTICSCONFIGURATION._serialized_start=7464
  _USERPOOLCLIENTANALYTICSCONFIGURATION._serialized_end=7648
  _USERPOOLCLIENTTOKENVALIDITYUNITS._serialized_start=7651
  _USERPOOLCLIENTTOKENVALIDITYUNITS._serialized_end=7805
  _USERPOOLCLIENT._serialized_start=7808
  _USERPOOLCLIENT._serialized_end=8569
  _USERPOOLDOMAINCUSTOMDOMAINCONFIGTYPE._serialized_start=8571
  _USERPOOLDOMAINCUSTOMDOMAINCONFIGTYPE._serialized_end=8691
  _USERPOOLDOMAIN._serialized_start=8694
  _USERPOOLDOMAIN._serialized_end=8898
  _USERPOOLGROUP._serialized_start=8901
  _USERPOOLGROUP._serialized_end=9074
  _USERPOOLIDENTITYPROVIDER._serialized_start=9077
  _USERPOOLIDENTITYPROVIDER._serialized_end=9564
  _USERPOOLIDENTITYPROVIDER_ATTRIBUTEMAPPINGENTRY._serialized_start=9453
  _USERPOOLIDENTITYPROVIDER_ATTRIBUTEMAPPINGENTRY._serialized_end=9508
  _USERPOOLIDENTITYPROVIDER_PROVIDERDETAILSENTRY._serialized_start=9510
  _USERPOOLIDENTITYPROVIDER_PROVIDERDETAILSENTRY._serialized_end=9564
  _USERPOOLRESOURCESERVERRESOURCESERVERSCOPETYPE._serialized_start=9567
  _USERPOOLRESOURCESERVERRESOURCESERVERSCOPETYPE._serialized_end=9718
  _USERPOOLRESOURCESERVER._serialized_start=9721
  _USERPOOLRESOURCESERVER._serialized_end=9946
  _USERPOOLRISKCONFIGURATIONATTACHMENTCOMPROMISEDCREDENTIALSACTIONSTYPE._serialized_start=9949
  _USERPOOLRISKCONFIGURATIONATTACHMENTCOMPROMISEDCREDENTIALSACTIONSTYPE._serialized_end=10098
  _USERPOOLRISKCONFIGURATIONATTACHMENTCOMPROMISEDCREDENTIALSRISKCONFIGURATIONTYPE._serialized_start=10101
  _USERPOOLRISKCONFIGURATIONATTACHMENTCOMPROMISEDCREDENTIALSRISKCONFIGURATIONTYPE._serialized_end=10372
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERACTIONTYPE._serialized_start=10375
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERACTIONTYPE._serialized_end=10532
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERACTIONSTYPE._serialized_start=10535
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERACTIONSTYPE._serialized_end=10980
  _USERPOOLRISKCONFIGURATIONATTACHMENTNOTIFYEMAILTYPE._serialized_start=10983
  _USERPOOLRISKCONFIGURATIONATTACHMENTNOTIFYEMAILTYPE._serialized_end=11147
  _USERPOOLRISKCONFIGURATIONATTACHMENTNOTIFYCONFIGURATIONTYPE._serialized_start=11150
  _USERPOOLRISKCONFIGURATIONATTACHMENTNOTIFYCONFIGURATIONTYPE._serialized_end=11615
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERRISKCONFIGURATIONTYPE._serialized_start=11618
  _USERPOOLRISKCONFIGURATIONATTACHMENTACCOUNTTAKEOVERRISKCONFIGURATIONTYPE._serialized_end=11968
  _USERPOOLRISKCONFIGURATIONATTACHMENTRISKEXCEPTIONCONFIGURATIONTYPE._serialized_start=11971
  _USERPOOLRISKCONFIGURATIONATTACHMENTRISKEXCEPTIONCONFIGURATIONTYPE._serialized_end=12157
  _USERPOOLRISKCONFIGURATIONATTACHMENT._serialized_start=12160
  _USERPOOLRISKCONFIGURATIONATTACHMENT._serialized_end=12728
  _USERPOOLUICUSTOMIZATIONATTACHMENT._serialized_start=12731
  _USERPOOLUICUSTOMIZATIONATTACHMENT._serialized_end=12878
  _USERPOOLUSERATTRIBUTETYPE._serialized_start=12880
  _USERPOOLUSERATTRIBUTETYPE._serialized_end=12993
  _USERPOOLUSER._serialized_start=12996
  _USERPOOLUSER._serialized_end=13488
  _USERPOOLUSER_CLIENTMETADATAENTRY._serialized_start=13435
  _USERPOOLUSER_CLIENTMETADATAENTRY._serialized_end=13488
  _USERPOOLUSERTOGROUPATTACHMENT._serialized_start=13491
  _USERPOOLUSERTOGROUPATTACHMENT._serialized_end=13639
  _IDENTITYPOOLROLEATTACHMENTMAPPINGRULE._serialized_start=13642
  _IDENTITYPOOLROLEATTACHMENTMAPPINGRULE._serialized_end=13806
  _IDENTITYPOOLROLEATTACHMENTRULESCONFIGURATIONTYPE._serialized_start=13809
  _IDENTITYPOOLROLEATTACHMENTRULESCONFIGURATIONTYPE._serialized_end=13995
  _IDENTITYPOOLROLEATTACHMENTROLEMAPPING._serialized_start=13998
  _IDENTITYPOOLROLEATTACHMENTROLEMAPPING._serialized_end=14260
# @@protoc_insertion_point(module_scope)
