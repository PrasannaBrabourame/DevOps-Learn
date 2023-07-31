aws s3api list-objects --bucket "***** Bucket Name *****" --prefix "**** Folder Name *****" --output json --query 'Contents[*].[Key, Size]' > S3_Details.json
