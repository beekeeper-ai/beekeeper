from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseGuardrail(ABC):
    """Abstract base class defining the interface for LLMs."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseGuardrail"

    @abstractmethod
    def enforce(self, text: str,  direction: str) -> Dict:
        """Runs policies enforcement to specified guardrail."""
