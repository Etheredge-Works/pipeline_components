#! /bin/bash
data_dir=$1
path_to_tar_file=$2
tar_file_name=$3
echo "Data Dir: " $data_dir
echo "Path to File: " $path_to_tar_file
echo "File Name: " $tar_file_name

mkdir -p $data_dir
gunzip -c -d $path_to_tar_file/$tar_file_name > $data_dir