from agents import Agent
from openai_assignment.config import model
from openai_assignment.agents.escalation_agent import EscalationAgent
from openai_assignment.agents.injury_support_agent import InjurySupportAgent
from openai_assignment.agents.nutrition_expert_agent import NutritionExpertAgent

TriageAgent = Agent(
    name="TriageAgent",
    instructions="""
You are the triage agent for a health & wellness system.

Your job:
- Understand the user's request
- If it's related to:
    - Human coach → handoff to EscalationAgent
    - Diabetes / allergies → handoff to NutritionExpertAgent
    - Injuries / pain → handoff to InjurySupportAgent
- Otherwise, give a friendly welcome and basic info.
""",
    handoffs=[
        EscalationAgent,
        NutritionExpertAgent,
        InjurySupportAgent,
    ],
    model=model,
)