from langchain_groq import ChatGroq
import json

from config import (
    LLM_MODEL,
    TEMPERATURE
)

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0
)

# ==========================================================
# QUESTION VALIDATOR
# ==========================================================

def validate_question(question: str, schema: str):

    prompt = f"""
You are a classifier for a Business Intelligence AI system.

Your task is ONLY to determine whether the user's question is:

1. VALID
or
2. INVALID

A VALID question:
- refers to the uploaded dataset
- asks about metrics
- asks about trends
- asks about charts
- asks about KPIs
- asks about business analysis
- asks about comparisons
- asks about statistics

Examples of VALID questions:

- Which product generated the highest revenue?
- Show monthly sales trend.
- Compare profit by region.
- What is the average order value?
- Create a chart of revenue by product.

Examples of INVALID questions:

- Hello
- Tell me a joke
- What is the weather?
- How do I code in Python?
- asdhuasdhauhsduahsd

Dataset schema:

{schema}

User question:

{question}

Return ONLY valid JSON:

{{
    "valid": true
}}

or

{{
    "valid": false
}}
"""

    response = llm.invoke(prompt)

    try:
        result = json.loads(response.content)
        return result["valid"]

    except:
        return False