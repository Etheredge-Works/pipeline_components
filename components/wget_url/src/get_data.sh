#! /bin/bash
data_URL=$1
tar_name=$2
echo "Data URL: " $data_URL
echo "Tar Name: " $tar_name
#mkdir -p ${tar_name##*/}
#echo "Making: " ${tar_name##/*}
echo "Making: " $tar_name
mkdir -p $tar_name
wget --directory-prefix=$tar_name/ $data_URL 
# TODO better naming

# According the the man pages, I'm using -O horribly wrong... I guess I'll just use a dir instead
#wget -O $tar_name $data_URL 