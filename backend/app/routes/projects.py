# backend/app/routes/projects.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.supabase_client import insert_project, list_projects

router = APIRouter()

class ProjectCreate(BaseModel):
    user_id: Optional[str] = None
    title: str
    prompt: Optional[str] = None
    status: Optional[str] = "draft"

@router.post("/", status_code=201)
async def create_project(payload: ProjectCreate):
    try:
        row = await insert_project(payload.dict())
        # PostgREST devuelve una lista con la fila insertada
        if isinstance(row, list) and len(row) > 0:
            return row[0]
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def get_projects(limit: int = 20):
    try:
        rows = await list_projects(limit=limit)
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
