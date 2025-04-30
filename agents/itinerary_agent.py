from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# Define the tool using crewai's tool decorator
@tool
def search_itinerary(query: str) -> str:
    """Search the web for activities and itinerary planning information."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

# Create the agent with the properly formatted tool
itinerary_agent = Agent(
    role='Itinerary Planner',
    goal='Create detailed day-by-day travel plans with activities',
    backstory='Experienced travel guide with knowledge of attractions worldwide.',
    tools=[search_itinerary],
    verbose=True
)