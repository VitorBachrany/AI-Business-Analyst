from agents.planner import plan_analysis
from data.executor import execute_plan
from business_analyst import analyze_result
from visualization.visualization import generate_chart
from data.data_analysis import dataframe_schema
from agents.question_validator import validate_question


import pandas as pd


def analyze_spreadsheet(
    question: str,
    df: pd.DataFrame
) -> dict:

    print(">>> analyze_spreadsheet() foi chamado!")

    schema = dataframe_schema(df)

    # ======================================================
    # QUESTION VALIDATION
    # ======================================================

    valid = validate_question(
        question,
        schema
    )

    if not valid:

        return {
            "analysis": """
I'm designed to answer Business Intelligence questions about the uploaded dataset.

Please ask questions related to:

- Revenue
- Profit
- Sales
- Trends
- KPIs
- Charts
- Business performance
""",
            "chart_path": None
        }

    # ======================================================
    # PLANNER
    # ======================================================

    plan = plan_analysis(
        question,
        schema
    )

    plan["question"] = question

    print("\n========== PLAN ==========")
    print(plan)
    print("==========================\n")

    # ======================================================
    # EXECUTOR
    # ======================================================

    result = execute_plan(
        df,
        plan
    )

    # ======================================================
    # CHART
    # ======================================================

    chart = None

    if hasattr(result, "columns"):

        print("\n===== RESULT =====")
        print(result)
        print(result.columns)
        print("==================\n")

        chart = generate_chart(
            question,
            result
        )

    # ======================================================
    # BUSINESS ANALYST
    # ======================================================

    answer = analyze_result(
        question,
        result
    )

    return {
        "analysis": answer,
        "chart_path": chart
    }
