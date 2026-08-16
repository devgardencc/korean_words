from supabase import Client
from services.database import supabase_client


def get_db() -> Client:
    return supabase_client


def get_current_user():
    return {"user_id": 123456789}
