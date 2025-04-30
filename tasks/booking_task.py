from crewai import Task
from agents.booking_agent import booking_agent

booking_task = Task(
    description='Find the best deals and booking times for a trip to San francisco.',
    expected_output='Current prices with suggestions for optimal booking time.',
    agent=booking_agent
)
