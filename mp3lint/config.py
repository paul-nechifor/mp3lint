from os.path import join
from json import load

from appdirs import user_config_dir


CONFIG_FILE_NAME = 'config.json'
APP_NAME = 'mp3lint'


def load_config():
    path = join(user_config_dir(APP_NAME), CONFIG_FILE_NAME)
    print(path)
    with open(path) as f:
        return load(f)
