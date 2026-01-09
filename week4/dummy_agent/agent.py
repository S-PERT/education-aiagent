from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm("openai/gpt-4o")

agent = Agent(
    name="DummyAgent",
    instruction="This is a dummy agent for demonstration purposes.",
    model=MODEL,
)
