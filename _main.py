import datetime

from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader


llm = ChatOpenAI(model="gpt-4o", temperature=0)

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

ai_chain = prompt | llm | StrOutputParser()

if __name__ == "__main__":
    loader = PyPDFLoader(file_path="project_meetings.pdf")
    docs = loader.load()

    question1="""
        Conduct the transcript analysis. It is necessary to determine specialization of each meeting participants
        Create a list of meeting participants, indicate the name and potential specialization for each.   
        Expected output format:
        Meeting (meeting date):
        Participants:
        1. Sarah Connor: scrum master
        2. Kent Smith: software engineer
        ...
        Agenda: (what was the meeting about, what was decided as the result of the meeting, top 3 challenges, top 3 insights)
    """

    question2 = """
        Create a general summary of all meetings for each participant: 
        name of the participant;
        summary what he was saying. 
        
        In addition, it is necessary to find out who generated ideas,
        who criticized it, who supported it, who was neutral. 
        
        Expected response structure should be as follow:
        
        Participant: Sarah Connor
        Summary: (Summary)
        Ideas: 
          1. (Sarah's idea 1)
             Supporters: John Doe, Mike Smith
             Opposition: -
             Neutrals: Kate Jones
          2. (Sarah's idea 2)
             Supporters: Kate Jones
             Opposition: John Doe
             Neutrals: -
    """

    question3="""
        Create a description of the project
        Include:
        - What the project is about?
        - What technologies are used in the project for the frontend, backend, data storage, etc.?
        - What problems does the project has, what is planned to be implemented in the near future?
    """

    question4=f"""
        Based on the results of the last three meetings, write the text of the letter for all participants. 
        Ensure optimistic and businesslike tone. In the text of the letter, 
        - summarize the meetings, 
        - include the next steps to be taken. 
        Don't forget to thank each participant. Also indicate the date of the next meeting as 10 days after today's date. 
    """

    result = ai_chain.invoke({"docs": docs, "question": question1})
    print(f"Question:\n{question1}\n\n")
    print(f"Answer:\n{result}\n\n")

    result = ai_chain.invoke({"docs": docs, "question": question2})
    print(f"Question:\n{question2}\n\n")
    print(f"Answer:\n{result}\n\n")

    result = ai_chain.invoke({"docs": docs, "question": question3})
    print(f"Question:\n{question3}\n\n")
    print(f"Answer:\n{result}\n\n")

    result = ai_chain.invoke({"docs": docs, "question": question4})
    print(f"Question:\n{question4}\n\n")
    print(f"Answer:\n{result}")
