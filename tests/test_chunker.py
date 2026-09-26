from app.chunker import chunk_text


def test_chunk_text():
    text = "one two three four five six"

    chunks = chunk_text(text, chunk_size=3)

    assert chunks == [
        "one two three",
        "four five six",
    ]