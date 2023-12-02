import json
import boto3
glue=boto3.client('glue');

def lambda_handler(event, context):
    print(event)
    response = glue.start_crawler(
    Name='test' # Name of the crawler
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }