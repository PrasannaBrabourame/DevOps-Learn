import boto3
import csv
from botocore.exceptions import NoCredentialsError

ecr = boto3.client('ecr',region_name='ap-southeast-1')

# Get all ECR repositories
try:
    repos = ecr.describe_repositories()['repositories']
except NoCredentialsError:
    print("No AWS credentials found.")
    exit(1)

# Prepare the CSV file
with open('ecr_repositories.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Repository ARN", "Image ARN"])

    # Loop through each repository
    for repo in repos:
        # Get images for the current repository
        images = ecr.describe_images(repositoryName=repo['repositoryName'])['imageDetails']

        # Filter images with 'latest' tag
        latest_images = [img for img in images if 'imageTags' in img and 'latest' in img['imageTags']]

        if latest_images:
            for latest_image in latest_images:
                # Write repository ARN and image ARN to the CSV
                writer.writerow([repo['repositoryArn'], latest_image['imageDigest']])
