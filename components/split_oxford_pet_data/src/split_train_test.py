#! python
import sys
import glob
from pathlib import Path
from random import shuffle, seed
import shutil
from os.path import basename
import re
import click


@click.command()
@click.option('--data-dir', type=click.Path(exists=True), help='')
@click.option('--ratio', type=click.FLOAT, help='')
@click.option('--train-dir', type=click.Path(exists=False), help='')
@click.option('--test-dir', type=click.Path(exists=False), help='')
@click.option('--random-seed', type=click.INT, help='')
@click.option('--by-label', type=click.BOOL, default=False, help='')
def main(data_dir, ratio, train_dir, test_dir, random_seed, by_label):
    seed(random_seed)

    by_label = 1 if by_label else 0

    data_dir = Path(data_dir)
    ratio = float(ratio)
    assert 0 <= ratio <= 1.0
    train_dir = Path(train_dir)
    if train_dir.exists():
        shutil.rmtree(str(train_dir))
    train_dir.mkdir(parents=True)
    test_dir = Path(test_dir)
    if test_dir.exists():
        shutil.rmtree(str(test_dir))
    test_dir.mkdir(parents=True)

    all_files = list(data_dir.glob('*jpg'))
    assert len(all_files) > 0
    
    def get_label(filename):
        # either get the whole thing or just the label
        return re.search(r'^(.*)_\d+\.jpg$', basename(filename)).group(by_label)

    labels = list(set([get_label(str(file)) for file in all_files]))
    for label in labels:
        print(f"test_label: {label}")

    for item in labels:
        assert item is not None
    label_count = len(labels)

    test_label_count = int(ratio * label_count)
    shuffle(labels)
    test_labels = labels[:test_label_count]

    for file in all_files:
        if get_label(str(file)) in test_labels:
            shutil.copyfile(file, str(test_dir / basename(file)))
        else:
            shutil.copyfile(file, str(train_dir / basename(file)))

    if ratio > 0:
        assert len(test_labels) > 0
        assert len(list(test_dir.glob('*'))) > 0


if __name__ == "__main__":
    main()