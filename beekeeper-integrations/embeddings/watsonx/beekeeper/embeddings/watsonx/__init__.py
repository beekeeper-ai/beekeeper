from beekeeper.embeddings.watsonx.base import WatsonxEmbedding
import warnings

warnings.warn(
    "The 'beekeeper.embeddings' package has been moved to 'novastack.embeddings.watsonx'. "
    "Please update your imports to use 'novastack.embeddings.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["WatsonxEmbedding"]
