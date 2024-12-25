from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock flight data
flights = [{"id": 1, "status": "On Time", "gate": "A12"}]

# Pydantic model for flight updates
class FlightUpdate(BaseModel):
    id: int
    status: str
    gate: str

@app.get("/")
async def root():
    return {"message": "FlyEase Backend is Running"}

@app.get("/flights")
async def get_flights():
    return flights

@app.post("/flights/update")
async def update_flight(update: FlightUpdate):
    for flight in flights:
        if flight["id"] == update.id:
            flight["status"] = update.status
            flight["gate"] = update.gate
            return {"message": f"Flight {update.id} updated successfully"}
    return {"error": "Flight not found"}
