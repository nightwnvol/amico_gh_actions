from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize
import cyspams
import sys
import configparser

class build_ext(_build_ext):
      def run(self):
            self.parallel = True
            _build_ext.run(self)

libraries = []
library_dirs = []
include_dirs = []
extra_compile_args = []

# cyspams headers
include_dirs.extend(cyspams.get_include())

# BLAS/LAPACK headers
config = configparser.ConfigParser()
config.read('site.cfg')
if 'openblas' in config:
      libraries.extend([config['openblas']['libraries']])
      library_dirs.extend([config['openblas']['library_dirs']])
      include_dirs.extend([config['openblas']['include_dirs']])
      print(f'\033[32mFound openblas section in site.cfg\033[0m')
      print(f'\033[32mlibraries: {libraries}\033[0m')
      print(f'\033[32mlibrary_dirs: {library_dirs}\033[0m')
      print(f'\033[32minclude_dirs: {include_dirs}\033[0m')
else:
      print(f'\033[31mKeyError: cannot find the openblas section in site.cfg\033[0m')
      exit(1)

if sys.platform.startswith('win32'):
      extra_compile_args.extend(['/std:c++14', '/fp:fast'])
if sys.platform.startswith('linux'):
      libraries.extend(['stdc++'])
      extra_compile_args.extend(['-std=c++14', '-Ofast'])
if sys.platform.startswith('darwin'):
      libraries.extend(['stdc++'])
      extra_compile_args.extend(['-std=c++14', '-Ofast'])

extensions = [
      Extension(
            'amico.models',
            sources=['amico/models.pyx'],
            include_dirs=include_dirs,
            libraries=libraries,
            library_dirs=library_dirs,
            extra_compile_args=extra_compile_args
      ),
      Extension(
            'amico.lut',
            sources=['amico/lut.pyx']
      )
]

setup(
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(extensions)
)
