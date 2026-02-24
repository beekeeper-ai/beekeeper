from abc import ABC, abstractmethod
from typing import Any

from beekeeper.core.document import DocumentWithScore


class BaseRetriever(ABC):
    """
    Abstract base class for document retrievers.
    """

    @abstractmethod
    def query_documents(
        self,
        query: str,
        **kwargs: Any,
    ) -> list[DocumentWithScore]:
        """
        Query and retrieve relevant documents.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement the query_documents() method"
        )
