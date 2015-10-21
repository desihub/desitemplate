============
desitemplate
============

Introduction
============

This repository is intended to be a template for other **Python** repositories.

Product Name
============

The name of a software product should be short but descriptive.  You may be
stuck with it for a long time.

There is one important guideline when creating a new product.
**Don't choose a name that contains a hyphen!**  Automation will be
converting the product name into an environment variable, and shells don't
like environment variable names that contain hyphens.

Installing a Product
====================

DESI products should be installed with desiInstall.  desiInstall decides how
to perform an installation based on the files it finds in the top level of
the product directory (see below).

There may be situations where a product contains no code by design.  In this
case it should still contain a stripped-down top-level Makefile that
contains enough functionality to install the product, but otherwise
does nothing.

Product Contents
================

Directory Structure
-------------------

A DESI **Python** product may contain these top-level directories.  It may contain
additional directories, but the directories listed here have special
meaning for desiInstall.

bin/
    This directory is only needed if the product contains executable scripts.
    If you do not have any scripts, you can omit this directory from your
    product.
doc/
    Contains high-level documentation of the software.  Typically, the code
    itself will contain its own documentation.  This area is for
    documentation that discusses the product as a whole.  Sphinx_
    will process files placed in this directory.
    Sphinx_ documents should be .rst files.
etc/
    Contains small data and configuration files used by the code.  This does not
    mean you should be checking in large data files!  This directory also
    contains the template module file for the product.  If additional files
    are found in this directory, they will be installed automatically.
py/
    Contains Python code.  Top-level Python package directories should be
    placed *within* the ``py/`` directory.  This simplifies the specification
    of the ``$PYTHONPATH`` variable.

You should only create the directories you actually need!  For example,
if you are writing a pure Python library, you don't need the bin directory.

.. _Sphinx: http://sphinx-doc.org

Top-level Files
---------------

README.rst Files
~~~~~~~~~~~~~~~~

Of course your product should have a README(.rst) file!  The preferred name and
format is ``README.rst``.  If your product lives on GitHub, it will automatically
be rendered!

If your product is in svn, be sure that the svn:mime-type property is set::

    svn propset svn:mime-type text/x-rst README.rst

This will allow Trac to render your README.rst file in HTML.  In fact, you should
set this mime-type for any and all .rst files that you have (in svn).

setup.py
~~~~~~~~

Your Python product should have a setup.py file.  See
the setup.py file included with this template product for further details.
desiInstall will process this file with::

    python setup.py install --prefix=$INSTALL_DIR.

**If your product contains a setup.py file, desiInstall will assume that your
product is Python-based and will process it accordingly.**

LICENSE Files
~~~~~~~~~~~~~

Your product should include a license!  The 3-clause BSD-style license is the
standard adopted by DESI.  You can just copy the LICENSE.rst file in this
package.  You might want to adjust the date on the copyright line though.

Other Files
-----------

.module file
~~~~~~~~~~~~

In the etc/ directory is a file called ``desitemplate.module``.  This file is used to
create a module file for the product at install time.  It should be renamed
to the name of the product plus ``.module``.  It should be customized for
the needs of the product.  In particular, any packages that your product
depends on should be added to the module file.

License
=======

desitemplate is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
