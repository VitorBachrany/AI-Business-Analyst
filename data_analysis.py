import pandas as pd
from pathlib import Path

# ==========================================================
# LOAD DATASET
# ==========================================================

def load_dataset(file_path: str):

    path = Path(file_path)

    if path.suffix.lower() == ".csv":

        return pd.read_csv(path)

    elif path.suffix.lower() == ".xlsx":

        return pd.read_excel(path)

    else:

        raise ValueError("Unsupported file type.")
    

# ==========================================================
# DATASET SHAPE
# ==========================================================

def get_shape(df):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1]
    }

# ==========================================================
# DATASET COLUMNS
# ==========================================================

def get_columns(df):

    return list(df.columns)


# ==========================================================
# DATA TYPES
# ==========================================================

def get_dtypes(df):

    return df.dtypes.astype(str).to_dict()

# ==========================================================
# MISSING VALUES
# ==========================================================

def get_missing_values(df):

    return df.isnull().sum().to_dict()

# ==========================================================
# NUMERIC SUMMARY
# ==========================================================

def get_numeric_summary(df):

    return df.describe().to_dict()

# ==========================================================
# SAMPLE DATA
# ==========================================================

def get_sample(df, n=5):

    return df.head(n)

# ==========================================================
# TOP PRODUCT
# ==========================================================

def get_top_product(df):

    sales = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return sales.idxmax(), sales.max()

# ==========================================================
# TOTAL REVENUE
# ==========================================================

def get_total_revenue(df):

    return df["Revenue"].sum()

# ==========================================================
# TOTAL PROFIT
# ==========================================================

def get_total_profit(df):

    return df["Profit"].sum()

# ==========================================================
# BEST REGION
# ==========================================================

def get_best_region(df):

    revenue = (
        df.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return revenue.idxmax(), revenue.max()

# ==========================================================
# BEST SALESPERSON
# ==========================================================

def get_best_salesperson(df):

    revenue = (
        df.groupby("Salesperson")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return revenue.idxmax(), revenue.max()

# ==========================================================
# BUSINESS REPORT
# ==========================================================

def build_business_report(df):

    product, product_revenue = get_top_product(df)

    region, region_revenue = get_best_region(df)

    salesperson, salesperson_revenue = get_best_salesperson(df)

    total_revenue = get_total_revenue(df)

    total_profit = get_total_profit(df)

    report = f"""
================ BUSINESS REPORT ================

Dataset

Rows: {get_shape(df)["rows"]}
Columns: {get_shape(df)["columns"]}

-------------------------------------------------

Top Product

Name: {product}

Revenue: ${product_revenue:.2f}

-------------------------------------------------

Best Region

Name: {region}

Revenue: ${region_revenue:.2f}

-------------------------------------------------

Best Salesperson

Name: {salesperson}

Revenue: ${salesperson_revenue:.2f}

-------------------------------------------------

Company Metrics

Total Revenue: ${total_revenue:.2f}

Total Profit: ${total_profit:.2f}

=================================================
"""

    return report


# ==========================================================
# DATAFRAME SCHEMA
# ==========================================================

def dataframe_schema(df):

    schema = []

    schema.append("DATASET INFORMATION")
    schema.append("====================")
    schema.append(f"Rows: {df.shape[0]}")
    schema.append(f"Columns: {df.shape[1]}")
    schema.append("")

    schema.append("COLUMNS")
    schema.append("-------")

    for column in df.columns:

        dtype = str(df[column].dtype)

        schema.append(f"- {column} ({dtype})")

    schema.append("")
    schema.append("MISSING VALUES")
    schema.append("")
    schema.append("SAMPLE DATA")
    schema.append("-----------")

    sample = df.head(5)

    schema.append(sample.to_string(index=False))
    schema.append("--------------")

    missing = df.isnull().sum()

    for column in df.columns:

        schema.append(f"- {column}: {missing[column]}")

    return "\n".join(schema)