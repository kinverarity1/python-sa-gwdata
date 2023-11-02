from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("python-sa-gwdata")
except PackageNotFoundError:
    __version__ = "unknown version"

from sa_gwdata.waterconnect import *
from sa_gwdata.waterconnect_funcs import *
from sa_gwdata.sarig import *
from sa_gwdata.identifiers import *
from sa_gwdata.local_cache import *

cache = LocalCache()
