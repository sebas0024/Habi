from fastapi import APIRouter
from backend.services.property_service import get_properties

# Crea una instancia de router para agrupar endpoints relacionados
router = APIRouter()

# Endpoint GET para consultar propiedades
@router.get("/properties")
def properties(city: str = None, status: str = None, year: int = None):
    # Llama al servicio que contiene la lógica de negocio
    return get_properties(city, status, year)