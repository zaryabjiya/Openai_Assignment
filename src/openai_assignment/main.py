import streamlit as st
import asyncio

from agents import Agent
from health_wellness_agent.context import UserSessionContext
from health_wellness_agent.tools.meal_planner import meal_planner
from health_wellness_agent.tools.tracker import update_progress
from health_wellness_agent.tools.goal_analyzer import analyze_goal
from health_wellness_agent.tools.workout_recommender import recommend_workout
from health_wellness_agent.tools.scheduler import schedule_checkins
from health_wellness_agent.config import model
from health_wellness_agent.utils.streaming import stream_agent_response  
from health_wellness_agent.agent import TriageAgent

agent = Agent(
    name="health_wellness_agent",
    instructions="""
You are a helpful health & wellness planner agent.
You are having an ongoing multi-turn conversation.
Use the past user and agent messages provided in the input to maintain memory and consistency.

Guidelines for every response:
- Provide answers in bullet points or numbered lists when appropriate.
- Always avoid repeating the same message.
- Use clean and simple formatting.
- Never return empty brackets or unnecessary data like {}.
- If user asks for a plan (e.g., 7-day meal plan), give it in a neat day-wise format.

**Use handoff() when appropriate**, for example:
- If the user mentions injury or pain → hand off to InjurySupportAgent
- If the user requests human help or says "I want to talk to someone" → hand off to EscalationAgent
- If the user has dietary conditions like diabetes or allergies → hand off to NutritionExpertAgent
""",
    tools=[
        meal_planner,
        update_progress,
        analyze_goal,
        recommend_workout,
        schedule_checkins,
    ],
    handoffs=[TriageAgent],
    model=model,
)

if "context" not in st.session_state:
    st.session_state.context = UserSessionContext(name="Maheen", uid=101)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

st.set_page_config(page_title="🏋️ Health & Wellness Agent", layout="wide")
st.title("Health & Wellness Planner Agent")

for role, message in st.session_state.chat_history:
    with st.chat_message(role.lower()):
        st.markdown(message)

user_input = st.chat_input("Ask your wellness agent anything...", key="main_input_box")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("User", user_input))

    with st.chat_message("assistant"):
        with st.spinner("🤖 Agent is responding..."):
            try:
                final_output = asyncio.run(stream_agent_response(
                    agent,
                    user_input,
                    st.session_state.context,
                    st.session_state.chat_history,
                ))
            except Exception as e:
                final_output = f"❌ Error: {str(e)}"

    st.session_state.chat_history.append(("Agent", final_output))

# ----- Sidebar -----
with st.sidebar:
    st.header("🛠️ Tools Included")
    st.markdown("""
- **🧠 GoalAnalyzerTool** – Structures user goals  
- **🍽️ MealPlannerTool** – Personalized 7-day plans  
- **🏋️ WorkoutRecommenderTool** – Custom workout suggestions  
- **📅 CheckinSchedulerTool** – Sets weekly check-ins  
- **📈 ProgressTrackerTool** – Tracks and updates progress  
    """)
   