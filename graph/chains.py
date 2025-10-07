from graph.prompts import prompt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(model="gpt-4o", temperature=0)

ai_chain = prompt | llm | StrOutputParser()