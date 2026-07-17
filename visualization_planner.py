from langchain_groq import ChatGroq
import json

from config import (
    LLM_MODEL,
    TEMPERATURE
)

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)

# ==========================================================
# CHART PLANNER
# ==========================================================

def plan_chart(question: str, result):

    prompt = f"""
You are a Business Data Visualization Expert.

Your task is to choose the SINGLE best chart for the user's question.

Available charts:

- bar
- line
- pie
- histogram

Rules:

BAR
- Compare categories
- Rankings
- Top products
- Top regions

LINE
- Trends
- Time series
- Monthly
- Daily
- Yearly

PIE
- Percentages
- Shares
- Composition
- Distribution of a whole

HISTOGRAM
- Distribution of ONE numeric variable
- Frequency analysis

Return ONLY valid JSON.

Example:

{{
    "chart_type":"pie"
}}

--------------------------------------------------

Question

{question}

--------------------------------------------------

Result

{result}

"""

    response = llm.invoke(prompt)

    return json.loads(response.content)