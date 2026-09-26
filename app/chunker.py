from pathlib import Path


def load_document(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if path.suffix.lower() != ".md":
        raise ValueError("Only Markdown documents are supported.")

    return path.read_text(encoding="utf-8")