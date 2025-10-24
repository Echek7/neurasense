from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ping import router as ping_router

app = FastAPI(title="NeuraSense Core - Backend (MVP)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ping_router, prefix="/api")
