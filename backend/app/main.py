from fastapi import FastAPI
from app.routes import external, local
from app.db import mongo

app = FastAPI(
    title="One Piece API",
    description="Backend para gestionar información de One Piece.",
    version="1.0.0",
)

# Registrar rutas
app.include_router(external.router, prefix="/api/external", tags=["External API"])
app.include_router(local.router, prefix="/api/local", tags=["Local CRUD"])