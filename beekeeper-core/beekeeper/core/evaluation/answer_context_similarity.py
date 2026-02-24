from typing import Any

import numpy as np
from beekeeper.core.bridge.pydantic import (
    ConfigDict,
    Field,
)
from beekeeper.core.embeddings import BaseEmbedding, SimilarityMode
from beekeeper.core.evaluation.base import BaseEvaluator


class AnswerContextSimilarityEvaluator(BaseEvaluator):
    """
    Measures how much context are related to the given answer.
    A higher value suggests a greater proportion of the context is present in the LLM's response.

    Attributes:
        embed_model (BaseEmbedding): The embedding model used to compute vector representations.
        similarity_mode (SimilarityMode, optional): Similarity strategy to use. Supported options are
            `"cosine"`, `"dot_product"`, and `"euclidean"`. Defaults to `"cosine"`.
        score_threshold (float, optional): Determining whether a context segment "passes". Must be between 0.0 and 1.0. Defaults to `0.8`.

    Example:
        ```python
        from beekeeper.core.evaluation import AnswerContextSimilarityEvaluator
        from beekeeper.embedding.huggingface import HuggingFaceEmbedding

        embedding = HuggingFaceEmbedding()
        answer_ctx_evaluator = AnswerContextSimilarityEvaluator(embed_model=embedding)
        ```
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    embed_model: BaseEmbedding = Field(
        description="Embedding model used to compute vector representations"
    )
    similarity_mode: SimilarityMode = Field(
        default=SimilarityMode.COSINE,
        description="Similarity computation method",
    )

    def evaluate(
        self,
        query: str | None = None,
        generated_text: str | None = None,
        contexts: list[str] | None = None,
        **kwargs: Any,
    ) -> dict:
        """
        Evaluate the given inputs and return evaluation results.

        Args:
            generated_text (str): LLM response based on given context.
            contexts (list[str]): List of contexts used to generate LLM response.

        Example:
            ```python
            evaluation_result = answer_ctx_evaluator.evaluate(
                contexts=["context 1", "context 2"],
                generated_text="The capital of France is Paris.",
            )
            print(f"Score: {evaluation_result['score']}")
            print(f"Passing: {evaluation_result['passing']}")
            ```
        """
        del query  # Unused
        del kwargs  # Unused

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
            score = self.embed_model.similarity(
                candidate_embedding,
                context_embedding,
                mode=self.similarity_mode,
            )
            contexts_score.append(score)

        if not contexts_score:
            raise ValueError("Unable to evaluate: no valid contexts provided")

        mean_score = float(np.mean(contexts_score))
        passing = mean_score >= self.score_threshold

        return {
            "contexts_score": contexts_score,
            "score": mean_score,
            "passing": passing,
        }
