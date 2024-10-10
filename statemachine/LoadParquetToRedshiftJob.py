import sys
import boto3
import json
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode
from awsglue.dynamicframe import DynamicFrame


def get_redshift_credentials(secret_name, region_name):
    client = boto3.client('secretsmanager', region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)

secret_name = "redshift!redshift-admin"
region_name = "us-east-1"

credentials = get_redshift_credentials(secret_name, region_name)




# Initialize Glue and Spark context
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])
spark = SparkSession.builder.appName("LoadParquetToRedshiftJob").getOrCreate()
glueContext = GlueContext(spark.sparkContext)




# Initialize the Glue job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# Convert DynamicFrame to DataFrame for Spark SQL transformations


df_parquet = spark.read.parquet(args['S3_INPUT_PATH'])

# Step 4: Define Redshift connection options
redshift_options = {
    "url": "jdbc:redshift://redshift.582140066777.us-east-1.redshift-serverless.amazonaws.com:5439/dev",
    "dbtable": "public.purchasehistory",
    "user": credentials['username'],
    "password": credentials['password'],
    "driver": "com.amazon.redshift.jdbc42.Driver"
}

df_parquet.write \
    .format("jdbc") \
    .options(**redshift_options) \
    .mode("append") \
    .save()



# Commit the Glue job
job.commit()




