cmake_minimum_required(VERSION 3.1.0)
project(pyvdb_bindings)
include(FetchContent)


# Define the minimum C++ standard that is required
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Try to find pybind11
message(STATUS "Getting pybind11")
find_package(pybind11 QUIET)

# If pybind11 is not found, fetch it
if (NOT pybind11_FOUND)
    message(STATUS "pybind11 not found, fetching it...")
    FetchContent_Declare(
      pybind11
      GIT_REPOSITORY https://github.com/pybind/pybind11.git
      GIT_TAG        v2.12.0
    )
    FetchContent_MakeAvailable(pybind11)
endif()


message(STATUS "Looking in directory: ${CMAKE_CURRENT_SOURCE_DIR}/cpp/")
file(GLOB SRC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/cpp/*.cpp")
message(STATUS "Found source files: ${SRC_FILES}")
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/cpp/include)

# Your target
message(STATUS "SRC_FILES: ${SRC_FILES}")
pybind11_add_module(pyvdb_bindings
    ${SRC_FILES})

# Link libraries
target_include_directories(pyvdb_bindings PUBLIC ${CMAKE_SOURCE_DIR}/cpp/include)
# target_link_libraries(pyvdb_bindingdds PUBLIC pybind11::module)

set(CMAKE_CXX_STANDARD 11)