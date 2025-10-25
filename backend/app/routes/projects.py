print(">>> projects.py se está cargando")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.supabase_client import supabase

projects_router = APIRouter()

class Project(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None

@projects_router.get("/", response_model=List[Project])
async def list_projects():
    return []  # temporal para probar sin Supabase
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.supabase_client import supabase

projects_router = APIRouter()

# Modelo de proyecto
class Project(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None

# Listar proyectos
@projects_router.get("/", response_model=List[Project])
async def list_projects():
    response = supabase.table("projects").select("*").execute()
    if response.error:
        raise HTTPException(status_code=500, detail=response.error.message)
    return response.data

# Crear proyecto
@projects_router.post("/", response_model=Project)
async def create_project(project: Project):
    response = supabase.table("projects").insert({
        "name": project.name,
        "description": project.description
    }).execute()
    if response.error:
        raise HTTPException(status_code=500, detail=response.error.message)
    return response.data[0]
