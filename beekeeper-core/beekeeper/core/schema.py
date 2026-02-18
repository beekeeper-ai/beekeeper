from abc import abstractmethod

from beekeeper.core.document import Document


class TransformerComponent:
    @abstractmethod
    def __call__(self, documents: list[Document]) -> list[Document]:
        """Transform documents."""
