#include "pyvdb/pyvdb.hpp"
#include <iostream>

int main(){
  int result = pyvdb::add_one(1);
  std::cout << "1 + 1 = " << result << std::endl;
}