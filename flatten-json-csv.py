import sys
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode

# Initialize Glue and Spark context
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])
spark = SparkSession.builder.appName("Flatten JSON to CSV").getOrCreate()
glueContext = GlueContext(spark.sparkContext)

# Initialize the Glue job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read the JSON data from the S3 input path

datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",  # Adjust the format if needed (e.g., csv, parquet, etc.)
    connection_options={
        "paths": [args['S3_INPUT_PATH']],
        "recurse": True
    }
)

# Convert DynamicFrame to DataFrame for Spark SQL transformations
df = datasource.toDF()



flattened_df = df.select(
    explode(col('users')).alias('user')
).select(
    col("user.id").alias("id"),
    col("user.name").alias("name"),
    col("user.work").alias("work"),
    col("user.email").alias("email"),
    col("user.dob").alias("dob"),
    col("user.address").alias("address"),
    col("user.city").alias("city"),
    col("user.optedin").alias("optedin")
)


flattened_df.write.mode("append").csv(args['S3_OUTPUT_PATH'], header=True)

# Commit the Glue job
job.commit()

