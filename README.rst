========
template
========

Introduction
------------

This repository is intended to be a template for other repositories.

Layout
------

A DESI software product may contain these directories:

bin/
    Contains executable scripts and binaries (after compilation).  Typically,
    this directory will be added to your ``$PATH``.
doc/
    Contains high-level documentation of the software.  Typically, the code
    itself will contain its own documentation.  This area is for
    documentation that discusses the package as a whole.
etc/
    Contains data and configuration files used by the code.  This does not
    mean you should be checking in large data files!
py/
    Contains Python code.
src/
    Contains C/C++ code.

README Files
------------

Of course your product should have a README file!  The preferred name and
format is ``README.rst``.  When you add such a file to svn, be sure that
the svn:mime-type property is set::

    svn propset svn:mime-type text/x-rst README.rst

This will allow Trac to render your README file in HTML.  In fact, you should
set this mime-type for any and all .rst files that you have.

