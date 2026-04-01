import warnings

warnings.warn(
    "The 'beekeeper.monitors.watsonx' package has been moved to 'beekeeper.observability.watsonx'. "
    "Please update your imports to use 'beekeeper.observability.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

from beekeeper.monitors.watsonx.base import (
    WatsonxExternalPromptMonitor,
    WatsonxPromptMonitor,
)
from beekeeper.monitors.watsonx.custom_metric import (
    WatsonxCustomMetric,
    WatsonxCustomMetricsManager,
)
from beekeeper.monitors.watsonx.supporting_classes.credentials import (
    CloudPakforDataCredentials,
    IntegratedSystemCredentials,
)
from beekeeper.monitors.watsonx.supporting_classes.metric import (
    WatsonxLocalMetric,
    WatsonxMetric,
    WatsonxMetricThreshold,
)

__all__ = [
    "CloudPakforDataCredentials",
    "IntegratedSystemCredentials",
    "WatsonxCustomMetric",
    "WatsonxExternalPromptMonitor",
    "WatsonxLocalMetric",
    "WatsonxCustomMetricsManager",
    "WatsonxMetric",
    "WatsonxMetricThreshold",
    "WatsonxPromptMonitor",
]
