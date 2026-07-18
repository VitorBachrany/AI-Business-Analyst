import streamlit as st
import pandas as pd

from spreadsheet_agent import analyze_spreadsheet
from dataset_manager import set_dataset

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Business Analyst",
    page_icon="",
    layout="wide"
)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    st.title("AI Business Analyst")

    st.caption(
        "AI-powered business intelligence assistant for spreadsheet and document analysis."
    )

    st.divider()

    st.subheader("Data Sources")

    uploaded_dataset = st.file_uploader(
        "Spreadsheet",
        type=["csv", "xlsx"]
    )

    uploaded_documents = st.file_uploader(
        "Documents",
        type=["pdf", "docx", "txt", "md"],
        accept_multiple_files=True
    )

    st.divider()

    st.subheader("About")

    st.caption("Version 1.0")
    st.caption("Powered by LangChain")
    st.caption("Groq")
    st.caption("Streamlit")

# ==========================================================
# MAIN PAGE
# ==========================================================

st.title("AI Business Analyst")

st.caption(
    "Enterprise AI assistant for spreadsheet analysis and document intelligence."
)

st.divider()

# ==========================================================
# NO DATASET
# ==========================================================

if uploaded_dataset is None:
    st.info("Upload a spreadsheet to begin your analysis.")

    st.write("""
This application combines:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Spreadsheet Analysis
- Business Intelligence
- Automatic Charts
- Executive Reports

Upload a spreadsheet and start asking questions.
""")

# ==========================================================
# DATASET LOADED
# ==========================================================

else:
    if uploaded_dataset.name.endswith(".csv"):
        df = pd.read_csv(uploaded_dataset)
    else:
        df = pd.read_excel(uploaded_dataset)

    set_dataset(df)

    # ======================================================
    # TABS
    # ======================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Dataset",
            "Analysis",
            "Visualization",
            "Documents"
        ]
    )

    # ======================================================
    # DATASET TAB
    # ======================================================

    with tab1:
        st.subheader("Dataset Overview")

        # ======================================================
        # BASIC METRICS
        # ======================================================

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric(
                "Numeric",
                len(df.select_dtypes(include="number").columns)
            )

        with col4:
            st.metric(
                "Categorical",
                len(df.select_dtypes(include="object").columns)
            )

        with col5:
            st.metric(
                "Missing",
                int(df.isna().sum().sum())
            )

        st.divider()

        # ======================================================
        # BUSINESS METRICS
        # ======================================================

        business_cols = st.columns(4)

        metric_position = 0

        if "Revenue" in df.columns:
            business_cols[metric_position].metric(
                "Total Revenue",
                f"${df['Revenue'].sum():,.2f}"
            )
            metric_position += 1

            business_cols[metric_position].metric(
                "Average Revenue",
                f"${df['Revenue'].mean():,.2f}"
            )
            metric_position += 1

        if "Profit" in df.columns:
            business_cols[metric_position].metric(
                "Total Profit",
                f"${df['Profit'].sum():,.2f}"
            )
            metric_position += 1

            if metric_position < 4:
                business_cols[metric_position].metric(
                    "Average Profit",
                    f"${df['Profit'].mean():,.2f}"
                )

        st.divider()

        # ======================================================
        # DATE RANGE
        # ======================================================

        date_column = None

        for column in df.columns:
            try:
                pd.to_datetime(df[column])
                date_column = column
                break
            except Exception:
                pass

        if date_column is not None:
            dates = pd.to_datetime(df[date_column])

            st.metric(
                "Date Range",
                f"{dates.min().date()} → {dates.max().date()}"
            )

            st.divider()

        # ======================================================
        # MEMORY
        # ======================================================

        memory = df.memory_usage(deep=True).sum() / 1024

        st.metric(
            "Memory Usage",
            f"{memory:.1f} KB"
        )

        st.divider()

        # ======================================================
        # DATASET INFORMATION
        # ======================================================

        st.subheader("Dataset Information")

        info = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isna().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            info,
            use_container_width=True
        )

        # ======================================================
        # DATA PREVIEW
        # ======================================================

        with st.expander("Dataset Preview", expanded=False):
            st.dataframe(
                df.head(20),
                use_container_width=True
            )

        # ======================================================
        # NUMERIC STATISTICS
        # ======================================================

        numeric = df.select_dtypes(include="number")

        if len(numeric.columns):
            with st.expander("Numeric Statistics", expanded=False):
                st.dataframe(
                    numeric.describe(),
                    use_container_width=True
                )

    # ======================================================
    # ANALYSIS TAB
    # ======================================================

    with tab2:
        st.subheader("Ask your Data")

        question = st.text_area(
            "Question",
            placeholder="Example: Show the monthly revenue trend over time",
            height=120
        )

        analyze = st.button(
            "Analyze",
            use_container_width=True
        )

        if analyze and question:
            with st.spinner("Analyzing data..."):
                response = analyze_spreadsheet(
                    question,
                    df
                )

            st.divider()

            st.subheader("Business Analysis")

            st.markdown(response["analysis"])

            st.download_button(
                label="Download Report",
                data=response["analysis"],
                file_name="Business_Analysis_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.session_state["chart"] = response["chart_path"]

    # ======================================================
    # VISUALIZATION TAB
    # ======================================================

    with tab3:
        st.subheader("Business Visualization")

        if "chart" in st.session_state:
            st.image(
                st.session_state["chart"],
                use_container_width=True
            )

            with open(st.session_state["chart"], "rb") as file:
                st.download_button(
                    label="Download Chart",
                    data=file,
                    file_name="Business_Chart.png",
                    mime="image/png",
                    use_container_width=True
                )
        else:
            st.info("Run an analysis to generate a visualization.")

    # ======================================================
    # DOCUMENTS TAB
    # ======================================================

    with tab4:
        st.subheader("Document Intelligence")

        if uploaded_documents:
            st.success(
                f"{len(uploaded_documents)} document(s) uploaded."
            )
            st.info(
                "Document analysis will be integrated in the next version."
            )
        else:
            st.info(
                "Upload PDF, DOCX, TXT or Markdown documents from the sidebar."
            )
