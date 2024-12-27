from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

print("sys.path:", sys.path)
# Add project root (Flyease-Project) to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.app.routes.flight_routes import router as flight_router
from backend.app.routes.services_routes import router as service_router

app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(flight_router, prefix="/api")
app.include_router(service_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to FlyEase!"}
