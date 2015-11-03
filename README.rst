============
desitemplate
============

Introduction
============

This repository is intended to be a template for other DESI_ **Python** repositories.

.. _DESI: https://desi.lbl.gov

This repository contains *examples* that should be *copied* into another product.
It is not designed to have much functionality on its own, or even to be installed.

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

DESI_ Python packages should be installable by pip_.  For example:

    pip install git+https://github.com/desihub/desitemplate.git@1.0.0

In this example the string ``@1.0.0`` means "install tag 1.0.0".  You can
also use this method to install branches (by branch name) or specific commits
(using the git sha).

At NERSC_, DESI_ products should be installed with desiInstall.  The main purpose
of desiInstall is to ensure that different versions of a package are kept
separate and to install `Module files`_.  desiInstall is not part of this package,
but part of desiutil_.

.. _pip: http://pip.readthedocs.org
.. _NERSC: http://www.nersc.gov
.. _desiutil: https://github.com/desihub/desiutil
.. _`Module files`: http://modules.sourceforge.net

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
    are found in this directory, desiInstall will install them automatically.
    However, you should not rely on pip installing these files for you.
py/
    Contains Python code.  Top-level Python package directories should be
    placed *within* the ``py/`` directory.  This simplifies the specification
    of the ``$PYTHONPATH`` variable.

For a standard DESI_ Python package, you will probably need all of these
directories, with the possible exception of the bin directory.

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
This will allow the package to be installed with pip.
In addition, desiInstall will process this file with::

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

Module files are intended for use at NERSC_.  They are not processed
automatically by pip.

Version File
~~~~~~~~~~~~

In the top-level of the py/destemplate directory, you will see a file called
``_version.py``.  This file is created and maintained by the command::

    python setup.py version

This file should not be altered except by that command.  In preparation for a
new tag of the product, you can use the variant::

    python setup.py version --tag 1.2.3

To set the version string to exactly '1.2.3'.  Make sure you check in your
changes and immediately tag after doing this!

Links to Automation
===================

DESI_ uses several online resources to test software and build documentation.
This section contains example links to those services.

Full Documentation
------------------

Please visit `desitemplate on Read the Docs`_

.. image:: https://readthedocs.org/projects/desitemplate/badge/?version=latest
    :target: http://desitemplate.readthedocs.org/en/latest/
    :alt: Documentation Status

.. _`desitemplate on Read the Docs`: http://desitemplate.readthedocs.org/en/latest/

Travis Build Status
-------------------

.. image:: https://img.shields.io/travis/desihub/desitemplate.svg
    :target: https://travis-ci.org/desihub/desitemplate
    :alt: Travis Build Status


Test Coverage Status
--------------------

.. image:: https://coveralls.io/repos/desihub/desitemplate/badge.svg?service=github
    :target: https://coveralls.io/github/desihub/desitemplate
    :alt: Test Coverage Status

License
=======

desitemplate is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
