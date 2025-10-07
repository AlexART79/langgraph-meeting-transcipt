from langchain_community.document_loaders import PyPDFLoader

from graph.state import State
from graph.chains import ai_chain
from graph.consts import TRANSCRIPT_ANALYSIS, GENERAL_SUMMARY, PROJECT_DESCRIPTION, GENERATE_EMAIL

def load_docs(state: State):
    file_path = state["file_path"]
    loader = PyPDFLoader(file_path=file_path)
    docs = loader.load()

    return {
        **state,
        "docs": docs
    }

def transcript_analysis(state: State):
    docs = state["docs"]
    question = """
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

    resp = ai_chain.invoke({"docs": docs, "question": question})

    return {
        **state,
        "generation": {TRANSCRIPT_ANALYSIS: resp}
    }

def general_summary(state: State):
    docs = state["docs"]
    question = """
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

    resp = ai_chain.invoke({"docs": docs, "question": question})

    return {
        **state,
        "generation": {GENERAL_SUMMARY: resp}
    }

def project_description(state: State):
    docs = state["docs"]
    question = """
        Create a description of the project
        Include:
        - What the project is about?
        - What technologies are used in the project for the frontend, backend, data storage, etc.?
        - What problems does the project has, what is planned to be implemented in the near future?
    """

    resp = ai_chain.invoke({"docs": docs, "question": question})

    return {
        **state,
        "generation": {PROJECT_DESCRIPTION: resp}
    }

def generate_email(state: State):
    docs = state["docs"]
    question = """
        Based on the results of the last three meetings, write the text of the letter for all participants. 
        Ensure optimistic and businesslike tone. In the text of the letter, 
        - summarize the meetings, 
        - include the next steps to be taken. 
        Don't forget to thank each participant. Also indicate the date of the next meeting as 10 days after today's date. 
    """

    resp = ai_chain.invoke({"docs": docs, "question": question})

    return {
        **state,
        "generation": {GENERATE_EMAIL: resp}
    }