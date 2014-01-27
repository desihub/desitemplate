========
template
========

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

Product Contents
================

Directory Structure
-------------------

A DESI software product may contain these directories:

bin/
    Contains executable scripts and binaries (after compilation).  Typically,
    this directory will be added to your ``$PATH``.
doc/
    Contains high-level documentation of the software.  Typically, the code
    itself will contain its own documentation.  This area is for
    documentation that discusses the product as a whole.
etc/
    Contains data and configuration files used by the code.  This does not
    mean you should be checking in large data files!
py/
    Contains Python code.  Top-level Python package directories should be
    placed *within* the py/ directory.  This simplifies the specification
    of the ``$PYTHONPATH`` variable.
src/
    Contains C/C++ code.

You should only create the directories you actually need.  For example,
if you are writing a pure Python product, you don't need the src directory.

Top-level Files
---------------

README Files
~~~~~~~~~~~~

Of course your product should have a README(.rst) file!  The preferred name and
format is ``README.rst``.  When you add such a file to svn, be sure that
the svn:mime-type property is set::

    svn propset svn:mime-type text/x-rst README.rst

This will allow Trac to render your README.rst file in HTML.  In fact, you should
set this mime-type for any and all .rst files that you have.

setup.py
~~~~~~~~

If your product is primarily Python, it should have a setup.py file.

configure
~~~~~~~~~

If your product is primarily C/C++, it should have a configure file or the
autotools files needed to generate a configure file.

.module file
~~~~~~~~~~~~

In this directory is a file called template.module.  This file is used to
create a module file for the product at install time.  It should be renamed
to the name of the product plus ``.module``.  It should be customized for
the needs of the product.

