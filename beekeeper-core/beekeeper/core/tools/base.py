import re
from abc import ABC, abstractmethod
from typing import Any, Literal

from beekeeper.core.bridge.pydantic import BaseModel, field_validator


class ToolInputSchema(BaseModel):
    """Tool input schema."""

    description: str
    input_type: Literal["integer", "string"]

    def to_dict(self) -> dict[str, Any]:
        self.dict()


class BaseTool(ABC, BaseModel):
    """Abstract base class defining the interface for tools."""

    name: str
    description: str
    input_schema: dict[str, ToolInputSchema]

    @field_validator("name")
    def _validate_name(cls, v):
        if not re.match(r"^[A-Za-z0-9_]+$", v):
            raise ValueError(
                "Invalid name: only letters, digits, and underscores are allowed. No spaces or special characters.",
            )
        return v

    @classmethod
    def class_name(cls) -> str:
        return "BaseTool"

    @abstractmethod
    def run(self, tool_input) -> Any:
        """Run the tool."""
