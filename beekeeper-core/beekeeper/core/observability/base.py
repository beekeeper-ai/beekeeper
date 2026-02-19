from abc import ABC, abstractmethod

from beekeeper.core.observability.types import PayloadRecord
from beekeeper.core.prompts import PromptTemplate


class BaseObservability(ABC):
    """Abstract base class defining the interface for observability."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseObservability"


class PromptObservability(BaseObservability):
    """Abstract base class defining the interface for prompt observability."""

    def __init__(self, prompt_template: PromptTemplate | None = None) -> None:
        self.prompt_template = PromptTemplate.from_value(prompt_template)

    @classmethod
    def class_name(cls) -> str:
        return "PromptObservability"

    @abstractmethod
    def __call__(self, payload: PayloadRecord) -> None:
        """PromptObservability."""
