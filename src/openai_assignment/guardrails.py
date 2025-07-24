from agents import RunContextWrapper, Agent, Runner
from .context import UserSessionContext
from agents import Agent, Runner
from .config import  config
from agents import input_guardrail, GuardrailFunctionOutput, TResponseInputItem,output_guardrail
from pydantic import BaseModel

class GoalAnalyzer(BaseModel):
    is_valid_goal:bool
    resoning:str

class GoalOutput(BaseModel):
    quantity: int
    metric: str
    duration: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user’s input follows this action --user`gain or loose weight`" 
        "Return a JSON with `is_valid_goal` (true/false) and a short `reasoning`.",
    output_type=GoalAnalyzer,
)

# input guardrail
@input_guardrail
async def goal_analyzer(
    ctx: RunContextWrapper[UserSessionContext], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context, run_config = config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= not result.final_output.is_valid_goal,
    )

# Output guardrail
@output_guardrail
async def goal_output_guardrail(ctx, agent, output: GoalOutput) -> GuardrailFunctionOutput:
    is_valid = (
        isinstance(output.quantity, int) and
        isinstance(output.metric, str) and
        isinstance(output.duration, str)
    )
    return GuardrailFunctionOutput(
        output_info="Output validation successful",
        tripwire_triggered=not is_valid,
    )