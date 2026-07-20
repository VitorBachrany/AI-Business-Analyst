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
    "group_by": "string for a single column OR array of strings for multiple columns",
    "metric": "string",
    "aggregation": "sum | mean | count | max | min",
    "time_granularity": "day | month | year | none",
    "filters": [],
    "sort_by": "",
    "ascending": true
}}

MULTIPLE GROUPING RULE

If more than one column is required, ALWAYS return an array.

Correct:

"group_by":["Region","Product"]

Incorrect:

"group_by":"Region, Product"

----------------------------------
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
    "aggregation":"sum",
    "time_regularity":"month"
}}

------------------------------------

Example 3

Question:
Average profit by category and region.
------------------------------------

Output:

{{
    "operation":"groupby",
    "group_by":["Category","Region"],
    "metric":"Profit",
    "aggregation":"mean",
    "time_regularity":"none"
}}
----------------------------------

Example 4
Question:
Show the yearly profit trend.
-----------------------------------
Output:

{{
    "operation":"groupby",
    "group_by":"Date",
    "metric":"Profit",
    "aggregation":"sum",
    "time_granularity":"year"
}}
-----------------------------

Rules:

- Return ONLY valid JSON.
- Do not use markdown.
- Do not explain anything.
- Do not answer the user's question.

Time Series Rules

If a Date column exists:

- Detect whether the user wants daily, monthly or yearly aggregation.

Examples that indicate MONTH:

- monthly
- month
- by month
- month over month
- monthly trend
- monthly revenue
- monthly sales

Return:

"time_granularity":"month"

Examples that indicate YEAR:

- yearly
- annual
- by year

Return:

"time_granularity":"year"

Examples that indicate DAY:

- daily
- by day
- each day

Return:

"time_granularity":"day"

If no temporal aggregation is requested:

"time_granularity":"none"

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
