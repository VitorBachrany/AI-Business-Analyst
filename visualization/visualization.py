import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
from visualization.visualization_planner import plan_chart
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

PRIMARY_COLOR = "#2563EB"

def human_format(x, pos):
    if abs(x) >= 1_000_000:
        return f"{x/1_000_000:.1f}M"
    if abs(x) >= 1_000:
        return f"{x/1_000:.1f}K"
    return f"{x:.0f}"

def create_bar_chart(df, x_column, y_column):
    charts = Path("charts")
    charts.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chart_path = charts / f"bar_chart_{timestamp}.png"

    plt.figure(figsize=(12,6))
    
    plt.bar(
        df[x_column],
        df[y_column],
        color=PRIMARY_COLOR
    )

    plt.title(
    f"{y_column} by {x_column}",
    fontsize=14,
    fontweight="bold",
    pad=15
)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.grid(axis="y")

   
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(human_format))

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path

def create_line_chart(df, x_column, y_column):
    charts = Path("charts")
    charts.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chart_path = charts / f"line_chart_{timestamp}.png"

    plt.figure(figsize=(14, 6))

    plt.plot(
        range(len(df)),
        df[y_column],
        marker="o",
        linewidth=2,
        color=PRIMARY_COLOR
    )

    plt.xticks(
        range(len(df)),
        df[x_column],
        rotation=45,
        ha="right"
    )

    plt.title(
    f"{y_column} by {x_column}",
    fontsize=14,
    fontweight="bold",
    pad=15
)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    
    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(human_format))

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path

def create_pie_chart(df, labels_column, values_column):
    charts = Path("charts")
    charts.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chart_path = charts / f"pie_chart_{timestamp}.png"

    plt.figure(figsize=(8,8))

    plt.pie(
        df[values_column],
        labels=df[labels_column],
        autopct="%1.1f%%",
        startangle=90,
        colors=plt.cm.Blues.colors
    )

    plt.title(f"{values_column} by {labels_column}")

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    
    

    return chart_path

def create_histogram(df, column):
    charts = Path("charts")
    charts.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chart_path = charts / f"histogram_{timestamp}.png"

    plt.figure(figsize=(12,6))

    plt.hist(
        df[column],
        bins=15,
        color=PRIMARY_COLOR 
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)

    
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(human_format))

    plt.tight_layout()
    plt.savefig(
    chart_path,
    dpi=200,
    bbox_inches="tight"
)
    plt.close()

    return chart_path

# ==========================================================
# GENERATE CHART
# ==========================================================

def generate_chart(question, result):
    if len(result.columns) < 2:
        return None

    plan = plan_chart(
        question,
        result
    )

    chart = plan["chart_type"]

    if chart == "bar":
        return create_bar_chart(
            result,
            result.columns[0],
            result.columns[1]
        )

    elif chart == "line":
        return create_line_chart(
            result,
            result.columns[0],
            result.columns[1]
        )

    elif chart == "pie":
        return create_pie_chart(
            result,
            result.columns[0],
            result.columns[1]
        )

    elif chart == "histogram":
        numeric = result.select_dtypes(include="number").columns
        
        if len(numeric):
            return create_histogram(
                result,
                numeric[0]
            )

    # Fallback padrão
    return create_bar_chart(
        result,
        result.columns[0],
        result.columns[1]
    )
