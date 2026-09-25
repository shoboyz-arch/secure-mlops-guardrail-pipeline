from pydantic import BaseModel, Field, field_validator
import re

INJECTION_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"system override",
    r"you are now an unfiltered ai",
    r"<script>",
    r"drop table"
]

class InferenceRequest(BaseModel):
    user_id: str = Field(..., min_length=3, max_length=50)
    query: str = Field(..., min_length=5, max_length=500)
    max_tokens: int = Field(default=128, ge=16, le=512)

    @field_validator("query")
    def guardrail_injection_check(cls, value: str) -> str:
        clean_text = value.strip()
        for pattern in INJECTION_PATTERNS:
            if re.search(pattern, clean_text, re.IGNORECASE):
                raise ValueError(f"Security Alert: Blocked pattern detected: '{pattern}'")
        return clean_text

class InferenceResponse(BaseModel):
    status: str
    prediction: str
    confidence: float
    model_version: str
