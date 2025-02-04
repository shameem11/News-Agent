
from crewai import Crew,Process
from Task import research_task,write_task
from Agent import News,researcher
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

load_dotenv()
Gorq_Api = os.getenv('GORQ_API_KEY')

Model = ChatGroq(
    api_key=Gorq_Api,
    model='deepseek-r1-distill-llama-70b',
    temperature=0.5,
    verbose=None
)




# Assemble your crew with planning capabilities
my_crew = Crew(
    agents=[News,researcher],
    tasks=[research_task,write_task],
    process=Process.sequential,
    #planning=True,
    #planning_llm=Model
)


result = my_crew.kickoff(inputs={'topic':'Discuss how the growth of quantum computing might reshape cybersecurity practices and policies'})
print(result)