from graph.prompts import prompt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os

GEP_API_KEY = os.environ["GEP_API_KEY"]
GEP_API_URL = os.environ["GEP_API_URL"]

llm = ChatOpenAI(
    model="openai.gpt-4o",
    base_url=GEP_API_URL,
    api_key=GEP_API_KEY,
    temperature=0,
    max_tokens=2048
)

ai_chain = prompt | llm | StrOutputParser()