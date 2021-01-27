
from pathlib import Path
import tensorflow as tf
import os

import click
@click.command()
@click.option('--data-dir', type=click.Path(exists=True), help='')
@click.option('--height', type=click.INT, help='')
@click.option('--width', type=click.INT, help='')
@click.option('--tf-data-dir', type=click.Path(exists=False), help='')
@click.option('--tf-label-dir', type=click.Path(exists=False), help='')
def main(
        data_dir: str, 
        height: int,
        width: int,
        tf_data_dir: str,
        tf_label_dir: str,
):
    data_dir = Path(data_dir)
    tf_data_dir = Path(tf_data_dir)
    tf_label_dir = Path(tf_label_dir)

    tf_data_dir.mkdir(parents=True)
    tf_label_dir.mkdir(parents=True)
    filename_ds = tf.data.Dataset.list_files(
        str(data_dir/r'*.jpg'), shuffle=False)

    def file_decode(file_path):
        img = tf.io.read_file(file_path)
        img = tf.image.decode_jpeg(img, channels=3)

        # have to resize due to loading ds requiring same size on all
        img = tf.image.resize(img, [height, width])
        return img


    ds = filename_ds.map(file_decode)
    tf.data.experimental.save(ds, str(tf_data_dir))


    all_files_tf = tf.io.gfile.listdir(str(data_dir)) # gets just file name
    labels = tf.strings.regex_replace(all_files_tf, pattern=r'_\d.*', rewrite='')

    def get_label(file_path):
        # convert the path to a list of path components
        split = tf.strings.split(file_path, os.path.sep)
        tf.debugging.assert_greater(tf.size(split), tf.constant(1), f"Split is wrong.\n")
        file_name = tf.gather(split, tf.size(split) - 1)
        
        label = tf.strings.regex_replace(file_name, r'_\d+\.jpg.*', '')

        one_hot = label == labels
        return tf.argmax(tf.cast(one_hot, tf.uint8)) # must cast since is bool

    label_ds = filename_ds.map(get_label)
    tf.data.experimental.save(label_ds, str(tf_label_dir))


if __name__ == "__main__":
    main()