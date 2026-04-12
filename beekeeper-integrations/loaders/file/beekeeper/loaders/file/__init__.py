import warnings

from beekeeper.loaders.file.docx import DocxLoader
from beekeeper.loaders.file.html import HTMLLoader
from beekeeper.loaders.file.json import JSONLoader
from beekeeper.loaders.file.pdf import PDFLoader

warnings.warn(
    "The 'beekeeper.loaders' package has been moved to 'novastack.loaders.file'. "
    "Please update your imports to use 'novastack.loaders.file' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "DocxLoader",
    "HTMLLoader",
    "JSONLoader",
    "PDFLoader",
]
