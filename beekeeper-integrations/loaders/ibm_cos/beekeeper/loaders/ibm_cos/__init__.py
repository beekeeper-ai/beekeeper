from beekeeper.loaders.ibm_cos.base import IBMCOSLoader
import warnings

warnings.warn(
    "The 'beekeeper.loaders' package has been moved to 'novastack.loaders.ibm_cos'. "
    "Please update your imports to use 'novastack.loaders.ibm_cos' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["IBMCOSLoader"]
