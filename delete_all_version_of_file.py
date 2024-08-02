import boto3

def permanently_delete_objects_in_folder(bucket_name, folder_prefix):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_object_versions')
    
    # Paginate through all versions and delete markers in the specified folder
    pages = paginator.paginate(Bucket=bucket_name, Prefix=folder_prefix)
    
    for page in pages:
        # Prepare objects to delete
        versions = [
            {'Key': version['Key'], 'VersionId': version['VersionId']}
            for version in page.get('Versions', [])
        ]
        
        delete_markers = [
            {'Key': delete_marker['Key'], 'VersionId': delete_marker['VersionId']}
            for delete_marker in page.get('DeleteMarkers', [])
        ]
        
        objects_to_delete = versions + delete_markers
        
        # Delete all versions and delete markers in batches
        if objects_to_delete:
            delete_response = s3.delete_objects(
                Bucket=bucket_name,
                Delete={'Objects': objects_to_delete}
            )
            print(f"Deleted objects: {delete_response.get('Deleted', [])}")

# Example usage
bucket_name = 'airflow-s3-1733'
folder_prefix = 'xade3/'

permanently_delete_objects_in_folder(bucket_name, folder_prefix)
