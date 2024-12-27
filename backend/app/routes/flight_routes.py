from fastapi import APIRouter
from app.controllers.flight_controller import get_all_flights, create_flight

router = APIRouter()

@router.get("/flights")
def fetch_flights():
    return get_all_flights()

@router.post("/flights")
def add_flight(flight_data: dict):
    return create_flight(flight_data)
