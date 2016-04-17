from contextlib import contextmanager
from shutil import rmtree
from tempfile import mkdtemp
from unittest import TestCase as UnitTestCase
import sys

from six import StringIO


class TestCase(UnitTestCase):

    @contextmanager
    def capture_output(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        yield sys.stdout
        sys.stdout = original_stdout

    @contextmanager
    def create_temp_dir(self):
        dir = mkdtemp()
        yield dir
        rmtree(dir)
