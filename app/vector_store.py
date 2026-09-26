import chromadb


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="technical_docs"
)


def add_documents(
    documents: list[str],
    embeddings: list[list[float]],
) -> None:
    ids = [f"doc_{i}" for i in range(len(documents))]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
    )


def search_documents(
    query_embedding: list[float],
    n_results: int = 3,
) -> list[str]:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    return results["documents"][0]