from beekeeper.loaders.docling.base import DoclingLoader
import warnings

warnings.warn(
    "The 'beekeeper.loaders' package has been moved to 'novastack.loaders.docling'. "
    "Please update your imports to use 'novastack.loaders.docling' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["DoclingLoader"]
