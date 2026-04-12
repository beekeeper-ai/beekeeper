from beekeeper.observability.watsonx.custom_metric import (
    WatsonxCustomMetricsManager,
)
from beekeeper.observability.watsonx.external_prompt_monitor import (
    WatsonxExternalPromptMonitor,
)
from beekeeper.observability.watsonx.prompt_monitor import (
    WatsonxPromptMonitor,
)
from beekeeper.observability.watsonx.supporting_classes.credentials import (
    CloudPakforDataCredentials,
    IntegratedSystemCredentials,
)
from beekeeper.observability.watsonx.supporting_classes.metric import (
    WatsonxMetricSpec,
    WatsonxMetricThreshold,
)
import warnings

warnings.warn(
    "The 'beekeeper.observability' package has been moved to 'novastack.observability.watsonx'. "
    "Please update your imports to use 'novastack.observability.watsonx' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = [
    "CloudPakforDataCredentials",
    "IntegratedSystemCredentials",
    "WatsonxExternalPromptMonitor",
    "WatsonxCustomMetricsManager",
    "WatsonxMetricSpec",
    "WatsonxMetricThreshold",
    "WatsonxPromptMonitor",
]
