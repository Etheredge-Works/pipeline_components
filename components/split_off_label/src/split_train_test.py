#! python
import sys
import glob
from pathlib import Path
from random import shuffle, seed
import shutil
from os.path import basename
import argparse
import pathlib
import re
import click

@click.command()
@click.option('--data-dir', type=click.Path(exists=True), help='')
@click.option('--label', type=click.STRING, help='')
@click.option('--label-dir', type=click.Path(exists=False), help='')
@click.option('--other-dir', type=click.Path(exists=False), help='')
def main(data_dir, label, label_dir, other_dir):
            
    #dir, ratio, train_dir, test_dir = sys.argv[1:]
    data_dir = Path(data_dir)

    label_dir = Path(label_dir)
    if label_dir.exists():
        shutil.rmtree(str(label_dir))
    label_dir.mkdir(parents=True)

    other_dir = Path(other_dir)
    if other_dir.exists():
        shutil.rmtree(str(other_dir))
    other_dir.mkdir(parents=True)

    all_files = list(data_dir.glob('*jpg'))
    assert len(all_files) > 0

    for file in all_files:
        file_name = str(file)
        if label in file_name:
            shutil.copyfile(file_name, str(label_dir / basename(file)))
        else:
            shutil.copyfile(file_name, str(other_dir / basename(file)))


if __name__ == "__main__":
    main()