from crewai import Task
from agents.recommender import recommender

recommendation_task = Task(
    description='Generate personalized travel packages for beach and culture lovers traveling in July.',
    expected_output='List of destinations, hotels, and flights in california.',
    agent=recommender
)