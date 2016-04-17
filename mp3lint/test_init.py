from unittest import TestCase

import mp3lint

from mock import patch


class EntryPoint(TestCase):

    @patch('mp3lint.main')
    def test_entry_point_calls_main(self, mock_main):
        mp3lint.entry_point()
        mock_main.assert_called_with('__main__')

    @patch('mp3lint.Linter.run')
    def test_main_calls_linter_run(self, mock_run):
        mp3lint.main('__main__')
        mock_run.assert_called_with()
