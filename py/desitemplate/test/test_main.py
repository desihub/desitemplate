# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desitemplate.main functions
"""
import contextlib
import io
import unittest
from unittest.mock import patch
from ..main import main


class TestMain(unittest.TestCase):
    """Test desitemplate.main functions
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('sys.argv', ['template_main_script'])
    def test_main(self):
        """Test the main() function.
        """
        sout = io.StringIO()
        with contextlib.redirect_stdout(sout):
            self.assertEqual(main(), 0)
        self.assertEqual(sout.getvalue(), 'Hello World!\n')

    @patch('sys.argv', ['template_main_script', '--verbose'])
    def test_main_verbose(self):
        """Test the main() function with -v.
        """
        sout = io.StringIO()
        with contextlib.redirect_stdout(sout):
            self.assertEqual(main(), 0)
        self.assertEqual(sout.getvalue(), 'Hello World!\nVerbose selected!\n')
