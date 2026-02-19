import glob
import os
from pathlib import Path
from typing import Type

from beekeeper.core.document import Document
from beekeeper.core.loaders import BaseLoader


def _get_default_file_loaders():
    try:
        from beekeeper.loaders.file import DocxLoader, HTMLLoader, PDFLoader
    except ImportError:
        raise ImportError(
            "beekeeper-loaders-file package not found, please install it with `pip install beekeeper-loaders-file`",
        )

    return {
        ".docx": DocxLoader,
        ".html": HTMLLoader,
        ".pdf": PDFLoader,
    }


class DirectoryLoader(BaseLoader):
    """
    Loads files from a directory, optionally filtering by file extension and
    allowing recursive directory traversal.

    Attributes:
        required_exts (list[str], optional): List of file extensions to filter by.
            Only files with these extensions will be loaded. Defaults to `None` (no filtering).
        recursive (bool, optional): Whether to recursively search subdirectories for files.
            Defaults to `False`.

    Example:
        ```python
        from beekeeper.core.loader import DirectoryLoader

        directory_loader = DirectoryLoader()
        ```
    """

    required_exts: list[str] = [".pdf", ".docx", ".html"]
    recursive: bool = False
    file_loader: dict[str, Type[BaseLoader]] | None = None

    def load_data(self, input_dir: str) -> list[Document]:
        """
        Loads data from the specified directory.

        Args:
            input_dir (str): Directory path from which to load the documents.

        Returns:
            list[Document]: A list of documents loaded from the directory.
        """
        if not os.path.isdir(input_dir):
            raise ValueError(f"`{input_dir}` is not a valid directory.")

        if self.file_loader is None:
            self.file_loader = _get_default_file_loaders()

        input_dir = str(Path(input_dir))
        documents = []

        pattern_prefix = "**/*" if self.recursive else ""

        for extension in self.required_exts:
            files = glob.glob(
                os.path.join(input_dir, pattern_prefix + extension),
                recursive=self.recursive,
            )

            for file_dir in files:
                loader_cls = self.file_loader.get(extension)
                if loader_cls:
                    try:
                        # TODO add `file_loader_kwargs`
                        doc = loader_cls().load_data(file_dir)
                        documents.extend(doc)
                    except Exception as e:
                        raise Exception(f"Error reading {file_dir}: {e}")
                else:
                    # TODO add `unstructured file` support
                    raise ValueError(f"Unsupported file type: {extension}")

        return documents
