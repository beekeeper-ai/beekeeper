from pydantic import BaseModel


class PayloadRecord(BaseModel):
    """Payload record."""

    system_prompt: str | None = None
    input_text: str | None = None
    prompt_variables: list[str] | None = None
    prompt_variable_values: dict[str, str] | None = None
    generated_text: str

    input_token_count: int
    generated_token_count: int
    response_time: int
