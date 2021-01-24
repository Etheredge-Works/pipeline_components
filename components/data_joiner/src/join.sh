#! /bin/bash
dir1=$1
dir2=$2
out_dir=$3

mkdir -p $out_dir
copy $dir1/* $out_dir/.
copy $dir2/* $out_dir/.
#tar xzf $path_to_tar_file/$tar_file_name -C $data_dir --strip-components 1