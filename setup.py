#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

# NOTE: The configuration for the package, including the name, version, and
# other information are set in the setup.cfg file.

import sys
from setuptools import setup

# First provide a helpful message if contributors try to run legacy commands.

HELP = """This command is no longer supported.
See https://desiutil.readthedocs.io/en/latest/helpers.html#replacing-setup-py
for replacements.
"""

message = ('api', 'build_docs', 'build_sphinx', 'module_file', 'test', 'version')

for m in message:
    if m in sys.argv:
        print(HELP)
        sys.exit(1)

setup()
