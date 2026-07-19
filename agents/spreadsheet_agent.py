from planner import plan_analysis
from executor import execute_plan
from business_analyst import analyze_result
from visualization import generate_chart
from data_analysis import dataframe_schema

import pandas as pd


def analyze_spreadsheet(
    question: str,
    df: pd.DataFrame
) -> dict:
    print(">>> analyze_spreadsheet() foi chamado!")

    schema = dataframe_schema(df)

    # Planner
    plan = plan_analysis(question, schema)
    plan["question"] = question
    print("\n========== PLAN ==========")
    print(plan)
    print("==========================\n")

    # Executor
    result = execute_plan(df, plan)

    # Automatic chart generation
    chart = None

    if hasattr(result, "columns"):
        print("\n===== RESULT =====")
        print(result)
        print(result.columns)
        print("==================\n")
        chart = generate_chart(question, result)

    # Business analysis
    answer = analyze_result(question, result)

    return {
        "analysis": answer,
        "chart_path": chart
    }
