import boto3
from botocore.client import Config
from botocore import UNSIGNED

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:8080",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
    config=Config(signature_version=UNSIGNED)  # <-- use UNSIGNED constant
)

# GET
resp = s3.get_object(Bucket="test-bucket", Key="sample.txt")
print(resp["Body"].read().decode())

# PUT
s3.put_object(Bucket="test-bucket", Key="upload.txt", Body=b"hello from test")
