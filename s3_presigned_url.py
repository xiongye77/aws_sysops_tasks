import argparse
import logging
import boto3
from botocore.exceptions import ClientError
import requests

logger = logging.getLogger(__name__)


def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
    """
    Generate a presigned Amazon S3 URL that can be used to perform an action.

    :param s3_client: A Boto3 Amazon S3 client.
    :param client_method: The name of the client method that the URL performs.
    :param method_parameters: The parameters of the specified client method.
    :param expires_in: The number of seconds the presigned URL is valid for.
    :return: The presigned URL.
    """
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
        logger.info("Got presigned URL: %s", url)
    except ClientError:
        logger.exception(
            "Couldn't get a presigned URL for client method '%s'.", client_method)
        raise
    return url

s3_client = boto3.client('s3')
url = generate_presigned_url(
        s3_client, 'put_object', {'Bucket': 'bucket_name', 'Key': 'payingorg.csv'}, 1000)
print(url)
print("Putting data to the URL.")

try:
    with open('payingorg.csv', 'r') as object_file:
        object_text = object_file.read()
        print(object_text)
        response = requests.put(url, data=object_text)
        print(response)
except:
    logger.info("error")
