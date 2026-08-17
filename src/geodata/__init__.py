"""geodata.

Earth Science Data Schema for describing the data holdings of diverse earth science repositories
"""

try:
    from geodata._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
