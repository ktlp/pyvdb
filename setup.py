import os
from setuptools import find_packages
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages, Extension
import sys
import subprocess
import platform 
import re 
from distutils.version import LooseVersion


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir='', exclude_arch=False):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)
        self.exclude_arch = exclude_arch


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: " +
                ", ".join(e.name for e in self.extensions))

        if platform.system() == "Windows":
            cmake_version = LooseVersion(re.search(r'version\s*([\d.]+)',
                                         out.decode()).group(1))
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable]
        print("*"*50)
        print("*"*50)
        print(f"CMAKE ARGS: {cmake_args}")
        print("*"*50)
        print("*"*50)
        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(
                cfg.upper(),
                extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j3']

        if self.distribution.verbose > 0:
            cmake_args += ['-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get('CXXFLAGS', ''),
            self.distribution.get_version())

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args,
                              cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args,
                              cwd=self.build_temp)
        print()  # Add an empty line for cleaner output



def main():
    setup(
    name="pyvdb",
    version="0.0.1",
    description="A package for manipulating vdb objects in python",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(where="pyvdb"),
    package_dir={"": "pyvdb"},
    include_package_data=True,
    zip_safe=False,
    # cmake_args=[
    #     "-GUnix Makefiles",
    #     "-DBUILD_TESTING=OFF",
    #     "-DBUILD_DOCS=OFF",
    #     f"-DCMAKE_PREFIX_PATH={os.path.dirname(pybind11.__file__)}",
    # ],
    ext_modules=[CMakeExtension('pyvdb_bindings')],
    cmdclass=dict(build_ext=CMakeBuild),
)




if __name__ == "__main__":
    main()
