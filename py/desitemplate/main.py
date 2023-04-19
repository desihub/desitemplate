# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
desitemplate.main
=================

This module contains an example command-line function.
"""
import os
import sys
from argparse import ArgumentParser


def main():
    """Entry-point for command-line scripts.

    Returns
    -------
    :class:`int`
        Exit status that will be passed to :func:`sys.exit`.
    """
    #
    # Parse arguments
    #
    executable = os.path.basename(sys.argv[0])
    parser = ArgumentParser(description="This is the overall description of the script",
                            prog=executable)
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                        help='Print extra information.')
    options = parser.parse_args()
    #
    #
    #
    print('Hello World!')
    if options.verbose:
        print('Verbose selected!')
    return 0
