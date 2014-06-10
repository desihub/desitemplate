/// \file main.cpp
///
/// \brief Defines main().
///
/// This file defines a main() function that forms the basis of a command-line
/// executable.
///
#include "template.hpp"
///
/// \brief Main program.
///
/// This function only exists to call desiUtil::version() and print its return value.
///
/// Note that the documentation for this function is here, rather than in
/// template.hpp, because main is not part of the namespace.  Nor is the
/// declaration of main() needed by the other functions.
///
/// \param argc Number of command line options.
/// \param argv The command line options.
///
/// \return The exit status that will be returned to the shell.
///
int main(int argc, char **argv)
{
    std::string headurl("$HeadURL$");
    std::cout << desiUtil::version(headurl) << std::endl;
    return 0;
}
