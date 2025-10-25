# backend/app/routes/ping.py
from fastapi import APIRouter

ping_router = APIRouter()

@ping_router.get("/")
async def ping():
    return {"message": "pong"}
