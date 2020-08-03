#! /bin/bash
data_dir = $1
tar_file = $2
echo $1
echo $2
mkdir -p $data_dir; tar xzf $tar_files -C $data_dir --strip-components 1