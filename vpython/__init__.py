from pkg_resources import get_distribution, DistributionNotFound

from .gs_version import glowscript_version

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
__gs_version__ = glowscript_version()

del glowscript_version
del get_distribution
del DistributionNotFound

# Keep the remaining imports later to ensure that __version__ and
#  __gs_version__ exist before importing vpython, which itself imports
# both of those.

from .vpython import canvas

# Need to initialise canvas before user does anything and before
# importing GSprint
scene = canvas()

from .vpython import *
from .shapespaths import *
from ._vector_import_helper import *
from .rate_control import rate
from .gsprint import GSprint

# gsprint and vpython are showing up in the
# namespace, so delete them
del gsprint, vpython
