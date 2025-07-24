from agents.tool import function_tool
from agents import RunContextWrapper
from ..context import UserSessionContext

@function_tool("ProgressTrackerTool")
async def update_progress(
    context: RunContextWrapper[UserSessionContext],
    user_input: str,
) -> str:
    """
    Accepts updates and logs user progress in the context
    """
    ctx = context.context
    progress_entry = {
        "update": user_input
    }

    ctx.progress_logs.append(progress_entry)
    return "Your progress has been logged successfully."