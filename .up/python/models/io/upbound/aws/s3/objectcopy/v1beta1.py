# generated by datamodel-codegen:
#   filename:  workdir/s3_aws_upbound_io_v1beta1_objectcopy.yaml

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import AwareDatetime, BaseModel, Field

from .....k8s.apimachinery.pkg.apis.meta import v1


class DeletionPolicy(Enum):
    Orphan = 'Orphan'
    Delete = 'Delete'


class CustomerKeySecretRef(BaseModel):
    key: str
    """
    The key to select.
    """
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class GrantItem(BaseModel):
    email: Optional[str] = None
    """
    Email address of the grantee. Used only when type is AmazonCustomerByEmail.
    """
    id: Optional[str] = None
    """
    Canonical user ID of the grantee. Used only when type is CanonicalUser.
    """
    permissions: Optional[List[str]] = None
    """
    List of permissions to grant to grantee. Valid values are READ, READ_ACP, WRITE_ACP, FULL_CONTROL.
    """
    type: Optional[str] = None
    """
    - Type of grantee. Valid values are CanonicalUser, Group, and AmazonCustomerByEmail.
    """
    uri: Optional[str] = None
    """
    URI of the grantee group. Used only when type is Group.
    """


class KmsEncryptionContextSecretRef(BaseModel):
    key: str
    """
    The key to select.
    """
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class KmsKeyIdSecretRef(BaseModel):
    key: str
    """
    The key to select.
    """
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class SourceCustomerKeySecretRef(BaseModel):
    key: str
    """
    The key to select.
    """
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class ForProvider(BaseModel):
    acl: Optional[str] = None
    """
    Canned ACL to apply. Valid values are private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, and bucket-owner-full-control. Conflicts with grant.
    """
    bucket: Optional[str] = None
    """
    Name of the bucket to put the file in.
    """
    bucketKeyEnabled: Optional[bool] = None
    cacheControl: Optional[str] = None
    """
    Specifies caching behavior along the request/reply chain Read w3c cache_control for further details.
    """
    checksumAlgorithm: Optional[str] = None
    """
    Indicates the algorithm used to create the checksum for the object. If a value is specified and the object is encrypted with KMS, you must have permission to use the kms:Decrypt action. Valid values: CRC32, CRC32C, SHA1, SHA256.
    """
    contentDisposition: Optional[str] = None
    """
    Specifies presentational information for the object. Read w3c content_disposition for further information.
    """
    contentEncoding: Optional[str] = None
    """
    Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read w3c content encoding for further information.
    """
    contentLanguage: Optional[str] = None
    """
    Language the content is in e.g., en-US or en-GB.
    """
    contentType: Optional[str] = None
    """
    Standard MIME type describing the format of the object data, e.g., application/octet-stream. All Valid MIME Types are valid for this input.
    """
    copyIfMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) matches the specified tag.
    """
    copyIfModifiedSince: Optional[str] = None
    """
    Copies the object if it has been modified since the specified time, in RFC3339 format.
    """
    copyIfNoneMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) is different than the specified ETag.
    """
    copyIfUnmodifiedSince: Optional[str] = None
    """
    Copies the object if it hasn't been modified since the specified time, in RFC3339 format.
    """
    customerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use to when encrypting the object (for example, AES256).
    """
    customerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    customerKeySecretRef: Optional[CustomerKeySecretRef] = None
    """
    Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side-encryption-customer-algorithm header.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account id of the expected destination bucket owner. If the destination bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expectedSourceBucketOwner: Optional[str] = None
    """
    Account id of the expected source bucket owner. If the source bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expires: Optional[str] = None
    """
    Date and time at which the object is no longer cacheable, in RFC3339 format.
    """
    forceDestroy: Optional[bool] = None
    """
    Allow the object to be deleted by removing any legal hold on any object version. Default is false. This value should be set to true only if the bucket has S3 object lock enabled.
    """
    grant: Optional[List[GrantItem]] = None
    """
    Configuration block for header grants. Documented below. Conflicts with acl.
    """
    key: Optional[str] = None
    """
    Name of the object once it is in the bucket.
    """
    kmsEncryptionContextSecretRef: Optional[KmsEncryptionContextSecretRef] = None
    """
    Specifies the AWS KMS Encryption Context to use for object encryption. The value is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
    """
    kmsKeyIdSecretRef: Optional[KmsKeyIdSecretRef] = None
    """
    Specifies the AWS KMS Key ARN to use for object encryption. This value is a fully qualified ARN of the KMS Key. If using aws_kms_key, use the exported arn attribute: kms_key_id = aws_kms_key.foo.arn
    """
    metadata: Optional[Dict[str, str]] = None
    """
    Map of keys/values to provision metadata (will be automatically prefixed by x-amz-meta-, note that only lowercase label are currently supported by the AWS Go API).
    """
    metadataDirective: Optional[str] = None
    """
    Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request. Valid values are COPY and REPLACE.
    """
    objectLockLegalHoldStatus: Optional[str] = None
    """
    The legal hold status that you want to apply to the specified object. Valid values are ON and OFF.
    """
    objectLockMode: Optional[str] = None
    """
    Object lock retention mode that you want to apply to this object. Valid values are GOVERNANCE and COMPLIANCE.
    """
    objectLockRetainUntilDate: Optional[str] = None
    """
    Date and time, in RFC3339 format, when this object's object lock will expire.
    """
    region: str
    """
    Region is the region you'd like your resource to be created in.
    """
    requestPayer: Optional[str] = None
    """
    Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets (https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the Amazon S3 Developer Guide. If included, the only valid value is requester.
    """
    serverSideEncryption: Optional[str] = None
    """
    Specifies server-side encryption of the object in S3. Valid values are AES256 and aws:kms.
    """
    source: Optional[str] = None
    """
    Specifies the source object for the copy operation. You specify the value in one of two formats. For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (/). For example, testbucket/test1.json. For objects accessed through access points, specify the ARN of the object as accessed through the access point, in the format arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key>. For example, arn:aws:s3:us-west-2:9999912999:accesspoint/my-access-point/object/testbucket/test1.json.
    """
    sourceCustomerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use when decrypting the source object (for example, AES256).
    """
    sourceCustomerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    sourceCustomerKeySecretRef: Optional[SourceCustomerKeySecretRef] = None
    """
    Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
    """
    storageClass: Optional[str] = None
    """
    Specifies the desired storage class for the object. Defaults to STANDARD.
    """
    taggingDirective: Optional[str] = None
    """
    Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request. Valid values are COPY and REPLACE.
    """
    tags: Optional[Dict[str, str]] = None
    """
    Key-value map of resource tags.
    """
    websiteRedirect: Optional[str] = None
    """
    Specifies a target URL for website redirect.
    """


class InitProvider(BaseModel):
    acl: Optional[str] = None
    """
    Canned ACL to apply. Valid values are private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, and bucket-owner-full-control. Conflicts with grant.
    """
    bucket: Optional[str] = None
    """
    Name of the bucket to put the file in.
    """
    bucketKeyEnabled: Optional[bool] = None
    cacheControl: Optional[str] = None
    """
    Specifies caching behavior along the request/reply chain Read w3c cache_control for further details.
    """
    checksumAlgorithm: Optional[str] = None
    """
    Indicates the algorithm used to create the checksum for the object. If a value is specified and the object is encrypted with KMS, you must have permission to use the kms:Decrypt action. Valid values: CRC32, CRC32C, SHA1, SHA256.
    """
    contentDisposition: Optional[str] = None
    """
    Specifies presentational information for the object. Read w3c content_disposition for further information.
    """
    contentEncoding: Optional[str] = None
    """
    Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read w3c content encoding for further information.
    """
    contentLanguage: Optional[str] = None
    """
    Language the content is in e.g., en-US or en-GB.
    """
    contentType: Optional[str] = None
    """
    Standard MIME type describing the format of the object data, e.g., application/octet-stream. All Valid MIME Types are valid for this input.
    """
    copyIfMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) matches the specified tag.
    """
    copyIfModifiedSince: Optional[str] = None
    """
    Copies the object if it has been modified since the specified time, in RFC3339 format.
    """
    copyIfNoneMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) is different than the specified ETag.
    """
    copyIfUnmodifiedSince: Optional[str] = None
    """
    Copies the object if it hasn't been modified since the specified time, in RFC3339 format.
    """
    customerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use to when encrypting the object (for example, AES256).
    """
    customerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    customerKeySecretRef: Optional[CustomerKeySecretRef] = None
    """
    Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side-encryption-customer-algorithm header.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account id of the expected destination bucket owner. If the destination bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expectedSourceBucketOwner: Optional[str] = None
    """
    Account id of the expected source bucket owner. If the source bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expires: Optional[str] = None
    """
    Date and time at which the object is no longer cacheable, in RFC3339 format.
    """
    forceDestroy: Optional[bool] = None
    """
    Allow the object to be deleted by removing any legal hold on any object version. Default is false. This value should be set to true only if the bucket has S3 object lock enabled.
    """
    grant: Optional[List[GrantItem]] = None
    """
    Configuration block for header grants. Documented below. Conflicts with acl.
    """
    key: Optional[str] = None
    """
    Name of the object once it is in the bucket.
    """
    kmsEncryptionContextSecretRef: Optional[KmsEncryptionContextSecretRef] = None
    """
    Specifies the AWS KMS Encryption Context to use for object encryption. The value is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
    """
    kmsKeyIdSecretRef: Optional[KmsKeyIdSecretRef] = None
    """
    Specifies the AWS KMS Key ARN to use for object encryption. This value is a fully qualified ARN of the KMS Key. If using aws_kms_key, use the exported arn attribute: kms_key_id = aws_kms_key.foo.arn
    """
    metadata: Optional[Dict[str, str]] = None
    """
    Map of keys/values to provision metadata (will be automatically prefixed by x-amz-meta-, note that only lowercase label are currently supported by the AWS Go API).
    """
    metadataDirective: Optional[str] = None
    """
    Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request. Valid values are COPY and REPLACE.
    """
    objectLockLegalHoldStatus: Optional[str] = None
    """
    The legal hold status that you want to apply to the specified object. Valid values are ON and OFF.
    """
    objectLockMode: Optional[str] = None
    """
    Object lock retention mode that you want to apply to this object. Valid values are GOVERNANCE and COMPLIANCE.
    """
    objectLockRetainUntilDate: Optional[str] = None
    """
    Date and time, in RFC3339 format, when this object's object lock will expire.
    """
    requestPayer: Optional[str] = None
    """
    Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets (https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the Amazon S3 Developer Guide. If included, the only valid value is requester.
    """
    serverSideEncryption: Optional[str] = None
    """
    Specifies server-side encryption of the object in S3. Valid values are AES256 and aws:kms.
    """
    source: Optional[str] = None
    """
    Specifies the source object for the copy operation. You specify the value in one of two formats. For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (/). For example, testbucket/test1.json. For objects accessed through access points, specify the ARN of the object as accessed through the access point, in the format arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key>. For example, arn:aws:s3:us-west-2:9999912999:accesspoint/my-access-point/object/testbucket/test1.json.
    """
    sourceCustomerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use when decrypting the source object (for example, AES256).
    """
    sourceCustomerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    sourceCustomerKeySecretRef: Optional[SourceCustomerKeySecretRef] = None
    """
    Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
    """
    storageClass: Optional[str] = None
    """
    Specifies the desired storage class for the object. Defaults to STANDARD.
    """
    taggingDirective: Optional[str] = None
    """
    Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request. Valid values are COPY and REPLACE.
    """
    tags: Optional[Dict[str, str]] = None
    """
    Key-value map of resource tags.
    """
    websiteRedirect: Optional[str] = None
    """
    Specifies a target URL for website redirect.
    """


class ManagementPolicy(Enum):
    Observe = 'Observe'
    Create = 'Create'
    Update = 'Update'
    Delete = 'Delete'
    LateInitialize = 'LateInitialize'
    field_ = '*'


class Resolution(Enum):
    Required = 'Required'
    Optional = 'Optional'


class Resolve(Enum):
    Always = 'Always'
    IfNotPresent = 'IfNotPresent'


class Policy(BaseModel):
    resolution: Optional[Resolution] = 'Required'
    """
    Resolution specifies whether resolution of this reference is required.
    The default is 'Required', which means the reconcile will fail if the
    reference cannot be resolved. 'Optional' means this reference will be
    a no-op if it cannot be resolved.
    """
    resolve: Optional[Resolve] = None
    """
    Resolve specifies when this reference should be resolved. The default
    is 'IfNotPresent', which will attempt to resolve the reference only when
    the corresponding field is not present. Use 'Always' to resolve the
    reference on every reconcile.
    """


class ProviderConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class ConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    """
    Annotations are the annotations to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.annotations".
    - It is up to Secret Store implementation for others store types.
    """
    labels: Optional[Dict[str, str]] = None
    """
    Labels are the labels/tags to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.labels".
    - It is up to Secret Store implementation for others store types.
    """
    type: Optional[str] = None
    """
    Type is the SecretType for the connection secret.
    - Only valid for Kubernetes Secret Stores.
    """


class PublishConnectionDetailsTo(BaseModel):
    configRef: Optional[ConfigRef] = Field(
        default_factory=lambda: ConfigRef.model_validate({'name': 'default'})
    )
    """
    SecretStoreConfigRef specifies which secret store config should be used
    for this ConnectionSecret.
    """
    metadata: Optional[Metadata] = None
    """
    Metadata is the metadata for connection secret.
    """
    name: str
    """
    Name is the name of the connection secret.
    """


class WriteConnectionSecretToRef(BaseModel):
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class Spec(BaseModel):
    deletionPolicy: Optional[DeletionPolicy] = 'Delete'
    """
    DeletionPolicy specifies what will happen to the underlying external
    when this managed resource is deleted - either "Delete" or "Orphan" the
    external resource.
    This field is planned to be deprecated in favor of the ManagementPolicies
    field in a future release. Currently, both could be set independently and
    non-default values would be honored if the feature flag is enabled.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    """
    forProvider: ForProvider
    initProvider: Optional[InitProvider] = None
    """
    THIS IS A BETA FIELD. It will be honored
    unless the Management Policies feature flag is disabled.
    InitProvider holds the same fields as ForProvider, with the exception
    of Identifier and other resource reference fields. The fields that are
    in InitProvider are merged into ForProvider when the resource is created.
    The same fields are also added to the terraform ignore_changes hook, to
    avoid updating them after creation. This is useful for fields that are
    required on creation, but we do not desire to update them after creation,
    for example because of an external controller is managing them, like an
    autoscaler.
    """
    managementPolicies: Optional[List[ManagementPolicy]] = ['*']
    """
    THIS IS A BETA FIELD. It is on by default but can be opted out
    through a Crossplane feature flag.
    ManagementPolicies specify the array of actions Crossplane is allowed to
    take on the managed and external resources.
    This field is planned to replace the DeletionPolicy field in a future
    release. Currently, both could be set independently and non-default
    values would be honored if the feature flag is enabled. If both are
    custom, the DeletionPolicy field will be ignored.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    and this one: https://github.com/crossplane/crossplane/blob/444267e84783136daa93568b364a5f01228cacbe/design/one-pager-ignore-changes.md
    """
    providerConfigRef: Optional[ProviderConfigRef] = Field(
        default_factory=lambda: ProviderConfigRef.model_validate({'name': 'default'})
    )
    """
    ProviderConfigReference specifies how the provider that will be used to
    create, observe, update, and delete this managed resource should be
    configured.
    """
    publishConnectionDetailsTo: Optional[PublishConnectionDetailsTo] = None
    """
    PublishConnectionDetailsTo specifies the connection secret config which
    contains a name, metadata and a reference to secret store config to
    which any connection details for this managed resource should be written.
    Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    """
    writeConnectionSecretToRef: Optional[WriteConnectionSecretToRef] = None
    """
    WriteConnectionSecretToReference specifies the namespace and name of a
    Secret to which any connection details for this managed resource should
    be written. Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    This field is planned to be replaced in a future release in favor of
    PublishConnectionDetailsTo. Currently, both could be set independently
    and connection details would be published to both without affecting
    each other.
    """


class AtProvider(BaseModel):
    acl: Optional[str] = None
    """
    Canned ACL to apply. Valid values are private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, and bucket-owner-full-control. Conflicts with grant.
    """
    arn: Optional[str] = None
    """
    ARN of the object.
    """
    bucket: Optional[str] = None
    """
    Name of the bucket to put the file in.
    """
    bucketKeyEnabled: Optional[bool] = None
    cacheControl: Optional[str] = None
    """
    Specifies caching behavior along the request/reply chain Read w3c cache_control for further details.
    """
    checksumAlgorithm: Optional[str] = None
    """
    Indicates the algorithm used to create the checksum for the object. If a value is specified and the object is encrypted with KMS, you must have permission to use the kms:Decrypt action. Valid values: CRC32, CRC32C, SHA1, SHA256.
    """
    checksumCrc32: Optional[str] = None
    """
    The base64-encoded, 32-bit CRC32 checksum of the object.
    """
    checksumCrc32C: Optional[str] = None
    """
    The base64-encoded, 32-bit CRC32C checksum of the object.
    """
    checksumSha1: Optional[str] = None
    """
    The base64-encoded, 160-bit SHA-1 digest of the object.
    """
    checksumSha256: Optional[str] = None
    """
    The base64-encoded, 256-bit SHA-256 digest of the object.
    """
    contentDisposition: Optional[str] = None
    """
    Specifies presentational information for the object. Read w3c content_disposition for further information.
    """
    contentEncoding: Optional[str] = None
    """
    Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read w3c content encoding for further information.
    """
    contentLanguage: Optional[str] = None
    """
    Language the content is in e.g., en-US or en-GB.
    """
    contentType: Optional[str] = None
    """
    Standard MIME type describing the format of the object data, e.g., application/octet-stream. All Valid MIME Types are valid for this input.
    """
    copyIfMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) matches the specified tag.
    """
    copyIfModifiedSince: Optional[str] = None
    """
    Copies the object if it has been modified since the specified time, in RFC3339 format.
    """
    copyIfNoneMatch: Optional[str] = None
    """
    Copies the object if its entity tag (ETag) is different than the specified ETag.
    """
    copyIfUnmodifiedSince: Optional[str] = None
    """
    Copies the object if it hasn't been modified since the specified time, in RFC3339 format.
    """
    customerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use to when encrypting the object (for example, AES256).
    """
    customerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    etag: Optional[str] = None
    """
    ETag generated for the object (an MD5 sum of the object content). For plaintext objects or objects encrypted with an AWS-managed key, the hash is an MD5 digest of the object data. For objects encrypted with a KMS key or objects created by either the Multipart Upload or Part Copy operation, the hash is not an MD5 digest, regardless of the method of encryption. More information on possible values can be found on Common Response Headers.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account id of the expected destination bucket owner. If the destination bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expectedSourceBucketOwner: Optional[str] = None
    """
    Account id of the expected source bucket owner. If the source bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expiration: Optional[str] = None
    """
    If the object expiration is configured, this attribute will be set.
    """
    expires: Optional[str] = None
    """
    Date and time at which the object is no longer cacheable, in RFC3339 format.
    """
    forceDestroy: Optional[bool] = None
    """
    Allow the object to be deleted by removing any legal hold on any object version. Default is false. This value should be set to true only if the bucket has S3 object lock enabled.
    """
    grant: Optional[List[GrantItem]] = None
    """
    Configuration block for header grants. Documented below. Conflicts with acl.
    """
    id: Optional[str] = None
    """
    Canonical user ID of the grantee. Used only when type is CanonicalUser.
    """
    key: Optional[str] = None
    """
    Name of the object once it is in the bucket.
    """
    lastModified: Optional[str] = None
    """
    Returns the date that the object was last modified, in RFC3339 format.
    """
    metadata: Optional[Dict[str, str]] = None
    """
    Map of keys/values to provision metadata (will be automatically prefixed by x-amz-meta-, note that only lowercase label are currently supported by the AWS Go API).
    """
    metadataDirective: Optional[str] = None
    """
    Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request. Valid values are COPY and REPLACE.
    """
    objectLockLegalHoldStatus: Optional[str] = None
    """
    The legal hold status that you want to apply to the specified object. Valid values are ON and OFF.
    """
    objectLockMode: Optional[str] = None
    """
    Object lock retention mode that you want to apply to this object. Valid values are GOVERNANCE and COMPLIANCE.
    """
    objectLockRetainUntilDate: Optional[str] = None
    """
    Date and time, in RFC3339 format, when this object's object lock will expire.
    """
    requestCharged: Optional[bool] = None
    """
    If present, indicates that the requester was successfully charged for the request.
    """
    requestPayer: Optional[str] = None
    """
    Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets (https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the Amazon S3 Developer Guide. If included, the only valid value is requester.
    """
    serverSideEncryption: Optional[str] = None
    """
    Specifies server-side encryption of the object in S3. Valid values are AES256 and aws:kms.
    """
    source: Optional[str] = None
    """
    Specifies the source object for the copy operation. You specify the value in one of two formats. For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (/). For example, testbucket/test1.json. For objects accessed through access points, specify the ARN of the object as accessed through the access point, in the format arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key>. For example, arn:aws:s3:us-west-2:9999912999:accesspoint/my-access-point/object/testbucket/test1.json.
    """
    sourceCustomerAlgorithm: Optional[str] = None
    """
    Specifies the algorithm to use when decrypting the source object (for example, AES256).
    """
    sourceCustomerKeyMd5: Optional[str] = None
    """
    Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    """
    sourceVersionId: Optional[str] = None
    """
    Version of the copied object in the source bucket.
    """
    storageClass: Optional[str] = None
    """
    Specifies the desired storage class for the object. Defaults to STANDARD.
    """
    taggingDirective: Optional[str] = None
    """
    Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request. Valid values are COPY and REPLACE.
    """
    tags: Optional[Dict[str, str]] = None
    """
    Key-value map of resource tags.
    """
    tagsAll: Optional[Dict[str, str]] = None
    """
    Map of tags assigned to the resource, including those inherited from the provider default_tags configuration block.
    """
    versionId: Optional[str] = None
    """
    Version ID of the newly created copy.
    """
    websiteRedirect: Optional[str] = None
    """
    Specifies a target URL for website redirect.
    """


class Condition(BaseModel):
    lastTransitionTime: AwareDatetime
    """
    LastTransitionTime is the last time this condition transitioned from one
    status to another.
    """
    message: Optional[str] = None
    """
    A Message containing details about this condition's last transition from
    one status to another, if any.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: str
    """
    A Reason for this condition's last transition from one status to another.
    """
    status: str
    """
    Status of this condition; is it currently True, False, or Unknown?
    """
    type: str
    """
    Type of this condition. At most one of each condition type may apply to
    a resource at any point in time.
    """


class Status(BaseModel):
    atProvider: Optional[AtProvider] = None
    conditions: Optional[List[Condition]] = None
    """
    Conditions of the resource.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration is the latest metadata.generation
    which resulted in either a ready state, or stalled due to error
    it can not recover from without human intervention.
    """


class ObjectCopy(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Spec
    """
    ObjectCopySpec defines the desired state of ObjectCopy
    """
    status: Optional[Status] = None
    """
    ObjectCopyStatus defines the observed state of ObjectCopy.
    """


class ObjectCopyList(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[ObjectCopy]
    """
    List of objectcopies. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """