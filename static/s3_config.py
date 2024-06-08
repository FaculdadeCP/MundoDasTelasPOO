import boto3 
from botocore.exceptions import NoCredentialsError

AWS_ACCESS_KEY = 'AKIA3FLD35XDAWX4XEUR'
AWS_SECRET_KEY = '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'
AWS_BUCKET_NAME = 'mundodastelas'
AWS_REGION = 'us-east-2'

def upload_to_s3(file_path, file_name):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

    try:
        s3.upload_file(file_path, AWS_BUCKET_NAME, file_name)
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
        return file_url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None