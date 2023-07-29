import boto3
import os

def get_latest_object_by_extension(bucket_name, extension):
    s3_client = boto3.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    latest_object = None
    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                if obj['Key'].lower().endswith(extension):
                    if latest_object is None or obj['LastModified'] > latest_object['LastModified']:
                        latest_object = obj

    return latest_object

def lambda_handler(event, context):
    # Replace with your source and destination bucket names
    source_bucket_name = 'source-bucket-name'
    destination_bucket_name = 'destination-bucket-name'
    
    # Create an S3 client for both source and destination buckets
    source_s3_client = boto3.client('s3')
    destination_s3_client = boto3.client('s3', region_name='destination-bucket-region')
    
    try:
        # Find the latest zip file and txt file based on last modified timestamp
        latest_zip_object = get_latest_object_by_extension(source_bucket_name, '.zip')
        latest_txt_object = get_latest_object_by_extension(source_bucket_name, '.txt')
        
        if latest_zip_object is None or latest_txt_object is None:
            return {
                'statusCode': 404,
                'body': 'No zip or txt file found in the source bucket.'
            }
        
        # Get the latest zip file data
        source_zip_key = latest_zip_object['Key']
        response = source_s3_client.get_object(Bucket=source_bucket_name, Key=source_zip_key)
        zip_object_data = response['Body'].read()
        
        # Upload the latest zip file to the destination bucket
        destination_zip_key = os.path.basename(source_zip_key)  # Use the zip file name as the destination key
        
        destination_s3_client.put_object(
            Bucket=destination_bucket_name,
            Key=destination_zip_key,
            Body=zip_object_data
        )

        # Get the latest txt file data
        source_txt_key = latest_txt_object['Key']
        response = source_s3_client.get_object(Bucket=source_bucket_name, Key=source_txt_key)
        txt_object_data = response['Body'].read()

        # Upload the latest txt file to the destination bucket
        destination_txt_key = os.path.basename(source_txt_key)  # Use the txt file name as the destination key
        
        destination_s3_client.put_object(
            Bucket=destination_bucket_name,
            Key=destination_txt_key,
            Body=txt_object_data
        )

        return {
            'statusCode': 200,
            'body': 'Successfully uploaded the latest zip and txt files to the destination bucket.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {e}'
        }
