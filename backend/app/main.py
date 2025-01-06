from fastapi import FastAPI
# from app.db.mongo import mongo
from fastapi.middleware.cors import CORSMiddleware
from app.db.mongo import connect_to_mongo, close_mongo_connection
from contextlib import asynccontextmanager
import os

from app.routes.external import sagasRoutesExt
from app.routes.local import sagasRoutes

@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_mongo(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    yield
    close_mongo_connection()

app = FastAPI(
    title="One Piece API",
    description="Backend para gestionar información de One Piece.",
    version="1.0.0",
    lifespan=lifespan,
)


# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto para limitar el acceso en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(sagasRoutesExt.router, prefix="/api/external", tags=["External API"])
app.include_router(sagasRoutes.router, prefix="/api/sagas", tags=["Sagas CRUD"])
