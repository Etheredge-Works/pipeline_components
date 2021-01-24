#!/bin/bash -e
image_name=etheredgeb/clean_oxford_pet_data
image_version=0.1

cd $(dirname $0)
source ../build.sh
build_push $(dirname $0) $image_name $image_version