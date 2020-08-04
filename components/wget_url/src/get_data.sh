#! /bin/bash
data_URL=$1
tar_name=$2
mkdir -p $(basedir $tar_name)
wget -O $tar_name $data_URL