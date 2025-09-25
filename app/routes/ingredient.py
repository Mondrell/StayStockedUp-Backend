from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.schemas.ingredient import Ingredient, IngredientCreate
from app.crud.ingredient import create_ingredient, get_ingredients

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ingredients/", response_model=Ingredient)
def add_ingredient(item: IngredientCreate, db: Session = Depends(get_db)):
    return create_ingredient(db, item)

@router.get("/ingredients/", response_model=list[Ingredient])
def list_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_ingredients(db, skip, limit)
