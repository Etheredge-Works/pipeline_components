#! /bin/bash
data_URL=$1
out_dir=$2
echo "Data URL: " $data_URL
echo "Out Dir: " $out_dir
#mkdir -p ${tar_name##*/}
#echo "Making: " ${tar_name##/*}
echo "Making: " $out_dir
mkdir -p $out_dir
wget --directory-prefix=$out_dir/ "$data_URL"
# TODO better naming

# According the the man pages, I'm using -O horribly wrong... I guess I'll just use a dir instead
#wget -O $tar_name $data_URL 