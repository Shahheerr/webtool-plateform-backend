from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

gemini_api_key = "AIzaSyAyN7WL84tC0sblzA9XvzL3fW-DoHImFM0"
gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url,
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)

gemini_config = RunConfig(
    model_provider=gemini_client,
    model=gemini_model,
    tracing_disabled=True
)