from fastapi import FastAPI
from app.routes import ingredient
from app.db import Base, engine

# Create DB tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"message": "StayStockedUp backend is running 🚀"}

# Include routes
app.include_router(ingredient.router)
