import warnings

warnings.warn(
    "The 'beekeeper.readers.docling' package has been moved to 'beekeeper.loaders.docling'. "
    "Please update your imports to use 'beekeeper.loaders.docling' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

from beekeeper.readers.docling.base import DoclingReader

__all__ = ["DoclingReader"]
