# License information goes here
# -*- coding: utf-8 -*-
"""
========
template
========

This package is a template for other DESI_ Python_ packages.

A Python package should have a `version()` method that returns the
version of the package.  This function should be used to set the ``__version__``
package variable.

.. _DESI: http://desi.lbl.gov
.. _Python: http://python.org
"""

def version():
    """Returns the version of this package.

    Parameters
    ----------
    None

    Returns
    -------
    version : str
        A PEP 386-compatible version string.

    Notes
    -----
    The version string should be compatible with `PEP 386`_ and
    `PEP 440`_.

    .. _`PEP 386`: http://legacy.python.org/dev/peps/pep-0386/
    .. _`PEP 440`: http://legacy.python.org/dev/peps/pep-0440/
    """
    from desiUtil.install import get_svn_devstr, most_recent_tag
    headurl = "$HeadURL$"
    if headurl.find('tags') > 0:
        myversion = headurl[headurl.find('tags')+5:].split('/')[0]
    elif (headurl.find('trunk') > 0) or (headurl.find('branches') > 0):
        url = headurl[10:len(headurl)-2]
        findstr = ('branches','trunk')[int(headurl.find('trunk') > 0)]
        tagurl = url[0:url.find(findstr)]+'tags'
        myversion = most_recent_tag(tagurl) + '.dev' + get_svn_devstr()
    else:
        myversion = '0.0.1.dev'
    return myversion
#
#
#
__version__ = version()
