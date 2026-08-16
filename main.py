from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Korean Learning WebApp API",
    description="API для Telegram WebApp по изучению корейского языка",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/health", tags=["System"])
async def health_check():
    """Проверка доступности сервиса."""
    return {"status": "ok"}
