# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from .routes.ping import router as ping_router
from .routes.projects import router as projects_router  # <- asegúrate que existe

app = FastAPI(title="NeuraSense Core - Backend (MVP)")

# Middleware global
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # ⚠️ en producción restringir orígenes
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers registrados
app.include_router(ping_router, prefix="/api")
app.include_router(projects_router, prefix="/api/projects")
