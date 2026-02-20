from abc import ABC, abstractmethod
from typing import Any

from beekeeper.core.bridge.pydantic import BaseModel, ConfigDict


class BaseEvaluator(BaseModel, ABC):
    """
    Abstract base class defining the interface for evaluation metrics.

    All evaluators should inherit from this class and implement the evaluate method.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
    )

    @classmethod
    def class_name(cls) -> str:
        return "BaseEvaluator"

    @abstractmethod
    def evaluate(self, *args: Any, **kwargs: Any) -> dict:
        """
        Evaluate the given inputs and return evaluation results.

        This method should be implemented by all concrete evaluator classes.
        The specific parameters will vary depending on the evaluation type.

        Returns:
            dict: Dictionary containing evaluation results. Should include at minimum:
                - score (float): The evaluation score
                - passing (bool): Whether the evaluation passed a threshold
                Additional keys can be included for specific evaluation details.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement the evaluate() method"
        )
