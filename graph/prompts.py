import datetime
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template("""
    You are helpful assistant that can answer user's questions about the meetings from the transcript.
    Use the provided project transcript to answer questions
    ---------------
    Current date is {date}
    Project transcript: 
    {docs}

    Question: 
    {question}

    ---------------
    Answer:
    """
).partial(
    date=datetime.date.today().isoformat()
)