#!/bin/bash
repository_names=$(cat ./ecr.list |tr "\n" " ")
repository_name=($repository_names)
image_name="latest"

for i in "${repository_name[@]}"
do
	echo "\n\ECR $i REPOSITORY"
	aws ecr describe-image-scan-findings --repository-name "$i" --image-id imageTag="$image_name" --output json >> scan_report/$i.json
done