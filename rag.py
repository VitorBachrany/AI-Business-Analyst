from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
    LLM_MODEL,
    TEMPERATURE,
)

load_dotenv()


# ==========================================================
# EMBEDDING MODEL
# ==========================================================

def create_embeddings():

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


# ==========================================================
# LLM
# ==========================================================

def create_llm():

    return ChatGroq(
        model=LLM_MODEL,
        temperature=TEMPERATURE
    )


# ==========================================================
# VECTOR STORE
# ==========================================================

def load_vector_store(embeddings):

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )


# ==========================================================
# RETRIEVER
# ==========================================================

def create_retriever(vector_store):

    return vector_store.as_retriever(
        search_kwargs={
            "k": 2
        }
    )


# ==========================================================
# INITIALIZATION
# ==========================================================

embeddings = create_embeddings()

vector_store = load_vector_store(embeddings)

retriever = create_retriever(vector_store)

llm = create_llm()


# ==========================================================
# RAG
# ==========================================================

def ask_rag(question: str):

    results = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in results
    )

    prompt = f"""
You are an AI assistant specialized in question answering.

Answer ONLY using the context below.

If the answer is not contained in the context,
reply only:

"I don't know."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    question = "What is the color of sky"

    answer = ask_rag(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)