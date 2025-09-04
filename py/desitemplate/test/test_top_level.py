# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test top-level desitemplate functions
"""
import unittest
import re
from .. import __version__ as theVersion


class TestTopLevel(unittest.TestCase):
    """Test top-level desitemplate functions
    """

    @classmethod
    def setUpClass(cls):
        """This function will be run before *any* tests in this class.
        """
        cls.versionre = re.compile(
            r'([0-9]+!)?([0-9]+)(\.[0-9]+)*((a|b|rc|\.post|\.dev)[0-9]+)?')

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

    def test_version(self):
        """Ensure the version conforms to PEP386/PEP440.
        """
        self.assertRegex(theVersion, self.versionre)
