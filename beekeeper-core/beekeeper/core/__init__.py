import warnings

warnings.warn(
    "The 'beekeeper.core' package has been moved to 'novastack.core'. "
    "Please update your imports to use 'novastack.core' instead. "
    "This package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)
