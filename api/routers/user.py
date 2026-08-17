from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from models.schemas import ProgressUpdateRequest
from api.dependencies import get_current_user, get_current_user, get_db

router = APIRouter(prefix="/user", tags=["User API"])


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
