import os
from dotenv import load_dotenv
from agents import  OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig

# Load secret
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Client Setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)