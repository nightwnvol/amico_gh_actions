from __future__ import absolute_import, division, print_function

# import sys
# import os

# NOTE not compatible with PEP 302-based import hooks
# extra_dll_dir = os.path.join(os.path.dirname(__file__), '.libs')

# if sys.platform == 'win32':
#     # from importlib.resources import files # NOTE Python >= 3.9
#     from importlib_resources import files # NOTE backport of Python standard library importlib.resources module for older Pythons
#     extra_dll_dir = files('amico').joinpath('.libs')
#     if os.path.isdir(extra_dll_dir):
#         os.add_dll_directory(extra_dll_dir)

from .core import Evaluation, setup
from .util import set_verbose, get_verbose
from . import core
from . import scheme
from . import lut
from . import models
from . import util

from pkg_resources import get_distribution
__version__ = get_distribution('dmri-amico').version
