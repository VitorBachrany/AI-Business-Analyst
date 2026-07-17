from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# LLM
# ==========================================================

LLM_MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0


# ==========================================================
# EMBEDDINGS
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ==========================================================
# TEXT SPLITTER
# ==========================================================

CHUNK_SIZE = 100

CHUNK_OVERLAP = 20


# ==========================================================
# PATHS
# ==========================================================

DOCUMENT_PATH = "documents/TesteAI.txt"

VECTOR_DB_PATH = "database"

OUTPUT_FILE = "research_output.txt"