from abc import ABC, abstractmethod

from beekeeper.core.bridge.pydantic import BaseModel
from beekeeper.core.document import Document


class BaseLoader(ABC, BaseModel):
    """Abstract base class defining the interface for document loader."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseLoader"

    @abstractmethod
    def load_data(self, *args, **kwargs) -> list[Document]:
        """Loads data."""
