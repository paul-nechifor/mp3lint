from os.path import join

from mock import patch

from . import config
from .test_utils import TestCase


class EntryPoint(TestCase):

    @patch('mp3lint.config.user_config_dir')
    def test_load_config(self, mock):
        with self.create_temp_dir() as dir:
            open(join(dir, config.CONFIG_FILE_NAME), 'w').write('{"a": 1}')
            mock.return_value = dir
            conf = config.load_config()
        self.assertEqual({'a': 1}, conf)
