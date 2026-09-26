import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)


def generate_answer(question: str, context: list[str]) -> str:
    context_text = "\n\n---\n\n".join(context)

    prompt = f"""
You are a technical documentation assistant.

Answer the user's question using ONLY the provided documentation.

If the documentation does not contain enough information to answer,
say that the documentation does not provide enough information.

Documentation:
{context_text}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text