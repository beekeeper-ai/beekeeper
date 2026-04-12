from beekeeper.retrievers.watson_discovery.base import WatsonDiscoveryRetriever
import warnings

warnings.warn(
    "The 'beekeeper.retrievers' package has been moved to 'novastack.retrievers.watson_discovery'. "
    "Please update your imports to use 'novastack.retrievers.watson_discovery' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["WatsonDiscoveryRetriever"]
