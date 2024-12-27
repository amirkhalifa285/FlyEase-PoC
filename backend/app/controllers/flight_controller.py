from app.models.flight import Flight
from app.database.database import SessionLocal

def get_all_flights():
    db = SessionLocal()
    flights = db.query(Flight).all()
    db.close()
    return flights

def create_flight(flight_data):
    db = SessionLocal()
    new_flight = Flight(**flight_data)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()
    return new_flight
