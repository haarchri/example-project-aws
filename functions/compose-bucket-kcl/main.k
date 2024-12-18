import models.io.upbound.aws.s3.v1beta1 as s3v1beta1
import models.com.example.platform.v1alpha1.xstoragebucket as xstoragebucketv1alpha1
import regex

oxr = xstoragebucketv1alpha1.XStorageBucket{**option("params").oxr}

bucketName = "{}-bucket".format(oxr.metadata.name)

_metadata = lambda name: str -> any {
  {
    name = name
    annotations = {
      "krm.kcl.dev/composition-resource-name" = name
    }
  }
}

ready = lambda o: any, statusPath = "atProvider" -> bool {
    status = o?.Resource?.status
    objstatus = status?.conditions or []
    len(objstatus) > 0 and all_true([c.status == "True" for c in objstatus]) and status and statusPath in status
}

get = lambda x: any, y: str, d: any -> any {
    """
    Get an item from a dictionary using a dot separated path.
    If the item is not found, return a default value.
    """
    p = regex.split(y, "\.")
    c = p[0]
    y = ".".join(p[1::])
    x[c] if len(p) == 1 and c in x else d if c not in x else get(x[c], y, d)
}

_items: [any] = [
    # Bucket in the desired region
    s3v1beta1.Bucket{
        metadata: _metadata(bucketName)
        spec = {
            forProvider = {
                region = oxr.spec.parameters.region
            }
        }
    },
    s3v1beta1.BucketOwnershipControls{
        metadata: _metadata("{}-boc".format(oxr.metadata.name))
        spec = {
            forProvider = {
                bucketRef = {
                    name = bucketName
                }
                region = oxr.spec.parameters.region
                rule:[{
                    objectOwnership:"BucketOwnerPreferred"
                }]
            }
        }
    },
    s3v1beta1.BucketPublicAccessBlock{
        metadata: _metadata("{}-pab".format(oxr.metadata.name))
        spec = {
            forProvider = {
                bucketRef = {
                    name = bucketName
                }
                region = oxr.spec.parameters.region
                blockPublicAcls: False
                ignorePublicAcls: False
                restrictPublicBuckets: False
                blockPublicPolicy: False
            }
        }
    }
]

bucket = get(option("params").ocds, bucketName, {})
if ready(bucket):
    _items += [
        # ACL for the bucket
        s3v1beta1.BucketACL{
            metadata: _metadata("{}-acl".format(oxr.metadata.name))
            spec = {
                forProvider = {
                    bucketRef = {
                        name = bucketName
                    }
                    region = oxr.spec.parameters.region
                    acl = oxr.spec.parameters.acl
                }
            }
        }
    ]

_items += [
    # Default encryption for the bucket
    s3v1beta1.BucketServerSideEncryptionConfiguration{
        metadata: _metadata("{}-encryption".format(oxr.metadata.name))
        spec = {
            forProvider = {
                region = oxr.spec.parameters.region
                bucketRef = {
                    name = bucketName
                }
                rule = [
                    {
                        applyServerSideEncryptionByDefault = [
                            {
                                sseAlgorithm = "AES256"
                            }
                        ]
                        bucketKeyEnabled = True
                    }
                ]
            }
        }
    }
]

# Set up versioning for the bucket if desired
if oxr.spec.parameters.versioning:
    _items += [
        s3v1beta1.BucketVersioning{
            metadata: _metadata("{}-versioning".format(oxr.metadata.name))
            spec = {
                forProvider = {
                    region = oxr.spec.parameters.region
                    bucketRef = {
                        name = bucketName
                    }
                    versioningConfiguration = [
                        {
                            status = "Enabled"
                        }
                    ]
                }
            }
        }
    ]

items = _items
