from datetime import datetime

from langchain_core.tools import tool

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from spreadsheet_agent import analyze_spreadsheet
from rag import ask_rag
from dataset_manager import get_dataset

# ==========================================================
# Save Tool
# ==========================================================

@tool
def save_tool(data: str) -> str:
    """
    Save research results into a text file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open("research_output.txt", "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return "Research successfully saved."
from langchain_core.tools import tool

from rag import ask_rag


@tool
def rag_tool(question: str) -> str:
    """
    Search the local knowledge base using Retrieval-Augmented Generation (RAG).
    Use this tool when the answer may be contained in the local documents.
    """

    return ask_rag(question)

# ==========================================================
# Spreadsheet Tool
# ==========================================================

@tool
def spreadsheet_tool(question: str) -> str:
    """
    Analyze CSV and Excel spreadsheets using the active dataset.
    """

    df = get_dataset()

    if df is None:
        return (
            "No spreadsheet is currently loaded. "
            "Load a CSV or Excel file before asking spreadsheet questions."
        )

    response = analyze_spreadsheet(question, df)

    return response["analysis"]

# ==========================================================
# DuckDuckGo
# ==========================================================

search_tool = DuckDuckGoSearchRun()


# ==========================================================
# Wikipedia
# ==========================================================

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=500,
)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
