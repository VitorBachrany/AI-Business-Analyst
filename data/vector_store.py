from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader


from config import (
    DOCUMENT_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
)

# ==========================================================
# FILE LOADERS
# ==========================================================

LOADERS = {

    ".txt": lambda path: TextLoader(
        path,
        encoding="utf-8"
    ),

    ".pdf": lambda path: PyPDFLoader(path),

    ".md": lambda path: TextLoader(
        path,
        encoding="utf-8"
    ),

    ".docx": lambda path: Docx2txtLoader(path),

}

# ==========================================================
# DOCUMENT LOADER
# ==========================================================

def load_documents():

    documents = []

    documents_path = Path("documents")

    files = list(documents_path.iterdir())

    print(f"\nFound {len(files)} files.\n")

    for file in files:

        print(f"Loading: {file.name}")

        loader_factory = LOADERS.get(file.suffix.lower())

        if loader_factory is None:

            print(f"Skipping unsupported file: {file.name}")

            continue

        loader = loader_factory(str(file))

        documents.extend(loader.load())

    return documents


# ==========================================================
# TEXT SPLITTER
# ==========================================================

def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


# ==========================================================
# EMBEDDING MODEL
# ==========================================================

def create_embeddings():

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


# ==========================================================
# VECTOR STORE
# ==========================================================

def create_vector_store(chunks, embeddings):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store
