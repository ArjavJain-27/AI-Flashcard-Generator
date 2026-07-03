from pydantic import BaseModel, Field


class FlashcardRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Study notes used to generate flashcards.",
    )


class Flashcard(BaseModel):
    question: str
    answer: str
    topic: str
    difficulty: str
    tags: list[str]


class FlashcardResponse(BaseModel):
    flashcards: list[Flashcard]