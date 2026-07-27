import httpx
import xmltodict
import collections.abc
import os
from dotenv import load_dotenv

load_dotenv() 
KRDICT_API_KEY = os.getenv("KRDICT_API_KEY")

async def search_word(word: str):
    url = f"https://krdict.korean.go.kr/api/search"
    params = {
        "key": KRDICT_API_KEY,
        "q": word,
        "translated": "y",
        "trans_lang": "10",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    data = xmltodict.parse(response.content)

    items = data["channel"]["item"]

    result = []
    for item in items:
        if item["word"] == word:
            trans = item["sense"] if isinstance(item["sense"], collections.abc.Sequence) else [item["sense"]]
            for sense in trans:

                if "translation" in sense:
                    result.append({
                        "translation": sense["translation"]["trans_word"],
                        "definition": sense["translation"]["trans_dfn"]
                    })
    return result
