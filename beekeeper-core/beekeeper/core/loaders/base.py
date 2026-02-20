from abc import ABC, abstractmethod

from beekeeper.core.bridge.pydantic import BaseModel, ConfigDict
from beekeeper.core.document import Document


class BaseLoader(BaseModel, ABC):
    """Abstract base class defining the interface for document loader."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="forbid",
    )

    @classmethod
    def class_name(cls) -> str:
        """Returns the class name of the loader."""
        return "BaseLoader"

    @abstractmethod
    def load_data(self, *args, **kwargs) -> list[Document]:
        """
        Loads data and returns a list of documents.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            list[Document]: A list of loaded documents.
        """
