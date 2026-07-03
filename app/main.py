from fastapi import FastAPI

from app.api.flashcards import router as flashcard_router


app = FastAPI(
    title="AI Flashcard Generator API",
    description="Generate AI-powered flashcards from study notes.",
    version="1.0.0",
)


app.include_router(flashcard_router)