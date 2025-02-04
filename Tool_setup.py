from crewai import Agent
import os 
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

internet_search = SerperDevTool()
