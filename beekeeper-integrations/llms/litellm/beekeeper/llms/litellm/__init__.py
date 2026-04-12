import warnings

from beekeeper.llms.litellm.base import LiteLLM

warnings.warn(
    "The 'beekeeper.llms' package has been moved to 'novastack.llms.litellm'. "
    "Please update your imports to use 'novastack.llms.litellm' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["LiteLLM"]
