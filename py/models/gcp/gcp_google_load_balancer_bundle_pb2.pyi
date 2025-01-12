"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import gcp.gcp_compute_backend_pb2
import gcp.gcp_compute_forwarding_pb2
import gcp.gcp_compute_global_pb2
import gcp.gcp_compute_health_pb2
import gcp.gcp_compute_http_pb2
import gcp.gcp_compute_https_pb2
import gcp.gcp_compute_region_pb2
import gcp.gcp_compute_ssl_pb2
import gcp.gcp_compute_target_pb2
import gcp.gcp_compute_url_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GoogleLoadBalancer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_BACKEND_BUCKET_FIELD_NUMBER: builtins.int
    COMPUTE_BACKEND_BUCKET_SIGNED_URL_KEY_FIELD_NUMBER: builtins.int
    COMPUTE_BACKEND_SERVICE_FIELD_NUMBER: builtins.int
    COMPUTE_BACKEND_SERVICE_SIGNED_URL_KEY_FIELD_NUMBER: builtins.int
    COMPUTE_FORWARDING_RULE_FIELD_NUMBER: builtins.int
    COMPUTE_GLOBAL_FORWARDING_RULE_FIELD_NUMBER: builtins.int
    COMPUTE_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    COMPUTE_HTTP_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    COMPUTE_HTTPS_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_BACKEND_SERVICE_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_SSL_CERTIFICATE_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_TARGET_HTTP_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_TARGET_HTTPS_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_REGION_URL_MAP_FIELD_NUMBER: builtins.int
    COMPUTE_SSL_CERTIFICATE_FIELD_NUMBER: builtins.int
    COMPUTE_SSL_POLICY_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_GRPC_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_HTTP_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_HTTPS_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_POOL_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_SSL_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_TARGET_TCP_PROXY_FIELD_NUMBER: builtins.int
    COMPUTE_URL_MAP_FIELD_NUMBER: builtins.int
    @property
    def compute_backend_bucket(self) -> gcp.gcp_compute_backend_pb2.ComputeBackendBucket: ...
    @property
    def compute_backend_bucket_signed_url_key(self) -> gcp.gcp_compute_backend_pb2.ComputeBackendBucketSignedUrlKey: ...
    @property
    def compute_backend_service(self) -> gcp.gcp_compute_backend_pb2.ComputeBackendService: ...
    @property
    def compute_backend_service_signed_url_key(self) -> gcp.gcp_compute_backend_pb2.ComputeBackendServiceSignedUrlKey: ...
    @property
    def compute_forwarding_rule(self) -> gcp.gcp_compute_forwarding_pb2.ComputeForwardingRule: ...
    @property
    def compute_global_forwarding_rule(self) -> gcp.gcp_compute_global_pb2.ComputeGlobalForwardingRule: ...
    @property
    def compute_health_check(self) -> gcp.gcp_compute_health_pb2.ComputeHealthCheck: ...
    @property
    def compute_http_health_check(self) -> gcp.gcp_compute_http_pb2.ComputeHttpHealthCheck: ...
    @property
    def compute_https_health_check(self) -> gcp.gcp_compute_https_pb2.ComputeHttpsHealthCheck: ...
    @property
    def compute_region_backend_service(self) -> gcp.gcp_compute_region_pb2.ComputeRegionBackendService: ...
    @property
    def compute_region_health_check(self) -> gcp.gcp_compute_region_pb2.ComputeRegionHealthCheck: ...
    @property
    def compute_region_ssl_certificate(self) -> gcp.gcp_compute_region_pb2.ComputeRegionSslCertificate: ...
    @property
    def compute_region_target_http_proxy(self) -> gcp.gcp_compute_region_pb2.ComputeRegionTargetHttpProxy: ...
    @property
    def compute_region_target_https_proxy(self) -> gcp.gcp_compute_region_pb2.ComputeRegionTargetHttpsProxy: ...
    @property
    def compute_region_url_map(self) -> gcp.gcp_compute_region_pb2.ComputeRegionUrlMap: ...
    @property
    def compute_ssl_certificate(self) -> gcp.gcp_compute_ssl_pb2.ComputeSslCertificate: ...
    @property
    def compute_ssl_policy(self) -> gcp.gcp_compute_ssl_pb2.ComputeSslPolicy: ...
    @property
    def compute_target_grpc_proxy(self) -> gcp.gcp_compute_target_pb2.ComputeTargetGrpcProxy: ...
    @property
    def compute_target_http_proxy(self) -> gcp.gcp_compute_target_pb2.ComputeTargetHttpProxy: ...
    @property
    def compute_target_https_proxy(self) -> gcp.gcp_compute_target_pb2.ComputeTargetHttpsProxy: ...
    @property
    def compute_target_pool(self) -> gcp.gcp_compute_target_pb2.ComputeTargetPool: ...
    @property
    def compute_target_ssl_proxy(self) -> gcp.gcp_compute_target_pb2.ComputeTargetSslProxy: ...
    @property
    def compute_target_tcp_proxy(self) -> gcp.gcp_compute_target_pb2.ComputeTargetTcpProxy: ...
    @property
    def compute_url_map(self) -> gcp.gcp_compute_url_pb2.ComputeUrlMap: ...
    def __init__(
        self,
        *,
        compute_backend_bucket: gcp.gcp_compute_backend_pb2.ComputeBackendBucket | None = ...,
        compute_backend_bucket_signed_url_key: gcp.gcp_compute_backend_pb2.ComputeBackendBucketSignedUrlKey | None = ...,
        compute_backend_service: gcp.gcp_compute_backend_pb2.ComputeBackendService | None = ...,
        compute_backend_service_signed_url_key: gcp.gcp_compute_backend_pb2.ComputeBackendServiceSignedUrlKey | None = ...,
        compute_forwarding_rule: gcp.gcp_compute_forwarding_pb2.ComputeForwardingRule | None = ...,
        compute_global_forwarding_rule: gcp.gcp_compute_global_pb2.ComputeGlobalForwardingRule | None = ...,
        compute_health_check: gcp.gcp_compute_health_pb2.ComputeHealthCheck | None = ...,
        compute_http_health_check: gcp.gcp_compute_http_pb2.ComputeHttpHealthCheck | None = ...,
        compute_https_health_check: gcp.gcp_compute_https_pb2.ComputeHttpsHealthCheck | None = ...,
        compute_region_backend_service: gcp.gcp_compute_region_pb2.ComputeRegionBackendService | None = ...,
        compute_region_health_check: gcp.gcp_compute_region_pb2.ComputeRegionHealthCheck | None = ...,
        compute_region_ssl_certificate: gcp.gcp_compute_region_pb2.ComputeRegionSslCertificate | None = ...,
        compute_region_target_http_proxy: gcp.gcp_compute_region_pb2.ComputeRegionTargetHttpProxy | None = ...,
        compute_region_target_https_proxy: gcp.gcp_compute_region_pb2.ComputeRegionTargetHttpsProxy | None = ...,
        compute_region_url_map: gcp.gcp_compute_region_pb2.ComputeRegionUrlMap | None = ...,
        compute_ssl_certificate: gcp.gcp_compute_ssl_pb2.ComputeSslCertificate | None = ...,
        compute_ssl_policy: gcp.gcp_compute_ssl_pb2.ComputeSslPolicy | None = ...,
        compute_target_grpc_proxy: gcp.gcp_compute_target_pb2.ComputeTargetGrpcProxy | None = ...,
        compute_target_http_proxy: gcp.gcp_compute_target_pb2.ComputeTargetHttpProxy | None = ...,
        compute_target_https_proxy: gcp.gcp_compute_target_pb2.ComputeTargetHttpsProxy | None = ...,
        compute_target_pool: gcp.gcp_compute_target_pb2.ComputeTargetPool | None = ...,
        compute_target_ssl_proxy: gcp.gcp_compute_target_pb2.ComputeTargetSslProxy | None = ...,
        compute_target_tcp_proxy: gcp.gcp_compute_target_pb2.ComputeTargetTcpProxy | None = ...,
        compute_url_map: gcp.gcp_compute_url_pb2.ComputeUrlMap | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compute_backend_bucket", b"compute_backend_bucket", "compute_backend_bucket_signed_url_key", b"compute_backend_bucket_signed_url_key", "compute_backend_service", b"compute_backend_service", "compute_backend_service_signed_url_key", b"compute_backend_service_signed_url_key", "compute_forwarding_rule", b"compute_forwarding_rule", "compute_global_forwarding_rule", b"compute_global_forwarding_rule", "compute_health_check", b"compute_health_check", "compute_http_health_check", b"compute_http_health_check", "compute_https_health_check", b"compute_https_health_check", "compute_region_backend_service", b"compute_region_backend_service", "compute_region_health_check", b"compute_region_health_check", "compute_region_ssl_certificate", b"compute_region_ssl_certificate", "compute_region_target_http_proxy", b"compute_region_target_http_proxy", "compute_region_target_https_proxy", b"compute_region_target_https_proxy", "compute_region_url_map", b"compute_region_url_map", "compute_ssl_certificate", b"compute_ssl_certificate", "compute_ssl_policy", b"compute_ssl_policy", "compute_target_grpc_proxy", b"compute_target_grpc_proxy", "compute_target_http_proxy", b"compute_target_http_proxy", "compute_target_https_proxy", b"compute_target_https_proxy", "compute_target_pool", b"compute_target_pool", "compute_target_ssl_proxy", b"compute_target_ssl_proxy", "compute_target_tcp_proxy", b"compute_target_tcp_proxy", "compute_url_map", b"compute_url_map"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_backend_bucket", b"compute_backend_bucket", "compute_backend_bucket_signed_url_key", b"compute_backend_bucket_signed_url_key", "compute_backend_service", b"compute_backend_service", "compute_backend_service_signed_url_key", b"compute_backend_service_signed_url_key", "compute_forwarding_rule", b"compute_forwarding_rule", "compute_global_forwarding_rule", b"compute_global_forwarding_rule", "compute_health_check", b"compute_health_check", "compute_http_health_check", b"compute_http_health_check", "compute_https_health_check", b"compute_https_health_check", "compute_region_backend_service", b"compute_region_backend_service", "compute_region_health_check", b"compute_region_health_check", "compute_region_ssl_certificate", b"compute_region_ssl_certificate", "compute_region_target_http_proxy", b"compute_region_target_http_proxy", "compute_region_target_https_proxy", b"compute_region_target_https_proxy", "compute_region_url_map", b"compute_region_url_map", "compute_ssl_certificate", b"compute_ssl_certificate", "compute_ssl_policy", b"compute_ssl_policy", "compute_target_grpc_proxy", b"compute_target_grpc_proxy", "compute_target_http_proxy", b"compute_target_http_proxy", "compute_target_https_proxy", b"compute_target_https_proxy", "compute_target_pool", b"compute_target_pool", "compute_target_ssl_proxy", b"compute_target_ssl_proxy", "compute_target_tcp_proxy", b"compute_target_tcp_proxy", "compute_url_map", b"compute_url_map"]) -> None: ...

global___GoogleLoadBalancer = GoogleLoadBalancer
