from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# import details from amico/info.py
import sys
sys.path.insert(0, './amico/')
import info

include_dirs = [
      'spams',
      'spams/decomp',
      'spams/dictLearn',
      'spams/linalg',
      'spams/prox',
      'nnls'
]
libraries = []
library_dirs = []
extra_compile_args = []
extra_link_args = []

if sys.platform.startswith('win32'):
      openblas_include = ['OpenBLAS-0.3.21/include']
      openblas_lib = ['OpenBLAS-0.3.21/lib']
      include_dirs.extend(openblas_include)
      libraries.extend(['libopenblas'])
      library_dirs.extend(openblas_lib)
      extra_compile_args.extend(['-std:c11'])
      extra_link_args.extend([])
if sys.platform.startswith('linux'):
      openblas_include = ['OpenBLAS-0.3.21']
      openblas_lib = ['OpenBLAS-0.3.21']
      include_dirs.extend(openblas_include)
      libraries.extend(['stdc++', 'openblas'])
      library_dirs.extend(openblas_lib)
      extra_compile_args.extend(['-std=c++11'])
      extra_link_args.extend([])
if sys.platform.startswith('darwin'):
      openblas_include = ['OpenBLAS-0.3.21']
      openblas_lib = ['OpenBLAS-0.3.21']
      include_dirs.extend(openblas_include)
      libraries.extend(['stdc++', 'openblas'])
      library_dirs.extend(openblas_lib)
      extra_compile_args.extend(['-std=c++11'])
      extra_link_args.extend([])

extensions = [
      Extension(
            'amico.models',
            sources=['amico/models.pyx'],
            include_dirs=include_dirs,
            libraries=libraries,
            library_dirs=library_dirs,
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args
      ),
      Extension(
            'amico.lut',
            sources=['amico/lut.pyx']
      )
]

setup(name=info.NAME,
      version=info.VERSION,
      description=info.DESCRIPTION,
      long_description=info.LONG_DESCRIPTION,
      author=info.AUTHOR,
      author_email=info.AUTHOR_EMAIL,
      url=info.URL,
      license=info.LICENSE,
      packages=find_packages(),
      install_requires=['packaging', 'wheel', 'numpy>=1.12', 'scipy>=1.0', 'dipy>=1.0', 'tqdm>=4.56.0', 'joblib>=1.0.1'],
      package_data={'amico': ['directions/*.bin']},
      ext_modules=cythonize(extensions))
