from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.flight_routes import router as flight_router
from app.routes.services_routes import router as service_router

app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific domains in production)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(flight_router, prefix="/api")
app.include_router(service_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to FlyEase!"}
