from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from data_analysis import load_dataset
from dataset_manager import set_dataset
from tools import (
    search_tool,
    wiki_tool,
    save_tool,
    rag_tool,
    spreadsheet_tool
)


load_dotenv()

# ============================================
# DEFAULT DATASET FOR TERMINAL TESTS
# ============================================

try:
    default_df = load_dataset("datasets/sales.csv")
    set_dataset(default_df)
    print("Default dataset loaded: datasets/sales.csv")
except Exception as e:
    print(f"Could not load default dataset: {e}")

# ============================================
# LLM
# ============================================

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0
)

# ============================================
# Tools
# ============================================

tools = [
    search_tool,
    wiki_tool,
    rag_tool,
    spreadsheet_tool,
    save_tool
]

# ============================================
# Agent
# ============================================

memory = InMemorySaver()

agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    system_prompt="""
You are an AI Research Assistant with Business Intelligence capabilities.

You have access to the following tools:

- Wikipedia:
Use for encyclopedic knowledge.

- DuckDuckGo:
Use for recent events, news and information from the internet.

- rag_tool:
Use whenever the answer may exist in the local knowledge base (TXT, PDF, DOCX or Markdown files).

- spreadsheet_tool:
Use whenever the user asks about:
- spreadsheets
- CSV
- Excel
- sales
- revenue
- profit
- KPIs
- dashboards
- business reports
- financial performance
- business insights

Always choose the most appropriate tool.

Never answer spreadsheet questions without using spreadsheet_tool.

Never answer questions about local documents without using rag_tool.
"""
)    #Descricao do agente

# ============================================
# Chat Loop
# ============================================

print("=" * 60)
print("AI Research Assistant")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":  #"exit" para sair do chat
        break

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": "research_chat"  #salvando as repostas anteriores na memoria
                }
            }
        )
        DEBUG = False #True para modo dev para saber toda etapa da IA
        if DEBUG:
            print("\n========== DEBUG ==========")

            for message in response["messages"]:
                print("=" * 60)
                print(type(message).__name__)
                print(message)

        print("\nAssistant:\n")


        last_response = False  #Printar apenas a ultima resposta no terminal
        for message in reversed(response["messages"]):
            if message.type == "ai" and message.content:
                print(message.content)
                break
        if last_response:
            print("\nAssistant:\n")
            print(last_response)

    except Exception as e: #Controle de erro

        print("\nERROR")
        print(e)