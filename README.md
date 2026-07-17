# AI Business Analyst

Enterprise AI Business Analyst capable of analyzing spreadsheets, generating executive insights and creating automatic visualizations using Large Language Models (LLMs).

---
## Examples



https://github.com/user-attachments/assets/aef019d1-5a6e-4ca1-a97d-9d0c74a4c41d







---
## Features

- Spreadsheet Analysis (CSV / Excel)
- Automatic Business Insights
- Executive Business Reports
- Automatic Chart Generation
- Interactive Streamlit Dashboard
- Business Intelligence Agent
- LangChain + Groq Integration
- Modular Architecture
- Local Python Interface

---

## Tech Stack

- Python
- LangChain
- Groq
- Pandas
- NumPy
- Matplotlib
- Streamlit
- OpenPyXL

---

## Architecture

```
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
```

---

## Project Structure

```
AI-Business-Analyst/

├── app.py
├── main.py
├── planner.py
├── executor.py
├── spreadsheet_agent.py
├── business_analyst.py
├── visualization.py
├── visualization_planner.py
├── dataset_manager.py
├── rag.py
├── config.py
│
├── datasets/
├── documents/
├── charts/
└── README.md
```

---

## Example Questions

- Which product generated the highest revenue?
- Show the monthly revenue trend.
- Compare revenue by region.
- Which salesperson sold the most?
- Show average profit by category.
- Which region has the highest profit?
- Create a revenue distribution chart.
- Summarize the business performance.

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Business-Analyst.git
```

Go to the project folder:

```bash
cd AI-Business-Analyst
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Or execute the local interface:

```bash
python main.py
```

---

## Author

**Vitor Bachrany**

Information Engineering Student

Artificial Intelligence • Business Intelligence • Data Engineering
