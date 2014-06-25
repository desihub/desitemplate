/// \file template.hpp
///
/// \brief Template header file.
///
/// Note how we have put most of the function documentation in this header
/// file rather than in the individual .cpp files.  This allows us to see
/// the interrelationship of the functions at a glance.
///
#ifndef _HAVE_TEMPLATE_HPP_
#define _HAVE_TEMPLATE_HPP_
#include <iostream>
#include <sstream>
#include <algorithm> // for std::transform()
#include <string>
#include <list>
#include <cctype> // for ::toupper()
#include <cstdio> // for ::popen(), etc.
#include <cstdlib> // for ::getenv()
///
/// \brief Define the desiUtil namespace.
///
namespace desiUtil {
    ///
    /// \brief Parse a string into version numbers.
    ///
    /// \param result An array of int to hold the result.
    /// \param input The string to parse.
    ///
    void parse_version(int result[4], const std::string& input);
    ///
    /// \brief Compare two version strings.
    ///
    /// \param a The first string to compare.
    /// \param b The second string to compare.
    ///
    /// \return True if the first version is "less" than the second version.
    ///
    bool compare_version(const std::string& a, const std::string& b);
    ///
    /// \brief Get the most recent tag.
    ///
    /// \param tags The URL pointing to the tags directory for this product.
    ///
    /// \return The most recent tag.
    ///
    /// \warning This function will try to communicate with the svn repository.
    ///
    std::string most_recent_tag(const std::string& tags);
    ///
    /// \brief Get the svn revision number.
    ///
    /// This function calls svnversion -n to get the svn revision number.  It
    /// is only called when the code appears to come from trunk or a branch,
    /// as indicated by the HeadURL svn keyword.
    ///
    /// \return The svn revision number in string form.  A value of "0"
    /// indicates an error of some kind.
    ///
    std::string get_svn_devstr(const std::string& product);
    ///
    /// \brief Version of the product.
    ///
    /// This function reads the value of HeadURL to determine the version.
    ///
    /// \param headurl A svn HeadURL string wrapped in a std::string object.
    ///
    /// \return The version name.
    ///
    std::string version(const std::string& headurl);
} // end namespace desiUtil
#endif // end ifndef _HAVE_TEMPLATE_HPP_
