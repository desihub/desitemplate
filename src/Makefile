#
# Directories where binary code will live.  Be sure any environment
# variables are properly exported.
#
BIN = $(TEMPLATE_DIR)/bin
LIB = $(TEMPLATE_DIR)/lib
#
# Pass these flags to the C compiler
#
CPPFLAGS  = -Wall -O -fPIC
#
# Objects to compile
#
OBJECTS = most_recent_tag.o get_svn_devstr.o version.o
#
# By default, make uses this rule to compile individual objects. Override
# if necessary
#
# COMPILE.cc = $(CXX) $(CXXFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c
# COMPILE.cpp = $(COMPILE.cc)
# OUTPUT_OPTION = -o $@
# %.o: %.cpp
#	$(COMPILE.cpp) $(OUTPUT_OPTION) $<
#
# Flags for the link stage.
#
LDLIBS = -L $(LIB) -l template
SOFLAGS = -shared -fPIC
#
# Set the shared library extension.  This is a simple way to get
# the appropriate extension on Mac OS.
#
SO = so
UNAME = $(shell uname)
ifeq ($(UNAME), Darwin)
	SO = dylib
	SOFLAGS = -dynamiclib
endif
#
# This line helps prevent make from getting confused in the case where you
# have a file named 'clean'.
#
.PHONY : clean
#
# Makefiles should always define this target.
#
all : $(BIN)/template_version
#
# This creates the executable.
#
$(BIN)/template_version: $(LIB)/libtemplate.$(SO) main.o
	$(LINK.cc) $^ $(LOADLIBES) $(LDLIBS) -o $@
#
# This creates the library.
#
$(LIB)/libtemplate.$(SO): $(OBJECTS)
	$(LINK.cc) $(SOFLAGS) $^ $(LOADLIBES) -o $@
#
# GNU make pre-defines $(RM).  The - in front of $(RM) causes make to
# ignore any errors produced by $(RM).
#
clean :
	- $(RM) $(LIB)/libtemplate.$(SO) $(BIN)/template_version *~ core *.o a.out
