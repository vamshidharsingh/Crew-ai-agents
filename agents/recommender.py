from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# Define the tool using crewai's tool decorator
@tool
def search_web(query: str) -> str:
    """Search the web for real-time travel information."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

# Create the agent with the properly formatted tool
recommender = Agent(
    role='Travel Recommender',
    goal='Suggest ideal travel options based on user preferences',
    backstory='Experienced in tailoring travel packages and accommodations.',
    tools=[search_web],
    verbose=True
)