# AI-Business-Analyst
Enterprise AI Business Analyst capable of analyzing spreadsheets, generating executive insights and creating automatic visualizations using LLMs.

Features:
✔ Spreadsheet Analysis (CSV / Excel)
✔ Automatic Business Insights
✔ Executive Reports
✔ Automatic Chart Generation
✔ Interactive Streamlit Dashboard
✔ Business Intelligence Agent
✔ LangChain + Groq Integration
✔ Modular Architecture
✔ Local Python Interface

Tech Stack:
Python
Langchain
Groq
Pandas
Matplotlib
Streamlit
OpenPyXL
NumPy

Architecture:
User Question
      │
      ▼
Planner (LLM)
      │
      ▼
Execution Plan (JSON)
      │
      ▼
Data Executor (Pandas)
      │
      ▼
Business Analyst (LLM)
      │
      ▼
Visualization Planner
      │
      ▼
Automatic Chart

Project Structure:
AI-Business-Analyst/

│
├── app.py
├── main.py
├── planner.py
├── executor.py
├── spreadsheet_agent.py
├── visualization.py
├── visualization_planner.py
├── business_analyst.py
├── dataset_manager.py
├── rag.py
├── config.py
│
├── datasets/
├── documents/
├── charts/
└── README.md

Example Questions:
Which product generated the highest revenue?

Show the monthly revenue trend.

Compare revenue by region.

Which salesperson sold the most?

Show average profit by category.

Which region has the highest profit?

Create a revenue distribution chart.

Summarize the business performance.

Running Locally:
git clone ...

cd AI-Business-Analyst

pip install -r requirements.txt

streamlit run app.py


Author
Vitor Bachrany

Information Engineering Student

Artificial Intelligence

Business Intelligence

Data Engineering
