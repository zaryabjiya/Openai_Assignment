from typing import List
from agents.tool import function_tool
from agents import RunContextWrapper
from ..context import UserSessionContext

@function_tool("MealPlannerTool")
async def meal_planner(
    context: RunContextWrapper[UserSessionContext],
) -> List[str]:
    """
    Async tool to suggest a 7-day meal plan honoring dietary preferences
    stored in context.diet_preferences. Saves the plan in context.meal_plan.

    
    """
    ctx = context.context 

    pref = (ctx.diet_preferences or "").lower()

    if pref == "vegetarian":
        plan = [
            "Day 1: Vegetable Stir Fry with Tofu",
            "Day 2: Chickpea Salad with Lemon Dressing",
            "Day 3: Lentil Soup with Whole Grain Bread",
            "Day 4: Grilled Paneer with Quinoa",
            "Day 5: Spinach & Mushroom Pasta",
            "Day 6: Baked Sweet Potato & Black Beans",
            "Day 7: Vegetable Biryani with Cucumber Raita"
        ]
    else:
        plan = [
            "Day 1: Oatmeal with Berries",
            "Day 2: Chicken Salad with Olive Oil",
            "Day 3: Fish Curry with Brown Rice",
            "Day 4: Egg Wraps with Veggies",
            "Day 5: Bean Soup with Multigrain Bread",
            "Day 6: Chicken Stir Fry with Rice",
            "Day 7: Greek Yogurt with Nuts"
        ]

    ctx.meal_plan = plan  
    return plan