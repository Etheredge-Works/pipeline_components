#! /bin/bash
data_dir=$1
path_to_zip_file=$2
tar_file_name=$3
echo "Data Dir: " $1
echo "Path to File: " $2
echo "File Name: " $3
echo "pls..."
#mkdir -p $data_dir
gunzip -c -d $path_to_tar_file > temp_data_out
stat temp_data_out
ls temp_data_out
mv temp_data_out $data_dir

#gunzip -c -d $path_to_tar_file/$tar_file_name > $data_dir
#mkdir -p $data_dir
#cd $data_dir && gunzip -c -d $path_to_zip_file 
