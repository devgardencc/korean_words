from fastapi import FastAPI
from dictionary import search_word # Load environment variables from .env file
from database import supabase, get_word

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Topik API works"}

@app.get("/words")
async def get_words():
    response = supabase.table("words").select("*").limit(5).execute()
    return response.data

@app.get("/dictionary/{word}")
async def get_dictionary(word: str):
    data = await search_word(word)
    return data

@app.get("/get_full_word")
async def get_full_word():

    db_word = get_word()

    if db_word is None:
        return {"error": "Database is empty"}

    dictionary = await search_word(db_word["word"])

    return {
        "word": db_word["word"],
        "type": db_word["type"],
        "level": db_word["level"],
        "example": db_word["example1"],
        "meanings": dictionary
    }
