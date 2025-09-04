# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test desitemplate.main functions
"""
import contextlib
import io
import unittest
from unittest.mock import patch
from ..main import main, _parse_arguments


class TestMain(unittest.TestCase):
    """Test desitemplate.main functions
    """

    @classmethod
    def setUpClass(cls):
        """This function will be run before *any* tests in this class.
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """This function will be run after *all* tests in this class.
        """
        pass

    def setUp(self):
        """This function will be run before every test in this class.
        """
        pass

    def tearDown(self):
        """This function will be run after every test in this class.
        """
        pass

    @patch('sys.argv', ['template_main_script'])
    @patch('builtins.print')
    def test_main(self, mock_print):
        """Test the main() function.
        """
        status = main()
        self.assertEqual(status, 0)
        mock_print.assert_called_once_with('Hello World!')

    @patch('sys.argv', ['template_main_script', '--verbose'])
    def test_parse_arguments(self):
        """Test command-line argument parsing.
        """
        options = _parse_arguments()
        self.assertTrue(options.verbose)
