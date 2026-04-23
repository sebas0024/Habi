from fastapi import FastAPI 
from src.api.endpoints import router


app = FastAPI(
    title="API Habi",
    version="1.0"
)

app.include_router(
    router,
    prefix="/api",
    tags=["Properties"]
)
