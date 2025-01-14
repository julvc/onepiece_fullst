from fastapi import FastAPI
# from app.db.mongo import mongo
from fastapi.middleware.cors import CORSMiddleware
from app.db.mongo import connect_to_mongo, close_mongo_connection
from contextlib import asynccontextmanager
import os

#Externals
from app.routes.external import sagasRoutesExt
from app.routes.external import locateRoutesExt
from app.routes.external import fruitRoutesExt
from app.routes.external import boatRoutesExt
from app.routes.external import bowRoutesExt
from app.routes.external import chapterRoutesExt
from app.routes.external import characterRoutesExt
from app.routes.external import crewRoutesExt
from app.routes.external import dialRoutesExt
from app.routes.external import episodeRoutesExt
from app.routes.external import filmRoutesExt
from app.routes.external import hakiRoutesExt
from app.routes.external import luffygearRoutesExt
from app.routes.external import luffytechniqueRoutesExt
from app.routes.external import swordRoutesExt
from app.routes.external import volumeRoutesExt

#Local
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
#region Rutas externas
app.include_router(sagasRoutesExt.router, prefix="/api/sagas", tags=["External API for Sagas"])
app.include_router(locateRoutesExt.router, prefix="/api/locates", tags=["External API for Locations"])
app.include_router(fruitRoutesExt.router, prefix="/api/fruits", tags=["External API for Fruits"])
app.include_router(boatRoutesExt.router, prefix="/api/boats", tags=["External API for Boats"])
app.include_router(bowRoutesExt.router, prefix="/api/arcs", tags=["External API for Bows"])
app.include_router(chapterRoutesExt.router, prefix="/api/chapters", tags=["External API for Chapters"])
app.include_router(characterRoutesExt.router, prefix="/api/characters", tags=["External API for Characters"])
app.include_router(crewRoutesExt.router, prefix="/api/crews", tags=["External API for Crews"])
app.include_router(dialRoutesExt.router, prefix="/api/dials", tags=["External API for Dials"])
app.include_router(episodeRoutesExt.router, prefix="/api/episodes", tags=["External API for Episodes"])
app.include_router(filmRoutesExt.router, prefix="/api/films", tags=["External API for Films"])
app.include_router(hakiRoutesExt.router, prefix="/api/hakis", tags=["External API for Hakis"])
app.include_router(luffygearRoutesExt.router, prefix="/api/luffysgears", tags=["External API for Luffys Gears"])
app.include_router(luffytechniqueRoutesExt.router, prefix="/api/luffystechniques", tags=["External API for Luffys Techniques"])
app.include_router(swordRoutesExt.router, prefix="/api/swords", tags=["External API for Swords"])
app.include_router(volumeRoutesExt.router, prefix="/api/volumes", tags=["External API for Volumes"])
#endregion


#region Rutas locales
app.include_router(sagasRoutes.router, prefix="/api/local/sagas", tags=["Sagas CRUD"])

#endregion