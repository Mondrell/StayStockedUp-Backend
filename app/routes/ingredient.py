from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.crud.ingredient import create_ingredient, get_ingredients
from app.schemas.ingredient import Ingredient, IngredientCreate
from app.db import get_db

router = APIRouter()

# --- Single insert ---
@router.post("/ingredients/", response_model=Ingredient)
def add_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return create_ingredient(db, ingredient)

# --- Bulk insert ---
@router.post("/ingredients/bulk", response_model=List[Ingredient])
def add_ingredients_bulk(ingredients: List[IngredientCreate], db: Session = Depends(get_db)):
    created_items = []
    for ingredient in ingredients:
        created = create_ingredient(db, ingredient)
        created_items.append(created)
    return created_items

# --- List ingredients ---
@router.get("/ingredients/", response_model=List[Ingredient])
def list_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_ingredients(db, skip=skip, limit=limit)
