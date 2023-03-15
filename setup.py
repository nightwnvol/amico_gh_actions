from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize
import cyspams
import sys
from os import cpu_count
import configparser
import shutil

# parallel compilation
class build_ext(_build_ext):
      def run(self):
            self.parallel = cpu_count()
            _build_ext.run(self)

libraries = []
library_dirs = []
include_dirs = []
extra_compile_args = []
# spams-cython headers
include_dirs.extend(cyspams.get_include())
# OpenBLAS headers
shutil.copyfile('site.cfg.example', 'site.cfg')
config = configparser.ConfigParser()
config.read('site.cfg')
if 'openblas' in config:
      libraries.extend([config['openblas']['library']])
      library_dirs.extend([config['openblas']['library_dir']])
      include_dirs.extend([config['openblas']['include_dir']])
else:
      print(f'\033[31mKeyError: cannot find the [openblas] section in site.cfg\033[0m')
      exit(1)

if sys.platform.startswith('win32'):
      extra_compile_args.extend(['/std:c++14', '/fp:fast'])
if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
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
            sources=['amico/lut.pyx'],
            extra_compile_args=extra_compile_args
      )
]

setup(
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(extensions)
)
