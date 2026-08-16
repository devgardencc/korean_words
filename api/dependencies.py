from supabase import Client
from services.database import supabase_client


def get_db() -> Client:
    return supabase_client
