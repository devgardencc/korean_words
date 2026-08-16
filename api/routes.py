from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from models.schemas import WordCardResponse, ProgressUpdateRequest
from api.dependencies import get_db

router = APIRouter(prefix="/api", tags=["WebApp API"])


def get_current_user():
    return {"user_id": 123456789}


@router.get("/card/{vocab_id}", response_model=WordCardResponse)
async def get_word_card(
    vocab_id: int, user: dict = Depends(get_current_user), db: Client = Depends(get_db)
):
    response = db.table("vocabulary").select("*").eq("id", vocab_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    word_data = response.data[0]

    return WordCardResponse(**word_data)


@router.get("/card/{vocab_word}", response_model=WordCardResponse)
async def get_word_card(
    vocab_word: str, user: dict = Depends(get_current_user), db: Client = Depends(get_db)
):
    response = db.table("vocabulary").select("*").eq("word", vocab_word).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    word_data = response.data[0]

    return WordCardResponse(**word_data)

@router.put("/progress", summary="Обновить прогресс")
async def update_progress(
    request: ProgressUpdateRequest,
    user: dict = Depends(get_current_user),
    db: Client = Depends(get_db),
):
    data = {
        "user_id": user["user_id"],
        "vocab_id": request.vocab_id,
        "status": request.status,
    }

    response = db.table("user_progress").upsert(data).execute()

    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to update progress")

    return {"status": "success", "message": "Progress updated"}
