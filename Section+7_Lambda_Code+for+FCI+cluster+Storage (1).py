import json
import boto3
client = boto3.client('fsx')
def lambda_handler(event, context):
    response = client.update_file_system(
    FileSystemId='fs-068f495d635b09f5a',
    StorageCapacity=36)
    
    print(response)



