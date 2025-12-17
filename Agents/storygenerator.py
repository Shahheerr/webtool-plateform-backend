from agents import Agent, Runner
from config.gemini_config import gemini_config


story_generator_agent = Agent(
    name="Story Generator",
    instructions="You're a Story Generator Agent.",
)

res = Runner.run_sync(story_generator_agent, "Write a story about a person who discovers they have the power to time travel.\nStory should be 500 words long.\nStory should be interesting and engaging.", run_config=gemini_config)