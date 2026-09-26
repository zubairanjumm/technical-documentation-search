from app.embeddings import create_embedding
from app.vector_store import search_documents


def search(query: str, n_results: int = 3) -> list[str]:
    query_embedding = create_embedding(query)

    return search_documents(
        query_embedding=query_embedding,
        n_results=n_results,
    )