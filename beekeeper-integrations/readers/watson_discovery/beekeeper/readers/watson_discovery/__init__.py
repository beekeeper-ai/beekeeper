import warnings

warnings.warn(
    "The 'beekeeper.readers.watson_discovery' package has been moved to 'beekeeper.loaders.watson_discovery'. "
    "Please update your imports to use 'beekeeper.loaders.watson_discovery' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

from beekeeper.readers.watson_discovery.base import WatsonDiscoveryReader

__all__ = ["WatsonDiscoveryReader"]
