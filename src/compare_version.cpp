/// \file compare_version.cpp
///
/// \brief Defines desiUtil::compare_version().
///
#include "template.hpp"
//
//
//
bool desiUtil::compare_version(const std::string& a, const std::string& b)
{
    int parsedA[4], parsedB[4];
    desiUtil::parse_version(parsedA, a);
    desiUtil::parse_version(parsedB, b);
    return std::lexicographical_compare(parsedA, parsedA + 4, parsedB, parsedB + 4);
}
//
// int main(int argc, char **argv) {
//     std::string first(argv[1]);
//     std::string second(argv[2]);
//     std::string op = desiUtil::compare_version(first,second) ? " < " : " > ";
//     std::cout << first << op << second << std::endl;
//     return 0;
// }
