from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# import details from amico/info.py
import sys
sys.path.insert(0, './amico/')
import info

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
# extra_link_args = []

openblas_dir = 'OpenBLAS-0.3.21'

if sys.platform.startswith('win32'):
      include_dirs.extend([openblas_dir+'/include'])
      libraries.extend(['libopenblas']) # .lib filenames
      library_dirs.extend([openblas_dir+'/lib'])
      extra_compile_args.extend(['/std:c++14'])
      # extra_link_args.extend([])
if sys.platform.startswith('linux'):
      include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      library_dirs.extend([openblas_dir])
      extra_compile_args.extend(['-std=c++14'])
      # extra_link_args.extend([])
if sys.platform.startswith('darwin'):
      include_dirs.extend([openblas_dir])
      libraries.extend(['stdc++', 'openblas']) # library names (not filenames)
      library_dirs.extend([openblas_dir])
      extra_compile_args.extend(['-std=c++14'])
      # extra_link_args.extend([])

extensions = [
      Extension(
            'amico.models',
            sources=['amico/models.pyx'],
            include_dirs=include_dirs,
            libraries=libraries,
            library_dirs=library_dirs,
            extra_compile_args=extra_compile_args
            # extra_link_args=extra_link_args
      ),
      Extension(
            'amico.lut',
            sources=['amico/lut.pyx']
      )
]

# TODO move metadata to setup.cfg
setup(name=info.NAME,
      version=info.VERSION,
      description=info.DESCRIPTION,
      long_description=info.LONG_DESCRIPTION,
      author=info.AUTHOR,
      author_email=info.AUTHOR_EMAIL,
      url=info.URL,
      license=info.LICENSE,
      packages=find_packages(),
      install_requires=['packaging', 'wheel', 'numpy>=1.12', 'scipy>=1.0', 'dipy>=1.0', 'tqdm>=4.56.0', 'joblib>=1.0.1', 'threadpoolctl>=3.1.0'],
      package_data={'amico': ['directions/*.bin']},
      ext_modules=cythonize(extensions))
