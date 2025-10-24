from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.ping import router as ping_router
from .routes.projects import router as projects_router

app = FastAPI(title="NeuraSense Core - Backend (MVP)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # ⚠️ cambiar en producción a dominios seguros
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ping_router, prefix="/api")
app.include_router(projects_router, prefix="/api/projects")
