import pandas as pd

# ==========================================================
# PLAN EXECUTOR
# ==========================================================

def execute_plan(df: pd.DataFrame, plan: dict):

    operation = plan["operation"]

    if operation == "groupby":
        return execute_groupby(df, plan)

    raise ValueError(f"Unsupported operation: {operation}")


# ==========================================================
# GROUPBY EXECUTOR
# ==========================================================

def execute_groupby(df, plan):

    group_by = plan["group_by"].strip()
    metric = plan["metric"]
    aggregation = plan["aggregation"]
    question = plan.get("question", "").lower()

    df = df.copy()

    # ======================================================
    # TIME SERIES
    # ======================================================

    if (
        isinstance(group_by, str)
        and group_by.lower() == "date"
    ):

        df["Date"] = pd.to_datetime(df["Date"])

        # Monthly
        if "monthly" in question:

            df["Month"] = (
                df["Date"]
                .dt.to_period("M")
                .dt.to_timestamp()
            )

            group_by = "Month"

        # Yearly
        elif "yearly" in question:

            df["Year"] = df["Date"].dt.year

            group_by = "Year"

        # Daily
        else:

            group_by = "Date"

    # ======================================================
    # MULTIPLE COLUMNS
    # ======================================================

    if isinstance(group_by, str) and "," in group_by:

        group_by = [
            column.strip()
            for column in group_by.split(",")
        ]

    grouped = df.groupby(group_by)[metric]

    # ======================================================
    # AGGREGATION
    # ======================================================

    if aggregation == "sum":

        result = grouped.sum()

    elif aggregation == "mean":

        result = grouped.mean()

    elif aggregation == "max":

        result = grouped.max()

    elif aggregation == "min":

        result = grouped.min()

    elif aggregation == "count":

        result = grouped.count()

    else:

        raise ValueError(
            f"Unsupported aggregation: {aggregation}"
        )

    # ======================================================
    # SORT
    # ======================================================

    ascending = plan.get("ascending", True)

    result = result.sort_index(
        ascending=ascending
    )

    result = result.reset_index()

    # ======================================================
    # MONTH LABEL
    # ======================================================

    if "Month" in result.columns:

        result["Month Label"] = (
            result["Month"]
            .dt.strftime("%b %Y")
        )

        result = result.drop(
            columns=["Month"]
        )

        result = result[
            ["Month Label", metric]
        ]

    # ======================================================
    # LIMIT
    # ======================================================

    limit = plan.get("limit")

    if limit is not None:

        result = result.head(limit)

    return result


# ==========================================================
# TEST
# ==========================================================

from data_analysis import load_dataset

if __name__ == "__main__":

    df = load_dataset(
        "datasets/sales.csv"
    )

    plan = {

        "operation": "groupby",

        "group_by": "Date",

        "metric": "Revenue",

        "aggregation": "sum",

        "ascending": True,

        "question": "Show the monthly revenue trend over time"

    }

    result = execute_plan(
        df,
        plan
    )

    print(result)