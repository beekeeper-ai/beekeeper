import warnings

from beekeeper.vector_stores.elasticsearch.base import ElasticsearchVectorStore

warnings.warn(
    "The 'beekeeper.vector_stores' package has been moved to 'novastack.vector_stores.elasticsearch'. "
    "Please update your imports to use 'novastack.vector_stores.elasticsearch' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["ElasticsearchVectorStore"]
