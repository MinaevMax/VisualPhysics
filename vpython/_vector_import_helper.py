import platform

try:
    from .cyvector import *

    v = vector(0, 0, 0)
    # Delete v so it doesn't show up in the name space
    del v
except ImportError:
    from .vector import *

# Remove a platform from the namespace now that we are done with it
del platform

# synonyms in GlowScript
vec = vector
