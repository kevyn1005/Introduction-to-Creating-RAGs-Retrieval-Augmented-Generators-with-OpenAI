import os
from dataclasses import dataclass
from langchain_groq import ChatGroq
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

os.environ["GROQ_API_KEY"] = "Por seguridad de git quite el api Key"

SYSTEM_PROMPT = """You are an expert weather forecaster who speaks in puns.
You have access to two tools:
- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location
If a user asks for the weather, make sure you know the location."""

@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def get_user_location() -> str:
    """Retrieve user location."""
    return "Florida"

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=1000
)

checkpointer = InMemorySaver()

agent = create_react_agent(
    model=model,
    tools=[get_user_location, get_weather_for_location],
    prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer
)

config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather outside?"}]},
    config=config
)
print("Respuesta 1:")
print(response["messages"][-1].content)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Thank you!"}]},
    config=config
)
print("\nRespuesta 2:")
print(response["messages"][-1].content)