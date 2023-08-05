import boto3
import csv

ecr = boto3.client('ecr',region_name='ap-southeast-1')

def get_image_tag_from_digest(repository_name, image_digest):
    response = ecr.list_images(repositoryName=repository_name, maxResults=1000)
    for image in response['imageIds']:
        if 'imageDigest' in image and image['imageDigest'] == image_digest:
            return image['imageTag']

# Open the CSV file with repository and image ARNs
with open('ecr_repositories.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    # Prepare the CSV file for findings
    with open('ecr_findings.csv', 'w', newline='') as findings_file:
        writer = csv.writer(findings_file)
        writer.writerow(["Repository ARN", "Image ARN", "Finding Name", "Severity", "Description"])

        # Loop through each row in the input CSV
        for row in reader:
            repo_arn, image_digest = row

            # Get the repository name from the ARN
            repo_name = repo_arn.split('/')[-1]
            image_tag = get_image_tag_from_digest(repo_name, image_digest)

            # Initial next_token for pagination
            next_token = None
            while True:
                try:
                    # Add nextToken to arguments if it's not the first page
                    kwargs = {
                        'repositoryName': repo_name,
                        'imageId': {
                            'imageDigest': image_digest,
                            'imageTag': "latest"
                        },
                        'nextToken': next_token
                    } if next_token else {
                        'repositoryName': repo_name,
                        'imageId': {
                            'imageDigest': image_digest,
                            'imageTag': "latest"
                        }
                    }

                    # Get image scan findings
                    scan_findings = ecr.describe_image_scan_findings(**kwargs)

                    # Access enhancedFindings directly, catching KeyError if it doesn't exist
                    try:
                        enhanced_findings = scan_findings['imageScanFindings']['enhancedFindings']
                        for finding in enhanced_findings:
                            # Write repository ARN, image ARN, and finding details to the CSV
                            writer.writerow([repo_arn, image_digest, finding['title'], finding['severity'], finding['description']])
                    except KeyError:
                        print(f"No enhanced findings for image: {image_digest} in repository: {repo_name}")

                    # Check if there are more findings to process
                    if 'nextToken' in scan_findings:
                        next_token = scan_findings['nextToken']
                    else:
                        break

                except ecr.exceptions.ScanNotFoundException:
                    print(f"No scan findings for image: {image_digest} in repository: {repo_name}")
                    break
