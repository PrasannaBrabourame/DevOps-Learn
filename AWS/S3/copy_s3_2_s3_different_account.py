import boto3
import os

def lambda_handler(event, context):
    # Replace with your source and destination bucket names
    source_bucket_name = '***** source-bucket-name *****'
    destination_bucket_name = '***** destination-bucket-name *****'
    
    # Create an S3 client for both source and destination buckets
    source_s3_client = boto3.client('s3')
    destination_s3_client = boto3.client('s3', region_name='***** destination-bucket-region *****')
    
    try:
        # List objects in the source bucket
        response = source_s3_client.list_objects_v2(Bucket=source_bucket_name)
        
        # Find the latest zip file based on last modified timestamp
        latest_zip_object = None
        for obj in response['Contents']:
            if obj['Key'].lower().endswith('.zip'):
                if latest_zip_object is None or obj['LastModified'] > latest_zip_object['LastModified']:
                    latest_zip_object = obj
        
        if latest_zip_object is None:
            return {
                'statusCode': 404,
                'body': 'No zip file found in the source bucket.'
            }
        
        # Get the latest zip file's data
        source_key = latest_zip_object['Key']
        response = source_s3_client.get_object(Bucket=source_bucket_name, Key=source_key)
        object_data = response['Body'].read()
        
        # Upload the latest zip file to the destination bucket
        destination_key = os.path.basename(source_key)  # Use the zip file name as the destination key
        
        destination_s3_client.put_object(
            Bucket=destination_bucket_name,
            Key=destination_key,
            Body=object_data
        )
        
        return {
            'statusCode': 200,
            'body': 'Successfully uploaded the latest zip file to the destination bucket.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {e}'
        }
