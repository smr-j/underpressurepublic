import boto3
import os

# S3 bucket configuration 
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID','default')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY','secret')
aws_region = os.environ.get('AWS_DEFAULT_REGION','us-east-1')
s3 = boto3.client('s3', 
                  endpoint_url='http://localstack:4566',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)

S3_BUCKET = os.environ.get('S3_BUCKET', 'measurements-bucket')

s3.create_bucket(Bucket=S3_BUCKET)
