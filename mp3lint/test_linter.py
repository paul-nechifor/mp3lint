from mock import patch

from .linter import Linter
from .test_utils import TestCase


class TestLinter(TestCase):

    @patch('mp3lint.linter.read_or_gen_config')
    def test_run_prints_done(self, mock):
        mock.return_value = {'music_dir': '/asdf/usr'}
        with self.capture_output() as stringio:
            Linter().run()
        output = (
            'Scanning "/asdf/usr"...\n'
            'Done.\n'
        )
        self.assertEqual(output, stringio.getvalue())
