#
# Template Makefile for use with desiInstall.  You can assume that
# desiInstall will set these environment variables:
#
# WORKING_DIR   : The directory containing the svn export
# INSTALL_DIR   : The directory the installed product will live in.
# (PRODUCT)_DIR : Where (PRODUCT) is replaced with the name of the
#                 product in upper case, e.g. TEMPLATE_DIR.  This should
#                 be the same as WORKING_DIR for typical installs.
#
# Use this shell to interpret shell commands, & pass its value to sub-make
#
export SHELL = /bin/sh
#
# This is like doing 'make -w' on the command line.  This tells make to
# print the directory it is in.
#
MAKEFLAGS = w
#
# This is a list of subdirectories that make should descend into.  Makefiles
# in these subdirectories should also understand 'make all' & 'make clean'.
# This list can be empty, but should still be defined.
#
SUBDIRS = src doc
#
# This is a list of directories that make should copy to $INSTALL_DIR.
#
INSTALLDIRS = bin doc lib pro
#
# This is a message to make that these targets are 'actions' not files.
#
.PHONY : all install clean
#
# This should compile all code prior to it being installed.
#
all :
	@ for f in $(SUBDIRS); do $(MAKE) -C $$f all ; done
#
# This should handle the installation of files in $INSTALL_DIR.  Note that
# 'all' is a dependency of 'install'.
#
install : all
	@ for f in $(INSTALLDIRS); do \
		if test -d $(WORKING_DIR)/$$f -a ! -d $(INSTALL_DIR)/$$f; then \
			/bin/cp -Rvf $(WORKING_DIR)/$$f $(INSTALL_DIR); fi; done
#
# GNU make pre-defines $(RM).  The - in front of $(RM) causes make to
# ignore any errors produced by $(RM).
#
clean :
	- $(RM) *~ core
	@ for f in $(SUBDIRS); do $(MAKE) -C $$f clean ; done
