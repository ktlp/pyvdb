#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "include/pyvdb.hpp"

namespace py = pybind11;

// namespace pyvdb {

PYBIND11_MODULE(pyvdb_bindings, m)
{
  m.doc() = "Python Bindings for pyvdb";
  m.def("add_one", &pyvdb::add_one, "Increments an integer value");
  m.def("hello", &pyvdb::hello, "Greets");
}

// } // namespace pyvdb
