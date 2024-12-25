from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Mock flight data
flights = [{"id": 1, "status": "On Time", "gate": "A12"}]

queue_times = {"Security": 5, "Check-in": 10, "Boarding": 7}

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

@app.get("/queue-times")
async def get_queue_times():
    # Simulate predictions with random adjustments
    predicted_times = {k: v + random.randint(-2, 5) for k, v in queue_times.items()}
    return {"current": queue_times, "predicted": predicted_times}