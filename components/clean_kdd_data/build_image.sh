#!/bin/bash -e
image_name=etheredgeb/clean_kdd_data
full_image_name=${image_name}

cd "$(dirname "$0")" 
docker build -t "${full_image_name}" .
docker push "$full_image_name"

# Output the strict image name (which contains the sha256 image digest)
docker inspect --format="{{index .RepoDigests 0}}" "${full_image_name}"