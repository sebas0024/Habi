from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from backend.api.endpoints import router

# Inicializa la aplicación FastAPI con metadatos básicos
app = FastAPI(
    title="API Habi",   # Nombre de la API (se muestra en /docs)
    version="1.0"       # Versión del servicio
)

# Configuración de CORS para permitir acceso desde otros orígenes (ej: frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Esto permite que cualquier origen acceda
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, etc.
    allow_headers=["*"], # Permite todos los encabezados
)

# Registro de rutas de la aplicación
app.include_router(
    router,
    prefix="/api", 
    tags=["Properties"]
)
