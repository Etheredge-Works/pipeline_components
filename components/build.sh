#!/bin/bash -e
build_push () {
   dir=$1
   image_name=$2
   image_version=$3

   #cd $dir 
   docker build -t "${image_name}:${image_version}" -t "${image_name}:latest" .
   #docker image push --all-tags "$image_name" #TODO update docker to use
   docker push "$image_name" # TODO current behavior is push all tags

   # Output the strict image name (which contains the sha256 image digest)
   docker inspect --format="{{index .RepoDigests 0}}" "${image_name}"
}