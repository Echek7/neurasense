print(">>> main.py cargado")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.ping import ping_router
from .routes.projects import projects_router

app = FastAPI(title="NeuraSense API", version="0.1.0")

# CORS para frontend
origins = ["http://localhost:3000"]  # ajusta si tu frontend está en otra URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ping_router, prefix="/api/ping", tags=["Ping"])
app.include_router(projects_router, prefix="/api/projects", tags=["Projects"])
