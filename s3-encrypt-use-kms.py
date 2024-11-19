import boto3
import botocore.exceptions

# Initialize the S3 client
s3 = boto3.client('s3')

def get_s3_objects(bucket_name):
    """
    List all objects in an S3 bucket.
    """
    try:
        paginator = s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get('Contents', []):
                yield obj['Key']
    except botocore.exceptions.ClientError as e:
        print(f"Error listing objects in bucket {bucket_name}: {e}")
        return

def check_and_encrypt(bucket_name, key, kms_key_id=None):
    """
    Check if an S3 object is encrypted. If not, copy it with encryption.
    """
    try:
        # Get object metadata
        response = s3.head_object(Bucket=bucket_name, Key=key)
        encryption = response.get('ServerSideEncryption')

        if encryption:
            print(f"Object '{key}' is already encrypted with {encryption}. Skipping.")
            return

        print(f"Encrypting object '{key}'...")

        # Copy the object to itself with encryption
        copy_source = {'Bucket': bucket_name, 'Key': key}
        s3.copy_object(
            Bucket=bucket_name,
            Key=key,
            CopySource=copy_source,
            ServerSideEncryption='aws:kms',
            SSEKMSKeyId=kms_key_id  # Optional, specify if using a custom KMS key
        )
        print(f"Object '{key}' encrypted successfully.")

    except botocore.exceptions.ClientError as e:
        print(f"Error processing object '{key}': {e}")

def encrypt_unencrypted_objects(bucket_name, kms_key_id=None):
    """
    Encrypt all unencrypted objects in an S3 bucket.
    """
    print(f"Scanning bucket '{bucket_name}' for unencrypted objects...")
    for key in get_s3_objects(bucket_name):
        check_and_encrypt(bucket_name, key, kms_key_id)

if __name__ == "__main__":
    # Replace with your bucket name and optional KMS key ID
    bucket_name = "your-bucket-name"
    kms_key_id = "your-kms-key-id"  # Optional, leave as None to use default AWS-managed key
    encrypt_unencrypted_objects(bucket_name, kms_key_id)
