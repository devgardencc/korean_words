from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class AuthRequest(BaseModel):
    init_data: str


class AuthResponse(BaseModel):
    access_token: str
    user_id: int


class WordCardResponse(BaseModel):
    id: int
    word: str
    pos: Optional[str]
    level: Optional[str]
    definition_kr: Optional[str]
    definition_ru: Optional[str]
    examples: List[Dict[str, Any]]


class ProgressUpdateRequest(BaseModel):
    vocab_id: int
    status: str  # 'learning', 'mastered'
