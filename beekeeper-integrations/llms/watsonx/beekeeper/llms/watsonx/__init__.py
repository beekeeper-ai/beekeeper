from beekeeper.llms.watsonx.base import WatsonxLLM
import warnings

warnings.warn(
    "The 'beekeeper.llms' package has been moved to 'novastack.llms.watsonx'. "
    "Please update your imports to use 'novastack.llms.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["WatsonxLLM"]
