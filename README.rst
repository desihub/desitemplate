============
desitemplate
============

|Actions Status| |Coveralls Status| |Documentation Status|

.. |Actions Status| image:: https://github.com/desihub/desitemplate/workflows/CI/badge.svg
    :target: https://github.com/desihub/desitemplate/actions
    :alt: GitHub Actions CI Status

.. |Coveralls Status| image:: https://coveralls.io/repos/desihub/desitemplate/badge.svg
    :target: https://coveralls.io/github/desihub/desitemplate
    :alt: Test Coverage Status

.. |Documentation Status| image:: https://readthedocs.org/projects/desitemplate/badge/?version=latest
    :target: https://desitemplate.readthedocs.io/en/latest/
    :alt: Documentation Status

Introduction
============

This repository is intended to be a template for other DESI_ **Python** repositories.

.. _DESI: https://www.desi.lbl.gov

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

Creating a New Product From Scratch
===================================

**DO NOT CLONE THIS PRODUCT!**

Again, do not clone this product.  This could result in your changes being
committed back to this product instead of your own product.  Nobody wants that.

To create a new product, download the most recent *tag* of this product.
You can find that in the Releases section on GitHub, or from the command-line::

    wget -O desitemplate-2.0.0.tar.gz https://github.com/desihub/desitemplate/archive/2.0.0.tar.gz

After you expand the tar file, replace all references to 'desitemplate' with the
name of your product.  Note that there are some hidden files in this product!
Then you can add your own files to the structure.  Then
see the `GitHub article`_ on adding a new project to GitHub.

.. _`GitHub article`: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github

Updating an Existing Product
============================

If any of the functionality provided by the template changes, this will be
announced on ``desi-data@desi.lbl.gov``.  Then download the latest tag and
update the corresponding files.

Installing a Product
====================

DESI_ Python packages should be installable by pip_.  For example::

    pip install git+https://github.com/desihub/desitemplate.git@2.0.0

In this example the string ``@2.0.0`` means "install tag 2.0.0".  You can
also use this method to install branches (by branch name) or specific commits
(using the git hash).

At NERSC_, DESI_ products should be installed with desiInstall.  The main purpose
of desiInstall is to ensure that different versions of a package are kept
separate and to install `Module files`_.  desiInstall is not part of this package,
but part of desiutil_.

.. _pip: https://pip.pypa.io/en/stable/
.. _NERSC: https://www.nersc.gov
.. _desiutil: https://github.com/desihub/desiutil
.. _`Module files`: https://modules.sourceforge.net

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

.. _Sphinx: https://www.sphinx-doc.org/en/master/

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

pyproject.toml
~~~~~~~~~~~~~~

``pyproject.toml`` is the eventual replacement for ``setup.py`` and ``setup.cfg``.
This file contains all the metadata about a project, as well as configuration for
other tools such as test coverage.

**If your product contains a pyproject.toml file, desiInstall will assume that your
product is Python-based and will process it accordingly.**

As of early 2025, a ``setup.py`` file may still be required if the Python package
contains C/C++ code to be compiled. That configuration is beyond the scope
of this template.

setup.cfg
~~~~~~~~~

As of early 2025, a stub ``setup.cfg`` file is still required to set the
cofiguration for ``pycodestyle``.

LICENSE Files
~~~~~~~~~~~~~

Your product should include a license!  The 3-clause BSD-style license is the
standard adopted by DESI.  You can just copy the LICENSE.rst file in this
package.  You might want to adjust the date on the copyright line though.

Automation Support Files
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the standard ``.gitignore`` file, there are two other
hidden files included in this product.

.readthedocs.yml
    Configuration for the ReadTheDocs builds.

.github/workflows/python-package.yml
    This is the configuration file for `GitHub Actions`_ tests.  This file might
    need to be adjusted to suit your package.

.. _`GitHub Actions`: https://github.com/desihub/desitemplate/actions

Manifest File
~~~~~~~~~~~~~

The ``MANIFEST.in`` file contains instructions for the setup system that will
be used to construct an "official" tarball of the package.  For example,
this file will be used by the command::

    python -m build --sdist

This file is absolutely necessary if your package will be distributed via
PyPI_.

.. _PyPI: https://pypi.org

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

    desi_update_version desitemplate

This file should not be altered except by that command.  ``desitemplate``
should be replaced by the name of your package. In preparation for a
new tag of the product, you can use the variant::

    desi_update_version --tag 1.2.3 desitemplate

To set the version string to exactly '1.2.3'.  Make sure you check in your
changes and immediately tag after doing this!

``desi_update_version`` is provided in the desiutil_ package.

Enabling Testing and Other Automation
=====================================

The instructions above concern installing the necessary *files* but to perform
`GitHub Actions`_ tests, Coverage checks and automated documentation.
In addition, GitHub packages also need special settings set.

#. Create accounts on `Read the Docs`_, and `Coveralls`_.
#. Visit *e.g.* https://github.com/desihub/desitemplate and click on
   Settings (look for a gear icon on the right).  If you do not see this,
   **stop now**.  In this case you probably don't have permission to
   perform any of these steps.
#. Under Settings click 'Webhooks & Services'.
#. Click 'Add Service', and select 'ReadTheDocs'.
   There is little to no account information to add here.
#. Go to your Coveralls account and activate the product you want to test.
   In some cases this product will be under the desihub group, rather than your
   personal account.
#. Go to your Read the Docs account, click 'Import a Project' and follow the
   instructions.  For 'Documentation Type', select 'Sphinx Html'.
#. Start testing...

.. _`Read the Docs`: https://readthedocs.org
.. _`Coveralls`: https://coveralls.io

Links to Automation
===================

DESI_ uses several online resources to test software and build documentation.
This section contains example links to those services.

Package API Documentation
=========================

Please visit `desitemplate on Read the Docs <https://desitemplate.readthedocs.io/en/latest/>`_.

License
=======

desitemplate is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
