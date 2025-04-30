from crewai import Task
from agents.itinerary_agent import itinerary_agent

itinerary_task = Task(
    description='Plan a 5-day San franscisco itinerary including local transport and weather-aware tips.',
    expected_output='Daily schedule with activities, links, and travel suggestions.',
    agent=itinerary_agent
)
