from crewai import Agent
import os 
from dotenv import load_dotenv

load_dotenv()

serper = os.getenv('SERPER')