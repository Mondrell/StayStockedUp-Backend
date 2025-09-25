from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import Base, engine
from app.routes import ingredient as ingredient_routes

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# allow your frontend to call the API (tighten origins later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # change to your Softr/Render domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "StayStockedUp backend is running 🚀"}

app.include_router(ingredient_routes.router)
