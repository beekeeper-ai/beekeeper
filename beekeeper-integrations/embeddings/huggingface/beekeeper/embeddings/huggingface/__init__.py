import warnings

from beekeeper.embeddings.huggingface.base import HuggingFaceEmbedding

warnings.warn(
    "The 'beekeeper.embeddings' package has been moved to 'novastack.embeddings.huggingface'. "
    "Please update your imports to use 'novastack.embeddings.huggingface' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["HuggingFaceEmbedding"]
