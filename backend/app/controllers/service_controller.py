from app.models.service import Service
from app.database.database import SessionLocal

def get_all_services():
    db = SessionLocal()
    services = db.query(Service).all()
    db.close()
    return services

def create_service(service_data):
    db = SessionLocal()
    new_service = Service(**service_data)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    db.close()
    return new_service
