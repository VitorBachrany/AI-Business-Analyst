from vector_store import (
    load_documents,
    create_chunks,
    create_embeddings,
    create_vector_store
)

print("=" * 60)
print("INDEXING DOCUMENTS")
print("=" * 60)

documents = load_documents()


print("Documents loaded.")

chunks = create_chunks(documents)

print(f"{len(chunks)} chunks created.")

embeddings = create_embeddings()

print("Embedding model loaded.")

create_vector_store(chunks, embeddings)

print("Vector database created successfully!")