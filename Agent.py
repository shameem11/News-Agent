from langchain_groq import ChatGroq
from crewai import Agent
import os 
from dotenv import load_dotenv
from Tool_setup import internet_search

# Load environment variables from .env file
load_dotenv()
Gorq_Api = os.getenv('GORQ_API_KEY')

# Initialize the model
Model = ChatGroq(
    api_key=Gorq_Api,
    model='deepseek-r1-distill-llama-70b',
    temperature=0.5,
    verbose=None
)

# Senior Market Research Analyst Agent
researcher = Agent(
    role='Senior Market Research Analyst',
    goal='Deliver actionable, data-driven insights into the AI industry by analyzing market trends, competitor strategies, and emerging technologies in {topic}',
    backstory=('''
        You are a seasoned market research analyst with over a decade of experience in the tech industry. 
        Your expertise lies in identifying market trends, analyzing competitor strategies, and predicting future opportunities in the AI sector. 
        You have a proven track record of helping companies make informed decisions by providing deep, data-driven insights. 
        Your ability to synthesize complex data into clear, actionable recommendations has made you a trusted advisor to top executives.
    '''),
    verbose=True,
    tools=[internet_search],
    llm=Model,
    allow_delegation=True
)

# Content Writer Agent
News = Agent(  # Changed from `News = writer`
    role="Content Writer",
    goal="Generate high-quality, engaging, and well-researched news content topics in {topic}",
    verbose=True,
    backstory=("A skilled writer with expertise in AI, technology, and market trends, capable of crafting insightful articles, blog posts, and reports"),
    llm=Model,
    memory=True,
    allow_delegation=True,
    tools=[internet_search]    
)
