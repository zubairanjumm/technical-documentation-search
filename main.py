from pathlib import Path

from app.pipeline import ask_question, index_document


DOCUMENT_PATH = Path("docs/sample.md")


def main() -> None:
    print("Indexing documentation...")

    index_document(DOCUMENT_PATH)

    print("Documentation indexed.")
    print()

    while True:
        question = input("Ask a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)

        print()
        print(answer)
        print()


if __name__ == "__main__":
    main()