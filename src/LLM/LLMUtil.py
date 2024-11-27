import os
import pandas as pd
from crewai import Agent, Task, Crew, Process

from src.config import *
from src.keys import *

class LLMUtil:
	def __init__(self):
		os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
		os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'  # Adjust based on available model
		os.environ["OPENAI_API_KEY"] = api_key
		
	def llm_ask(self,receipt_list):
		# Create summarizer agent for bio
		summarizer_receipt = Agent(
			role='Summarizer',
			goal=Prompt_no_original,
			backstory=(
				"Equipped with advanced summarization techniques, "
				"the goal is to distill complex information into concise summaries."
			),
			allow_delegation=False  
		)

		# Create a task that requires code execution
		data_analysis_task = Task(  
			description='''Summarize the items recepit based on the goal. {receipt}''',
			expected_output="A concise summary of the recepit for the receipt.",
			agent=summarizer_receipt
		)


		crew = Crew(
			agents=[summarizer_receipt],
			tasks=[data_analysis_task],
			verbose=True,
			memory=False,
			respect_context_window=True  # enable by default
		)
		
		datasets = []
		for image in receipt_list:
			datasets.append({ "receipt": [image] })
		print(datasets)

		# Execute the crew
		result = crew.kickoff_for_each(inputs=datasets)
		
		return result
