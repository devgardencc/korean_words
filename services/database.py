from supabase import create_client, Client
from core.config import settings


def init_supabase() -> Client:
    """Инициализация подключения к Supabase."""
    url: str = settings.SUPABASE_URL
    key: str = settings.SUPABASE_KEY
    return create_client(url, key)


supabase_client: Client = init_supabase()


def get_word():
    response = supabase_client.table("words").select("*").limit(1).execute()

    if not response.data:
        return None

    return response.data[0]
