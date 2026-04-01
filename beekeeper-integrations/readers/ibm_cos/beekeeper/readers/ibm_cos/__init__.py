import warnings

warnings.warn(
    "The 'beekeeper.readers.ibm_cos' package has been moved to 'beekeeper.loaders.ibm_cos'. "
    "Please update your imports to use 'beekeeper.loaders.ibm_cos' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

from beekeeper.readers.ibm_cos.base import IBMCOSReader

__all__ = ["IBMCOSReader"]
