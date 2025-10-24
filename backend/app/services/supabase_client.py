# backend/app/services/supabase_client.py
import os
import httpx

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
