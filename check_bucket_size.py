import boto3
import datetime
import sys

account_id = boto3.client('sts').get_caller_identity().get('Account')
orig_stdout = sys.stdout
f = open('Bucket_size_larger_than_1TB_%s.txt' % account_id, 'w')
sys.stdout = f


ec2 = boto3.client('ec2')
regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

# We only check Sydney region here. 
regions=["ap-southeast-2"]
measurable_metrics = [
    ('BucketSizeBytes', 'StandardStorage'),
    ('NumberOfObjects', 'AllStorageTypes'),
]

for region in regions:
    print(region)
    s3 = boto3.resource('s3',region)

    def cw(region, cws = {}):
        '''Caching Cloudwatch accessor by region.'''

        if region not in cws:
            cws[region] = boto3.client('cloudwatch', region_name = region)

        return cws[region]

    def bucket_stats(name, date):
        '''Get the number object count and size of a bucket on a given date.'''

        results = {}

        for metric_name, storage_type in measurable_metrics:
            #for region in regions:
                metrics = cw(region).get_metric_statistics(
                    Namespace = 'AWS/S3',
                    MetricName = metric_name,
                    StartTime = date - datetime.timedelta(days = 365),
                    EndTime = date,
                    Period = 86400,
                    Statistics = ['Average'],
                    Dimensions = [
                        {'Name': 'BucketName', 'Value': name},
                        {'Name': 'StorageType', 'Value': storage_type},
                    ],
                )

                if metrics['Datapoints']:
                    results[metric_name] = sorted(metrics['Datapoints'], key = lambda row: row['Timestamp'])[-1]['Average']
                    results['region'] = region
                    continue

        return results

    date = datetime.datetime.utcnow().replace(hour = 0, minute = 0, second = 0, microsecond = 0)

    print('name', 'region', 'TB size', 'objects', sep = '\t')
    res = []

    for bucket in sorted(s3.buckets.all(), key = lambda bucket: bucket.name):
        results = bucket_stats(bucket.name, date)
        if int(results.get('BucketSizeBytes', 0)) >= 1099511627776:
            res.append((bucket.name, results.get('region'), int(results.get('BucketSizeBytes', 0))/(1024*1024*1024*1024), int(results.get('NumberOfObjects', 0))))
            #print(bucket.name, results.get('region'), int(results.get('BucketSizeBytes', 0))/(1024*1024*1024*1024), int(results.get('NumberOfObjects', 0)), sep = '\t')

    res.sort(key=lambda x: x[2], reverse=True)
    for item in res:
        print(item)


sys.stdout = orig_stdout
f.close()
