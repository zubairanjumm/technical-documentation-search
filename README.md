# Technical Documentation Semantic Search

A simple RAG application that searches technical documentation using semantic similarity and generates answers from the most relevant sections.

## What It Does

The application:

1. Loads technical documentation.
2. Splits the documentation into smaller chunks.
3. Creates embeddings for each chunk.
4. Stores the embeddings in ChromaDB.
5. Converts the user's question into an embedding.
6. Retrieves the most relevant documentation chunks.
7. Sends the retrieved context to Gemini.
8. Generates an answer based on the documentation.

## Architecture

```text
Documentation
      ↓
   Chunking
      ↓
  Embeddings
      ↓
   ChromaDB
      ↓
   User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
    Gemini
      ↓
     Answer
```

## Tech Stack

* Python
* Gemini API
* Gemini Embeddings
* ChromaDB
* python-dotenv
* Pytest

## Project Structure

```text
technical-documentation/
│
├── app/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── search.py
│   ├── llm.py
│   └── pipeline.py
│
├── docs/
│   └── sample.md
│
├── tests/
│   ├── test_loader.py
│   ├── test_chunker.py
│   └── test_search.py
│
├── main.py
├── pyproject.toml
├── .env.example
└── README.md
```

## Running the Project

Create the virtual environment:

```bash
uv venv
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the tests:

```bash
uv run pytest
```

Run the application:

```bash
uv run python main.py
```

## Example

```text
Ask a question: How do I create a Python virtual environment?

Answer:
You can create a Python virtual environment using:
python -m venv .venv
```

## What I Learned

This project demonstrates the fundamental components of a RAG system:

* Document loading
* Text chunking
* Embeddings
* Vector databases
* Semantic search
* Retrieval
* Context injection
* LLM-based generation

## Project Type

**RAG (Retrieval-Augmented Generation)**
