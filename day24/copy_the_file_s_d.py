import boto3

import os

from dotenv import load_dotenv

load_dotenv()


aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3 = boto3.client("s3",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)



source_bucket = "test-bharathi-bk"

destination_bucket = "abc-bharathi-bk"


source_key_file = "boto3_upload_image.py"
destination_file_key = "abc.py"

s3.copy_object(Bucket=destination_bucket,CopySource={'Bucket': source_bucket, 'Key': source_key_file},Key=destination_file_key)


print("file copied successfully")

