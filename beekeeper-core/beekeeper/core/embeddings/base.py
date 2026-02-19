from abc import ABC, abstractmethod

import numpy as np
from beekeeper.core.document import Document
from beekeeper.core.embeddings.enums import SimilarityMode
from beekeeper.core.schema import TransformerComponent
from beekeeper.core.utils.pairwise import cosine_similarity

Embedding = list[float]


def similarity(
    embedding1: Embedding,
    embedding2: Embedding,
    mode: SimilarityMode = SimilarityMode.COSINE,
):
    """Get embedding similarity."""
    if mode == SimilarityMode.EUCLIDEAN:
        return -float(np.linalg.norm(np.array(embedding1) - np.array(embedding2)))

    elif mode == SimilarityMode.DOT_PRODUCT:
        return np.dot(embedding1, embedding2)

    else:
        return cosine_similarity(embedding1, embedding2)


class BaseEmbedding(TransformerComponent, ABC):
    """Abstract base class defining the interface for embedding models."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseEmbedding"

    @abstractmethod
    def embed_text(
        self, input: str | list[str]
    ) -> list[Embedding]:
        """Embed one or more text strings."""

    def embed_documents(self, documents: list[Document]) -> list[Document]:
        """
        Embed a list of documents and assign the computed embeddings to the 'embedding' attribute.

        Args:
            documents (List[Document]): List of documents to compute embeddings.
        """
        texts = [document.get_content() for document in documents]
        embeddings = self.embed_text(texts)

        for document, embedding in zip(documents, embeddings):
            document.embedding = embedding

        return documents

    @staticmethod
    def similarity(
        embedding1: Embedding,
        embedding2: Embedding,
        mode: SimilarityMode = SimilarityMode.COSINE,
    ):
        """Get embedding similarity."""
        return similarity(embedding1, embedding2, mode)

    def __call__(self, documents: list[Document]) -> list[Document]:
        return self.embed_documents(documents)
