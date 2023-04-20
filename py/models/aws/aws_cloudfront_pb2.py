# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_cloudfront.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61ws/aws_cloudfront.proto\x12\x1aoak9.tython.aws.cloudfront\x1a\x13shared/shared.proto\"}\n\x18\x43\x61\x63hePolicyCookiesConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63ookie_behavior\x18\x02 \x01(\t\x12\x0f\n\x07\x63ookies\x18\x03 \x03(\t\"}\n\x18\x43\x61\x63hePolicyHeadersConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0fheader_behavior\x18\x02 \x01(\t\x12\x0f\n\x07headers\x18\x03 \x03(\t\"\x8e\x01\n\x1d\x43\x61\x63hePolicyQueryStringsConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15query_string_behavior\x18\x02 \x01(\t\x12\x15\n\rquery_strings\x18\x03 \x03(\t\"\x88\x03\n3CachePolicyParametersInCacheKeyAndForwardedToOrigin\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12L\n\x0e\x63ookies_config\x18\x02 \x01(\x0b\x32\x34.oak9.tython.aws.cloudfront.CachePolicyCookiesConfig\x12#\n\x1b\x65nable_accept_encoding_gzip\x18\x03 \x01(\x08\x12L\n\x0eheaders_config\x18\x04 \x01(\x0b\x32\x34.oak9.tython.aws.cloudfront.CachePolicyHeadersConfig\x12W\n\x14query_strings_config\x18\x05 \x01(\x0b\x32\x39.oak9.tython.aws.cloudfront.CachePolicyQueryStringsConfig\"\xb8\x02\n\x1c\x43\x61\x63hePolicyCachePolicyConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65\x66\x61ult_ttl\x18\x03 \x01(\x01\x12\x0f\n\x07max_ttl\x18\x04 \x01(\x01\x12\x0f\n\x07min_ttl\x18\x05 \x01(\x01\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x88\x01\n/parameters_in_cache_key_and_forwarded_to_origin\x18\x07 \x01(\x0b\x32O.oak9.tython.aws.cloudfront.CachePolicyParametersInCacheKeyAndForwardedToOrigin\"\x9d\x01\n\x0b\x43\x61\x63hePolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12U\n\x13\x63\x61\x63he_policy_config\x18\x02 \x01(\x0b\x32\x38.oak9.tython.aws.cloudfront.CachePolicyCachePolicyConfig\"\xfa\x02\n\nCloudFront\x12=\n\x0c\x63\x61\x63he_policy\x18\x01 \x03(\x0b\x32\'.oak9.tython.aws.cloudfront.CachePolicy\x12>\n\x0c\x64istribution\x18\x02 \x01(\x0b\x32(.oak9.tython.aws.cloudfront.Distribution\x12N\n\x15origin_request_policy\x18\x03 \x03(\x0b\x32/.oak9.tython.aws.cloudfront.OriginRequestPolicy\x12J\n\x13realtime_log_config\x18\x04 \x03(\x0b\x32-.oak9.tython.aws.cloudfront.RealtimeLogConfig\x12Q\n\x16streaming_distribution\x18\x05 \x01(\x0b\x32\x31.oak9.tython.aws.cloudfront.StreamingDistribution\"\x8e\x01\nBCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"\xed\x01\n\x1e\x43loudFrontOriginAccessIdentity\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x91\x01\n)cloud_front_origin_access_identity_config\x18\x02 \x01(\x0b\x32^.oak9.tython.aws.cloudfront.CloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig\"\x87\x01\n\x13\x44istributionLogging\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0finclude_cookies\x18\x02 \x01(\x08\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\x12\x0e\n\x06prefix\x18\x04 \x01(\t\"\x84\x01\n\x1e\x44istributionOriginCustomHeader\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cheader_value\x18\x02 \x01(\t\x12\x13\n\x0bheader_name\x18\x03 \x01(\t\"u\n\x1a\x44istributionS3OriginConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1e\n\x16origin_access_identity\x18\x02 \x01(\t\"\xfe\x01\n\x1e\x44istributionCustomOriginConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13origin_read_timeout\x18\x02 \x01(\x05\x12\x13\n\x0bhttp_s_port\x18\x03 \x01(\x05\x12 \n\x18origin_keepalive_timeout\x18\x04 \x01(\x05\x12\x1c\n\x14origin_ssl_protocols\x18\x05 \x03(\t\x12\x11\n\thttp_port\x18\x06 \x01(\x05\x12\x1e\n\x16origin_protocol_policy\x18\x07 \x01(\t\"\xb4\x04\n\x12\x44istributionOrigin\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12\x63onnection_timeout\x18\x02 \x01(\x05\x12Y\n\x15origin_custom_headers\x18\x03 \x03(\x0b\x32:.oak9.tython.aws.cloudfront.DistributionOriginCustomHeader\x12\x1b\n\x13\x63onnection_attempts\x18\x04 \x01(\x05\x12\x13\n\x0b\x64omain_name\x18\x05 \x01(\t\x12P\n\x10s3_origin_config\x18\x06 \x01(\x0b\x32\x36.oak9.tython.aws.cloudfront.DistributionS3OriginConfig\x12\x13\n\x0borigin_path\x18\x07 \x01(\t\x12\n\n\x02id\x18\x08 \x01(\t\x12X\n\x14\x63ustom_origin_config\x18\t \x01(\x0b\x32:.oak9.tython.aws.cloudfront.DistributionCustomOriginConfig\x12W\n\x13\x64istribution_config\x18\n \x01(\x0b\x32:.oak9.tython.aws.cloudfront.DistributionDistributionConfig\x12\x16\n\x0e\x63ustom_headers\x18\x0b \x01(\t\"\xf8\x01\n\x1d\x44istributionViewerCertificate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1a\n\x12iam_certificate_id\x18\x02 \x01(\t\x12\x1a\n\x12ssl_support_method\x18\x03 \x01(\t\x12 \n\x18minimum_protocol_version\x18\x04 \x01(\t\x12\'\n\x1f\x63loud_front_default_certificate\x18\x05 \x01(\x08\x12\x1b\n\x13\x61\x63m_certificate_arn\x18\x06 \x01(\t\"\xa7\x01\n%DistributionLambdaFunctionAssociation\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x14\n\x0cinclude_body\x18\x02 \x01(\x08\x12\x12\n\nevent_type\x18\x03 \x01(\t\x12\x1b\n\x13lambda_function_arn\x18\x04 \x01(\t\"z\n\x13\x44istributionCookies\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x19\n\x11whitelisted_names\x18\x02 \x03(\t\x12\x0f\n\x07\x66orward\x18\x03 \x01(\t\"\xe0\x01\n\x1b\x44istributionForwardedValues\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12@\n\x07\x63ookies\x18\x02 \x01(\x0b\x32/.oak9.tython.aws.cloudfront.DistributionCookies\x12\x0f\n\x07headers\x18\x03 \x03(\t\x12\x14\n\x0cquery_string\x18\x04 \x01(\x08\x12\x1f\n\x17query_string_cache_keys\x18\x05 \x03(\t\"\xfd\x04\n DistributionDefaultCacheBehavior\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63ompress\x18\x02 \x01(\x08\x12g\n\x1clambda_function_associations\x18\x03 \x03(\x0b\x32\x41.oak9.tython.aws.cloudfront.DistributionLambdaFunctionAssociation\x12\x18\n\x10target_origin_id\x18\x04 \x01(\t\x12\x1e\n\x16viewer_protocol_policy\x18\x05 \x01(\t\x12\x1f\n\x17realtime_log_config_arn\x18\x06 \x01(\t\x12\x17\n\x0ftrusted_signers\x18\x07 \x03(\t\x12\x13\n\x0b\x64\x65\x66\x61ult_ttl\x18\x08 \x01(\x01\x12!\n\x19\x66ield_level_encryption_id\x18\t \x01(\t\x12\x17\n\x0f\x61llowed_methods\x18\n \x03(\t\x12\x16\n\x0e\x63\x61\x63hed_methods\x18\x0b \x03(\t\x12\x18\n\x10smooth_streaming\x18\x0c \x01(\x08\x12Q\n\x10\x66orwarded_values\x18\r \x01(\x0b\x32\x37.oak9.tython.aws.cloudfront.DistributionForwardedValues\x12 \n\x18origin_request_policy_id\x18\x0e \x01(\t\x12\x0f\n\x07min_ttl\x18\x0f \x01(\x01\x12\x17\n\x0f\x63\x61\x63he_policy_id\x18\x10 \x01(\t\x12\x0f\n\x07max_ttl\x18\x11 \x01(\x01\"\xc0\x01\n\x1f\x44istributionCustomErrorResponse\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x15\n\rresponse_code\x18\x02 \x01(\x05\x12\x1d\n\x15\x65rror_caching_min_ttl\x18\x03 \x01(\x01\x12\x12\n\nerror_code\x18\x04 \x01(\x05\x12\x1a\n\x12response_page_path\x18\x05 \x01(\t\"s\n\x17\x44istributionStatusCodes\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\r\n\x05items\x18\x03 \x03(\x05\"\xad\x01\n\'DistributionOriginGroupFailoverCriteria\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12I\n\x0cstatus_codes\x18\x02 \x01(\x0b\x32\x33.oak9.tython.aws.cloudfront.DistributionStatusCodes\"k\n\x1d\x44istributionOriginGroupMember\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\torigin_id\x18\x02 \x01(\t\"\xb5\x01\n\x1e\x44istributionOriginGroupMembers\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12H\n\x05items\x18\x03 \x03(\x0b\x32\x39.oak9.tython.aws.cloudfront.DistributionOriginGroupMember\"\x8b\x02\n\x17\x44istributionOriginGroup\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12^\n\x11\x66\x61ilover_criteria\x18\x03 \x01(\x0b\x32\x43.oak9.tython.aws.cloudfront.DistributionOriginGroupFailoverCriteria\x12K\n\x07members\x18\x04 \x01(\x0b\x32:.oak9.tython.aws.cloudfront.DistributionOriginGroupMembers\"\xa9\x01\n\x18\x44istributionOriginGroups\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x42\n\x05items\x18\x03 \x03(\x0b\x32\x33.oak9.tython.aws.cloudfront.DistributionOriginGroup\"\x82\x01\n\x1a\x44istributionGeoRestriction\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x11\n\tlocations\x18\x02 \x03(\t\x12\x18\n\x10restriction_type\x18\x03 \x01(\t\"\xa4\x01\n\x18\x44istributionRestrictions\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12O\n\x0fgeo_restriction\x18\x02 \x01(\x0b\x32\x36.oak9.tython.aws.cloudfront.DistributionGeoRestriction\"\x8c\x05\n\x19\x44istributionCacheBehavior\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08\x63ompress\x18\x02 \x01(\x08\x12g\n\x1clambda_function_associations\x18\x03 \x03(\x0b\x32\x41.oak9.tython.aws.cloudfront.DistributionLambdaFunctionAssociation\x12\x18\n\x10target_origin_id\x18\x04 \x01(\t\x12\x1e\n\x16viewer_protocol_policy\x18\x05 \x01(\t\x12\x1f\n\x17realtime_log_config_arn\x18\x06 \x01(\t\x12\x17\n\x0ftrusted_signers\x18\x07 \x03(\t\x12\x13\n\x0b\x64\x65\x66\x61ult_ttl\x18\x08 \x01(\x01\x12!\n\x19\x66ield_level_encryption_id\x18\t \x01(\t\x12\x17\n\x0f\x61llowed_methods\x18\n \x03(\t\x12\x14\n\x0cpath_pattern\x18\x0b \x01(\t\x12\x16\n\x0e\x63\x61\x63hed_methods\x18\x0c \x03(\t\x12\x18\n\x10smooth_streaming\x18\r \x01(\x08\x12Q\n\x10\x66orwarded_values\x18\x0e \x01(\x0b\x32\x37.oak9.tython.aws.cloudfront.DistributionForwardedValues\x12 \n\x18origin_request_policy_id\x18\x0f \x01(\t\x12\x0f\n\x07min_ttl\x18\x10 \x01(\x01\x12\x17\n\x0f\x63\x61\x63he_policy_id\x18\x11 \x01(\t\x12\x0f\n\x07max_ttl\x18\x12 \x01(\x01\"\xff\x06\n\x1e\x44istributionDistributionConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12@\n\x07logging\x18\x02 \x01(\x0b\x32/.oak9.tython.aws.cloudfront.DistributionLogging\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x1b\n\x13\x64\x65\x66\x61ult_root_object\x18\x04 \x01(\t\x12?\n\x07origins\x18\x05 \x03(\x0b\x32..oak9.tython.aws.cloudfront.DistributionOrigin\x12U\n\x12viewer_certificate\x18\x06 \x01(\x0b\x32\x39.oak9.tython.aws.cloudfront.DistributionViewerCertificate\x12\x13\n\x0bprice_class\x18\x07 \x01(\t\x12\\\n\x16\x64\x65\x66\x61ult_cache_behavior\x18\x08 \x01(\x0b\x32<.oak9.tython.aws.cloudfront.DistributionDefaultCacheBehavior\x12[\n\x16\x63ustom_error_responses\x18\t \x03(\x0b\x32;.oak9.tython.aws.cloudfront.DistributionCustomErrorResponse\x12K\n\rorigin_groups\x18\n \x01(\x0b\x32\x34.oak9.tython.aws.cloudfront.DistributionOriginGroups\x12\x0f\n\x07\x65nabled\x18\x0b \x01(\x08\x12\x0f\n\x07\x61liases\x18\x0c \x03(\t\x12\x15\n\rip_v6_enabled\x18\r \x01(\x08\x12\x14\n\x0cweb_a_c_l_id\x18\x0e \x01(\t\x12\x14\n\x0chttp_version\x18\x0f \x01(\t\x12J\n\x0crestrictions\x18\x10 \x01(\x0b\x32\x34.oak9.tython.aws.cloudfront.DistributionRestrictions\x12N\n\x0f\x63\x61\x63he_behaviors\x18\x11 \x03(\x0b\x32\x35.oak9.tython.aws.cloudfront.DistributionCacheBehavior\"\x8f\x02\n\x0c\x44istribution\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12W\n\x13\x64istribution_config\x18\x02 \x01(\x0b\x32:.oak9.tython.aws.cloudfront.DistributionDistributionConfig\x12@\n\x04tags\x18\x03 \x03(\x0b\x32\x32.oak9.tython.aws.cloudfront.Distribution.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x85\x01\n OriginRequestPolicyCookiesConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0f\x63ookie_behavior\x18\x02 \x01(\t\x12\x0f\n\x07\x63ookies\x18\x03 \x03(\t\"\x85\x01\n OriginRequestPolicyHeadersConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x17\n\x0fheader_behavior\x18\x02 \x01(\t\x12\x0f\n\x07headers\x18\x03 \x03(\t\"\x96\x01\n%OriginRequestPolicyQueryStringsConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1d\n\x15query_string_behavior\x18\x02 \x01(\t\x12\x15\n\rquery_strings\x18\x03 \x03(\t\"\x93\x03\n,OriginRequestPolicyOriginRequestPolicyConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12T\n\x0e\x63ookies_config\x18\x03 \x01(\x0b\x32<.oak9.tython.aws.cloudfront.OriginRequestPolicyCookiesConfig\x12T\n\x0eheaders_config\x18\x04 \x01(\x0b\x32<.oak9.tython.aws.cloudfront.OriginRequestPolicyHeadersConfig\x12\x0c\n\x04name\x18\x05 \x01(\t\x12_\n\x14query_strings_config\x18\x06 \x01(\x0b\x32\x41.oak9.tython.aws.cloudfront.OriginRequestPolicyQueryStringsConfig\"\xbe\x01\n\x13OriginRequestPolicy\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12n\n\x1corigin_request_policy_config\x18\x02 \x01(\x0b\x32H.oak9.tython.aws.cloudfront.OriginRequestPolicyOriginRequestPolicyConfig\"\x85\x01\n$RealtimeLogConfigKinesisStreamConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x10\n\x08role_arn\x18\x02 \x01(\t\x12\x12\n\nstream_arn\x18\x03 \x01(\t\"\xca\x01\n\x19RealtimeLogConfigEndPoint\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12_\n\x15kinesis_stream_config\x18\x02 \x01(\x0b\x32@.oak9.tython.aws.cloudfront.RealtimeLogConfigKinesisStreamConfig\x12\x13\n\x0bstream_type\x18\x03 \x01(\t\"\xcc\x01\n\x11RealtimeLogConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12I\n\nend_points\x18\x02 \x03(\x0b\x32\x35.oak9.tython.aws.cloudfront.RealtimeLogConfigEndPoint\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x15\n\rsampling_rate\x18\x05 \x01(\x01\"\x88\x01\n\x1cStreamingDistributionLogging\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x0e\n\x06prefix\x18\x04 \x01(\t\"\x8d\x01\n\x1dStreamingDistributionS3Origin\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0b\x64omain_name\x18\x02 \x01(\t\x12\x1e\n\x16origin_access_identity\x18\x03 \x01(\t\"\x8c\x01\n#StreamingDistributionTrustedSigners\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x1b\n\x13\x61ws_account_numbers\x18\x03 \x03(\t\"\xa6\x03\n0StreamingDistributionStreamingDistributionConfig\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12I\n\x07logging\x18\x02 \x01(\x0b\x32\x38.oak9.tython.aws.cloudfront.StreamingDistributionLogging\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x13\n\x0bprice_class\x18\x04 \x01(\t\x12L\n\ts3_origin\x18\x05 \x01(\x0b\x32\x39.oak9.tython.aws.cloudfront.StreamingDistributionS3Origin\x12\x0f\n\x07\x65nabled\x18\x06 \x01(\x08\x12\x0f\n\x07\x61liases\x18\x07 \x03(\t\x12X\n\x0ftrusted_signers\x18\x08 \x01(\x0b\x32?.oak9.tython.aws.cloudfront.StreamingDistributionTrustedSigners\"\xbd\x02\n\x15StreamingDistribution\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12s\n\x1dstreaming_distribution_config\x18\x02 \x01(\x0b\x32L.oak9.tython.aws.cloudfront.StreamingDistributionStreamingDistributionConfig\x12I\n\x04tags\x18\x03 \x03(\x0b\x32;.oak9.tython.aws.cloudfront.StreamingDistribution.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_cloudfront_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DISTRIBUTION_TAGSENTRY._options = None
  _DISTRIBUTION_TAGSENTRY._serialized_options = b'8\001'
  _STREAMINGDISTRIBUTION_TAGSENTRY._options = None
  _STREAMINGDISTRIBUTION_TAGSENTRY._serialized_options = b'8\001'
  _CACHEPOLICYCOOKIESCONFIG._serialized_start=77
  _CACHEPOLICYCOOKIESCONFIG._serialized_end=202
  _CACHEPOLICYHEADERSCONFIG._serialized_start=204
  _CACHEPOLICYHEADERSCONFIG._serialized_end=329
  _CACHEPOLICYQUERYSTRINGSCONFIG._serialized_start=332
  _CACHEPOLICYQUERYSTRINGSCONFIG._serialized_end=474
  _CACHEPOLICYPARAMETERSINCACHEKEYANDFORWARDEDTOORIGIN._serialized_start=477
  _CACHEPOLICYPARAMETERSINCACHEKEYANDFORWARDEDTOORIGIN._serialized_end=869
  _CACHEPOLICYCACHEPOLICYCONFIG._serialized_start=872
  _CACHEPOLICYCACHEPOLICYCONFIG._serialized_end=1184
  _CACHEPOLICY._serialized_start=1187
  _CACHEPOLICY._serialized_end=1344
  _CLOUDFRONT._serialized_start=1347
  _CLOUDFRONT._serialized_end=1725
  _CLOUDFRONTORIGINACCESSIDENTITYCLOUDFRONTORIGINACCESSIDENTITYCONFIG._serialized_start=1728
  _CLOUDFRONTORIGINACCESSIDENTITYCLOUDFRONTORIGINACCESSIDENTITYCONFIG._serialized_end=1870
  _CLOUDFRONTORIGINACCESSIDENTITY._serialized_start=1873
  _CLOUDFRONTORIGINACCESSIDENTITY._serialized_end=2110
  _DISTRIBUTIONLOGGING._serialized_start=2113
  _DISTRIBUTIONLOGGING._serialized_end=2248
  _DISTRIBUTIONORIGINCUSTOMHEADER._serialized_start=2251
  _DISTRIBUTIONORIGINCUSTOMHEADER._serialized_end=2383
  _DISTRIBUTIONS3ORIGINCONFIG._serialized_start=2385
  _DISTRIBUTIONS3ORIGINCONFIG._serialized_end=2502
  _DISTRIBUTIONCUSTOMORIGINCONFIG._serialized_start=2505
  _DISTRIBUTIONCUSTOMORIGINCONFIG._serialized_end=2759
  _DISTRIBUTIONORIGIN._serialized_start=2762
  _DISTRIBUTIONORIGIN._serialized_end=3326
  _DISTRIBUTIONVIEWERCERTIFICATE._serialized_start=3329
  _DISTRIBUTIONVIEWERCERTIFICATE._serialized_end=3577
  _DISTRIBUTIONLAMBDAFUNCTIONASSOCIATION._serialized_start=3580
  _DISTRIBUTIONLAMBDAFUNCTIONASSOCIATION._serialized_end=3747
  _DISTRIBUTIONCOOKIES._serialized_start=3749
  _DISTRIBUTIONCOOKIES._serialized_end=3871
  _DISTRIBUTIONFORWARDEDVALUES._serialized_start=3874
  _DISTRIBUTIONFORWARDEDVALUES._serialized_end=4098
  _DISTRIBUTIONDEFAULTCACHEBEHAVIOR._serialized_start=4101
  _DISTRIBUTIONDEFAULTCACHEBEHAVIOR._serialized_end=4738
  _DISTRIBUTIONCUSTOMERRORRESPONSE._serialized_start=4741
  _DISTRIBUTIONCUSTOMERRORRESPONSE._serialized_end=4933
  _DISTRIBUTIONSTATUSCODES._serialized_start=4935
  _DISTRIBUTIONSTATUSCODES._serialized_end=5050
  _DISTRIBUTIONORIGINGROUPFAILOVERCRITERIA._serialized_start=5053
  _DISTRIBUTIONORIGINGROUPFAILOVERCRITERIA._serialized_end=5226
  _DISTRIBUTIONORIGINGROUPMEMBER._serialized_start=5228
  _DISTRIBUTIONORIGINGROUPMEMBER._serialized_end=5335
  _DISTRIBUTIONORIGINGROUPMEMBERS._serialized_start=5338
  _DISTRIBUTIONORIGINGROUPMEMBERS._serialized_end=5519
  _DISTRIBUTIONORIGINGROUP._serialized_start=5522
  _DISTRIBUTIONORIGINGROUP._serialized_end=5789
  _DISTRIBUTIONORIGINGROUPS._serialized_start=5792
  _DISTRIBUTIONORIGINGROUPS._serialized_end=5961
  _DISTRIBUTIONGEORESTRICTION._serialized_start=5964
  _DISTRIBUTIONGEORESTRICTION._serialized_end=6094
  _DISTRIBUTIONRESTRICTIONS._serialized_start=6097
  _DISTRIBUTIONRESTRICTIONS._serialized_end=6261
  _DISTRIBUTIONCACHEBEHAVIOR._serialized_start=6264
  _DISTRIBUTIONCACHEBEHAVIOR._serialized_end=6916
  _DISTRIBUTIONDISTRIBUTIONCONFIG._serialized_start=6919
  _DISTRIBUTIONDISTRIBUTIONCONFIG._serialized_end=7814
  _DISTRIBUTION._serialized_start=7817
  _DISTRIBUTION._serialized_end=8088
  _DISTRIBUTION_TAGSENTRY._serialized_start=8045
  _DISTRIBUTION_TAGSENTRY._serialized_end=8088
  _ORIGINREQUESTPOLICYCOOKIESCONFIG._serialized_start=8091
  _ORIGINREQUESTPOLICYCOOKIESCONFIG._serialized_end=8224
  _ORIGINREQUESTPOLICYHEADERSCONFIG._serialized_start=8227
  _ORIGINREQUESTPOLICYHEADERSCONFIG._serialized_end=8360
  _ORIGINREQUESTPOLICYQUERYSTRINGSCONFIG._serialized_start=8363
  _ORIGINREQUESTPOLICYQUERYSTRINGSCONFIG._serialized_end=8513
  _ORIGINREQUESTPOLICYORIGINREQUESTPOLICYCONFIG._serialized_start=8516
  _ORIGINREQUESTPOLICYORIGINREQUESTPOLICYCONFIG._serialized_end=8919
  _ORIGINREQUESTPOLICY._serialized_start=8922
  _ORIGINREQUESTPOLICY._serialized_end=9112
  _REALTIMELOGCONFIGKINESISSTREAMCONFIG._serialized_start=9115
  _REALTIMELOGCONFIGKINESISSTREAMCONFIG._serialized_end=9248
  _REALTIMELOGCONFIGENDPOINT._serialized_start=9251
  _REALTIMELOGCONFIGENDPOINT._serialized_end=9453
  _REALTIMELOGCONFIG._serialized_start=9456
  _REALTIMELOGCONFIG._serialized_end=9660
  _STREAMINGDISTRIBUTIONLOGGING._serialized_start=9663
  _STREAMINGDISTRIBUTIONLOGGING._serialized_end=9799
  _STREAMINGDISTRIBUTIONS3ORIGIN._serialized_start=9802
  _STREAMINGDISTRIBUTIONS3ORIGIN._serialized_end=9943
  _STREAMINGDISTRIBUTIONTRUSTEDSIGNERS._serialized_start=9946
  _STREAMINGDISTRIBUTIONTRUSTEDSIGNERS._serialized_end=10086
  _STREAMINGDISTRIBUTIONSTREAMINGDISTRIBUTIONCONFIG._serialized_start=10089
  _STREAMINGDISTRIBUTIONSTREAMINGDISTRIBUTIONCONFIG._serialized_end=10511
  _STREAMINGDISTRIBUTION._serialized_start=10514
  _STREAMINGDISTRIBUTION._serialized_end=10831
  _STREAMINGDISTRIBUTION_TAGSENTRY._serialized_start=8045
  _STREAMINGDISTRIBUTION_TAGSENTRY._serialized_end=8088
# @@protoc_insertion_point(module_scope)