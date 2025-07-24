from agents import Agent
from openai_assignment.config import model

InjurySupportAgent = Agent(
    name="InjurySupportAgent",
    instructions="""
You provide workout and recovery suggestions based on physical injuries or limitations.
Always consider the user's pain or constraints while recommending workouts.
""",
    model=model,
)