/// \file get_svn_devstr.cpp
///
/// \brief Defines desiUtil::get_svn_devstr().
///
#include "template.hpp"
//
//
//
std::string desiUtil::get_svn_devstr(const std::string& product)
{
    std::string cbuff("");
    std::string unversioned("0");
    FILE *in;
    char buff[512];
    std::string product_dir = product;
    std::transform(product_dir.begin(), product_dir.end(), product_dir.begin(), ::toupper);
    product_dir += "_DIR";
    std::string command("svnversion -n ");
    command += getenv(product_dir.c_str());
    if (!(in = popen(command.c_str(),"r"))) return cbuff;
    if (fgets(buff, sizeof(buff), in) != NULL) {
        cbuff = buff;
        if (cbuff == "Unversioned directory") return unversioned;
        std::size_t colon = cbuff.find(":");
        if (colon != std::string::npos) {
            cbuff = cbuff.substr(colon+1);
        }
        while (cbuff[cbuff.length()-1] == 'M' || cbuff[cbuff.length()-1] == 'C' || cbuff[cbuff.length()-1] == 'P') cbuff = cbuff.substr(0,cbuff.length()-1);
    }
    pclose(in);
    return cbuff;
}
