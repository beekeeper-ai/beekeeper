from abc import ABC, abstractmethod

from beekeeper.core.guardrails.types import GuardrailResponse


class BaseGuardrail(ABC):
    """
    Abstract base class defining the interface for guardrails.

    This class provides the foundation for implementing guardrail systems
    that can validate and enforce policies on text inputs and outputs.
    """

    @classmethod
    def class_name(cls) -> str:
        return "BaseGuardrail"

    @abstractmethod
    def enforce(self, text: str, direction: str) -> GuardrailResponse:
        """Run policy enforcement on the specified text."""
