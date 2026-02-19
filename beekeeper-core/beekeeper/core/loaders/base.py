from abc import ABC, abstractmethod

from beekeeper.core.document import Document
from pydantic.v1 import BaseModel


class BaseLoader(ABC, BaseModel):
    """Abstract base class defining the interface for document loader."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseLoader"

    @abstractmethod
    def load_data(self, *args, **kwargs) -> list[Document]:
        """Loads data."""
