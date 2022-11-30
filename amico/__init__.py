from __future__ import absolute_import, division, print_function

from .core import Evaluation, setup
from .util import set_verbose, get_verbose
from . import core
from . import scheme
from . import lut
from . import models
from . import util

# from pkg_resources import get_distribution
# __version__ = get_distribution('dmri-amico').version

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadaata import version
__version__ = version('dmri-amico')
