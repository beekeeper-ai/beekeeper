from abc import abstractmethod
from typing import Optional

import numpy as np
from beekeeper.core.bridge.pydantic import BaseModel, ConfigDict, Field
from beekeeper.core.document import Document
from beekeeper.core.embeddings.enums import SimilarityMode
from beekeeper.core.schema import TransformerComponent
from beekeeper.core.utils.pairwise import cosine_similarity

Embedding = list[float]


def similarity(
    embedding1: Embedding,
    embedding2: Embedding,
    mode: SimilarityMode = SimilarityMode.COSINE,
) -> float:
    """
    Calculate similarity between two embeddings.

    Args:
        embedding1: First embedding vector
        embedding2: Second embedding vector
        mode: Similarity calculation mode (cosine, dot_product, or euclidean)
    """
    # Validate embeddings are not empty
    if len(embedding1) == 0 or len(embedding2) == 0:
        raise ValueError("Embeddings cannot be empty")

    # Validate embeddings have same dimension
    if len(embedding1) != len(embedding2):
        raise ValueError(
            f"Embeddings must have same dimension. "
            f"Got {len(embedding1)} and {len(embedding2)}"
        )

    if mode == SimilarityMode.EUCLIDEAN:
        return -float(np.linalg.norm(np.array(embedding1) - np.array(embedding2)))

    elif mode == SimilarityMode.DOT_PRODUCT:
        return float(np.dot(embedding1, embedding2))

    else:
        return float(cosine_similarity(embedding1, embedding2))


class BaseEmbedding(BaseModel, TransformerComponent):
    """
    Abstract base class defining the interface for embedding models.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="forbid",
    )

    model_name: Optional[str] = Field(
        default=None,
        description="Name of the embedding model"
    )


    @classmethod
    def class_name(cls) -> str:
        return "BaseEmbedding"

    @abstractmethod
    def embed_text(
        self, input: str | list[str]
    ) -> list[Embedding]:
        """
        Embed one or more text strings.

        Args:
            input: Single text string or list of text strings to embed
        """

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
