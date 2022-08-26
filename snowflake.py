import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd

import os
from io import StringIO
import boto3

bucket = 'xxxxxxxxxxxxxxx'

session = boto3.session.Session()
client = session.client(service_name='secretsmanager', region_name='us-east-1')
get_secret_value_response = client.get_secret_value(SecretId='arn:aws:secretsmanager:us-east-1:xxxxxxxxxx:secret:snowflake.user.privatekey.xxxxxxxxx')
print (get_secret_value_response['SecretString'])
secret=get_secret_value_response['SecretString']
with open('private_key.txt', 'w') as f:
         f.write(secret)

with open("private_key.txt", "rb") as key:
    p_key= serialization.load_pem_private_key(
            key.read(),
            password=None,
            backend=default_backend()
    )

pkb = p_key.private_bytes(encoding=serialization.Encoding.DER,
                         format=serialization.PrivateFormat.PKCS8,
                         encryption_algorithm=serialization.NoEncryption())
                         
ctx = snowflake.connector.connect(user='xxxxxxxxxxxx_sa',
                                  private_key=pkb,
                                  warehouse='xxxxxxxxxxxxx',
                                  database='xxxxxxxx',
                                  schema='xxxxxxxxxxxx',
                                  account='xxxxxx.us-east-1')
cs = ctx.cursor()
try:
    cs.execute("select * from xxxxxxxxxxxxxxxxxxxxxxxxx limit 300")
    cs.fetch_pandas_all().to_csv("table.csv")
    cs.fetch_pandas_all().to_csv("s3://xxxxxxxxxxxxxxxx/table2.csv")
    csv_buffer = StringIO()
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, 'table.csv').put(Body=open('table.csv', 'rb'))
finally:
    cs.close()
    ctx.close()
