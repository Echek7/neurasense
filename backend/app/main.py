from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.ping import router as ping_router  # Import relativo correcto

app = FastAPI(title="NeuraSense Core - Backend (MVP)")

# Middleware global
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # ⚠️ en producción cambiar a dominios seguros
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ping_router, prefix="/api")
