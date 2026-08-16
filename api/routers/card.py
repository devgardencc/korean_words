from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from models.schemas import WordCardResponse
from api.dependencies import get_current_user, get_db


router = APIRouter(prefix="/card", tags=["Card API"])


@router.get("/{vocab_id}", response_model=WordCardResponse)
async def get_word_card(
    vocab_id: int, user: dict = Depends(get_current_user), db: Client = Depends(get_db)
):
    response = db.table("vocabulary").select("*").eq("id", vocab_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    word_data = response.data[0]

    return WordCardResponse(**word_data)


@router.get("/{vocab_word}", response_model=WordCardResponse)
async def get_word_card(
    vocab_word: str, user: dict = Depends(get_current_user), db: Client = Depends(get_db)
):
    response = db.table("vocabulary").select("*").eq("word", vocab_word).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    word_data = response.data[0]

    return WordCardResponse(**word_data)


