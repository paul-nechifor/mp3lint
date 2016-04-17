from .linter import Linter
from .test_utils import TestCase


class TestLinter(TestCase):

    def test_run_prints_done(self):
        with self.capture_output() as stringio:
            Linter().run()
        value = stringio.getvalue()
        self.assertEqual('Done.\n', value)
