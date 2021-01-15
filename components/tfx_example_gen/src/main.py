#! python
from tfx.components import CsvExampleGen
from tfx.utils.dsl_utils import external_input

def main(data_dir):
    CsvExampleGen(input=external_input(str(data_dir)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script will split data.
    """)
    parser.add_argument("--data_dir", help="")

    args = parser.parse_args()

    data_dir = pathlib.Path(args.data_dir)
    return main(data_dir)

