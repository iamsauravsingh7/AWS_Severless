import json

import boto3
import json
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = s3.Bucket('aws-glue-bucket-test-demo')
    dest_bucket = s3.Bucket('prod-glue-test-bucket')
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.filter(Prefix='target-data-store/parquet-reports/', Delimiter='/'):
        dest_key = obj.key
        print(dest_key)
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})
    #    print('print file from the source bucket' + dest_key)
    #    s3.Object(bucket.name, obj.key).delete()