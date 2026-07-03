from fastapi import APIRouter

from app.models.flashcard import FlashcardRequest, FlashcardResponse
from app.services.ai_service import generate_flashcards


router = APIRouter()


@router.post(
    "/generate-flashcards",
    response_model=FlashcardResponse,
)
def create_flashcards(
    request: FlashcardRequest,
) -> FlashcardResponse:
    return generate_flashcards(request.text)