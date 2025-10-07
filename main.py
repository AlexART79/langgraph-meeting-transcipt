from dotenv import load_dotenv
load_dotenv()

from graph.consts import TRANSCRIPT_ANALYSIS, GENERAL_SUMMARY, PROJECT_DESCRIPTION, GENERATE_EMAIL
from graph.graph import app

if __name__ == "__main__":
    file_path = "project_meetings.pdf"

    result = app.invoke({"file_path": file_path})
    print(f"Answer:")

    for key in [TRANSCRIPT_ANALYSIS, GENERAL_SUMMARY, PROJECT_DESCRIPTION, GENERATE_EMAIL]:
        print(f"----- {key} -----")
        print(f"{result["generation"][key]}\n")
