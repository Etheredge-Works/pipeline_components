#! /bin/bash
data_dir = $1
path_to_tar_file=$2
tar_file = $3
echo "Data Dir: " $1
echo "Path to Tar File: " $2
echo "Tar File Name: " $3
mkdir -p $data_dir
tar xzf $path_to_tar_file/$tar_files -C $data_dir --strip-components 1