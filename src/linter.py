import os


class Linter(object):

    def __init__(self, library_path):
        self.library_path = os.path.abspath(library_path)
        self.structure = None

    def run(self):
        self.structure = self.load_files()
        print self.structure

    def load_files(self):
        ret = {}

        for root, dirs, files in os.walk(self.library_path):
            sub = get_dict(ret, os.path.relpath(root, self.library_path))
            for file in files:
                sub[file] = {'type': 'file', 'name': file}
            for dir in dirs:
                sub[dir] = {'type': 'dir', 'name': dir}

        return ret


def get_dict(d, path):
    parts = path.split('/')
    ret = d
    for part in parts:
        ret = ret.setdefault(part, {})
    return ret
