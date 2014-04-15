#!/usr/bin/env python
# License information goes here
#
# Imports
#
import glob
import os
import sys
from setuptools import setup, find_packages
#
# Import this module to get __doc__ and version().
#
setup_keywords = dict()
sys.path.insert(int(sys.path[0] == ''),'./py')
#
# THESE SETTINGS NEED TO BE CHANGED FOR EVERY PRODUCT.
#
setup_keywords['name'] = 'template'
setup_keywords['description'] = 'DESI template package'
setup_keywords['author'] = 'Benjamin Alan Weaver'
setup_keywords['author_email'] = 'baweaver@lbl.gov'
setup_keywords['license'] = 'BSD'
setup_keywords['url'] = 'https://desi.lbl.gov/svn/code/tools/template'
#
# END OF SETTINGS THAT NEED TO BE CHANGED.
#
try:
    from importlib import import_module
    product = import_module(setup_keywords['name'])
    setup_keywords['long_description'] = product.__doc__
    setup_keywords['version'] = product.version()
except ImportError:
    #
    # Try to get the long description from the README.rst file.
    #
    if os.path.exists('README.rst'):
        with open('README.rst') as readme:
            setup_keywords['long_description'] = readme.read()
    else:
        setup_keywords['long_description'] = ''
    setup_keywords['version'] = '0.0.1.dev'
#
# Obtain svn information.
#
def get_svn_devstr():
    """Get the svn revision number.

    Parameters
    ----------
    None

    Returns
    -------
    get_svn_devstr : str
        The latest svn revision number.
    """
    from subprocess import Popen, PIPE
    proc = Popen(['svnversion','-n'],stdout=PIPE,stderr=PIPE)
    out, err = proc.communicate()
    rev = out
    if ':' in out:
        rev = out.split(':')[1]
    rev = rev.replace('M','').replace('S','').replace('P','')
    return rev
#
# Indicates if this version is a release version.
#
RELEASE = 'dev' not in setup_keywords['version']
if not RELEASE:
    setup_keywords['version'] += get_svn_devstr()
#
# Set general settings.  Change these as needed.
#
#
# Set other keywords for the setup function.  These are automated, & should
# be left alone unless you are an expert.
#
# Treat everything in bin/ except *.rst as a script to be installed.
#
setup_keywords['scripts'] = [fname for fname in glob.glob(os.path.join('bin', '*'))
    if not os.path.basename(fname).endswith('.rst')]
setup_keywords['provides'] = [PRODUCT_NAME]
setup_keywords['requires'] = ['Python (>2.6.0)']
#setup_keywords['install_requires'] = ['Python (>2.6.0)']
setup_keywords['zip_safe'] = False
setup_keywords['use_2to3'] = True
setup_keywords['packages'] = find_packages('py')
setup_keywords['package_dir'] = {'':'py'}
#
# Run setup command.
#
setup(**setup_keywords)
