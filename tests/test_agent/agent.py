from __future__ import annotations

from google.adk import Agent

root_agent = Agent(
    name="root",
    model="gemini-2.5-flash",
    instruction="You are a concise test agent. Reply with one sentence.",
)
