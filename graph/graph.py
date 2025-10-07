from langgraph.graph import StateGraph, END

from graph.state import State
from graph.consts import LOAD_DOCS, TRANSCRIPT_ANALYSIS, GENERAL_SUMMARY, PROJECT_DESCRIPTION, GENERATE_EMAIL
from graph.nodes import load_docs, transcript_analysis, general_summary, project_description, generate_email


flow = StateGraph(State)

flow.add_node(LOAD_DOCS, load_docs)
flow.add_node(TRANSCRIPT_ANALYSIS, transcript_analysis)
flow.add_node(GENERAL_SUMMARY, general_summary)
flow.add_node(PROJECT_DESCRIPTION, project_description)
flow.add_node(GENERATE_EMAIL, generate_email)

flow.set_entry_point(LOAD_DOCS)
flow.add_edge(LOAD_DOCS, TRANSCRIPT_ANALYSIS)
flow.add_edge(LOAD_DOCS, GENERAL_SUMMARY)
flow.add_edge(LOAD_DOCS, PROJECT_DESCRIPTION)
flow.add_edge(LOAD_DOCS, GENERATE_EMAIL)
flow.add_edge([TRANSCRIPT_ANALYSIS, GENERAL_SUMMARY, PROJECT_DESCRIPTION, GENERATE_EMAIL], END)

app = flow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")

