from os.path import dirname, join
import json
import os

from linter import Linter

config_file = join(dirname(dirname(__file__)), 'config.json')


def main():
    config = json.load(open(config_file))
    Linter(library_path=config['libraryPath']).run()


if __name__ == '__main__':
    main()
