from agents.tool import function_tool
from agents import RunContextWrapper
from ..context import UserSessionContext

@function_tool("WorkoutRecommenderTool")
async def recommend_workout(
    context: RunContextWrapper[UserSessionContext],
) -> dict:
    """
    Suggests a workout plan based on user's parsed goal.
    """

    goal = context.context.goal
    workout_plan = {
        "schedule": "Rest",
        "type": "None"
    }

    if goal:
        try:
            action = "lose"  # Default fallback
            value = goal.quantity
            unit = goal.metric
            duration = goal.duration

            # Logic based on goal
            if action == "lose":
                workout_plan = {
                    "schedule": "5 days/week: Cardio + Strength",
                    "type": "Fat Burn & Endurance",
                    "tips": f"Target to lose {value}{unit} in {duration}. Maintain consistency!"
                }

            elif action == "gain":
                workout_plan = {
                    "schedule": "4 days/week: Strength + Hypertrophy",
                    "type": "Muscle Gain",
                    "tips": f"Target to gain {value}{unit} in {duration}. Eat a high-protein diet!"
                }

        except Exception as e:
            print("⚠️ Workout plan generation failed:", e)
            return {"error": "Workout plan generation failed."}

    context.context.workout_plan = workout_plan
    return workout_plan