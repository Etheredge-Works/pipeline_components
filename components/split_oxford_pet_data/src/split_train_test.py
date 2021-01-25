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
@click.option('--ratio', type=click.FLOAT, help='')
@click.option('--train-dir', type=click.Path(exists=False), help='')
@click.option('--test-dir', type=click.Path(exists=False), help='')
@click.option('--random-seed', type=click.INT, help='')
def main(data_dir, ratio, train_dir, test_dir, random_seed):
    seed(random_seed)
    def copy_files(files: list, dir: Path) -> None:
        for file in files:
            shutil.copyfile(str(file), str(dir/basename(file)))
            
    #dir, ratio, train_dir, test_dir = sys.argv[1:]
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
    '''
    for file in all_files:
        file_name = str(file)
        if "Maine_Coon" in file_name or "boxer" in file_name:
            shutil.copyfile(file_name, str(test_dir / basename(file)))
        else:
            shutil.copyfile(file_name, str(train_dir / basename(file)))
    '''
    
    def get_label(filename):
        return re.search(r'^(.*)_\d+\.jpg$', basename(filename)).group(0)

    labels = list(set([get_label(str(file)) for file in all_files]))
    for label in labels:
        print(f"test_label: {label}")

    for item in labels:
        assert item is not None
    label_count = len(labels)

    #all_main_coon_files = list(dir.glob("Main_Coon*"))
    #all_boxer_files = list(dir.glob("boxer*"))


    #shuffle(all_files)
    test_label_count = int(ratio * label_count)
    shuffle(labels)
    test_labels = labels[:test_label_count]

    for file in all_files:
        if get_label(str(file)) in test_labels:
            shutil.copyfile(file, str(test_dir / basename(file)))
        else:
            shutil.copyfile(file, str(train_dir / basename(file)))
    #test_file_count = len(all_main_coon_files) + len(all_boxer_files)
    #copy_files(all_main_coon_files, test_dir)
    #copy_files(all_boxer_files, test_dir)

    if ratio > 0:
        assert len(test_labels) > 0
        assert len(list(test_dir.glob('*'))) > 0

    #train_files = all_files[test_files_count:]
    #copy_files(train_files, train_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script will split data.
    """)
    main()
    '''
    parser.add_argument("--data_dir", help="")
    parser.add_argument("--train_dir", help="")
    parser.add_argument("--test_dir", help="")
    parser.add_argument("--ratio", help="")
    #parser.add_argument("--cleaned_dir_name", help="")

    args = parser.parse_args()

    data = pathlib.Path(args.data_dir)
    #clean = pathlib.Path(args.cleaned_dir_name)
    #dir, ratio, train_dir, test_dir = sys.argv[1:]
    dir = args.data_dir
    ratio = args.ratio
    train_dir = args.train_dir
    test_dir = args.test_dir
    main(dir, ratio, train_dir, test_dir)
    '''

