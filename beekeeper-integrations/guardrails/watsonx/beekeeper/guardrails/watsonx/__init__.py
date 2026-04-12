import warnings

from beekeeper.guardrails.watsonx.base import WatsonxGuardrail

warnings.warn(
    "The 'beekeeper.guardrails' package has been moved to 'novastack.guardrails.watsonx'. "
    "Please update your imports to use 'novastack.guardrails.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "WatsonxGuardrail",
]
