"""
Standardized Pydantic Schemas for Agent Request/Response.
Follows strict schema to prevent hallucination and ensure consistency.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
import uuid


class ModelSettingsSchema(BaseModel):
    """Model settings that can be passed from frontend."""
    temperature: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=2.0,
        description="Controls randomness: 0.0 = deterministic, 2.0 = very random"
    )
    top_p: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Nucleus sampling: controls diversity of output"
    )
    max_tokens: Optional[int] = Field(
        default=None,
        gt=0,
        description="Maximum number of tokens to generate"
    )


class AgentRequest(BaseModel):
    """
    Standardized input schema for all agent endpoints.
    Prevents hallucination by enforcing strict structure.
    """
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=50000,
        description="The user's input prompt for the agent"
    )
    settings: Optional[ModelSettingsSchema] = Field(
        default=None,
        description="Optional model settings to override defaults"
    )
    user_context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional additional context for the agent"
    )


class UsageInfo(BaseModel):
    """Token usage information from the model."""
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None


class AgentResponse(BaseModel):
    """
    Standardized output schema for all agent endpoints.
    Ensures clean JSON output without meta-talk or debugging strings.
    """
    status: str = Field(
        default="success",
        description="Status of the request: 'success' or 'error'"
    )
    agent_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique identifier for this agent execution"
    )
    content: str = Field(
        ...,
        description="The AI's response content - ONLY the generated text, no meta information"
    )
    usage: Optional[UsageInfo] = Field(
        default=None,
        description="Token usage statistics"
    )


class ErrorResponse(BaseModel):
    """
    Standardized error response schema.
    Clean JSON error without exposing internal details.
    """
    status: str = Field(
        default="error",
        description="Always 'error' for error responses"
    )
    message: str = Field(
        ...,
        description="Human-readable error message"
    )
    agent_id: Optional[str] = Field(
        default=None,
        description="Agent ID if available"
    )
