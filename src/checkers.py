from inspect import isclass


class Checker(object):

    def __init__(self, linter):
        self.linter = linter

    def run(self):
        raise NotImplementedError()


class EmptyDirChecker(Checker):

    def run(self):
        self.check_dir((), self.linter.structure)

    def check_dir(self, parents, structure):
        for name, files in structure.items():
            if files is None:
                continue

            new_parent = parents + (name,)

            if files:
                self.check_dir(new_parent, files)
                continue

            self.linter.problems.append({
                'type': 'empty_dir',
                'path': '/'.join(new_parent),
            })


checker_classes = [
    x
    for x in locals().values()
    if isclass(x) and issubclass(x, Checker) and x is not Checker
]
