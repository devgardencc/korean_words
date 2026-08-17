from fastapi import APIRouter, Depends
from supabase import Client
from api.dependencies import get_db
from services.dictionary import search_word

router = APIRouter(prefix="/dict", tags=["Korean Dict API"])


@router.get("/{word}")
async def get_dictionary(word: str):
    data = await search_word(word)
    return data
