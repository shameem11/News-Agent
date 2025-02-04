from langchain_groq import ChatGroq
from crewai import Agent
import os 
from dotenv import load_dotenv
from Tool_setup import internet_search
from crewai import Agent, LLM
# Load environment variables from .env file
load_dotenv()
Gorq_Api = os.getenv('GORQ_API_KEY')
Google_Api = os.getenv('GOOGLE_API_KEY')

# Initialize the model

llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7,
    api_key=Google_Api
)

# Senior Market Research Analyst Agent
researcher = Agent(
    role="Senior Market Research Analyst",
    goal=(
        "Deliver actionable, data-driven insights into the AI industry by analyzing market trends, "
        "competitor strategies, and emerging technologies in {topic}."
    ),
    backstory=(
        "An experienced market research analyst with over a decade in the tech industry, specializing in AI sector trends, "
        "competitive intelligence, and future market opportunities. "
        "Renowned for delivering deep, data-driven insights that help businesses make informed strategic decisions. "
        "Highly skilled in synthesizing complex data into clear, actionable recommendations, making you a trusted advisor to top executives."
    ),
    verbose=True,
    tools=[internet_search],
    llm=llm,
    allow_delegation=True
)


# Content Writer Agent
News = Agent(  # Changed from `News = writer`
    role="Content Writer",
    goal="Generate high-quality, engaging, and well-researched news content topics in {topic}",
    verbose=True,
    backstory=("A skilled writer with expertise in AI, technology, and market trends, capable of crafting insightful articles, blog posts, and reports"),
    llm=llm,
    memory=True,
    allow_delegation=True,
    tools=[internet_search]    
)
