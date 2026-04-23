from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from backend.api.endpoints import router


app = FastAPI(
    title="API Habi",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Esto permite que cualquier origen acceda
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, etc.
    allow_headers=["*"], # Permite todos los encabezados
)

app.include_router(
    router,
    prefix="/api",
    tags=["Properties"]
)
