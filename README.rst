============
desitemplate
============

Introduction
============

This repository is intended to be a template for other repositories.

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

A DESI product may contain these top-level directories.  It may contain
additional directories, but the directories listed here have special
meaning for desiInstall.

bin/
    This directory is only needed if the product contains executable code.
    If you do not have any scripts, and you are not planning to compile any
    C/C++ code to create an executable, you can omit this directory from your
    svn product.  This is more likely to be the case for Python-based products
    than for C/C++-based products.  If this directory is present, but empty,
    this is a signal to desiInstall that you intend to compile C/C++ code
    to create an executable binary.
doc/
    Contains high-level documentation of the software.  Typically, the code
    itself will contain its own documentation.  This area is for
    documentation that discusses the product as a whole.  Both Sphinx_ (for
    Python) and Doxygen_ can and will process files placed in this directory.
    Sphinx_ documents should be .rst files, while Doxygen_ documents should
    be .dox files.
etc/
    Contains small data and configuration files used by the code.  This does not
    mean you should be checking in large data files!  This directory also
    contains the template module file for the product.  If additional files
    are found in this directory, they will be installed automatically,
    independent of any Makefile.
lib/
    If this directory is present, even if it is empty, it is a signal to
    desiInstall that you intend to compile C/C++ code to produce a library
    (static or shared). *At this time we have not set a policy on include
    files (.h/.hpp) that may be required to use such libraries.*
pro/
    If this directory is present, support for IDL code will be added to the
    Module file.
py/
    Contains Python code.  Top-level Python package directories should be
    placed *within* the ``py/`` directory.  This simplifies the specification
    of the ``$PYTHONPATH`` variable.
src/
    Contains C/C++ code.

You should only create the directories you actually need.  For example,
if you are writing a pure Python product, you don't need the src directory.

.. _Sphinx: http://sphinx-doc.org
.. _Doxygen: http://www.stack.nl/~dimitri/doxygen/

Top-level Files
---------------

README Files
~~~~~~~~~~~~

Of course your product should have a README(.rst) file!  The preferred name and
format is ``README.rst``.  If your product lives on GitHub, it will automatically
be rendered!

If your product is in svn, be sure that the svn:mime-type property is set::

    svn propset svn:mime-type text/x-rst README.rst

This will allow Trac to render your README.rst file in HTML.  In fact, you should
set this mime-type for any and all .rst files that you have (in svn).

setup.py
~~~~~~~~

If your product is primarily Python, it should have a setup.py file.  See
the setup.py file included with this template product for further details.
desiInstall will process this file with::

    python setup.py install --prefix=$INSTALL_DIR.

**If your product contains a setup.py file, desiInstall will assume that your
product is Python-based and will process it accordingly.**

Makefile
~~~~~~~~

If your product is C/C++-based, at minimum you will need a top-level Makefile,
which should point to a Makefile in the ``src/`` directory.  This may suffice
for relatively simple C/C++-based products.  More complicated compiles will
require a configure file or the autotools files needed to generate a
configure file.

The Makefile will be called with ``make install``.  Helpful environment
variables such as ``WORKING_DIR`` and ``INSTALL_DIR`` will be supplied by
desiInstall.  In the example Makfile included with the template product,
``make install`` performs a ``make all`` automatically.

The Makefile should be prepared to handle the installation of
files and directories in ``INSTALL_DIR``.  That is, desiInstall won't try
to second-guess what files and directories you want to install.

**If your product contains a setup.py file in addition to a Makefile,
desiInstall will process the setup.py file first, then process the Makefile.**

Other Files
-----------

.module file
~~~~~~~~~~~~

In the etc/ directory is a file called ``desitemplate.module``.  This file is used to
create a module file for the product at install time.  It should be renamed
to the name of the product plus ``.module``.  It should be customized for
the needs of the product.  In particular, any packages that your product
depends on should be added to the module file.

src/Makefile
~~~~~~~~~~~~

It is assumed that most of the heavy-duty work of compiling a C/C++-based
product will take place in the src directory, and that the src/Makefile
will handle that compiling.  It should be set up (or created in a configure
stage) accordingly.  Libraries (shared or static) should be written to the
``lib/`` directory, and executables should be written to the ``bin/`` directory.


Travis Build Status
===================

.. image:: https://img.shields.io/travis/desihub/desitemplate.svg
    :target: https://travis-ci.org/desihub/desitemplate
    :alt: Travis Build Status


Test Coverage Status
====================

.. image:: https://coveralls.io/repos/desihub/desitemplate/badge.svg?branch=pre-1.0&service=github
    :target: https://coveralls.io/github/desihub/desitemplate?branch=pre-1.0
    :alt: Test Coverage Status

License
=======

desitemplate is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
