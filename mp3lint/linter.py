from .config import read_or_gen_config


class Linter(object):
    def __init__(self):
        self.config = {}

    def load(self):
        self.config = read_or_gen_config()

    def run(self):
        self.load()
        print('Scanning "%s"...' % self.config['music_dir'])
        print('Done.')
