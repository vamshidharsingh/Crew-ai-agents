from crewai import Crew
from tasks.recommendation_task import recommendation_task
from tasks.booking_task import booking_task
from tasks.itinerary_task import itinerary_task
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")






crew = Crew(
    agents=[
        recommendation_task.agent,
        booking_task.agent,
        itinerary_task.agent
    ],
    tasks=[
        recommendation_task,
        booking_task,
        itinerary_task
    ],
    verbose=True
)

crew.kickoff()

