from fastapi import APIRouter, Depends, HTTPException, Query
from supabase import Client
from models.schemas import PaginatedWordsResponse, WordCardResponse
from api.dependencies import get_current_user, get_db

router = APIRouter(prefix="/card", tags=["Word API"])


@router.get("/words", response_model=PaginatedWordsResponse)
async def get_words(
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(10, ge=1, le=100, description="Количество записей на странице"),
    db: Client = Depends(get_db),
):
    start = (page - 1) * limit
    end = start + limit - 1

    response = (
        db.table("vocabulary").select("*", count="exact").range(start, end).execute()
    )

    total_items = response.count if response.count else 0

    total_pages = (total_items + limit - 1) // limit

    return {
        "items": response.data,
        "total": total_items,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
    }


@router.get("/id/{vocab_id}", response_model=WordCardResponse)
async def get_word_card_by_id(
    vocab_id: int, user: dict = Depends(get_current_user), db: Client = Depends(get_db)
):
    response = db.table("vocabulary").select("*").eq("id", vocab_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    return WordCardResponse(**response.data[0])


@router.get("/word/{vocab_word}", response_model=WordCardResponse)
async def get_word_card_by_word(
    vocab_word: str,
    user: dict = Depends(get_current_user),
    db: Client = Depends(get_db),
):
    response = db.table("vocabulary").select("*").eq("word", vocab_word).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Word not found in database")

    return WordCardResponse(**response.data[0])
