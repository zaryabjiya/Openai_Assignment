from agents.tool import function_tool
from agents import RunContextWrapper
from ..context import UserSessionContext

@function_tool("CheckinSchedulerTool")
async def schedule_checkins(
    context: RunContextWrapper[UserSessionContext],
) -> dict:
    """
    Schedules recurring weekly progress check-ins based on user's goal duration.
    """

    goal = context.context.goal
    checkin_schedule = {
        "frequency": "weekly",
        "total_checkins": 4,  
        "notes": "No goal found, using default 1 month (4 weeks)."
    }

    if goal:
        try:
            duration_text = goal.duration.lower()
            if "month" in duration_text:
                weeks = int(duration_text.split()[0]) * 4
            elif "week" in duration_text:
                weeks = int(duration_text.split()[0])
            else:
                weeks = 4 

            checkin_schedule = {
                "frequency": "weekly",
                "total_checkins": weeks,
                "notes": f"Scheduled {weeks} weekly check-ins based on your goal duration."
            }

        except Exception as e:
            checkin_schedule["notes"] = f"Error parsing duration: {e}"

    context.context.progress_logs.append({"checkin_schedule": checkin_schedule})

    return checkin_schedule