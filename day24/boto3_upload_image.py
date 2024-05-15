import boto3
import os


from dotenv import load_dotenv

load_dotenv()
#create an s3 client

# Retrieve AWS credentials from environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


bucket_name = 'test-bharathi-bk'
file_path = '/home/bharathibk/github/python_project/day24/boto3_upload_image.py'

file_name = os.path.basename(file_path)

with open(file_path,'rb') as file:
    s3.upload_fileobj(file,bucket_name,file_name)

print("file uploaded successfully")


