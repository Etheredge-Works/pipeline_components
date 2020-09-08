#! /bin/bash
tar_args=$1
data_dir=$2
path_to_tar_file=$3
tar_file_name=$4
echo "Tar Args: " $1
echo "Data Dir: " $2
echo "Path to Tar File: " $3
echo "Tar File Name: " $4

mkdir -p $data_dir
tar $tar_args $path_to_tar_file -C $data_dir --strip-components 1
#tar xzf $path_to_tar_file/$tar_file_name -C $data_dir --strip-components 1