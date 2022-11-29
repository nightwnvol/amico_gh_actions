from setuptools import setup, Extension
from Cython.Build import cythonize
import sys

include_dirs = [
      'include/spams',
      'include/spams/decomp',
      'include/spams/dictLearn',
      'include/spams/linalg',
      'include/spams/prox',
      'include/nnls'
]
libraries = []
library_dirs = []
extra_compile_args = []

openblas_dir = 'OpenBLAS-0.3.21'

if sys.platform.startswith('win32'):
      include_dirs.extend([openblas_dir+'/include'])
      libraries.extend(['libopenblas']) # .lib filenames
      library_dirs.extend([openblas_dir+'/lib'])
      extra_compile_args.extend(['/std:c++14'])
if sys.platform.startswith('linux'):
      include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      library_dirs.extend([openblas_dir])
      extra_compile_args.extend(['-std=c++14'])
if sys.platform.startswith('darwin'):
      include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      library_dirs.extend([openblas_dir])
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


setup(ext_modules=cythonize(extensions))
