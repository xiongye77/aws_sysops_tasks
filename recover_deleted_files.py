import boto3

def recover_deleted_files_in_folder(bucket_name, folder_prefix):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_object_versions')
    
    # Paginate through all versions and delete markers in the specified folder
    pages = paginator.paginate(Bucket=bucket_name, Prefix=folder_prefix)
    
    for page in pages:
        # Find delete markers
        delete_markers = [
            {'Key': delete_marker['Key'], 'VersionId': delete_marker['VersionId']}
            for delete_marker in page.get('DeleteMarkers', [])
        ]
        
        # Remove delete markers to recover the files
        if delete_markers:
            delete_response = s3.delete_objects(
                Bucket=bucket_name,
                Delete={'Objects': delete_markers}
            )
            print(f"Recovered objects: {delete_response.get('Deleted', [])}")

# Example usage
bucket_name = 'airflow-s3-1733'
folder_prefix = 'xade2/'

recover_deleted_files_in_folder(bucket_name, folder_prefix)
