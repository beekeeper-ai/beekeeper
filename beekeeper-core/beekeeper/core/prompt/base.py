from __future__ import annotations

from beekeeper.core.prompt.utils import SafeFormatter
from pydantic import BaseModel


class PromptTemplate(BaseModel):
    """
    Prompt Template.

    Attributes:
        template (str): Prompt template string.

    Example:
        ```python
        from beekeeper.core.prompt import PromptTemplate

        PromptTemplate("Summarize the following text: {input_text}")
        ```
    """

    template: str

    def __init__(self, template: str):
        super().__init__(template=template)

    @classmethod
    def from_value(cls, value: str | PromptTemplate | None) -> PromptTemplate | None:
        if value is None:
            return None

        if isinstance(value, cls):
            return value

        if isinstance(value, str):
            return cls(value)

        raise TypeError(
            f"Invalid type for parameter 'template'. Expected str or PromptTemplate, but received {type(value).__name__}."
        )

    def format(self, **kwargs):
        """
        Formats the template using the provided dynamic variables.
        Missing variables are left as placeholders.
        """
        return self.template.format_map(SafeFormatter(**kwargs))
