from json import loads
from os.path import join

from mock import patch

from . import config
from .test_utils import TestCase


@patch('mp3lint.config.user_config_dir')
class ConfigWithPatchUserConfigDir(TestCase):

    def test_load_config(self, mock):
        with self.create_temp_dir() as dir:
            open(join(dir, config.CONFIG_FILE_NAME), 'w').write('{"a": 1}')
            mock.return_value = dir
            conf = config.load_config()
        self.assertEqual({'a': 1}, conf)

    def test_return_error_when_file_not_found(self, mock):
        with self.create_temp_dir() as dir:
            mock.return_value = join(dir, 'asdf')
            with self.assertRaises(config.ConfigNotFoundError):
                config.load_config()

    def test_write_config(self, mock):
        with self.create_temp_dir() as dir:
            inner_dir = join(dir, 'inner_dir')
            mock.return_value = inner_dir
            config.write_config({'z': 5})
            config_path = join(inner_dir, config.CONFIG_FILE_NAME)
            read = loads(open(config_path).read())
        self.assertEqual({'z': 5}, read)

    def test_read_or_gen_config_with_file(self, mock):
        with self.create_temp_dir() as dir:
            mock.return_value = dir
            open(join(dir, config.CONFIG_FILE_NAME), 'w').write('{"a": 1}')
            conf = config.read_or_gen_config()
        self.assertEqual({'a': 1}, conf)

    @patch('mp3lint.config.generate_config')
    def test_read_or_gen_config_without_file(
        self,
        mock_generate_config,
        mock_user_config_dir,
    ):
        with self.create_temp_dir() as dir:
            mock_user_config_dir.return_value = dir
            mock_generate_config.return_value = {'asdf': 'ff'}
            conf = config.read_or_gen_config()
            written = loads(open(join(dir, config.CONFIG_FILE_NAME)).read())
        self.assertEqual({'asdf': 'ff'}, conf)
        self.assertEqual({'asdf': 'ff'}, written)


class GenerateConfig(TestCase):

    def test_generate_config(self):
        with self.patch_stdin('/home/user/music\n'):
            conf = config.generate_config()
        self.assertEqual({'music_dir': '/home/user/music'}, conf)
