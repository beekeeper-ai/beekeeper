from typing import Any

from pydantic import BaseModel, Field


class GuardrailResponse(BaseModel):
    """Guardrail response."""

    text: str = Field(..., description="Generated text response")
    action: str | None = Field(
        default=None, description="Action taken by the guardrail"
    )
    raw: Any | None = Field(default=None)
