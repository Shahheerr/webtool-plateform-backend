"""
Core Configuration Module
Handles environment variables and API client initialization.
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Configuration
    GEMINI_API_KEY: str = "AIzaSyAklVj4ZPRDYUUjbKbFAQ4ZEglMWGGNykM"
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    GEMINI_MODEL: str = "gemini-2.5-flash"
    
    # Server Configuration
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS Configuration
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Ignore extra env variables


@lru_cache()
def get_settings() -> Settings:
    """Cached settings instance."""
    return Settings()


# Global settings instance
settings = get_settings()


# Cached clients to avoid recreation
_gemini_client = None
_gemini_model = None


def get_gemini_client() -> AsyncOpenAI:
    """Get Gemini API client (singleton)."""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = AsyncOpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_BASE_URL,
        )
    return _gemini_client


def get_gemini_model() -> OpenAIChatCompletionsModel:
    """Get Gemini model instance (singleton)."""
    global _gemini_model
    if _gemini_model is None:
        _gemini_model = OpenAIChatCompletionsModel(
            model=settings.GEMINI_MODEL,
            openai_client=get_gemini_client()
        )
    return _gemini_model


def get_run_config() -> RunConfig:
    """Get RunConfig for agent execution."""
    return RunConfig(
        model_provider=get_gemini_client(),
        model=get_gemini_model(),
        tracing_disabled=True
    )
