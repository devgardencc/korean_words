from fastapi import APIRouter

from .routers.card import router as card_router
from .routers.user import router as user_router
from .routers.dict import router as dict_router

router = APIRouter(prefix="/api")

router.include_router(card_router)
router.include_router(user_router)
router.include_router(dict_router)