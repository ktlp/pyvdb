from skbuild import setup
import os
from setuptools import find_packages
import pybind11
import sys

cmake_install_dir = os.path.join('python', 'pyvdb')
library_output = "/pyramida/Kostas/Documents/IDEs/"



def main():setup(
    name="pyvdb",
    version="0.0.1",
    description="A package for manipulating vdb objects in python",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    include_package_data=True,
    zip_safe=False,
    cmake_args=[
        "-GUnix Makefiles",
        "-DBUILD_TESTING=OFF",
        "-DBUILD_DOCS=OFF",
        f"-DPYTHON_EXECUTABLE={sys.executable}",
        f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={library_output}",
        f"-DCMAKE_PREFIX_PATH={os.path.dirname(pybind11.__file__)}",
    ],
    cmake_install_dir=cmake_install_dir,
)




if __name__ == "__main__":
    main()
