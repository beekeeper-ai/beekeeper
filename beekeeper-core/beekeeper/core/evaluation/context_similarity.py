import numpy as np
from beekeeper.core.bridge.pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)
from beekeeper.core.embeddings import BaseEmbedding, SimilarityMode


class ContextSimilarityEvaluator(BaseModel):
    """
    Measures how much context has contributed to the answer's.
    A higher value suggests a greater proportion of the context is present in the LLM's response.

    Attributes:
        embed_model (BaseEmbedding): The embedding model used to compute vector representations.
        similarity_mode (SimilarityMode, optional): Similarity strategy to use. Supported options are
            `"cosine"`, `"dot_product"`, and `"euclidean"`. Defaults to `"cosine"`.
        similarity_threshold (float, optional): Embedding similarity threshold for determining
            whether a context segment "passes". Must be between 0.0 and 1.0. Defaults to `0.8`.

    Example:
        ```python
        from beekeeper.core.evaluation import ContextSimilarityEvaluator
        from beekeeper.embedding.huggingface import HuggingFaceEmbedding

        embedding = HuggingFaceEmbedding()
        ctx_sim_evaluator = ContextSimilarityEvaluator(embed_model=embedding)
        ```
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    embed_model: BaseEmbedding = Field(
        description="Embedding model used to compute vector representations"
    )
    similarity_mode: SimilarityMode = Field(
        default=SimilarityMode.COSINE,
        description="Similarity strategy to use",
    )
    similarity_threshold: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Similarity threshold for determining if a context 'passes'",
    )

    @field_validator("similarity_threshold")
    @classmethod
    def _validate_threshold(cls, v: float) -> float:
        """Validate that threshold is within valid range."""
        if not 0.0 <= v <= 1.0:
            raise ValueError(
                f"similarity_threshold must be between 0.0 and 1.0, got: {v}"
            )
        return v

    def evaluate(self, contexts: list[str], generated_text: str) -> dict:
        """
        Evaluate similarity between provided contexts and generated text.

        Args:
            contexts (list[str]): List of contexts used to generate LLM response.
            generated_text (str): LLM response based on given context.

        Example:
            ```python
            evaluation_result = ctx_sim_evaluator.evaluate(
                contexts=["context 1", "context 2"],
                generated_text="<candidate>"
            )
            print(f"Score: {evaluation_result['score']}")
            print(f"Passing: {evaluation_result['passing']}")
            ```
        """
        if not contexts or not generated_text:
            raise ValueError(
                "Must provide these parameters [`contexts`, `generated_text`]",
            )

        contexts_score: list[float] = []
        candidate_embedding = self.embed_model.embed_text(generated_text)[0]

        for context in contexts:
            if not context or not context.strip():
                continue

            context_embedding = self.embed_model.embed_text(context)[0]
            similarity_score = self.embed_model.similarity(
                candidate_embedding,
                context_embedding,
                mode=self.similarity_mode,
            )
            contexts_score.append(similarity_score)

        if not contexts_score:
            raise ValueError("No valid contexts provided for evaluation")

        mean_score = float(np.mean(contexts_score))
        passing = mean_score >= self.similarity_threshold

        return {
            "contexts_score": contexts_score,
            "score": mean_score,
            "passing": passing,
        }
