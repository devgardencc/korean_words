from fastapi import APIRouter

from .routers.word import router as word_router
from .routers.user import router as user_router
from .routers.dict import router as dict_router

router = APIRouter(prefix="/api")

router.include_router(word_router)
router.include_router(user_router)
router.include_router(dict_router)
