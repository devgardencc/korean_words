from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class AuthRequest(BaseModel):
    init_data: str


class AuthResponse(BaseModel):
    access_token: str
    user_id: int


class WordCardResponse(BaseModel):
    id: int
    id_lvl: int
    level: str
    word: str
    type: str
    example: str
    grade_type: str
    grade_id: str


class ProgressUpdateRequest(BaseModel):
    vocab_id: int
    status: str  # 'learning', 'mastered'


class PaginatedWordsResponse(BaseModel):
    items: List[WordCardResponse]
    total: int
    page: int
    limit: int
    total_pages: int
