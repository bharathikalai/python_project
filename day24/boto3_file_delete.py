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
file_key = 'boto3_upload_image.py'

#delete the file

s3.delete_object(Bucket=bucket_name,Key=file_key)

print("file deleted successfully")