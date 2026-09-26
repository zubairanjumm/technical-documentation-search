from pathlib import Path

from app.loader import load_document


def test_load_document(tmp_path: Path):
    document = tmp_path / "test.md"
    document.write_text("Hello documentation", encoding="utf-8")

    result = load_document(document)

    assert result == "Hello documentation"