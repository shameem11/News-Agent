from crewai import Agent
import os 
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()

serper = os.getenv('SERPER')
tool = SerperDevTool()

