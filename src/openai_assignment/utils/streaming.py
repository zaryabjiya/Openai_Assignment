import asyncio
import streamlit as st

from agents import Agent, Runner
from openai_assignment.config import config

async def stream_agent_response(agent: Agent, user_input: str, context, chat_history):
    """
    Runs the agent in streaming mode and updates UI output in real-time.
    """
    # Use last 4 messages to preserve context
    past = "\n".join([f"{r}: {m}" for r, m in chat_history[-4:]])
    enriched_input = f"{past}\nUser: {user_input}"

    result = Runner.run_streamed(
        starting_agent=agent,
        input=enriched_input,
        context=context,
        run_config=config,
    )

    full_output = ""
    placeholder = st.empty()

    async for event in result.stream_events():
        delta = getattr(getattr(event, "data", {}), "delta", None)
        if delta:
            full_output += delta
            placeholder.markdown(full_output)
            await asyncio.sleep(0.01)

    return full_output