#! /bin/bash
data_dir=$1
path_to_tar_file=$2
tar_file_name=$3
echo "Data Dir: " $1
echo "Path to File: " $3
echo "File Name: " $4

mkdir -p $data_dir
gunzip -c -d $path_to_tar_file/$tar_file_name > $data_dir