import json
import boto3
client = boto3.client('s3')

def lambda_handler(event, context):
    
    response = client.create_bucket(
    Bucket='s3demo01032022abc',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    },
)