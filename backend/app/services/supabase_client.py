<<<<<<< HEAD
# backend/app/services/supabase_client.py
import os import httpx

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
REST_URL = f"{SUPABASE_URL}/rest/v1"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

async def insert_project(payload: dict):
    """
    inserta un project en la tabla 'projects' usando la REST API de Supabase (PostgREST).
    payload: dict con keys: user_id, title, prompt, status
    """

    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(
            f"{REST_URL}/projects",
            json=payload,
            headers=HEADERS,
        )
        r.raise_for_status()
        return r.json()  # representación de la fila insertada

async def list_projects(limit: int = 20):
    """
    lista proyectos (order by created_at desc)
    """
    params = {
        "select": "*",
        "order": "created_at.desc",
        "limit": str(limit),
    }
    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.get(
            f"{REST_URL}/projects",
            params=params,
            headers=HEADERS,
        )
        r.raise_for_status()
        return r.json()
=======
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://fyxvkustmfelhvseentt.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5eHZrdXN0bWZlbGh2c2VlbnR0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEyODE2MjcsImV4cCI6MjA3Njg1NzYyN30.lsklap3XSIKBxq5LDOlnAxflpkC9Kz065uDQEkyEDEk")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
>>>>>>> 59b957c (add supabase client)
