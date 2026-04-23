from fastapi import APIRouter
from src.services.property_service import get_properties

router = APIRouter()

@router.get("/properties")
def properties(city: str = None, status: str = None, year: int = None):
    return get_properties(city, status, year)