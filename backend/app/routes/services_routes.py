from fastapi import APIRouter
from backend.app.controllers.service_controller import get_all_services, create_service

router = APIRouter()

@router.get("/services")
def fetch_services():
    return get_all_services()

@router.post("/services")
def add_service(service_data: dict):
    return create_service(service_data)
