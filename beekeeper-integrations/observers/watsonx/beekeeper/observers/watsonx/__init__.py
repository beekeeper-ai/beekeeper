import warnings

warnings.warn(
    "The 'beekeeper.observers.watsonx' package has been moved to 'beekeeper.observability.watsonx'. "
    "Please update your imports to use 'beekeeper.observability.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

from beekeeper.observers.watsonx.base import (
    CloudPakforDataCredentials,
    IntegratedSystemCredentials,
    WatsonxCustomMetric,
    WatsonxExternalPromptObserver,
    WatsonxLocalMetric,
    WatsonxMetric,
    WatsonxMetricThreshold,
    WatsonxPromptObserver,
)

__all__ = [
    "CloudPakforDataCredentials",
    "IntegratedSystemCredentials",
    "WatsonxExternalPromptObserver",
    "WatsonxPromptObserver",
    "WatsonxLocalMetric",
    "WatsonxMetricThreshold",
    "WatsonxMetric",
    "WatsonxCustomMetric",
]
