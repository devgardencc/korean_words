from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_word():
    response = supabase.table("words").select("*").limit(1).execute()

    if not response.data:
        return None

    return response.data[0]
