from beekeeper.loaders.watson_discovery.base import WatsonDiscoveryLoader
import warnings

warnings.warn(
    "The 'beekeeper.loaders' package has been moved to 'novastack.loaders.watson_discovery'. "
    "Please update your imports to use 'novastack.loaders.watson_discovery' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["WatsonDiscoveryLoader"]
