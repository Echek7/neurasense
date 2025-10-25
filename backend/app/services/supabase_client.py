# backend/app/supabase_client.py
from supabase import create_client, Client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL") or "https://tu-proyecto.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY") or "tu-api-key"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
