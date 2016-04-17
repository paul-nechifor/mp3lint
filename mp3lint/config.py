from os.path import join
from json import load, dump

from appdirs import user_config_dir


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
    with open(get_path(), 'w') as f:
        dump(config, f)


def get_path():
    return join(user_config_dir(APP_NAME), CONFIG_FILE_NAME)
