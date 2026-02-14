from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    ASSISTANT = "assistant"
    SYSTEM = "system"
    USER = "user"
    TOOL = "tool"


class ChatMessage(BaseModel):
    """Chat message."""

    model_config = {"use_enum_values": True}
    role: MessageRole | str = None
    content: str | None = None

    def to_dict(self) -> dict:
        """Convert ChatMessage to dict."""
        return self.model_dump(exclude_none=True)

    @classmethod
    def from_value(cls, value: dict) -> "ChatMessage":
        if value is None:
            raise ValueError("Unexpected 'ChatMessage', cannot be None")

        if isinstance(value, cls):
            return value

        if isinstance(value, dict):
            try:
                return cls.model_validate(value)
            except Exception as e:
                raise ValueError(
                    "Unexpected 'ChatMessage' dict. Received: '{}'.".format(e)
                )

        raise TypeError(
            f"Unexpected 'ChatMessage' type. Expected dict or ChatMessage, but received {type(value).__name__}."
        )


class GenerateResponse(BaseModel):
    """Generate response."""

    text: str = Field(..., description="Generated text response")

    input_token_count: int
    generated_token_count: int
    raw: Any | None = None


class ChatResponse(BaseModel):
    """Chat completion response."""

    message: ChatMessage
    raw: Any | None = None
