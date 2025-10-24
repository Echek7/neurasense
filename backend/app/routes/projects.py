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
        if isinstance(row, list) and len(row) > 0:
            return {"status": "success", "project": row[0]}
        return {"status": "error", "message": "Failed to insert project"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", status_code=200)
async def get_projects():
    try:
        rows = await list_projects()
        return {"status": "success", "projects": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
