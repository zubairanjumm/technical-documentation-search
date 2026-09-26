from pathlib import Path

from app.chunker import chunk_text
from app.embeddings import create_embedding
from app.llm import generate_answer
from app.loader import load_document
from app.search import search
from app.vector_store import add_documents


def index_document(path: Path) -> None:
    text = load_document(path)

    chunks = chunk_text(text)

    embeddings = [
        create_embedding(chunk)
        for chunk in chunks
    ]

    add_documents(
        documents=chunks,
        embeddings=embeddings,
    )


def ask_question(question: str) -> str:
    relevant_chunks = search(question)

    return generate_answer(
        question=question,
        context=relevant_chunks,
    )