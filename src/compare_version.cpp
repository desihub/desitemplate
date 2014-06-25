/// \file compare_version.cpp
///
/// \brief Defines desiUtil::compare_version().
///
//#include "template.hpp"
#include <iostream>
#include <string>
//
//
//
//bool desiUtil::compare_version(const std::string& first, const std::string& second)
//{
//    return true;
//}

int main(int argc, char **argv) {
    std::string first("0.0.1");
    std::string second("0.1.0");
    size_t p1,p2,p3,p4;
    int i_major = std::stoi(first,&p1);
    int i_minor = std::stoi(first.substr(p1+1),&p2);
    int i_patch = std::stoi(first.substr(p1+1),&p2);
    std::cout << i_major << " " << i_minor << std::endl;
    return 0;
}
    // version_re = re.compile(r'^(\d+) \. (\d+) (\. (\d+))? ([ab](\d+))?$',
    //                         re.VERBOSE)
    //
    //
    // def parse (self, vstring):
    //     match = self.version_re.match(vstring)
    //     if not match:
    //         raise ValueError, "invalid version number '%s'" % vstring
    //
    //     (major, minor, patch, prerelease, prerelease_num) = \
    //         match.group(1, 2, 4, 5, 6)
    //
    //     if patch:
    //         self.version = tuple(map(string.atoi, [major, minor, patch]))
    //     else:
    //         self.version = tuple(map(string.atoi, [major, minor]) + [0])
    //
    //     if prerelease:
    //         self.prerelease = (prerelease[0], string.atoi(prerelease_num))
    //     else:
    //         self.prerelease = None
    //
    // def __cmp__ (self, other):
    //     if isinstance(other, StringType):
    //         other = StrictVersion(other)
    //
    //     compare = cmp(self.version, other.version)
    //     if (compare == 0):              # have to compare prerelease
    //
    //         # case 1: neither has prerelease; they're equal
    //         # case 2: self has prerelease, other doesn't; other is greater
    //         # case 3: self doesn't have prerelease, other does: self is greater
    //         # case 4: both have prerelease: must compare them!
    //
    //         if (not self.prerelease and not other.prerelease):
    //             return 0
    //         elif (self.prerelease and not other.prerelease):
    //             return -1
    //         elif (not self.prerelease and other.prerelease):
    //             return 1
    //         elif (self.prerelease and other.prerelease):
    //             return cmp(self.prerelease, other.prerelease)
    //
    //     else:                           # numeric versions don't match --
    //         return compare              # prerelease stuff doesn't matter
    //
