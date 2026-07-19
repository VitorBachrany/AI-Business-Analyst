from langchain_groq import ChatGroq

from config import (
    LLM_MODEL,
    TEMPERATURE
)

# ==========================================================
# LLM
# ==========================================================

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)

# ==========================================================
# ANALYSIS PLANNER
# ==========================================================

def plan_analysis(question: str, schema: str) -> str:

    prompt = f"""
You are an AI planning module for a Business Intelligence Agent.

You DO NOT answer the user's question.

Your task is ONLY to generate a JSON execution plan.

The JSON MUST follow exactly this structure.

{{
    "operation": "groupby | filter | sort | describe | correlation",
    "group_by": "string OR array of strings",
    "metric": "string",
    "aggregation": "sum | mean | count | max | min",
    "filters": [],
    "sort_by": "",
    "ascending": true (boolean)
}}
Examples:

Example 1

Question:
Total revenue by region.

Output:

{{
    "operation":"groupby",
    "group_by":"Region",
    "metric":"Revenue",
    "aggregation":"sum"
}}

------------------------------------

Example 2

Question:
Monthly revenue by product.

Output:

{{
    "operation":"groupby",
    "group_by":["Date","Product"],
    "metric":"Revenue",
    "aggregation":"sum"
}}

------------------------------------

Example 3

Question:
Average profit by category and region.

Output:

{{
    "operation":"groupby",
    "group_by":["Category","Region"],
    "metric":"Profit",
    "aggregation":"mean"
}}

Rules:

- Return ONLY valid JSON.
- Do not use markdown.
- Do not explain anything.
- Do not answer the user's question.

Time Series Rules:

- If the user requests a monthly analysis and a Date column exists, use Date as the group_by field. The execution layer will aggregate by month.
- If the user requests a yearly analysis and a Date column exists, use Date as the group_by field. The execution layer will aggregate by year.
- If the user requests a daily analysis, group by Date.

Dataset schema:

{schema}

User Question:

{question}
"""
    import json
    response = llm.invoke(prompt)

    return json.loads(response.content)



if __name__ == "__main__":

    schema = """
Columns:

Product
Revenue
Profit
Region
Salesperson
Quantity
"""

    plan = plan_analysis(
        "Which product generated the highest revenue?",
        schema
    )

    print(plan)
