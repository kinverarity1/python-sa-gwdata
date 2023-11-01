from sa_gwdata.waterconnect import *
from sa_gwdata.waterconnect_funcs import *
from sa_gwdata.sarig import *
from sa_gwdata.identifiers import *
from sa_gwdata.local_cache import *

from .version import version

__version__ = version()

cache = LocalCache()
