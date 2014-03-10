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
RELEASE = 'dev' not in VERSION
if not RELEASE:
    VERSION += get_svn_devstr()
#
# Treat everything in bin/ except *.rst as a script to be installed.
#
scripts = [fname for fname in glob.glob(os.path.join('bin', '*'))
           if not os.path.basename(fname).endswith('.rst')]
#
# If we are using --prefix, manipulate the prefix directory and make sure
# it is in sys.path
#
prefix = [arg for arg in sys.argv if arg.startswith('--prefix')]
if len(prefix) > 0:
    i = sys.argv.index(prefix[0])
    prefdir = prefix[0].split('=')[1]
    if os.path.basename(prefdir) == PACKAGENAME:
        prefdir = os.path.join(prefdir,VERSION)
    else:
        prefdir = os.path.join(prefdir,PACKAGENAME,VERSION)
    sys.argv[i] = '--prefix='+prefdir
    # print(sys.argv)
    #
    # Get the Python version
    #
    pyversion = "python{0:d}.{1:d}".format(*sys.version_info)
    libdir = os.path.join(prefdir,'lib',pyversion,'site-packages')
    # If os.makedirs raises an exception, we want this to halt!
    os.makedirs(libdir)
    os.environ['PYTHONPATH'] = libdir + ':' + os.environ['PYTHONPATH']
    sys.path.insert(int(sys.path[0] == ''),libdir)
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
      packages=find_packages('py'),
      package_dir = {'':'py'}
)
