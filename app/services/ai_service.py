import json

from openai import OpenAI

from app.config import settings
from app.models.flashcard import FlashcardResponse


client = OpenAI(api_key=settings.OPENAI_API_KEY)


SYSTEM_PROMPT = """
You are an expert educator.

Generate high-quality flashcards from the provided study notes.

Rules:
- Return ONLY valid JSON.
- Generate between 5 and 20 flashcards depending on the input.
- Avoid duplicate questions.
- Keep answers concise.
- Include:
  - question
  - answer
  - topic
  - difficulty (Easy, Medium, Hard)
  - tags
"""


def generate_flashcards(text: str) -> FlashcardResponse:
    response = client.responses.create(
        model=settings.OPENAI_MODEL,
        temperature=settings.OPENAI_TEMPERATURE,
        max_output_tokens=settings.OPENAI_MAX_TOKENS,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": (
                    "Generate flashcards from the following notes.\n\n"
                    f"{text}\n\n"
                    "Return JSON in this format:\n"
                    '{"flashcards":[{"question":"","answer":"","topic":"","difficulty":"","tags":[]}]}'
                ),
            },
        ],
    )

    data = json.loads(response.output_text)

    return FlashcardResponse.model_validate(data)