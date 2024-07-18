add_executable(pyvdb_app pyvdb_app.cpp)
target_include_directories(pyvdb_app PRIVATE ../src/cpp/include)
target_link_libraries(pyvdb_app PRIVATE pyvdb)
