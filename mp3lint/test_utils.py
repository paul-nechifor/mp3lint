from six import StringIO
from contextlib import contextmanager
from unittest import TestCase as UnitTestCase
import sys


class TestCase(UnitTestCase):

    @contextmanager
    def capture_output(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        yield sys.stdout
        sys.stdout = original_stdout
