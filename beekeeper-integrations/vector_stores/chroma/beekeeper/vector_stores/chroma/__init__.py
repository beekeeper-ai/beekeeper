from beekeeper.vector_stores.chroma.base import ChromaVectorStore
import warnings

warnings.warn(
    "The 'beekeeper.vector_stores' package has been moved to 'novastack.vector_stores.chroma'. "
    "Please update your imports to use 'novastack.vector_stores.chroma' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["ChromaVectorStore"]
