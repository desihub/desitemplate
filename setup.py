#!/usr/bin/env python
# License information goes here
#
import glob
import os
import sys
from setuptools import setup
#
# Import this module to get __doc__ and version().
#
sys.path.insert(int(sys.path[0] == ''),'./py')
try:
    import template
    LONG_DESCRIPTION = template.__doc__
    VERSION = template.version()
except ImportError:
    #
    # Try to get the long description from the README.rst file.
    #
    if os.path.exists('README.rst'):
        with open('README.rst') as readme:
            LONG_DESCRIPTION = readme.read()
    else:
        LONG_DESCRIPTION = ''
    VERSION = '0.0.1.dev'
#
# Set affiliated package-specific settings.  Change these as needed.
#
PACKAGENAME = 'template'
DESCRIPTION = 'DESI template package'
AUTHOR = 'Benjamin Alan Weaver'
AUTHOR_EMAIL = 'baweaver@lbl.gov'
LICENSE = 'BSD'
URL = 'https://desi.lbl.gov'
#
# Indicates if this version is a release version.
#
RELEASE = 'dev' not in VERSION
#if not RELEASE:
#    VERSION += get_svn_devstr(False)
#
# Treat everything in bin/ except *.rst as a script to be installed.
#
scripts = [fname for fname in glob.glob(os.path.join('bin', '*'))
           if not os.path.basename(fname).endswith('.rst')]
#
# Run setup command
#
setup(name=PACKAGENAME,
      version=VERSION,
      description=DESCRIPTION,
      scripts=scripts,
      requires=['Python (>2.6.0)'],
      #install_requires=['Python (>2.6.0)'],
      provides=[PACKAGENAME],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,
      use_2to3=True,
      package_dir = {'':'py'}
)
