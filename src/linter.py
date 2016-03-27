import json
import os

from checkers import checker_classes


class Linter(object):

    def __init__(self, library_path):
        self.library_path = os.path.abspath(library_path)
        self.structure = None
        self.checkers = [x(self) for x in checker_classes]
        self.problems = []

    def run(self):
        self.structure = self.load_files()
        for x in self.checkers:
            x.run()
        print json.dumps(self.problems, indent=2)

    def load_files(self):
        ret = {}

        for root, dirs, files in os.walk(self.library_path):
            sub = get_dict(ret, os.path.relpath(root, self.library_path))
            for file in files:
                sub[file] = None

        return ret



def get_dict(d, path):
    if path == '.':
        return d
    parts = path.split('/')
    ret = d
    for part in parts:
        ret = ret.setdefault(part, {})
    return ret
