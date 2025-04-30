from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# Define the tool using crewai's tool decorator
@tool
def search_booking(query: str) -> str:
    """Search the web for booking information and availability."""
    search = DuckDuckGoSearchRun()
    return search.run(query)

# Create the agent with the properly formatted tool
booking_agent = Agent(
    role='Travel Booking Specialist',
    goal='Find and book the best travel deals for flights and accommodations',
    backstory='Expert at finding discounts and handling all booking arrangements.',
    tools=[search_booking],
    verbose=True
)