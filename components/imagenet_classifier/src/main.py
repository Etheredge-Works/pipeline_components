#! python
from pathlib import Path
from random import shuffle, seed
from os.path import basename
import click
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Flatten, Dense, Droput
from tensorflow.keras.regularizers import l2
from tensorflow.keras.applications.resnet_v2 import ResNet50V2 as pre_trained_model
from tensorflow.keras.applications.resnet_v2 import preprocess_input


def weight_init():
    return tf.random_normal_initializer(mean=0, stddev=0.01)


def bia_init():
    return tf.random_normal_initializer(mean=0.5, stddev=0.01)

def reg(factor=2e-4):
    return l2(factor)


@click.command()
@click.option('--data-dir', type=click.Path(exists=True), help='')
@click.option('--height', type=click.INT, help='')
@click.option('--width', type=click.INT, help='')
@click.option('--label-dir', type=click.Path(exists=True), help='')
@click.option('--random-seed', type=click.INT, help='')
@click.option('--dense-nodes', default=32, type=click.INT, help='')
@click.option('--model-dir', type=click.Path(exists=False), help='')
def main(
    data_dir: Path, 
    height: int,
    width: int,
    label_dir: Path, 
    random_seed: int,
    dense_nodes: int,
    model_dir: Path,
):
    seed(random_seed)

    input_shape = (height,width,3)
    ds = tf.data.experimental.load(
        str(data_dir), 
        tf.TensorSpec(shape=(input_shape), 
        dtype=tf.float32)) # TODO maybe handle passing in the dtype?
    # TODO write custom ds

    label_ds = tf.data.experimental.load(
        str(label_dir), 
        tf.TensorSpec(shape=(), 
        dtype=tf.int64)) # TODO maybe handle passing in the dtype?
    unique_labels = list(set(iter(label_ds)))

    ds_joined = tf.data.Dataset.zip((ds, label_ds))

    base_model = pre_trained_model(weights='imagenet', include_top=False, input_shape=input_shape)
    for layer in base_model.layers:
        layer.trainable = False
    x = base_model.output
    x = Flatten()(x)
    x = Dense(dense_nodes, activation='relu', dtype='float32',
                kernel_initializer=weight_init(),
                bias_initializer=bia_init(),
                kernel_regularizer=reg()
                )(x)
    #x = Dropout(0.5)(x)
    x = Dense(len(unique_labels, activation='softmax', dtype='float32'))
    model = Model(base_model.inputs, x)

    model.fit(ds_joined, batch_size=32, epochs=1, verbose=1)

if __name__ == "__main__":
    main()