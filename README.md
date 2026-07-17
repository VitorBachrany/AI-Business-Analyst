# AI Business Analyst

Enterprise AI Business Analyst capable of analyzing spreadsheets, generating executive insights and creating automatic visualizations using Large Language Models (LLMs).



https://github.com/user-attachments/assets/aef019d1-5a6e-4ca1-a97d-9d0c74a4c41d

---
## Screenshots
Prompt used: Based on the business results, identify the areas that should receive the highest investment next year.


## Dashboard
<img width="1904" height="923" alt="image" src="https://github.com/user-attachments/assets/9edd1135-1f59-4864-abaf-67f811e78bb5" />
## Business Analysis
<img width="1916" height="919" alt="image" src="https://github.com/user-attachments/assets/48e0cecd-24cc-4c26-b237-05e9f552efe4" />
## Business Analysis
<img width="1096" height="872" alt="image" src="https://github.com/user-attachments/assets/0d5fd75e-0de9-4f56-bb77-3e0c01369d97" />
## Vizualization
<img width="1520" height="802" alt="image" src="https://github.com/user-attachments/assets/f4b3b28a-36bd-441b-ad74-c323d3936d2f" />







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
-Based on the business results, identify the areas that should receive the highest investment next year.

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
