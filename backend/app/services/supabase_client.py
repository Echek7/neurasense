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
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{REST_URL}/projects", headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()

async def list_projects():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REST_URL}/projects", headers=HEADERS)
        response.raise_for_status()
        return response.json()
