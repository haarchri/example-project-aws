import models.io.upbound.dev.meta.v1alpha1.compositiontest as t
import models.com.example.platform.v1alpha1.xstoragebucket as xstoragebucketv1alpha1
import models.io.upbound.aws.s3.v1beta1 as s3v1beta1
import file
import datetime

_testmetadata = lambda name: str -> any {
  {
    name = name
    annotations = {
      "crossplane.io/composition-resource-name" = name
    }
  }
}

_xr = xstoragebucketv1alpha1.XStorageBucket{
    metadata.name: "test"
    spec: {
        parameters: {
            acl: "private"
            region: "eu-central-1"
            versioning: False
        }
    }
}

_input = t.CompositionTest{
    spec = {
        xrd = (file.read("apis/xstoragebuckets/definition.yaml"))
        composition = (file.read("apis/xstoragebuckets/composition.yaml"))
        xr = _xr
    }
}

_test1 = t.CompositionTest{
    **_input
    spec.assert: [
        s3v1beta1.Bucket{
            metadata: _testmetadata("{}-boc".format(_xr.metadata.name))
            spec: {
                forProvider: {
                    region: _xr.spec.parameters.region
                }
            }
        }
    ]
}

_test2= t.CompositionTest{
    **_input
    spec.observedResources = [
        s3v1beta1.Bucket{
            **_test1.spec.assert[0]
            status: {
                atProvider: {
                    arn: "{}-boc".format(_xr.metadata.name)
                }
                conditions: [
                    {
                        reason: "Available"
                        status: "True"
                        type: "Ready"
                        lastTransitionTime: datetime.now("%Y-%m-%dT%H:%M:%SZ")
                    }
                    {
                        reason: "Success"
                        status: "True"
                        type: "FunctionSuccess"
                        lastTransitionTime: datetime.now("%Y-%m-%dT%H:%M:%SZ")
                    }
                    {
                        reason: "ReconcileSuccess"
                        status: "True"
                        type: "Synced"
                        lastTransitionTime: datetime.now("%Y-%m-%dT%H:%M:%SZ")
                    }
                ]
            }
        }
    ]
    spec.assert = _test1.spec.assert + [
        s3v1beta1.BucketACL{
            spec: {
                forProvider: {
                    region: _xr.spec.parameters.region
                }
            }
        }
    ]
}

items = [_test1, _test2]