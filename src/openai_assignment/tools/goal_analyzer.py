from agents.tool import function_tool
from agents import RunContextWrapper, Agent, Runner
from ..context import UserSessionContext
import json
from agents import Agent, Runner
from ..config import model, config
from ..guardrails import goal_analyzer,goal_output_guardrail,GoalOutput

@function_tool("GoalAnalyzerTool")
async def analyze_goal(
    context: RunContextWrapper[UserSessionContext],
    goal_text: str
) -> dict:
    """
    Parses user goal like "I want to lose 5kg in 2 months" into structured format.
    """

    agent = Agent(
        name="Goal Parser Agent",
        instructions="Validate goal input format: quantity, metric, duration (e.g. ‘lose 5kg in 2 months’). Return it in JSON format.",
        model=model,
        input_guardrails=[goal_analyzer],
        output_guardrails=[goal_output_guardrail],
        output_type=GoalOutput,        
    )

    result = await Runner.run(agent, goal_text, context=context.context, run_config=config)
    print(f"💬 Agent raw output: {result.final_output}")

    try:
        parsed_goal = json.loads(result.final_output)
    except Exception:
        parsed_goal = result.final_output  # fallback if it's already a dict

    context.context.goal = parsed_goal

    print(f"this is goal_analyzer:: --{parsed_goal}")
    return parsed_goal
