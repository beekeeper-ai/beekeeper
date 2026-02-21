from abc import ABC, abstractmethod

from beekeeper.core.document import DocumentWithScore


class BaseRetriever(ABC):
    """
    Abstract base class for document retrievers.
    """

    @abstractmethod
    def query_documents(
        self,
        query: str,
    ) -> list[DocumentWithScore]:
        """
        Query and retrieve relevant documents.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement the query_documents() method"
        )
