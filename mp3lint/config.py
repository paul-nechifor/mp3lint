from json import dump, load
from os import makedirs
from os.path import dirname, join

from appdirs import user_config_dir

from six.moves import input

CONFIG_FILE_NAME = 'config.json'
APP_NAME = 'mp3lint'


class ConfigNotFoundError(Exception):
    pass


def load_config():
    try:
        with open(get_path()) as f:
            return load(f)
    except IOError:
        raise ConfigNotFoundError('File not found: "%s"' % get_path())


def write_config(config):
    path = get_path()
    try:
        makedirs(dirname(path))
    except OSError:
        pass
    with open(path, 'w') as f:
        dump(config, f)


def read_or_gen_config():
    try:
        return load_config()
    except ConfigNotFoundError:
        gen_config = generate_config()
        write_config(gen_config)
        return gen_config


def generate_config():
    music_dir = input('What is your music dir: ')
    return {
        'music_dir': music_dir,
    }


def get_path():
    return join(user_config_dir(APP_NAME), CONFIG_FILE_NAME)
