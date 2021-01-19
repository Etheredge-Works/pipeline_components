for build_file in $(find "components" -name build_image.sh)
do
  $build_file
done