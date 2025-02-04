
from crewai import Crew,Process
from Task import research_task,write_task
from Agent import News,researcher
from langchain_groq import ChatGroq
from crewai import Agent, LLM
import os 
from dotenv import load_dotenv

load_dotenv()
Gorq_Api = os.getenv('GORQ_API_KEY')
Google_Api = os.getenv('')

llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7
)




# Assemble your crew with planning capabilities
my_crew = Crew(
    agents=[News,researcher],
    tasks=[research_task,write_task],
    process=Process.sequential,
    #planning=True,
    #planning_llm=llm
)


result = my_crew.kickoff(inputs={'topic':'Discuss the growth of quantum computing might reshape cybersecurity practices and policies'})
print(result)