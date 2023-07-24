import json
import boto3
client=boto3.client('ec2')

def lambda_handler(event, context):
     response = client.run_instances(
     ImageId= 'ami-0d147324c76e8210a', # Please Modify ImageID as per your AWS region. This AMI id is valid for Sydney Region
     InstanceType = 't2.micro',
     MaxCount=1,
     MinCount=1)
     print(response['Instances'][0]['InstanceId'])
   