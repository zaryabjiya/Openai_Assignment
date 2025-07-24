# 🏋️ Health & Wellness Planner Agent

A full-featured AI assistant powered by the OpenAI Agents SDK and Gemini API, designed for:

- ✅ Personalized **7-day meal planning**
- ✅ Goal analysis, workout recommendations, and check-in scheduling
- ✅ Multi-turn memory & real-time streaming UI via Streamlit
- ✅ Intelligent **handoffs** to specialized agents (nutrition, injury support, human escalation)

---

## 📂 Project Structure

```text
src/
├── health_wellness_agent/
│   ├── main.py                  # Streamlit entry‑point
│   ├── agent.py                 # Main agent & optional triage setup
│   ├── config.py                # API key & model config
│   ├── context.py               # UserSessionContext definition
│   ├── utils/
│   │   └── streaming.py         # Real-time response streaming logic
│   └── tools/
│       ├── goal_analyzer.py
│       ├── meal_planner.py
│       ├── progress_tracker.py
│       ├── workout_recommender.py
│       └── scheduler.py
└── agents/
    ├── escalation_agent.py
    ├── nutrition_expert_agent.py
    └── injury_support_agent.py

---
```
1. **Clone the repository:**

```bash
git clone https://github.com/Maheen-Zubair/Health-Wellness-Agent.git
cd Health-Wellness-Agent
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your API key** to `src/health_wellness_agent/config.py`:

```python
model = {
    "type": "gemini",
    "api_key": "YOUR_GEMINI_API_KEY"
}
```

---

## 🚀 Running the App

Start the Streamlit interface:

```bash
streamlit run src/health_wellness_agent/main.py
```

⛔️ **Important:** Don’t use `python main.py` or `uv run main.py`—Streamlit requires its runner.

---

## 💬 How to Use

1. Open your browser via Streamlit.
2. Type in your health goal or question (e.g., “I want to lose 5kg in 2 months”).
3. The agent:

   * Streams the response live.
   * Uses context tools for planning or tracking.
   * Hands off to a specialized agent if needed.

### 🧐 Example Inputs:

* Meal Plan: `I have diabetes and need a meal plan.`
* Escalation: `I need to talk to a real health coach.`
* Injury: `I hurt my knee; recommend safe workouts.`

---

## 🛠️ Tools Overview

| Tool Name                  | Description                                       |
| -------------------------- | ------------------------------------------------- |
| **GoalAnalyzerTool**       | Parses natural goals into structured action plans |
| **MealPlannerTool**        | Generates 7-day meal recommendations              |
| **WorkoutRecommenderTool** | Suggests workouts based on your fitness goals     |
| **ProgressTrackerTool**    | Logs results and updates session context          |
| **CheckinSchedulerTool**   | Automatically schedules weekly check-ins          |

---

## 🚦 Handoff Agents

When the user requests or needs specialized help, the system hands off to:

* **EscalationAgent** – Connects to a real coach
* **NutritionExpertAgent** – Handles medical or serious dietary needs
* **InjurySupportAgent** – Provides guidance for safe workouts

Use input triggers like:

* “I don’t trust AI...” → `EscalationAgent`
* “I have diabetes or allergy...” → `NutritionExpertAgent`
* “I have knee/back pain...” → `InjurySupportAgent`

---

## 🧐 Architecture & Flow

1. **User Input** → Main Agent (`health_wellness_agent`)
2. The agent **checks triggers** for handoffs
3. If needed, control passes to a **specialized agent**
4. Otherwise, responds using one of the tools
5. **Streaming response** shows live typing via `stream_agent_response()`
6. **Context** and **chat history** are updated dynamically


---

## 📌 Developer Tips

* **Modify Tools:** Create new Python files under `tools/` and add to `main.py`
* **Add Agents:** Define in `agents/` and add to `TriageAgent` inside `agent.py`
* **Logging:** Enabled in `streaming.py` (console output) — extend for file logs if needed
* **Context Memory:** Found in `context.py` — store user progress as needed


---

## 📜 License & Credits

* Developed by **Zaryab Irfan**
* Built with ❤️ using **OpenAI Agents SDK**, **Gemini API**, **Streamlit**

---

Enjoy your intelligent wellness assistant! 😊
Feel free to open issues or submit a PR for improvements.