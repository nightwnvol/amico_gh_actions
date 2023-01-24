from setuptools import setup, Extension
from Cython.Build import cythonize
import cyspams
import sys
import os

include_dirs = []
libraries = []
library_dirs = []
extra_compile_args = []

# cyspams headers
include_dirs.extend(cyspams.get_include())

# OpenBLAS library (cyspams requirement)
try:
      openblas_dir = os.environ['OPENBLAS_DIR']
      print('openblas_dir', openblas_dir)
except KeyError as err:
      print(f"\033[31mKeyError: cannot find the {err} env variable\033[0m")
      exit(1)

include_dirs.extend([openblas_dir+'/include'])
library_dirs.extend([openblas_dir+'/lib'])

if sys.platform.startswith('win32'):
      # include_dirs.extend([openblas_dir+'/include'])
      libraries.extend(['libopenblas']) # .lib filenames
      # library_dirs.extend([openblas_dir+'/lib'])
      extra_compile_args.extend(['/std:c++14'])
if sys.platform.startswith('linux'):
      # include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      # library_dirs.extend([openblas_dir])
      extra_compile_args.extend(['-std=c++14'])
if sys.platform.startswith('darwin'):
      # include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      # library_dirs.extend([openblas_dir])
      extra_compile_args.extend(['-std=c++14'])

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
      ext_modules=cythonize(extensions)
)
