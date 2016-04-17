from .linter import Linter


def main(name):
    if name != '__main__':
        return
    Linter().run()


def entry_point():
    main('__main__')


main(__name__)
