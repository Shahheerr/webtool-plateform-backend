"""
Gemini Configuration Module
Initializes Gemini API client and model using environment variables.
"""
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables (override system env vars with .env file)
load_dotenv(override=True)

# Get credentials from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAklVj4ZPRDYUUjbKbFAQ4ZEglMWGGNykM")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set!")

# Initialize Gemini client
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL,
)

# Initialize Gemini model
gemini_model = OpenAIChatCompletionsModel(
    model=GEMINI_MODEL_NAME,
    openai_client=gemini_client
)

# Default run configuration
gemini_config = RunConfig(
    model_provider=gemini_client,
    model=gemini_model,
    tracing_disabled=True
)