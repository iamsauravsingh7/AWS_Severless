import json
import boto3
client = boto3.client('s3')

def lambda_handler(event, context):
    
    response = client.get_object(
    Bucket='firstbucket01092022',
    Key='bucket1.json',

)
    # convert from streaming to bytes
    
    data_bytes = response['Body'].read()
    
    #bytes to string
    
    data_strings = data_bytes.decode("UTF-8")
    
# convert from strings to dict

    data_dict = json.loads(data_strings)

    return {
        'statusCode': 200,
        'body': data_dict
    }



